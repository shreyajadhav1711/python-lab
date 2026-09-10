print("*" * 40)
print("       Bus Reservation System")
print("*" * 40)
total_rows = int(input("Enter number of rows in the bus: "))
total_columns = int(input("Enter number of columns in the bus: "))
bus_layout = []
for r in range(total_rows):
    rows = []
    for c in range(total_columns):
        rows.append("O")
    bus_layout.append(rows)
print(f"\nBus layout created: {total_rows} rows * {total_columns} columns.")
print("All seats are currently Open (O).\n")
while True:
    print("*" * 40)
    print("1. Display Bus Layout.")
    print("2. Reserve a Seat.")
    print("3. Cancel a Reservation.")
    print("4. Count Available / Reserved Seats.")
    print("5. Check a Specific Seat Status.")
    print("6. Exit.")
    print("*" * 40)
    choice = input("Enter your choice (1-6): ").strip()
    if choice == "1":
        print("\nCurrent Bus Layout:")
        print("(Rows top to bottom = Rows 1 to", total_rows, ")\n")
        for r in range(len(bus_layout)):
            print(f"Row {r + 1}: ", end="")
            for c in range(len(bus_layout[r])):
                print(bus_layout[r][c], end=" ")
            print()
        print()
    elif choice == "2":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {total_columns}): ")) - 1
        if 0 <= row_num < total_rows and 0 <= col_num < total_columns:
            if bus_layout[row_num][col_num] == "X":
                print("This seat is already reserved.\n")
            else:
                bus_layout[row_num][col_num] = "X"
                print(
                    f"Seat at Row {row_num + 1}, "
                    f"Seat {col_num + 1} reserved successfully.\n"
                )
        else:
            print("Invalid row or seat number.\n")
    elif choice == "3":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {total_columns}): ")) - 1
        if 0 <= row_num < total_rows and 0 <= col_num < total_columns:
            if bus_layout[row_num][col_num] == "O":
                print("This seat is already open.\n")
            else:
                bus_layout[row_num][col_num] = "O"
                print(
                    f"Reservation cancelled for Row {row_num + 1}, "
                    f"Seat {col_num + 1}.\n"
                )
        else:
            print("Invalid row or seat number.\n")
    elif choice == "4":
        open_count = 0
        reserved_count = 0
        for r in range(len(bus_layout)):
            for c in range(len(bus_layout[r])):
                if bus_layout[r][c] == "O":
                    open_count += 1
                else:
                    reserved_count += 1
        print(f"\nTotal Seats: {total_rows * total_columns}")
        print(f"Open Seats: {open_count}")
        print(f"Reserved Seats: {reserved_count}\n")
    elif choice == "5":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {total_columns}): ")) - 1
        if 0 <= row_num < total_rows and 0 <= col_num < total_columns:
            status = bus_layout[row_num][col_num]
            if status == "O":
                print(
                    f"Seat Row {row_num + 1}, Seat {col_num + 1} "
                    f"is Open.\n"
                )
            else:
                print(
                    f"Seat Row {row_num + 1}, Seat {col_num + 1} "
                    f"is Reserved.\n"
                )
        else:
            print("Invalid row or seat number.\n")
    elif choice == "6":
        print("Exiting program. Thank you.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
