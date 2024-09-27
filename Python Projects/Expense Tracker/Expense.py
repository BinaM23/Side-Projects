
class Expense:
    
    def __init__(self,name,category,amount):
        self.name = name
        self.category = category
        self.amount = amount
        
    def __repr__(self): #using str doesn't work on list of objects
        return f"Expense name: {self.name}, category: {self.category}, amount: ${self.amount:.2f}"