# create mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#basic set of states and some cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Flordia's abbreviation is: ", states['Florida'])

#do it by using the same state, then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida ha: ", cities[states['Florida']])

#print every abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get an abbrevation by state that may not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for state 'TX' is: {city}")