import csv
from convertor import distance as d
from typing import List

def process_data(filename):
    DB_ft = []
    DB_m = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) >= 3:
                distance = row[1]

                if "ft" in distance:
                    DB_ft.append([row[0], distance, row[2]])
                    dis_converted = d.convert_feets_to_meters(distance)
                    DB_m.append([row[0], dis_converted, row[2]])

                elif "m" in distance:
                    DB_m.append([row[0], distance, row[2]])
                    dis_converted = d.convert_meters_to_feets(distance)
                    DB_ft.append([row[0], dis_converted, row[2]])
    return DB_ft, DB_m

def write_data(data: List, filename:str) -> None:
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    filename = "data_storage/distance/distance.csv"
    DB_ft, DB_m = process_data(filename)

    write_data(DB_ft, "out/distance/distance_ft.csv")
    write_data(DB_m, "out/distance/distance_m.csv")

if __name__ == "__main__":
    main()

