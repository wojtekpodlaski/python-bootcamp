


print("   ", end="")
for x in range (10):
    print(f"{x:3}", end="")
print()
print()

for x in range(10):
    print(x, end="  ")
    for y in range (1, 10) :
        print(f"{x*y:4}", end="")
    print()

