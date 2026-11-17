def compare(p1, p2):
    if p1[1] == p2[1]:
        if p1[2] == p2[2]:
            if p1[0] < p2[0]:
                return p1
            else:
                return p2
        elif p1[2] > p2[2]:
            return p2
        else:
            return p1
    elif p1[1] > p2[1]:
        return p1
    else:
        return p2
            
students = []
for i in range(3):
    name, score, absences = input().split()
    students.append((name, int(score), int(absences)))

winner = students[0]
for student in students[1:]:
    winner = compare(winner, student)

print(winner[0] if winner[1] >= 50 else "NONE")