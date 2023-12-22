import pandas as pd
from faker import Faker
import random

# Sample DataFrame (replace this with your actual DataFrame)
data = {'name__full': ['John Doe', 'Jane Smith'], 'email': ['jdoe@example.com', 'jsmith@example.com']}
df = pd.DataFrame(data)

# Initialize Faker
fake = Faker()

# Set to store unique names
unique_names = set()

# Function to generate a unique full name
def generate_unique_name():
    full_name = fake.name()
    while full_name in unique_names:
        full_name = fake.name()
    unique_names.add(full_name)
    return full_name

# Function to generate email from name
def generate_email(name):
    first_name, last_name = name.split(' ')[:2]
    email = f"{first_name.lower()}.{last_name.lower()}@va.gov"
    return email

# Update DataFrame with fake data
for index, row in df.iterrows():
    fake_name = generate_unique_name()
    df.at[index, 'name__full'] = fake_name
    df.at[index, 'email'] = generate_email(fake_name)

# Display the updated DataFrame
print(df)





from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate employee details
def generate_employee():
    # Generate a name
    name = fake.name()

    # Generate a random age (you can adjust the range as needed)
    age = random.randint(18, 65)

    # Generate a gender
    # Faker can generate a random 'male' or 'female' gender
    # If you need more options, you'll have to customize this part
    gender = fake.random_element(elements=('male', 'female'))

    return name, age, gender

# Generate an employee's details
employee_name, employee_age, employee_gender = generate_employee()

print(f"Name: {employee_name}, Age: {employee_age}, Gender: {employee_gender}")
