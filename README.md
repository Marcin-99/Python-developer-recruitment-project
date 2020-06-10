# Python-developer-recruitment-project

To run the code (Chapter 2) you need to have sqlalchemy installed.

pip install sqlalchemy

<br>
<br>

***Chapter 1***

cd Chapter 1

To test the class "Car", type in this code in the same file where a class is located:

c = Car(3, 1600, 5)
print(c.total_mass)

wrong_car_1 = Car(3, 2001, 5)

c.pax_count = 6

**Run the code:**

car.py

<br>
<br>

***Chapter 2***

cd Chapter 2

Database file should create itself automaticly after running any command given below.

***Adding tasks to database***

Command:  tasks.py add --name NAME --deadline DEADLINE --description DESCRIPTION

**IMPORTANT** 

<span class="text-purple">Pattern for deadline: %Y-%m-%d,%H:%M<span>

**Example**

tasks.py add --name trening --deadline 2020-06-10,18:30 --description "Push training"

***Listing tasks***

Command:  tasks.py list --all | --today

***Updating tasks***

Command: tasks.py update --name NAME --deadline DEADLINE --description DESCRIPTION --hash HASH

**Examples**

tasks.py update --name "Nauka" --deadline 2020-06-12,19:00 --description "Egzamin z obwodów" --hash -4297185180708895369

Not every element must be specified, for example: tasks.py update --name "Nauka" --hash -4297185180708895369

**Important**

Since the hash chains are quite long, I reccomend listing all of them first, then copying them to the next command.

***Removing tasks***

Command: tasks.py remove --hash HASH

**example**

tasks.py remove --hash -4297185180708895369

<br>
<br>

***Chapter 3***

cd Chapter 3

To test the code, go to main.py and type in print(how_many_numbers_do_you_have_to_check()) in the same file, where function is located.

Command: main.py

**IMPORTANT**

 possible_numbers = [num for num in range(372^2, 809^2 + 1)...
 
To change the scope of the loop, just change the numbers given in range () from those imposed in the task, to any other numbers. The program is written to work in every range.




