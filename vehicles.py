# vehicles.py

# Each vehicle will be stored as a dictionary
vehicles = [
    {"name": "Toyota", "edition": "2020", "reliability": 9},
    {"name": "Honda", "edition": "2019", "reliability": 8},
    {"name": "Ford", "edition": "2021", "reliability": 7},
    {"name": "Mazda", "edition": "2018", "reliability": 8},
    {"name": "BMW", "edition": "2022", "reliability": 6},
    {"name": "Mercedes", "edition": "2023", "reliability": 9},
]

print("Vehicle List with Editions and Reliability:")
print("Name       Edition   Reliability")
print("---------------------------------")

for v in vehicles:
    print(f"{v['name']:<10} {v['edition']:<8} {v['reliability']}")
