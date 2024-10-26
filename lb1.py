import csv

data = [
    ["День", "Температура"],
    [1, -5],
    [2, -6],
    [3, -2],
    [4, -7],
    [5, 0.0],
]

with open("january_temperatures.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Файл створено успішно!")

temperatures = []
with open("january_temperatures.csv", mode="r") as fd:
    reader = csv.reader(fd)
    next(reader)  
    for row in reader:
        day = int(row[0])
        temp = float(row[1])
        temperatures.append((day, temp))
        print(row) 

min_temp_day, min_temp = min(temperatures, key=lambda x: x[1])
max_temp_day, max_temp = max(temperatures, key=lambda x: x[1])

print(f"\nНайменша температура: {min_temp}°C на день {min_temp_day}")
print(f"Найбільша температура: {max_temp}°C на день {max_temp_day}")


