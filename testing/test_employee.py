import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    new_employee = Employee('David', 'Gallego', 20000000)
    return new_employee

def test_give_default_raise(new_employee):
    new_employee.give_raise()
    assert new_employee.annual_salary == 20005000

def test_give_custom_raise(new_employee):
    new_employee.give_raise(50000)
    assert new_employee.annual_salary == 20050000

