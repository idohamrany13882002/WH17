dict1: dict[str, object] = {"name": "israel", "birth": 1948, "population": 9.3, "capital": "jerusalem",
                            "language": "hebrew",
                            "cities": ["jerusalem", "tel aviv", "haifa", "rishon lezion", "petah tikva", "ashdod"],
                            "currancy": "ILS", "area": 22145, "gpd": 450}

print("capital:", dict1.get("capital"))
print(dict1.keys())
print(dict1.values())
for x, y in dict1.items():
    print(f"{x}: {y}")
dict2 = dict1.copy()
print(dict2)  # to check
gpd: int = dict2.pop("gpd")
print(dict2)  # to check
print(gpd)  # to check

dict3 = dict1.fromkeys(dict1.keys(), )
print(dict3)
cities: list[str] = []

for i in dict3:
    if i == "cities":
        for _ in range(3):
            city: str = input("enter city")
            cities.append(city)
        dict3[i] = cities
    else:
        dict3[i] = input(f"enter {i}: ")
dict3["birth"] = int(dict3["birth"])
dict3["population"] = int(dict3["population"])
dict3["area"] = int(dict3["area"])
dict3["gpd"] = int(dict3["gpd"])

print(dict3)
