# main.py
from fn_generate_data import fake_gen  # Importing directly from the file

def main():
    table_name = 'hired_employees'
    quantity = 1000
    hired_employees_data = fake_gen(table_name, quantity)
    print(f"=== {table_name.capitalize()} ===")
    print(hired_employees_data.head())

    table_name = 'departments'
    quantity = 1000
    departments_data = fake_gen(table_name, quantity)
    print(f"=== {table_name.capitalize()} ===")
    print(departments_data.head())

    table_name = 'jobs'
    quantity = 1000
    jobs_data = fake_gen(table_name, quantity)
    print(f"=== {table_name.capitalize()} ===")
    print(jobs_data.head())

if __name__ == "__main__":
    main()
