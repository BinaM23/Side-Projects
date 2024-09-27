#Author: Bina Mukuyamba
#Date: 25/09/2024
#Expense tracker app
#credit: pixegami
#src code: https://www.youtube.com/watch?v=HTD86h69PtE&list=WL&index=6
from Expense import Expense
from typing import List
import calendar
import datetime
import sys
import os

#My modifications: 
    #let user decide how many items to add in one go - DONE
    #error handling on user input - DONE
    #menu with options to view remaining budget, add expenses, view budget using external file(Assumes correct format) - DONE
    #-Memory to store budget information, option to change budget
    #-must have logic to calculate new budget correctly, if budget exceeded, say 0 left - DONE
   
    #can add more categories
    #logic to determine most expensive expense/category/item
    #data on spending patterns etc

def main():
    print(f"running expense tracker")
    expense_file_path = "expenses.csv"
    choice = int(input("Enter 1 to add expenses, 2 to view remaining budget or 0 to exit program:\n"))
    if choice == 1:
        
        try:
            No_of_Expenses = int(input("Enter the number of expenses to record:\n"))
            if No_of_Expenses<=0:
                raise ValueError("Number of expenses cannot be 0 or negative.")
        except ValueError as e:
            print(f"Input error: {e}.")
            sys.exit(0)
        #Enter N expenses and send to csv file after each entry
        for i in range(No_of_Expenses):
            #get user expense
            expense = getUserExpense()
            #write to a CSV file, can do other procesess with csv file
            write_to_file(expense,expense_file_path)
    elif choice == 2:
        #summarize all expenses,show remaining budget
        decision = int(input("Enter 1 to summarize saved file or 2 to summarize expenses from external csv file:\n"))
        #Logic to implement budget being stored and updated
        budgetfile="budget.txt"
        #do you have a budget? if yes ->ask if updated? if no enter budget and save to file
        isbudget=input("Do you have a budget alredy?(Enter yes or no):\n")
        if isbudget=="yes":
            update=input("Do you need to update your budget?(Enter yes or no):\n")
            if update == "no":
                if os.path.exists(budgetfile):
                    budget=getBudget(budgetfile)
                else:
                    print("You dont have a budget.Create one first.")
                    sys.exit(0)
            elif update == "yes":
                 try:
                    budget = float(input("Enter your new monthly budget:\n$")) #user enters budget
                    saveBudget(budgetfile,budget)
                    if budget<=0:
                            raise ValueError("Budget cannot be 0 or negative.")
                 except ValueError as e:
                    print(f"Input error: {e}.")
                    sys.exit(0)
            else:
                sys.exit(0)
        elif isbudget=="no":
            try:
                budget = float(input("Enter your monthly budget:\n$")) #user enters budget
                saveBudget(budgetfile,budget)
                if budget<=0:
                        raise ValueError("Budget cannot be 0 or negative.")
            except ValueError as e:
                    print(f"Input error: {e}.")
                    sys.exit(0)
        else:
            sys.exit(0)
                    
        if decision ==1:
            if os.path.exists(expense_file_path):
                 summarize_expenses(expense_file_path, budget)
            else:
                print("No expenses to summarize. Add expenses first.")
                sys.exit(0)
        elif decision ==2:
            filepath2=input("Enter external csv file path (in the form \"filename.csv\"):\n")
            if os.path.exists(filepath2):
                 summarize_expenses(filepath2, budget)
            else:
                print("File not found.")
                sys.exit(0)
        else:
            sys.exit(0)
           
    else:
        sys.exit(0)
    
#neater to use funtions
def saveBudget(budgetfile,budget):
    #print(f"Saving budget {budget} to {budgetfile}")
    with open(budgetfile,"w") as f: #if they say they had no budget but forgot they had one that's their loss!
        f.write(f"{budget}")
        f.close()

def getBudget(budgetfile):
    thebudget=0
    with open(budgetfile, "r") as f:
        thebudget = f.readline()
        f.close()
    thebudget=float(thebudget.strip())
    return thebudget

def getUserExpense(): #in future more error checks
    #print("getting expense")
    expense_name = input("Enter the name of expense: ")
    expense_amount = float (input("Enter the amount of the expense: ")) #sort out currency later
    #print(f"expense:{expense_name}, amount:{expense_amount:.2f}")
    expense_categories = ["Food","Housing","Work","Entertainment","Misc"]
    
    while True:
        print("Select a category of the expense")
        for i,cat in enumerate(expense_categories):
            print(f"  {i+1}.{cat}")
        value_range = f"[1 - {len(expense_categories)}]"
        choice = int(input(f"Enter the category number for the expense {value_range}: ")) - 1
        if choice in range(len(expense_categories)):
            category_name=expense_categories[choice] #name of category from list
            new_expense = Expense(name=expense_name,category=category_name,amount=expense_amount) #make new obj
            return new_expense
        else:
            print("Invalid category, please try again")
            
      
    
def write_to_file(Expense,expense_file_path):
    #print(f"Saving user expense {Expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{Expense.name},{Expense.amount},{Expense.category}\n")    
        f.close()
    
def summarize_expenses(expense_file_path,budget):
    print("Expenses by category")
    expenses:List [Expense]=[] #list of expenses for easier processing
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category = line.strip().split(",") #remove whitespace then split
            An_expense = Expense(name=expense_name,category=expense_category,amount=float(expense_amount))
            expenses.append(An_expense) #add expense obj to list 
        f.close()
    #print(expenses)
    #dictionary to group total expenses by category
    amount_by_category ={}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else: #starting value for category if not there
            amount_by_category[key] = expense.amount
            
    #print(amount_by_category)
    for key,amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")
    print()  
    #somthing off here
    total_spent = sum([x.amount for x in expenses]) #list comprehension
    print(f"total spent this month ${total_spent:.2f}")
    budget_left = budget - total_spent
    if budget_left <=0:
        print(f"budget remaing this month: ${0:.2f}\n")
        print("You cannot spend anymore this month!")
    else:
        print(f"budget remaing this month: ${budget_left:.2f}\n")
    
        #daily budget
        now = datetime.datetime.now() #today
        theMonth = now.strftime("%B")
        days_in_month = calendar.monthrange(now.year, now.month)[1] #no of days in month
        remaining_days = days_in_month - now.day
        print(f"Days left in {theMonth}: {remaining_days} days")

        daily_budget = budget_left/remaining_days
        print(f"Budget per day: ${daily_budget:.2f}")
    
if __name__== "__main__": #this causes the main method to run only when we run this file direclty!,
    #if we import this into another file it prevents the main method from running when we run that file
    main()
    