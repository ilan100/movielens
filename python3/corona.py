import string
import csv
import json


def read_corona_file(filename : str) -> list:
    corona_data = []
    with (open(filename, "r") as f):
       reader = csv.DictReader(f)
       for line in reader:
           corona_data.append(line)
       return corona_data

def min_max_age_vaccinated(cor_data : list):
    MinY = 1000
    MinN = 1000
    MaxY = 0
    MaxN = 0
    for line in cor_data:
        age = int(line["Age"])
        if (line["Is_vaccinated"] == "Y"):
            if (age < MinY):
                MinY = age
            elif (age > MaxY):
                MaxY = age
        elif (line["Is_vaccinated"] == "N"):
            if (age < MinN):
                MinN = age
            elif (age > MaxN):
                MaxN = age
    print("minimum age for vaccinated:", MinY)
    print("maximum age for vaccinated:", MaxY)
    print("minimum age for non-vaccinated:", MinN)
    print("maximum age for non-vaccinated:", MaxN)

def avg_len_hospital(corona_data : list):
    durations = [int(d["Length_of_hospitalization"]) for d in corona_data if int(d["Length_of_hospitalization"]) > 0]
    avg = sum(durations) / len(durations) if durations else 0
    return avg

def get_filter_values(line : str) -> tuple:
    ret = (False,)
    parts = [p.strip() for p in line.split(",")]
    if (len(parts) < 3):
        return ret

    if (parts[0] != "F" and parts[0] != "M" and parts[0] == "A"):
        return ret
    if (parts[2] != "Y" and parts[2] != "N" and parts[2] != "A"):
        return ret

    age_range = parts[1].split("-")
    if (len(age_range) != 2):
        return ret

    if (int(age_range[0]) < 0 or int(age_range[0]) > 130
        or int(age_range[1]) < 0 or int(age_range[1]) > 130):
        return ret

    ret = (parts[0], int(age_range[0]), int(age_range[1]), parts[2])
    return ret

def filter_corona_data(corona_data : list) -> list:
    filtered = []
    user_filter = input("Enter your required filter in following format:\n"
                        "Gender (F/M/A), Age range(min-max), Vaccinated(Y/N/A)"
                        " [A - any]\nFor example: if you want Only Female, "
                        "between Ages of 20 and 40, vaccinated or not\n"
                        "you should write: \"F, 20-40, A\"\n"
                        "Exnter your filter: ")
    filter = get_filter_values(user_filter)
    if (filter[0] == False):
        print("Filter mismatch, try again\n")
        return filtered

    #print(filter)

    filtered = [
        d for d in corona_data
        if d.get("gender") == filter[0] and
           int(d.get("Age")) >= filter[1] and
           int(d.get("Age")) <= filter[2] and
           (d.get("Is_vaccinated") == filter[3] or filter[3] == "A")
    ]

    return filtered

def save_corona_data_to_file(name: str, data : list):
    if len(data) < 1:
        print("No data to save")
        return
    with open(name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames = data[0].keys())
        writer.writeheader()  # write column names
        writer.writerows(data)  # write all rows

def write_json_file(name: str, data : list):
    with open(name, "w", newline="") as f:
        json.dump(data, f, indent=4)

#----------------------------------------------------------------------------------------
if __name__ == '__main__':
    corona_data = read_corona_file("corona.csv")
# EX 3-1
    min_max_age_vaccinated(corona_data)
# EX 3-2
    print("average hospitalization duration:", avg_len_hospital(corona_data))
# EX 3-3
    filtered_corona_data = filter_corona_data(corona_data)
    save_corona_data_to_file("updated_corona_data.csv", filtered_corona_data)
# EX4
    write_json_file("updated_corona_data.json", filtered_corona_data)
