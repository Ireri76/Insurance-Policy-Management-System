# main.py
import csv
from policyholder import Policyholder
from product import Product
from payment import Payment

# Load policyholders, products, and payments from the CSV
policyholders = []
products = []
payments = []

try:
    with open('insurance_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Remove spaces before and after the text from the column names
            row = {key.strip(): value.strip() for key, value in row.items()}

            # Check for required fields and handle missing data
            if all(key in row and row[key] for key in ['policy_id', 'name', 'age', 'gender', 'product_name', 'product_amount', 'monthly_premium']):
                try:
                    # Instantiate a policyholder instance
                    policyholder = Policyholder(row['policy_id'], row['name'], row['age'], row['gender'])
                    policyholders.append(policyholder)

                    # Instantiate a product instance for the policyholder
                    product = Product(row['policy_id'], row['product_name'], row['product_amount'])
                    products.append(product)

                    # Instantiate a payment instance (monthly premium) for the policyholder
                    payment = Payment(row['policy_id'], policyholder, product, row['monthly_premium'])
                    payments.append(payment)
                except Exception as e:
                    print(f"Error in processing row {row}: {e}")
            else:
                print(f"Missing or empty data in row: {row}")

except FileNotFoundError:
    print("Error: The file 'insurance_data.csv' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Function to search for a policyholder by policyID in case the dataset was huge
def search_policyholder(policyID):
    for i, policyholder in enumerate(policyholders):
        if policyholder.policyID == policyID:  
            print(f"Details for {policyholder.name}:")
            policyholder.display_details()  # Display policyholder details
            products[i].display_details()   # Display product details
            payments[i].process_payment()   # Process and display payment details
            payments[i].display_payment_details()  # Display payment information
            return  # Exit the function after displaying the details
    print(f"Policyholder with ID {policyID} not found.")

# Get user input for the policy_id to search
search_id = input("Enter the Policy ID to search: ").strip()
search_policyholder(search_id)
