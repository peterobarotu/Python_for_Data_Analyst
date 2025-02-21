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