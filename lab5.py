rows = 8
cols = 35

for i in range(rows):
    for j in range(cols):
        # Print border
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()




print("--------------------------------------------------------------------------")




rows = 5

for i in range(1, rows + 1):
    for j in range(1, 6):
        print(j, end=" ")
    print()



print("---------------------------------------------------------------------------")



rows = 7
cols = 25

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        elif j == 5:
            print(i, end="")
        else:
            print(" ", end="")
    print()



print("-------------------------------------------------------------------------------")




print("*" * 30)
print("        RECEIPT")
print("*" * 30)

for i in range(1, 6):
    print("Item", i, ":", "*" * i)

print("*" * 30)
print("      THANK YOU")
print("*" * 30)
