from ps1_partition import get_partitions
a = 0
cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}


# def is_list(oko):
#     if isinstance(oko, list):
#         for i in oko:
#             # print("tak", i)
#             is_list(i)

#     else:
#         # print("nie", oko)
#         return oko

# print(isinstance("oko", list))

for item in (get_partitions(cows)):
    for i in item:
        x = []
        weight = 0
        for j in i:
            weight += cows[j]
            x.append(j)
            # print(cows[j])
        print(weight)
        # print(x)
# print(x)
# print(len(item), " - ", item)
#     for i in item:
#         if isinstance(i, list):

# a += cows[i]
# print("tot: ", a)

# print('is_list("oko"): ', is_list(["oko", "o"]))

# myGen = get_partitions(cows)

# x = next(myGen)

# print(x)
