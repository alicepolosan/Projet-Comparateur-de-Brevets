import json

def calcul(list):
    L = []
    L.append(json.dumps(['2021','2022','2023','2024']))
    L.append(json.dumps([3600, 6600, 11000, 13600]))
    L.append(json.dumps([3000, 6200, 9100, 13700]))
    L.append(json.dumps([3000, 3200, 2900, 4000]))
    L.append(json.dumps([3600, 3000, 3500, 2600]))
    return json.dumps(L)


