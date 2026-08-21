print("First Program in Visual Studio Code\n")

# Dictionaries -- Introduction
marks = {"Mathematics": 80, "Basic Science": 70, "English Language": 90}
print(marks) 

average_mark = sum(marks.values()) / len(marks)
highest_mark = max(marks.values())
highest_subject = max(marks, key=marks.get)

print("\nAverage mark:", average_mark)
print("Highest mark:", highest_mark)
print("Subject with highest mark:", highest_subject, "\n")
