#list containing lists
odds = [7, 5, 9, 1, 13, 11, 3] #odd numbers
evens = [8, 4, 10, 6, 2] #even numbers
prime_numbers = [2,3,5,7,11,13,17,19,23,29,31]
special_numbers_list = [
  odds, evens, prime_numbers
]

#a list containing dictionaries
state_capitals = {
"Washington" : "Olympia",
"Oregon" : "Salem",
"Idaho" : "Boise",
"Montana" : "Helena"
}

state_population = {
  "Washington" : "7.61 million",
  "Oregon": "4.21 million",
  "Idaho": "1.78 million",
  "Montana": "1.06 million"
}

info_about_some_states = [state_population, state_capitals]

#dictionary containing a list and another dictionary
states_and_cities_as_dictionary = { #dictionary level 1
  "Washington": { #dictionary level 2
    'major_cities': ['Seattle', 'Spokane','Tacoma'], #list
    'capital_city': 'Olympia' 
  },
  "Oregon" : {
    'major_cities': ['Portland', 'Bend','Eugene', 'Corvallis'],
    'capital_city': 'Salem'
  },
  "California" : {
    'major_cities': ['Los Angeles', 'San Francisco','San Diego'],
    'capital_city': 'Sacramento'
  }
}


# Iterating over a list of lists
for inner_list in special_numbers_list:
  for inner_element in inner_list:
    print("Inner Element:", inner_element) 


# Iterating over a list of dictionaries
for inner_dictionary in info_about_some_states:
  for key in inner_dictionary:
    print("Key  :",key)
    print("Value:",inner_dictionary[key])

    
# Iterating over just the innermost level of a nested collection with only one for loop
for city in states_and_cities_as_dictionary['Oregon']['major_cities']:
  print(city)
