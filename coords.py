import json
import numpy as np
import matplotlib.pyplot as plt

def lat_lng_to_pixels(lat, lng):
    lat_rad = lat * np.pi / 180.0
    lat_rad = np.log(np.tan((lat_rad + np.pi / 2.0) / 2.0))
    x = 100 * (lng + 180.0) / 360.0
    y = 100 * (lat_rad - np.pi) / (2.0 * np.pi)
    return (x, y)

greek_towns = []
with open('city.list.json', 'rt', encoding='utf8') as data:
    for line in data:
        town = json.loads(line)
        if town['country'] == 'GR':
            greek_towns.append((town['coord']['lat'], town['coord']['lon']))

cart = [lat_lng_to_pixels(lat, lng) for lat,lng in greek_towns]

# plt.scatter(*zip(*cart))


px,py=zip(*cart)

plt.figure(figsize=(10, 8))
plt.axis('equal')
plt.xlim(min(px), max(px))
plt.ylim(min(py), max(py))
plt.axis('off')
# plt.gca().set_axis_bgcolor('white')
plt.scatter(px,py, s=.8, alpha=.8)

plt.show()

