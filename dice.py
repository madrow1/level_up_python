import random 
from collections import Counter

def dice(rolls,sides,dice_count):
    recorded_rolls = []
    number_count = {}
    count = 0
    total_sides = sides * dice_count
    for roll in range(rolls):
        recorded_rolls.append(random.randint(1,total_sides))

    #print(recorded_rolls)

    dict_items = Counter(recorded_rolls).items()

    dict_items_sorted = dict(sorted(dict_items))

    print(dict_items_sorted)

    for unique, index in dict_items_sorted.items():
       print("The percentage chance of " + str(unique) + " is: " + str(index/rolls * 100) + "%")


dice(1000000,6, 1)