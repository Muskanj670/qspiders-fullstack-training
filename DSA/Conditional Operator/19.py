marks = int(input("Enter the marks: "))
print("Distinction" if marks >= 75 else "First Class" if marks >= 60 else "Second Class" if marks >= 50 else "Pass" if marks >= 35 else "Fail")