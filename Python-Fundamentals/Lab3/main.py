


def add_student():
   id = int(input("Enter student ID: "))
   name = input("Enter student name: ")   

   found = False

   file = open("students.txt", "r")
   for line in file:
      studentId = int(line.split(",")[0])
      if studentId == id:
         found = True
         break
   file.close()

   if found:
      print("Student ID exists")
   else:
      file = open("students.txt", "a")
      file.write(f"{id}, {name}\n")
      file.close()


def add_Subject():
   studentId = int(input("Enter student ID: "))
   subjectName = input("Enter subject: ")
   grade = input("Enter grade: ")

   file = open("subjects.txt", "a")
   file.write(f"{studentId}, {subjectName}, {grade}\n")
   file.close()


def readStudents():
   file = open("students.txt", 'r')
   for line in file:
      id, name = line.strip().split(", ")
      print(name)


def readGrades(subject):
   file = open("subjects.txt", 'r')
   for line in file:
      id, subjectName, grade = line.strip().split(",")
      if(subjectName.strip() == subject):
         print(f"{id}, {subjectName}, {grade}")

   file.close()


def getStudentInfo():
   studentId = int(input("Enter student ID: "))
   file1 = open("students.txt", 'r')

   for line1 in file1:
      line1 = line1.strip()
      if not line1:
         continue

      id, name = line1.split(",")

      if(int(id) == studentId):
         print(f"----- Student Name: {name} -----")
         print("----- Subjects and Grades ----- ")
         
         file2 = open("subjects.txt", 'r')
         for line2 in file2:
            line2 = line2.strip()
            id2, subjectName, grade = line2.split(",")
            if(int(id2) == studentId):
               print(f"| {subjectName.strip()}: {grade.strip()} |")

         file2.close()

   file1.close()


def getAvgGrades():
    studentId = int(input("Enter Student ID: "))
    file = open("subjects.txt", 'r')
    total = 0
    count = 0

    for line in file:
        line = line.strip()
        if not line:
            continue

        id, subName, grade = line.strip().split(",")

        if int(id.strip()) == studentId:
            total += float(grade.strip())
            count += 1

    file.close()

    if count == 0:
        return 0

    return total / count
      


add_student()

#add_Subject()

#readStudents()

#readGrades('Python')



#getStudentInfo()

#print(getAvgGrades())