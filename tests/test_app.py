import pytest

from src.app import EmployeeManager


def test_add_employee():
    manager = EmployeeManager()

    manager.add_employee(
        employee_id=1001,
        name="Alice Johnson",
        department="Security Operations"
    )

    employee = manager.get_employee(1001)

    assert employee["name"] == "Alice Johnson"
    assert employee["department"] == "Security Operations
    

def test_total_employees():
    manager = EmployeeManager()

    manager.add_employee(1001, "Alice", "Security")
    manager.add_employee(1002, "Bob", "Engineering")

    assert manager.total_employees() == 2


def test_remove_employee():
    manager = EmployeeManager()

    manager.add_employee(1001, "Alice", "Security")
    manager.remove_employee(1001)

    assert manager.get_employee(1001) is None


def test_duplicate_employee():
    manager = EmployeeManager()

    manager.add_employee(1001, "Alice", "Security")

    with pytest.raises(ValueError):
        manager.add_employee(1001, "Alice", "Security")


def test_remove_nonexistent_employee():
    manager = EmployeeManager()

    with pytest.raises(ValueError):
        manager.remove_employee(9999)


def test_get_nonexistent_employee():
    manager = EmployeeManager()

    assert manager.get_employee(9999) is None