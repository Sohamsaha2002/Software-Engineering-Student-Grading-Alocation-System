def main():
    # name,mark
    marks= {}
    with open ("marking.csv") as file:
        for line in file:
            roll,name,phy,che,bio,math,computer,grade = line.strip().split(",")
            marks[roll] = [name,phy,che,bio,math,computer,grade]
    print(marks)
    print("Welcome to the Marking System")
    print("1. Add a new student")
    print("2. Delete a student")
    print("3. Update a student's marks")
    print("4. View a student's marks")
    print("5. View all students' marks")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addStudent(marks)
    elif choice == 2:
        deleteStudent(marks)
    elif choice == 3:
        updateStudent(marks)
    elif choice == 4:
        viewStudent(marks)
    elif choice == 5:
        viewAll(marks)
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        main()
    main()

def addStudent(marks):
    roll = input("Enter roll number: ").strip()
    if roll in marks:
        print("Student already exists")
        main()
    name = input("Enter name: ").strip()
    phy = input("Enter Physics marks: ").strip()
    che = input("Enter Chemistry marks: ").strip()
    bio = input("Enter Biology marks: ").strip()
    math = input("Enter Mathematics marks: ").strip()
    computer = input("Enter Computer Science marks: ").strip()

    grade = calculateGrade(phy,che,bio,math,computer)
    marks[roll] = [name,phy,che,bio,math,computer,grade]
    print("Student added successfully")
    store_marks(marks)

def deleteStudent(marks):
    roll = input("Enter roll number: ").strip()
    if roll not in marks:
        print("Student does not exist")
        main()
    del marks[roll]
    print("Student deleted successfully")
    store_marks(marks)


def updateStudent(marks):
    roll = input("Enter roll number: ").strip()
    if roll not in marks:
        print("Student does not exist")
        return
    name = input("Enter name: ").strip()
    phy = input("Enter Physics marks: ").strip()
    che = input("Enter Chemistry marks: ").strip()
    bio = input("Enter Biology marks: ").strip()
    math = input("Enter Mathematics marks: ").strip()
    computer = input("Enter Computer Science marks: ").strip()

    grade = calculateGrade(phy,che,bio,math,computer)
    marks[roll] = [name,phy,che,bio,math,computer,grade]
    print("Student updated successfully")
    store_marks(marks)


def viewStudent(marks):
    roll = input("Enter roll number: ").strip()
    if roll not in marks:
        print("Student does not exist")
        main()
    print("Name:",marks[roll][0])
    print("Physics:",marks[roll][1])
    print("Chemistry:",marks[roll][2])
    print("Biology:",marks[roll][3])
    print("Mathematics:",marks[roll][4])
    print("Computer Science:",marks[roll][5])
    print("Grade:",marks[roll][6])
    print()



def viewAll(marks):
    for roll in marks:
        print("Roll:",roll)
        print("Name:",marks[roll][0])
        print("Physics:",marks[roll][1])
        print("Chemistry:",marks[roll][2])
        print("Biology:",marks[roll][3])
        print("Mathematics:",marks[roll][4])
        print("Computer Science:",marks[roll][5])
        print("Grade:",marks[roll][6])
        print()


def calculateGrade(phy,che,bio,math,computer):
    total = int(phy) + int(che) + int(bio) + int(math) + int(computer)
    if total >= 450:
        return "A"
    elif total >= 400:
        return "B"
    elif total >= 350:
        return "C"
    elif total >= 300:
        return "D"
    else:
        return "F"
    



def store_marks(marks):
    with open("marking.csv","w") as file:
        for roll in marks:
            file.write(roll+","+marks[roll][0]+","+marks[roll][1]+","+marks[roll][2]+","+marks[roll][3]+","+marks[roll][4]+","+marks[roll][5]+","+marks[roll][6]+"\n")

if __name__ == "__main__":
    main()