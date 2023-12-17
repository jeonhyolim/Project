import random

class Student:
    def __init__(self, name: str, department: str):
        ### Edit Here ###
        self.__name = name
        self.__department =department
        # generate student number
        # save student info
        student_number_rand = str(random.randrange(0, 10000))
        if len(student_number_rand) !=4:
            student_number_rand += '0'*(4-len(student_number_rand))
        self.__student_number = '202171'+ student_number_rand
        #################
        
    def __str__(self):
        ### Edit Here ###
        
        # save student info
        info = "Name: {0} \nStudent ID: {1} \nDepartment: {2}".format(self.__name, self.__student_number,self.__department)
        #################
        
        return info
        
def main():
    ### Edit Here ###
    
    # get student name, department
    name = str(input("Input Student Name: "))
    department = str(input("Input Department: "))
    #################
    
    student = Student(name, department)
    
    print(student)

if __name__ == "__main__":
    main()
