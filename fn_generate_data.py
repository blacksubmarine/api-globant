# fake_data_generator.py
from faker import Faker
import pandas as pd
import random

def fake_gen(table_name, quantity):
    faker = Faker()
    data = []

    if table_name == 'hired_employees':
        for _ in range(quantity):
            id_value = faker.random_int(min=1, max=10000)
            if random.random() < 0.1:  # 10% chance of having a null id
                id_value = None
            data.append({
                'id': id_value,
                'name': faker.name(),
                'hire_datetime': faker.date_time_this_decade(),
                'department_id': faker.random_int(min=1, max=10),
                'job_id': faker.random_int(min=1, max=5)
            })
    
    elif table_name == 'departments':
        for _ in range(quantity):
            id_value = faker.random_int(min=1, max=100)
            if random.random() < 0.1:  # 10% chance of having a null id
                id_value = None
            data.append({
                'id': id_value,
                'department': faker.job(),
            })
    
    elif table_name == 'jobs':
        for _ in range(quantity):
            id_value = faker.random_int(min=1, max=50)
            if random.random() < 0.1:  # 10% chance of having a null id
                id_value = None
            data.append({
                'id': id_value,
                'job': faker.job(),
            })
    
    else:
        raise ValueError(f"Unsupported table name '{table_name}'. Supported tables: 'hired_employees', 'departments', 'jobs'")
    
    return pd.DataFrame(data)
