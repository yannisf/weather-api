import json

cities = []

with open('city.list.json', 'r') as data:
    for line in data:
        city = json.loads(line)
        cities.append(city)

greek_towns = []
for city in cities:
    if city['country'] == 'GR':
        coord = (city['coord']['lat'],city['coord']['lon'])
        greek_towns.append(coord)

for coords in greek_towns:
    print (coords)

maxs = map(max, zip(*coords))
mins = map(min, zip(*coords))

print (maxs)
print (mins)

# top_left = (mins[0],maxs[1])
# bottom_left = (mins[0],mins[1])
# top_right = (maxs[0],maxs[1])
# bottom_right = (maxs[0],mins[1])

