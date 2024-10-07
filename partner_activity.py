#Partner activity.. Names:Esteban Galvan, Lance Espino, Ryan Ostrowski
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"

#Find the student who is making an A and upgrade it to an A +
school["class"]["students"]["student1"] = "A+"
#Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20] },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]}}


# Find the total number of oranges in warehouse1
oranges = product_inventory["warehouse1"]["quantities"][1]
print(oranges)
#Sum up all the quantities in the warehouse
Quantity1 = product_inventory["warehouse1"]["quantities"][0:-1]
Quantity2 = product_inventory["warehouse2"]["quantities"][0:-1]
print(sum(Quantity1) + sum(Quantity2))