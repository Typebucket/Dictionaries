dict = {2:"School", 3:"House", 4:"School", 5:"School"}
value = "School"
count = 0
for x in dict:
    if dict[x] == value:
        count +=1
print("The frequency of", value, "is", count)