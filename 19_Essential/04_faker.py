# Faker is a Python package that generates fake data for you.
# pip install faker

from faker import Faker
fake = Faker()

print(fake.name()) # everytime run, print different fake name

print(fake.address())

print(fake.text())


for i in range(10):
    print(i+1, fake.name())


# resources: https://pypi.org/project/Faker/