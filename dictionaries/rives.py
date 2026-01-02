rivers = {
    "The Nile": "Egypt",
    "The Amazon": "Brazil",
    "Yangtze River": "China",
}

for river, country in rivers.items():
    print(f"{river}, runs through {country}")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)