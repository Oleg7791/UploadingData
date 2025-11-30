import csv
from matplotlib import pyplot as plt
from pexpect import which

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # чтение максимальных температур
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
print(highs)

# нанесение данных на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# форматирование диаграммы
plt.title('Daile high temperatures, July 2018',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()