
def employee_info(name, employee_id, department, salary):
    """
    Accept employee details and return them as a formatted string.
    """
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {employee_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


# Example usage
if __name__ == "__main__":
    result = employee_info("sneha", 101, "IT", 50000)
    print(result)
