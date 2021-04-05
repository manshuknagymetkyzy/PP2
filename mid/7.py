students = list(map(str, input().split()))
participated = list(map(str, input().split()))
absent = []
lost = []
for student in students:
    if student not in participated:
        absent.append(student)
for student in participated:
    if student not in students:
        lost.append(student)
print("Absent:", *absent)
print("Lost:", *lost)