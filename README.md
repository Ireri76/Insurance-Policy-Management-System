Overview
This README file describes a simple interactive policy management system developed for an insurance company to manage policyholders, products, and payments. The system allows policy managers to perform various tasks, such as adding and suspending policyholders, registering new members, and managing policy products. 
1.	Class Creation:
The program has three main separate classes for policyholders, products, and payments.
2.	Policyholder Management:
Implementation methods to register, suspend, and reactivate policyholders.
The policyholder class attributes include policyID (unique identification number), name, age, and gender.
3.	Payment Management:
Implementation methods for payment processing, reminders, and penalties.
The payment class attributes include payment_id, policyholder, product and monthly premium.
4.	Product Management:
Implementation methods for creating, updating, and removing/suspending policy products.
The product class attributes include product_id, name, and currency in Kenya shillings.
5.	Policyholder Demonstration:
A dummy CSV file with data for 10 policyholders was manually created and imported into the main.py file for querying, retrieving, and printing results. See the insurance_data.csv file. This was designed to simulate a dataset containing hundreds of thousands of policyholders.
Three instances were created: Policyholder, Product, and Payment.
The program is designed to retrieve one policyholder at a time by entering their specific policy_id.
Error handling, data validation, consistent attribute naming, and user feedback have been implemented in the main.py file to make the code more efficient, robust, and easier to maintain.
Five separate .ipynb files were created and then converted to .py files so they could run on the Jupyter Notebook platform: payment.py, policyholder.py, product.py, main.py, and RUN Code.py.
To avoid accidental interference with the main.py file, the file was named RUN Code.py, as it only contains a simple snippet that is easy to recall if accidentally deleted: %run main.py.
To access the details of any policyholder, simply input their policy_id in the input prompt below the code and press ENTER.
