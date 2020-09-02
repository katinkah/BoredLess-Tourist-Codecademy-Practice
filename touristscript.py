destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination): 
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
    print("Error caught!")
    return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

  for interest in interests:
    if interest in attraction_tags:
      attractions_with_interest.append(possible_attraction[0])
  
  return attractions_with_interest


la_arts = find_attractions("Los Angeles, USA", ["art"])

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + str(traveler[0]) + ", we think you'll like these places around " + str(traveler_destination) + ":" 
  
  if len(traveler_attractions) == 0:
        interests_string = "Unfortunately there are no places around " + str(traveler_destination) + " that match those interests. But check out these attractions near you: " + str(attractions_in_city) + "."
  elif len(traveler_attractions) == 1: 
    interests_string = "Hi " + str(traveler[0]) + ", we think you'll like this place around " + str(traveler_destination) + ": the " + str(traveler_attractions[0]) + "."
  elif len(traveler_attractions) == 2:
    interests_string = "Hi " + str(traveler[0]) + ", we think you'll like this place around " + str(traveler_destination) + ": " + str(traveler_attractions[0]) + " and " + str(traveler_attractions[1]) + "."
  else:
    for i in range(len(traveler_attractions)):
      if traveler_attractions[i] == traveler_attractions[0:-2]:
        interests_string += " " + str(traveler_attractions[i]) + ","
      elif traveler_attractions[i] == traveler_attractions[-1]:
        interests_string += " and " + str(traveler_attractions[-1]) + "."
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)
