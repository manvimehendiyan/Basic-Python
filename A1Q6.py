def gross_salary(basic):
    gross=0
    if basic<=10000:
        gross=basic+(basic*0.2)+(basic*0.8)
    elif basic>10000 and basic<=20000:
        gross=basic+(basic*0.25)+(basic*0.9)
    else:
        gross=basic+(basic*0.3)+(basic*0.95)
    print("Your Gross Salary is ",gross)
    
salary=float(input("Enter your Basic Salary: "))
gross_salary(salary)