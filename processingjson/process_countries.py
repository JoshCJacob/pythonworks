
from json import load

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\countries.json",encoding="utf-8")

data=load(f)

# print the no. of countries

# print(len(data))


# print all countries

all_country_names=[country.get("name") for country in data]

# print(all_country_names)


# print all region

all_regions=[country.get("region") for country in data]

# print(set(all_regions))


# print all region count

region_count={region:all_regions.count(region) for region in all_regions}

# print(region_count)


# print max. region count in countries

max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count,region_count.get(max_region_count))


# capital of India

country_captial=[country.get("capital") for country in data if country.get("name")=="India"]

# print(country_captial)


# countries with most number of borders

country_borders={country.get("name"):len(country.get("borders",[])) for country in data}

# print(country_borders)

max_country_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_country_border)


# most populated country


most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")

print(most_populated_country)


# names of countries sharing India border
