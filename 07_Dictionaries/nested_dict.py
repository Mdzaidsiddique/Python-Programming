# dictionary inside dictionary is called nested dictionary

cars = {
    "hundai" :{
        "name":"i10",
        "model":2010
    },
    "mahindra" :{
        "name":"thar",
        "model":2020
    },
    "tata" : {
        "series" : ["safari", 'nexon', 'punch'],
        "model": [2022, 2021, 2023]
    }

}

print(cars)

# accessing utems from nesed dictionary 

print(cars["tata"]["series"][0]) #safari

# Loop Through Nested Dictionaries: using items() method
for x, y in cars.items():
    print(x, ":", y)

    for x1 in y:
        print(x1, ":", y[x1])

