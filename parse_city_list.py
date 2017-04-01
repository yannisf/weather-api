import json

greek_towns = []
with open('city.list.json', 'r') as data:
    for line in data:
        town = json.loads(line)
        if town['country'] == 'GR':
            greek_towns.append(
                (town['_id'], town['name'], town['coord']['lat'], town['coord']['lon']))

_id, name, lat, lon = zip(*greek_towns)

# max_lat = max(lat)
# max_lon = max(lon)
# min_lat = min(lat)
# min_lon = min(lon)

# top_left = (max_lat, min_lon)
# bottom_left = (min_lat, min_lon)
# top_right = (max_lat, max_lon)
# bottom_right = (min_lat, max_lon)

# print(top_left)
# print(bottom_left)
# print(top_right)
# print(bottom_right)

for town in greek_towns:
    print("['{}', {}, {}, {}],".format(town[1], town[2], town[3], town[0]))
