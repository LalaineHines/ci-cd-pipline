"""
Simple Employee Management Application

Used to demonstrate:
- Unit testing
- Static security scanning
- Dependency scanning
- CI/CD security automation
"""

from typing import Dict


class EmployeeManager:
    
    def __init__(self):
        self.employees: Dict[int, dict] = {}

    def add_employee(self, employee_id: int, name: str, department: str):
        """Add a new employee."""

        if employee_id in self.employees:
            raise ValueError("Employee already exists.")
        
        self.employees[employee_id] = {
            "name": name,
            "department": department
        }

    def get_employee(self, employee_id: int):
        """Retrieve employee information."""

        return self.employees.get(employee_id)
    
    def remove_employee(self, employee_id: int):
        """Remove employee from system."""

        if employee_id not in self.employee:
            raise ValueError("Employee not found.")
        
        del self.employees[employee_id]

    def total_employees(self):
        """Return total employee count."""

        return len(self.employees)
    

def main():
    manager = EmployeeManager()

    manager.add_employee(
        employee_id=1001,
        name="Alice Johnson",
        department="Security Operations"
    )

    employee = manager.employee(1001)

    print("Employee Record")
    print("-" * 30)
    print(employee)
    print(f"Total Employees: {manager.total_employees()}")


if __name__ == "__main__":
    main()