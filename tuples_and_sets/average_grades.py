import statistics

n = int(input())
students = {}
for _ in range(n):
    student = input().split()
    if student[0] not in students:
        students[student[0]] = []
        students[student[0]].append((float(student[1])))
    else:
        students[student[0]].append(float(student[1]))
for key, value in students.items():
    grades = ' '.join([f"{g:.2f}" for g in value])
    avr_mark = sum(value)/len(value)
    print(f"{key} -> {grades} (avg: {statistics.mean(value):.2f})")