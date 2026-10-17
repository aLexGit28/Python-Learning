import pandas as pd

names = []
marks = []

n = int(input("How many students? "))

for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    mark = int(input(f"Enter marks of {name}: "))

    names.append(name)
    marks.append(mark)

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("\nFull DataFrame:")
print(df)

print("\nStudent Names:", names)

roll = int(input("\nEnter roll number (0 to n-1) to view details: "))
print(df.loc[roll])

roll = int(input("\nEnter roll number to update marks: "))
new_marks = int(input("Enter new marks: "))

df.loc[roll, "Marks"] = new_marks

print("\nUpdated DataFrame:")
print(df)