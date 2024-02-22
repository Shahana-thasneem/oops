class student:
    def details(self):
        self.name=input("enter your name")
        self.mark1=int(input("enter mark of first subject"))
        self.mark2=int(input("enter mark of second subject"))
        self.mark3=int(input("enter mark of third subject"))
    def output(self):
        print("\nName : ",self.name)
        print("marks in each subject:\nSubject 1:",self.mark1,"\nSubject 2:",self.mark2,"\nSubject 3:",self.mark3)
std=student()
stds=student()

std.details()
stds.details()
stds.output()
std.output()
