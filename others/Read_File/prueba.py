
aquarium_creatures = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]

# dato = [element for element in aquarium_creatures if  element['species'] == 'shark']

dato = list(map(lambda x:x['species'], aquarium_creatures ))

print(dato)