pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and more than 15 gold

def pirates_list(input):
    pirates_name_list = []
    for pirate in input:
        if pirate['has_wooden_leg'] == True and pirate['gold'] > 15:
            pirates_name_list.append(pirate['Name'])
    return pirates_name_list

print(pirates_list(pirates))
