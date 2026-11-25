print("Multiplication Table")

for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row * col:4}", end=" ")
    print()

print("Table Completed!")