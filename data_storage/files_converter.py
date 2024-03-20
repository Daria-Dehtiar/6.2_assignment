import csv

input_file = "temperature/temperature.txt"
output_file = "temperature/temperature.csv"

input_file2 = "distance.txt"
output_file2 = "distance.csv"


with open(input_file, "r", encoding="utf-8") as file:
    next(file)
    data = []

    for line in file:
        temp_and_date = line.strip().split(",")
        
        date = str(temp_and_date[0])
        temp_and_unit = temp_and_date[1].strip('"').split("°")
        
        temp = (temp_and_unit[0])
        unit = temp_and_unit[1]
        
        data.append([date, temp, unit])

with open(output_file, "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Temperature", "Unit"])
    writer.writerows(data)

with open(input_file2, "r", encoding="utf-8") as file:
    next(file)
    data2 = []
    for line in file:
        date_distance_temp = line.strip().split(",")

        date = str(date_distance_temp[0])
        distance_and_unit = date_distance_temp[1].strip('""')
        temp = date_distance_temp[2].strip('""')

        data2.append([date, distance_and_unit, temp])

with open(output_file2, "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Distance", "Temperature"])
    writer.writerows(data2)
