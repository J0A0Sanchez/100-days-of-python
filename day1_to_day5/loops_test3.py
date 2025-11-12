student_score = [45, 3, 182, 77, 59, 101, 200, 8, 91, 66, 34, 120, 5, 142, 89, 173, 28, 56, 134, 11]

# max = max(student_score)
# print(max)


# Doing the same as comment above (max formula) but 
# using loop for:
max = 0

for i in student_score:
    if i > max:
        max = i
    else:
        pass

print(max)