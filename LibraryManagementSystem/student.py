students = []

def add_student(name, reg):
    students.append((name, reg))
    print("Added:", name)

def show_students():
    print("Students:")
    for s in students:
        print(s)


add_student("Ravi", 101)
add_student("Anu", 102)
add_student("Kumar", 103) 
show_students()
