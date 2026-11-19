from employee import employee_info

def test_employee_info():
    # Sample employee data
    name = "John"
    employee_id = 101
    department = "IT"
    salary = 50000

    # Expected output
    expected = (
        "Employee Name: John\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    # Actual output
    result = employee_info(name, employee_id, department, salary)

    # Compare actual and expected output
    assert result == expected