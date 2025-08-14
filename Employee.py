#Employee data management software with classification
def emp_statistics(emps):
    salas=[salary for salary,name in emps]
    print("="*40)
    print("employees numbers : ",len(emps))
    print(f"total salaries : {sum(salas)}")
    print(f"hieghtest salary : {max(salas)}")
    print(f"lowest salary  : {min(salas)}")
    print(f"average salary : {sum(salas)/len(salas)}")
    print("*"*40)
#//////////////////////////////////
def emp_rating(emps):
    high=[]
    medium=[]
    low=[]
    
    for salary,name in emps:
        if salary >= 800:
            high.append(name)
        elif salary >=500:
            medium.append(name)
        else:
            low.append(name)
        
    print("classification by salary:")
    print("high salaries" if high else "nothing")
    for h in high:
        print(" ",h)
    print("medium salaries" if medium else "nothing")
    for m in medium:
        print(" ",m)
    print("low salaries" if low else "nothing")
    for l in low:
        print(" ",l)
    print("*"*40)
#///////////////////////////////////
#search function
def search_emp(emps):
    search_name=input("enter employee name to search :")
    existing=False
    for salary,name in emps:
        if search_name ==name:
             print(f"the employee {name} existing and his salary is {salary}")
             existing=True
             break
    if not existing:
        print("the employee is not existing")
        
#//////////////////////////////////
employees=[]
numbers=int(input("how many employees do you want to enter?"))
for i in range(numbers):
    name=input("enter employee name :")
    salary=float(input("enter employee salary :"))
    employees.append((salary,name))
    
    
#////////////////////////////////////
emp_statistics(employees)
emp_rating(employees)
search_emp(employees)
    
    

    
    
    
    
    
    
