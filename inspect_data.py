import csv 

with open('Karu Dumpsite data cordinates.csv', encoding= 'utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

    # print("Number of Rows", len(rows))
    # print("columns: ", list(rows[0].keys()))

# values = []
# for row in rows:
#     value = float(row["Longitude"])
#     values.append(value)

#     print("Largest Value: ", max(values))
#     print("Smallest Value: ", min(values)) 
#     print("Count: ", len(values))  

# values = []
# for row in rows:
#     raw = row["Longitude"].strip()
#     if raw =="":
#         continue
#     values.append(float(raw))

# print("Largest Value: ", max(values))
# print("Smallest Value: ", min(values)) 
# print("Count: ", len(values))  

def inspect_column(filename, column):
    with open(filename, encoding= "utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw =="":
            continue
        values.append(float(raw))

    return{
        "smallest":min(values),
        "largest":max(values),
        "cunt":len(values)
    }

result = inspect_column("Karu Dumpsite data cordinates.csv", "Longitude")
print(result)