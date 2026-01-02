malik = {
    "animal": "dog",
    "owner": "david",
}

sakura = {
    "animal": "cat",
    "owner": "geraldine",
}

poli = {
    "animal": "australian parrot",
    "owner": "maria",
}

snivy = {
    "animal": "ball python",
    "owner": "david",
}

pets = [malik, sakura, poli, snivy]

for pet in pets:
    print(f"{pet["owner"]}, has a {pet["animal"]}")