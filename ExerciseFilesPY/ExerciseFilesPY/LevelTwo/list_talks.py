marvel_heros = ["Spiderman", "Ironman", "Thor"]
dc_heros = ["Batman", "Flash", "Aquaman", "Batman"]


print(dc_heros[1:2])

del dc_heros[1]
print(dc_heros)

dc_heros.append("Flash")
print(dc_heros)

dc_heros.insert(1, "Green Arrow")
print(dc_heros)

dc_heros.remove("Flash")
print(dc_heros)

dc_heros.reverse()
print(dc_heros)

print(dc_heros.count("Batman"))

print(len(dc_heros))