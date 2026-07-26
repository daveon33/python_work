from employee import Employee



def test_give_default_raise():
    new_employee = Employee('David', 'Gallego', 20000000)
    new_employee.give_raise()
    assert new_employee.annual_salary == 20005000

def test_give_custom_raise():
    new_employee = Employee('Santiago', 'Gal', 10000000)
    new_employee.give_raise(50000)
    assert new_employee.annual_salary == 10050000

