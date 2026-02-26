for i in range(1,11):
    print(i, end=" ")
print(" ")

for i in "python":
    print(i, end=" ")
print(" ")

for i in ["hello", "world", 2, 4.5, [1,2]]:
    print(i, end=" ")
print(" ")

for i in ("hello", "world", 2, 4.5, [1,2]):
    print(i, end=" ")
print(" ")

for i in {"hello", "world", (1,2)}:
    print(i, end=" ")
print(" ")

for i in {1:1, 2:4, 3:9}.items():
    print(i, end=" ")