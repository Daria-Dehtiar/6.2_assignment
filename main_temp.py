import csv
from convertor import temperature as t
from typing import List

def process_data(filename):
    DB_F = []
    DB_C = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) >= 3 and row[0] != "Date" and row[1] != "Temperature" and row[2] != "Unit":
                temperature = float(row[1])
                unit = row[2]

                if unit == "C":
                    DB_C.append([row[0], temperature, unit])
                    temp_converted = t.convert_celsius_to_fahrenheit(temperature, unit)
                    DB_F.append([row[0], temp_converted, unit.replace("C", "F")])

                elif unit == "F":
                    DB_F.append([row[0], temperature, unit])
                    temp_converted = t.convert_fahrenheit_to_celsius(temperature, unit)
                    DB_C.append([row[0], temp_converted, unit.replace("F", "C")])

    return DB_F, DB_C

def write_data(data: List, filename:str) -> None:
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    filename = "data_storage/temperature/temperature.csv"
    DB_F, DB_C = process_data(filename)

    write_data(DB_F, "out/temperature/temperature_F.csv")
    write_data(DB_C, "out/temperature/temperature_C.csv")

if __name__ == "__main__":
    main()