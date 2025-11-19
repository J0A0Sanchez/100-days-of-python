"""Figure out on how to print the letter 'D' from the nested list
below"""

nested_list = ["A","B",["C","D"]]

for item1 in nested_list:
    for item in item1:
        if item == "C":
            print(item)

print(nested_list[2][0])