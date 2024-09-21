grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = []
list_grades = []
dict_average_score = {}

for i in range(len(students)):
    list_students.append(students.pop())
    list_grades.append(sum(grades[i])/len(grades[i]))

list_students.sort()

for i in range(len(list_students)):
    dict_average_score.update({list_students[i] : list_grades[i]})
print(dict_average_score)
