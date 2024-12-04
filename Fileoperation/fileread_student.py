

f1=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\all_students.txt")

f2=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\failed.txt")

all_students_set=set()

failed_student_set=set()

for line in f1:

    line=line.rstrip("\n")

    all_students_set.add(line)

for line in f2:

    line=line.rstrip("\n")

    failed_student_set.add(line)

passed_students=all_students_set.difference(failed_student_set)

print(passed_students)

f1.close()
f2.close()
