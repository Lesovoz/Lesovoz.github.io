from area import area

obj = {'type': 'Polygon', 'coordinates': [
        [[-180, -90], [-180, 90], [180, 90], [180, -90], [-180, -90]]]}
print(area(obj))
