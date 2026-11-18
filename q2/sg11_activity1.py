class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.name = name
        self.bill_amount = bill_amount

# Getters
    def get_name (self):
        return self.name

    def get_bill_amount(self):
        return self.bill_amount

#Setters
    def set_name(self, name):
        self.name = name

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self): #Calculates the full bill for regular patients
        print("regular patient")

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.8 #Gives 20% discount

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85 #Gives 15% discount

  def main ():
    patient1 = Patient ("Juan Dela Cruz", 15000)  
    patient2 = SeniorPatient ("Maria Santos", 15000)
    patient3 = PhilHealthPatient ("Pedro Reyes", 15000)

    print ("Hospital Billing System")
    print("------------------------")

    

    
