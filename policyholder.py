# policyholder_management.py
class Policyholder:
    def __init__(self, policyID, name, age, gender):
        self.policyID = policyID  # unique policy ID
        self.name = name          # name of the policyholder
        self.age = age            # age of the policyholder
        self.gender = gender      # gender of the policyholder
        self.is_active = True     # default status of the policyholder (active)
    
    # Register new policyholder
    def register(self):
        print(f"Policyholder {self.name} (ID: {self.policyID}) registered successfully.")
    
    # Suspend policyholder
    def suspend(self):
        self.is_active = False
        print(f"Policyholder {self.name} (ID: {self.policyID}) has been suspended.")
    
    # Reactivate policyholder
    def reactivate(self):
        self.is_active = True
        print(f"Policyholder {self.name} (ID: {self.policyID}) has been reactivated.")
    
    # Display policyholder details
    def display_details(self):
        status = "Active" if self.is_active else "Suspended"
        print(f"Policyholder ID: {self.policyID}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Status: {status}")
