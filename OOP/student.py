class students:
    class_year=2025
    num_students=0

    def __init__ (self,name,age):
         self.name=name
         self.age=age
         students.num_students+=1

student1 =students("rohan",20)
student2 =students("mohan",21)   
student2 =students("sohan",21) 
student2 =students("bohan",21) 
print(students.num_students)
print(students.class_year)      