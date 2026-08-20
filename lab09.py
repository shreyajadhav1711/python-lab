student_names = []
student_marks = []

while True:
    print("=" * 40)
    print("STUDENT MARKS MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1.insert student record")
    print("2.delete student record")
    print("3.update student marks")
    print("4.traverse/display all records")
    print("5.search student")
    print("6.show statistics")
    print("7.exit")
    print("=" * 40)

    choice = input("Enter your choice(1-7:)").strip()

    #--------------------------INSERTION-----------------------------
    if choice =='1':
        name = input("Enter student name:").strip()

        if name in student_names:
            print(f"student'{name}' already exists! use update option instead.\n")
        else:
            marks = float(input(f"Enter marks for {name}:"))
            student_names.append(name)
            student_marks.append(marks)
            print(f"Record for'{name}' inserted successfully.\n")

    #-----------------------------DELETION-----------------------------
    elif choice =='2':
        name = input("Enter student name to delete:").strip()

        if name in student_names:
            index = student_names.index(name) #find position
            student_names.pop(index) #deletion from list
            student_marks.pop(index)
            print(f"Record for '{name}' deleted successfully.\n")
        else:
            print(f"Student '{name}' not found.\n")

    #---------------------------UPDATION-------------------------------
    elif choice =='3':
         name = input("Enter student name to update:").strip()

         if name in student_names:
             index = student_names.index(name)
             new_marks = float(input(f"Enter new marks for {name}:"))
             student_marks[index] = new_marks #update by index
             print(f"marks for '{name}' updated successfully.\n")
         else:
            print(f"student'{name}' not found.\n")   

    #-------------------------TRAVERSAL-------------------------------
    elif choice == '4':
        if len(student_names) == 0:
            print("No records to display.\n")
        else:
            print("\n{:<5} {:<20} {:<10}".format("no.", "name", "marks"))
            print("-" * 35) 
            for i in range(len(student_names)):
                print("{:<5} {:<20} {:<10}".format(i + 1 , student_names[i], student_marks[i]))
            print()

    elif choice =='5':
        name = input("Enter student name to seach:").strip()

        if name in student_names:
            index = student_names.index(name)
            print(f"{name} -> marks: {student_marks[index]}\n")
        else:
            print(f"student'{name}' not found.\n")

    #----------------------------STATISTICS--------------------------------------
    elif choice == '6':
        if len(student_marks) == 0:
            print("no records available for statistics.\n")
        else:
            total = sum(student_marks)
            average = total/len(student_marks)
            highest = max(student_marks)
            lowest = min(student_marks)

            topper_index = student_marks.index(highest)
            weakest_index = student_marks.index(lowest)

            print("\n--------Class statistics------")
            print(f"total students : {len[student_names]}")
            print(f"avearge marks : {average:.2f}")
            print(f"highest marks : {highest} (student: {student_names[topper_index]})")
            print(f"lowesr marks : {lowest} (student: {student_names[weakest_index]})")
            print()

    #--------------------------------EXIT------------------------------------------
    elif choice == '7':
        print("Exiting program.Thank you!")
        break

    else:
        print("Invalid choice. please enter a number between 1 and 7.\n")