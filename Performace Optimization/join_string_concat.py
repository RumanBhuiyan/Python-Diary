# dont use + in string concatenation rather use join method
# + takes new memory but "".join doesn't take so you use it instead
country = ["Bangladesh","India","USA"]
print(" ".join(country))

#dont do this
country_list = country[0]+" " + country[1] +" "+country[2]
print(country_list)