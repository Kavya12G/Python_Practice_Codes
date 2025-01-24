class Employee:
    def __init__(self,name,age,designation):
        company_name = 'code' #class Based 
        self.name = name
        self.age = age
        self.designation = designation

    def login(self,time):
        print(f'{self.name} logged in at {time}')

    def logout(self,time):
        print(f'{self.name} logged in at {time}')

    def work(self,hours):
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee Designation: ',self.designation)

e1 = Employee('Ak',24,'SDE')
e2 = Employee('pk',34,'Manager')
e3 = Employee('rk',30,'Developer')

e1.getDetails()
e2.getDetails()
e3.getDetails()