countries = [country for country in input().split(', ')]
capitals = [capital for capital in input().split(', ')]
# [print(f"{countries[p]} -> {capitals[p]}") for p in range(len(countries))]
c_p = zip(countries, capitals)
[print(f"{p[0] }{p[1]}") for p in c_p]