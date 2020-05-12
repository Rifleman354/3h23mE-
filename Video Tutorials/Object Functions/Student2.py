class Student_Class:

    def __init__(self, name, major, gpa):
        self.name = str(name)
        self.major = str(major)
        self.gpa = int(gpa)
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
