# payment.py
class Payment:
    def __init__(self, payment_id, policyholder, product, monthly_premium):
        self.payment_id = payment_id
        self.policyholder = policyholder
        self.product = product
        self.monthly_premium = monthly_premium
        self.status = 'pending'

    def process_payment(self):
        self.status = 'completed'
        print(f"Payment {self.payment_id} for {self.policyholder.name} has been completed.")

    def send_payment_reminder(self):
        if self.status == 'pending':
            print(f"Reminder: Payment {self.payment_id} for {self.policyholder.name} is pending.")
    
    def apply_penalty(self):
        penalty = 0.1 * self.monthly_premium  # 10% penalty
        self.monthly_premium += penalty
        print(f"A penalty of {penalty} has been applied. New amount is kes {self.monthly_premium}")

    def display_payment_details(self):
        print(f"Payment ID: {self.payment_id}, Product: {self.product.name}, Monthly premium: kes {self.monthly_premium}, Status: {self.status}")
