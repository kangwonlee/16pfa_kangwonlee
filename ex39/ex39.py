# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: %s" % states['Michigan'])
print("Florida's abbreviation is: %s" % states['Florida'])

# print every state abbreviation
print('-' * 10)
print("stats = %s" % states)
print("states.items() = %s" % str(states.items()))
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]
    ))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Not Entered Yet')
print("The city for the state 'TX' is: %s" % city)

# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성