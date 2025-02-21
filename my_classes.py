class Employee:
    """Models an Employee class"""
    def __init__(self, f_name, l_name, job, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.job = job
        self.salary = salary
    
    def update_salary(self, new_salary):
        """Set or reassign the salary of a worker"""
        if new_salary > self.salary:
            self.salary = new_salary
        else:
            print("New salary must be greater than the current salary.")
    
    def give_bonus(self, percent=0.08):            # 8% bonus by default
        """Calculate an employee bonus base on a percentage"""
        return self.salary*percent
    
    def give_raise(self, percent=0.12):       # 12% raise by default
        """Calculate and update an employee salary base on a percentage"""
        self.salary = int(self.salary * (1 + percent))
        
    def compute_salary(self, percent=0):           # O% default in cases  where no bonus is given
        """Compute total salary for a given period(month)"""
        return int(self.salary + self.give_bonus(percent))
    
    def __repr__ (self):
        """Return employee infomation"""
        return f"Employee\n{8*'='} \nName:{self.f_name.title()} {self.l_name.title()} \nRole:{self.job} \nBasic salary:{int(self.salary)}"    

    
class Benefits():
    """Models all work benefits package available to an employee"""
    def __init__(self, f_name, l_name, pto=0, health_ins=0, life_ins=0, pension=0):
        self.f_name = f_name
        self.l_name = l_name
        self.pto = pto                          # Avg. annual paid time off 
        self.health_ins = health_ins            # Avg. annual paid health insurance plan 
        self.life_ins = life_ins                # Life insurance
        self.pension = pension                  # Pension
        
    
    def set_pto(self, days):
        self.pto = days
    
    def adjust_pto(self, used_pto):
        if self.pto > used_pto:
            self.pto -= used_pto
            print(f"You have {self.pto} days of your annual paid time off left")
        else:
            print('You no longer have any paid time off')
    
    def set_health_ins(self, amount):
        self.health_ins = amount
    
    def set_life_ins(self, amount):
        self.life_ins = amount
    
    def pay_life_ins(self):
        self.life_ins = 0
        print(f'{self.f_name.title()} {self.l_name.title()} life insurance has been paid')
    
    def set_pension(self, amount):
        self.pension = amount
    
    def pay_pension(self):
        self.pension = 0
        print(f'{self.f_name.title()} {self.l_name.title()} pension has been paid')
        
    def __repr__(self):
        str_1 = f"Benefits: \nPTO:{self.pto} days \nHealth Insurance:{self.health_ins}\n"
        str_2 = f"Life Insurance:{self.life_ins} \nPension:{self.pension}"
        return str_1 + str_2
        

class Manager(Employee):
    """Simple Model of subclass of Employee"""
    def __init__(self, f_name, l_name, salary, job='manager', dept='sales', **kwargs):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to a Manager.
        """
        super().__init__(f_name, l_name, job, salary)      
        self.dept = dept
        self.benefits = Benefits(f_name, l_name, **kwargs) 
    
    def give_bonus(self, percent=0.08, add_on=0.10):       # extra 10% bonus after 8% general bonus for avg. employee
        """
        Calculate a manger bonus base on a
        percentage and add_ons(additional bonus)
        """
        return Employee.give_bonus(self, percent + add_on)
        
    def give_raise(self, percent=0.12, add_on=0.10):       # extra 10% raise after 12% general raise for an avg. employee
        """
        Calculate and update a manger salary base 
        on a percentage and add_ons(additional bonus)
        """
        Employee.give_raise(self, percent + add_on)
    
    def compute_salary(self, percent=0, add_on=0):          # 0% by default in cases of no bonuses
        return int(self.salary + Employee.give_bonus(self, percent + add_on))
    
    def __repr__ (self):
        """Return employee infomation"""
        str_1 = f"Manager\n{7*'='} \nName:{self.f_name.title()} {self.l_name.title()}"
        str_2 = f"\nDepartment:{self.dept.title()} \nBasic salary:{int(self.salary)}"
        return str_1 + str_2