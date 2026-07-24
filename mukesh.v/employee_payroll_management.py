employee=[]



while True:
    choose = input('please choose an option from the following menu: \n 1. Add employee \n 2. Calculate salary \n 3. Search employee \n 4. List all employees \n 5. Exit \n')
    
    match choose:
        case '1':
            for i in range(5):
                name = input('please enter employee name ')
                employee_id = input('please enter your id ')
                department = input('please enter your department ')
                basic_salary = int(input('please enter your basic salary '))        
                employee.append({
                    'name': name, 
                    'id': employee_id, 
                    'department': department, 
                    'basic_salary': basic_salary})
                print('employee added successfully')
        case '2':
            tax=0.05*basic_salary
            hra=0.1*basic_salary
            ba=0.1*basic_salary
            salary =hra+ba+basic_salary-tax
            print(f'salary calculated successfully here is your total salary amount: {salary}')
        case '3':
            search_id = input('please enter the id of the employee you want to search for ')
            for emp in employee:
                if emp['id'] == search_id:
                    print ('here is the employee you searched for:22')
                    print(f'Employee found: Name: {emp["name"]}, ID: {emp["id"]}, Department: {emp["department"]}, Basic Salary: {emp["basic_salary"]}')
                    break
            else:
                print('Employee not found')
           
        case '4':
            print(f'here is the list of all employees: ')
            for emp in employee:
                print (f'''
                    name : {emp['name']},
                    id : {emp['id']},''')
        case '5':
            print('Nandri vanakam')
            break
    
performance = input(f'are you eligible for performance bonus? (yes/no) ')
bonus= lambda basic_salary: 0.1*basic_salary if performance.lower() == 'yes' else 0
if performance.lower() == 'yes':
    print(f'you are eligible for performance bonus of {bonus(basic_salary)} and your total salary is {salary+bonus(basic_salary)}')
else:
    print(f'Sorry, you are not eligible for performance bonus this time and your total salary is {salary}')
    print('Nandri vanakam!, kk')

grade = None    
if salary >= 80000:
    grade = 'A'
    print('you are Grade A employee')
elif salary >= 60000 and salary < 80000:
    grade = 'B'
    print('you are Grade B employee')
elif salary >= 40000 and salary < 60000:
    grade = 'C'
    print('you are Grade C employee')
else :
    grade = 'D'
    print('you are Grade D employee')


print (name.upper())
print (name.lower())
print (name[:3])
print (name[3:])
print(name[::-1])
string_search = input('please enter a character to search in your name ')
print(string_search in name)

print(name)
print(employee_id)
print(department)
print(basic_salary)
print(salary)
print(bonus(basic_salary))
print(grade)