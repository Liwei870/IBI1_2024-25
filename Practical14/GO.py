import xml.dom.minidom as xdm
import xml.sax as xs
import time

# SAX parser handler for processing GO XML files
class GOHandler(xs.ContentHandler):
    
    def __init__(self):
        self.current = ""
        self.ns = ""
        self.id = ""
        self.name = ""
        self.is_a = 0
        self.max = {
            "molecular_function": {"count": 0, "terms": []},
            "biological_process": {"count": 0, "terms": []},
            "cellular_component": {"count": 0, "terms": []}
        }
    
    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "term":
            # Reset fields for new term
            self.ns = ""
            self.id = ""
            self.name = ""
            self.is_a = 0
        elif tag == "is_a":
            self.is_a += 1
    
    def characters(self, content):
        if self.current == "namespace":
            self.ns += content.strip()
        elif self.current == "id":
            self.id += content.strip()
        elif self.current == "name":
            self.name += content.strip()
    
    def endElement(self, tag):
        if tag == "term":
            if self.ns in self.max:
                # Update max count and terms list
                if self.is_a > self.max[self.ns]["count"]:
                    self.max[self.ns] = {"count": self.is_a, "terms": [{"id": self.id, "name": self.name}]}
                elif self.is_a == self.max[self.ns]["count"]:
                    self.max[self.ns]["terms"].append({"id": self.id, "name": self.name})
            self.current = ""

# Analyze GO XML file using DOM API
def dom_analyze(file):
    start = time.time()
    dom = xdm.parse(file)
    terms = dom.getElementsByTagName("term")
    max_counts = {
        "molecular_function": {"count": 0, "terms": []},
        "biological_process": {"count": 0, "terms": []},
        "cellular_component": {"count": 0, "terms": []}
    }
    
    for term in terms:
        try:
            ns = term.getElementsByTagName("namespace")[0].firstChild.data
            if ns in max_counts:
                id_node = term.getElementsByTagName("id")[0].firstChild
                name_node = term.getElementsByTagName("name")[0].firstChild
                if id_node and name_node:
                    id = id_node.data
                    name = name_node.data
                    is_a = len(term.getElementsByTagName("is_a"))
                    
                    if is_a > max_counts[ns]["count"]:
                        max_counts[ns] = {"count": is_a, "terms": [{"id": id, "name": name}]}
                    elif is_a == max_counts[ns]["count"]:
                        max_counts[ns]["terms"].append({"id": id, "name": name})
        except (IndexError, AttributeError):
            # Skip malformed term nodes
            continue
    
    return max_counts, time.time() - start

# Analyze GO XML file using SAX API
def sax_analyze(file):
    start = time.time()
    parser = xs.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.max, time.time() - start

# Format and print analysis results
def print_result(data, api, time):
    print(f"\n{api} Results:")
    for ns in data:
        terms = data[ns]["terms"]
        ids = [term["id"] for term in terms]
        print(f"{ns}: {ids} with {data[ns]['count']} is_a elements")

if __name__ == "__main__":
    # Note: Use raw string to avoid escape characters
    file = "E:\IBI1\IBI1_2024-25\IBI1_2024-25\Practical14\go_obo.xml"
    
    try:
        dom, t1 = dom_analyze(file)
        sax, t2 = sax_analyze(file)
        
        print_result(dom, "DOM", t1)
        print_result(sax, "SAX", t2)
        
        if t2 > t1:
            print("\nSAX is slower than DOM")
        elif t1 > t2:
            print("\nSAX is faster than DOM")
        else:
            print("\nThe two methods have the same performance")
    except FileNotFoundError:
        print(f"Error: File {file} not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")