
class Employee:
    def __init__(self,basic_salary=500):
        self.basic_salary = basic_salary
    def get_salary():
        pass
    
class Chef(Employee):
    def __init__(self, hourly_wage, hours, days):
        super().__init__(550)
        self.hourly_wage= hourly_wage
        self.hours = hours
        self.days=days
    def get_monthly_income(self):
        return self.hourly_wage*self.hours*self.days + self.basic_salary

class Waiter(Employee):
    def __init__(self,monthly_salary,tips):
        super().__init__(600)
        self.monthly_salary=monthly_salary
        self.tips = tips
    def get_monthly_income(self):
        return self.monthly_salary+ self.tips/2 + self.basic_salary
class Cleaner(Employee):
    def __init__(self, monthly_salary, extra_hours, extra_hour_wage):
        super().__init__()
        self.monthly_salary=monthly_salary
        self.extra_hours=extra_hours
        self.extra_hour_wage=extra_hour_wage
    def get_monthly_income(self):
        return self.monthly_salary+self.extra_hours*self.extra_hour_wage\
            +self.basic_salary
            
peter = Chef(20,8,26)
peter_income = peter.get_monthly_income()
print(peter_income)

gary = Waiter(3000,200)
gary_income = gary.get_monthly_income()
print(gary_income)

michael = Cleaner(3500,15,20)
michael_income=michael.get_monthly_income()
print(michael_income)

income = 20000
profit = income - peter_income - gary_income - michael_income
print(profit)