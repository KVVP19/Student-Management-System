import json
try:
    with open("students.json","r") as file:
        students = json.load(file)
except (FileNotFoundError,json.JSONDecodeError):
    students =[]
while True:
    print("=====STUDENT MANAGEMENT SYSTEM=====")

    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Student by name")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        if student_id.strip() == "":
            print("Student ID cannot be empty")

          #check for duplicate student ID
        duplicate = False
        for student in students:
            if student["id"] == student_id:
                duplicate = True
                break
        if duplicate:
            print("Student ID is already exist")
            continue

        name = input("Enter student name: ")
        age = input("Enter student age: ")
        if not age.isdigit():
            print("Age must contain numbers only")
            continue
        age = int(age)
        if age < 1 or age>120:
            print("Age must be between 1 and 120")
            continue
        course = input("Enter course : ")
        if course.strip() == "":
            print("Course cannot be empty")
            continue

        student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        }
        students.append(student)

        with open("students.json","w") as file:
          json.dump(students,file,indent=4)

        print("\nStudent Added Successfully")
    elif choice == "2":
        if len(students) == 0:
            print("No Student Found")
        else:
            print("\n=====All Students=====\n")
            print(f"{'ID':<10}{'NAME':<25}{'AGE':<8}{'COURSE':<20}")
            print("-" * 63)
        for student in students:
            print(f"{student ['id']:<10}"
                  f"{student['name']:<25}"
                  f"{student['age']:<8}"
                  f"{student.get('course','Not Added'):<20}")
        print("\n Total Students:",len(students))
    elif choice == "3":
        search_id = input("Enter student ID or Name: ").strip()

        found = False
        for student in students:
            if (student["id"].lower() == search_id.lower()
                    or student["name"].lower() == search_id.lower()):

                print("\n=====STUDENT FOUND=====")
                print("ID: ", student["id"])
                print("Name: ", student["name"])
                print("Age: ", student["age"])
                print("Course: ",student["course"])
                found = True
                break
        if not found :
            print("\n=====STUDENT NOT FOUND=====")
    elif choice == "4":
        update_id = input("Enter student ID to update: ")
        found = False
        for student in students:
            if student["id"] == update_id:
                print("\n=====Student Foud!=====")
                new_name=input("Enter new name: ")
                if new_name.strip() == "":
                    print("Name cannot be empty")
                    break
                new_age=input("Enter new age: ")
                if not new_age.isdigit():
                    print("Age must be contain numbers only")
                    continue
                new_age = int(new_age)
                if new_age < 1 or new_age>120:
                    print("Age must be between 1 and 120")
                    break
                new_course = input("Enter new course: ")
                if new_course.strip() == "":
                    print("Course cannot be empty")
                    break
                student["name"]=new_name
                student["age"]=new_age
                student["course"]=new_course

                with open("students.json","w") as file:
                  json.dump(students,file,indent=4)
                print("\nStudent Updated Successfully")
                found = True
                break
        if not found :
            print("\n=====STUDENT NOT FOUND=====")


    elif choice == "5":
        delete_id = input("Enter student ID to delete: ")
        found = False
        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("\nStudent Deleted Successfully")
                found = True
                break
        if not found :
            print("\n=====STUDENT NOT FOUND=====")
    elif choice == "6":
        if not students:
            print("\n=====No Students to sort!")
        else:
            students.sort(key=lambda student : student["name"].lower())
            print("Student sorted by name successfully")

    elif choice == "7":
        print("Good bye")
        break
    else:
        print("Invalid Choice")


