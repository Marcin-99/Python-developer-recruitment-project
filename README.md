# Python-developer-recruitment-project

To run the code (Chapter 2) you need to have sqlalchemy installed.

pip install sqlalchemy

***Chapter 1***

To test the class "Car", type in this code in the same file where a class is located:

c = Car(3, 1600, 5)
print(c.total_mass)

wrong_car_1 = Car(3, 2001, 5)

c.pax_count = 6

**To run the code on Windows, type in:**

cd Chapter 1

car.py

***Chapter 2***

cd Chapter 2

Database file should create itself automaticly after running any command given below.

**Adding tasks to database**

Command:  tasks.py add --name NAME --deadline DEADLINE --description DESCRIPTION

**IMPORTANT** 

Pattern for typing in deadline: %Y-%m-%d,%H:%M

**example**

tasks.py add --name trening --deadline 2020-06-10,18:30 --description "Push training"


