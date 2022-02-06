#Remember import random function here:
import random

def add_random_numbers(my_list):
    for i in range(1, 11):
        my_list.append(random.randint(1, 10))

my_list = [4,5,734,43,45]
print(my_list)

#The magic is here:
add_random_numbers(my_list)
print(my_list)
