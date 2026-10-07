students = ["Nurislam", "Olzhas", "Elaman"]

def find_student(name):
    for s in students:
        if s.lower() == name.lower():
            return s
    return None