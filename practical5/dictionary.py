# Creat a dictionary to contain all the data
# Generate a bar plot through the dictionary
# Output the of debelopers using a specified language
import matplotlib.pyplot as plt
languages = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51,"SQL": 51, "TypeScript": 38.5}
print(languages)
plt.bar(languages.keys(), languages.values())
plt.xlabel('Language')
plt.ylabel('Users (percentage)')
plt.title('Developer Language Usage')
plt.show()
# 3. Output the percentage of developers using a specified language
# Pseudocode: Assume the language we want to query is "Python"
selected_language = "Python"
percentage = languages.get(selected_language, "Language not found")
print(f"Percentage of developers using {selected_language}: {percentage}%")