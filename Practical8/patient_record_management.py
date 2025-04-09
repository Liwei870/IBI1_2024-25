#creat a class
#define a class to manage patient records
class patients:
    def __init__(self, name, age, latest_admission_date, medical_history):
        self.name = name
        self.age = age
        self.latest_admission_date = latest_admission_date
        self.medical_history = medical_history
    def patient_info(self):
        print(f"Name:{self.name}, Age: {self.age}, Latest Admission Date: {self.latest_admission_date}, Medical History: {self.medical_history}")
        #example      
patient1 = patients("Zhang Sentao", 19, "2025-04-08", "No known allergies")
patient1.patient_info()
    