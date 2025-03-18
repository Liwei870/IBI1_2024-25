#Input the data
# 1. Print sorted lists
import matplotlib.pyplot as plt
uk_countries = ["England", "Wales", "Northern Ireland", "Scotland"]
uk_populations = [57.11, 3.13, 1.91, 5.45]
china_provinces = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]
china_populations = [65.77, 41.88, 45.28, 61.27, 85.15]
sorted_uk_populations = sorted(uk_populations)
sorted_china_populations = sorted(china_populations)
print("Sorted UK populations:", sorted_uk_populations)
print("Sorted China populations:", sorted_china_populations)
# 2. Generate pie charts
# Population distribution in UK countries
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(uk_populations, labels=uk_countries, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Population Distribution in UK Countries')
# Population distribution in Zhejiang-neighbouring provinces
plt.subplot(1, 2, 2)
plt.pie(china_populations, labels=china_provinces, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold', 'violet'])
plt.title('Population Distribution in Zhejiang-Neighbouring Provinces')
plt.tight_layout()
plt.show()