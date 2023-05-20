import random
import csv
csv_file = "data_Area_Of_circle.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Height', 'A','B','Area'])
    for i in range(1000):
       
        H = random.uniform(0.0, 10.0)
       
        A = random.uniform(0.0, 10.0)

        B =random.uniform(0.0, 10.0)
    
        Area=((A+B)/2)*H

        print(Area)

        writer.writerow([H, A , B, Area ])