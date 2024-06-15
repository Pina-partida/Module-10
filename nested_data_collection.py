#list containing lists
odds = [7, 5, 9, 1, 13, 11, 3] #odd numbers
evens = [8, 4, 10, 6, 2] #even numbers
prime_numbers = [2,3,5,7,11,13,17,19,23,29,31]
special_numbers_list = [0, odds, evens, prime_numbers]


# two dictionaries
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

# a list that contains the two dictionaries
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

# examples of retrieving elements from inside these nested data collections
print("Some even numbers are", special_numbers_list[2])
print("The population of Oregon is", info_about_some_states[0]['Oregon'])
print("The capital of Oregon is", states_and_cities_as_dictionary['Oregon']['capital_city'])
