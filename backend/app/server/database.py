import asyncpg
import os


#DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
#    user=os.environ["DB_USER"],  
#    password=os.environ["DB_PASSWORD"],  
#    host=os.environ["DB_HOST"],  
#    port=os.environ["DB_PORT"],  
#    dbname=os.environ["DB_NAME"],  
#)


# Initialize connection to PostgreSQL
async def init_db():
    return await asyncpg.connect(DATABASE_URL)

# Define a helper function to format the employee data as a dictionary
def employee_helper(employee) -> dict:
    return {
        "id": employee["id"],
        "firstName": employee["first_name"],
        "lastName": employee["last_name"],
        "profile": employee["profile"],
        "salary": employee["salary"],
        "integration": employee["integration"]
    }

# Retrieve all employees present in the database
async def retrieve_employees():
    conn = await init_db()
    employees = []
    rows = await conn.fetch("SELECT * FROM employees_collection")
    for row in rows:
        employees.append(employee_helper(row))
    await conn.close()
    return employees

# Add a new employee to the database
async def add_employee(employee_data: dict) -> dict:
    conn = await init_db()
    query = """
    INSERT INTO employees_collection (first_name, last_name, profile, salary, integration)
    VALUES ($1, $2, $3, $4, $5) RETURNING id
    """
    employee_id = await conn.fetchval(
        query, 
        employee_data["firstName"], 
        employee_data["lastName"], 
        employee_data["profile"], 
        employee_data["salary"], 
        employee_data["integration"]
    )
    employee_data["id"] = employee_id
    await conn.close()
    return employee_data

# Retrieve an employee with a matching ID
async def retrieve_employee(id: int) -> dict:
    conn = await init_db()
    query = "SELECT * FROM employees_collection WHERE id = $1"
    employee = await conn.fetchrow(query, id)
    await conn.close()
    if employee:
        return employee_helper(employee)

# Update an employee with a matching ID
async def update_employee(id: int, data: dict) -> bool:
    if not data:
        return False
    
    conn = await init_db()
    set_query = ", ".join([f"{k} = ${i+2}" for i, k in enumerate(data.keys())])
    query = f"UPDATE employees_collection SET {set_query} WHERE id = $1"
    values = [id] + list(data.values())
    
    result = await conn.execute(query, *values)
    await conn.close()
    return result == "UPDATE 1"

# Delete an employee from the database
async def delete_employee(id: int) -> bool:
    conn = await init_db()
    query = "DELETE FROM employees_collection WHERE id = $1"
    result = await conn.execute(query, id)
    await conn.close()
    return result == "DELETE 1"