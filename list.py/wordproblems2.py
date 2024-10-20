# You are given a list of tuples where each tuple contains a
# student's name and their score on a test:
# students = [('Alice', 85), ('Bob', 90), ('Charlie', 78),
# ('David', 92)].
# Write a program that converts this list into a dictionary where the student's name is the
# key and their score is the value. Then, print the names of students who scored above 80

students = [('alice', 85), ('bob', 90), ('charlie', 78), ('david', 92)]

student_dict ={name: score for name, score in students}

for name, score in student_dict.items():
    print(name)