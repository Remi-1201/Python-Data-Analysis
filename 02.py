"""
1/ Iterating over dictionaries.
"""

# Mapping from various cities to their country
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

'''
Direct Iteration
================
Beijing, China
Rome, Italy
Paris, France
Washington, D.C., USA
Canberra, Australia
Lima, Peru
London, England
Tokyo, Japan
Moscow, Russia
'''

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")

'''
Iteration over Keys
===================
Beijing, China
Lima, Peru
London, England
Moscow, Russia
Washington, D.C., USA
Canberra, Australia
Rome, Italy
Tokyo, Japan
Paris, France
'''

print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")

'''
Iteration over Values
=====================
Capital city: Canberra
Capital city: Beijing
Capital city: Paris
Capital city: Moscow
Capital city: Washington, D.C.
Capital city: Rome
Capital city: London
Capital city: Lima
Capital city: Tokyo
'''

print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")

'''
Iteration over Items
===================
Tokyo, Japan
Beijing, China
Washington, D.C., USA
London, England
Rome, Italy
Moscow, Russia
Canberra, Australia
Paris, France
Lima, Peru
'''

print("Checking Membership")
print("===================")

print('England' in capitals)
print('Lima' in capitals)

print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())

'''
Checking Membership
===================
True
False
False
True
False
True
'''
