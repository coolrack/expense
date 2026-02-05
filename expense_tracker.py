"""
Expense Tracker - Collaborative Project
A Python program to manage and track personal expenses using dictionaries.

Features:
- Add new expenses
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Delete specific expenses
- Generate expense summaries by week, month, or year
- Visualize spending trends
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt

# Global dictionary to store all expenses
# Structure: {expense_id: {'category': str, 'amount': float, 'date': str, 'description': str}}
expenses = {}
expense_counter = 1

# File to persist expenses
EXPENSE_FILE = 'expenses_data.json'


def load_expenses():
    """
    Load expenses from JSON file if it exists.
    Handles error if file is corrupted or doesn't exist.
    """
    global expenses, expense_counter
    
    try:
        if os.path.exists(EXPENSE_FILE):
            with open(EXPENSE_FILE, 'r') as file:
                data = json.load(file)
                expenses = {int(k): v for k, v in data.get('expenses', {}).items()}
                expense_counter = data.get('counter', 1)
                print(f"✓ Loaded {len(expenses)} expenses from file.")
        else:
            print("No saved expenses found. Starting fresh.")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load expenses file: {e}")
        expenses = {}
        expense_counter = 1


def save_expenses():
    """
    Save expenses to JSON file for persistence.
    Ensures data is preserved between program runs.
    """
    try:
        with open(EXPENSE_FILE, 'w') as file:
            data = {
                'expenses': expenses,
                'counter': expense_counter
            }
            json.dump(data, file, indent=2)
        print("✓ Expenses saved successfully.")
    except IOError as e:
        print(f"Error: Could not save expenses: {e}")


def validate_date(date_string):
    """
    Validate if the date string is in YYYY-MM-DD format.
    
    Args:
        date_string (str): Date string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_amount(amount_string):
    """
    Validate if the amount is a positive number.
    
    Args:
        amount_string (str): Amount string to validate
        
    Returns:
        tuple: (bool, float) - (is_valid, converted_amount)
    """
    try:
        amount = float(amount_string)
        if amount <= 0:
            return False, 0
        return True, amount
    except ValueError:
        return False, 0


def add_expense():
    """
    Add a new expense to the tracker.
    Prompts user for category, amount, date, and description.
    Includes input validation and error handling.
    
    Team Member: Handles adding expenses
    """
    global expense_counter
    
    print("\n=== Add New Expense ===")
    
    # Get and validate category
    category = input("Enter expense category (e.g., Food, Transport, Entertainment): ").strip()
    if not category:
        print("Error: Category cannot be empty.")
        return
    
    # Get and validate amount
    amount_input = input("Enter amount ($): ").strip()
    is_valid, amount = validate_amount(amount_input)
    if not is_valid:
        print("Error: Amount must be a positive number.")
        return
    
    # Get and validate date
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_input = datetime.now().strftime('%Y-%m-%d')
    elif not validate_date(date_input):
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return
    
    # Get description (optional)
    description = input("Enter description (optional): ").strip()
    
    # Create expense entry
    expenses[expense_counter] = {
        'category': category.title(),
        'amount': amount,
        'date': date_input,
        'description': description
    }
    
    print(f"\n✓ Expense added successfully! (ID: {expense_counter})")
    expense_counter += 1
    save_expenses()


def view_all_expenses():
    """
    Display all expenses in a clear and organized format.
    Shows expenses sorted by date with formatted output.
    
    Team Member: Handles viewing expenses
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10} {'Description':<30}")
    print("="*80)
    
    # Sort expenses by date (most recent first)
    sorted_expenses = sorted(expenses.items(), key=lambda x: x[1]['date'], reverse=True)
    
    for exp_id, expense in sorted_expenses:
        print(f"{exp_id:<5} {expense['date']:<12} {expense['category']:<15} "
              f"${expense['amount']:>9.2f} {expense['description']:<30}")
    
    print("="*80)
    print(f"Total expenses: {len(expenses)}")


def filter_expenses_by_category():
    """
    Filter and display expenses by a specific category.
    Shows all expenses matching the selected category.
    
    Team Member: Handles filtering expenses
    """
    if not expenses:
        print("\nNo expenses to filter.")
        return
    
    # Get all unique categories
    categories = set(expense['category'] for expense in expenses.values())
    
    print("\n=== Filter by Category ===")
    print("Available categories:")
    for idx, category in enumerate(sorted(categories), 1):
        print(f"{idx}. {category}")
    
    choice = input("\nEnter category name or number: ").strip()
    
    # Handle numeric choice
    if choice.isdigit():
        choice_num = int(choice)
        sorted_cats = sorted(categories)
        if 1 <= choice_num <= len(sorted_cats):
            category = sorted_cats[choice_num - 1]
        else:
            print("Error: Invalid category number.")
            return
    else:
        category = choice.title()
    
    # Filter expenses
    filtered = {exp_id: exp for exp_id, exp in expenses.items() 
                if exp['category'] == category}
    
    if not filtered:
        print(f"\nNo expenses found in category '{category}'.")
        return
    
    print(f"\n=== Expenses in '{category}' ===")
    print("="*80)
    print(f"{'ID':<5} {'Date':<12} {'Amount':>10} {'Description':<30}")
    print("="*80)
    
    total = 0
    for exp_id, expense in sorted(filtered.items(), key=lambda x: x[1]['date'], reverse=True):
        print(f"{exp_id:<5} {expense['date']:<12} ${expense['amount']:>9.2f} {expense['description']:<30}")
        total += expense['amount']
    
    print("="*80)
    print(f"Total in {category}: ${total:.2f}")


def calculate_total_expenses():
    """
    Calculate and display the total of all expenses.
    Also shows breakdown by category.
    
    Team Member: Handles calculating total expenses
    """
    if not expenses:
        print("\nNo expenses to calculate.")
        return
    
    print("\n=== Total Expenses Summary ===")
    
    # Calculate total
    total = sum(expense['amount'] for expense in expenses.values())
    
    # Calculate by category
    category_totals = defaultdict(float)
    for expense in expenses.values():
        category_totals[expense['category']] += expense['amount']
    
    # Display breakdown
    print("\nBreakdown by Category:")
    print("-" * 40)
    for category in sorted(category_totals.keys()):
        amount = category_totals[category]
        percentage = (amount / total) * 100
        print(f"{category:<20} ${amount:>8.2f} ({percentage:>5.1f}%)")
    
    print("-" * 40)
    print(f"{'TOTAL':<20} ${total:>8.2f}")
    print(f"\nTotal number of expenses: {len(expenses)}")
    print(f"Average expense: ${total/len(expenses):.2f}")


def delete_expense():
    """
    Delete a specific expense by ID.
    Includes confirmation to prevent accidental deletion.
    
    Team Member: Handles deleting expenses
    """
    if not expenses:
        print("\nNo expenses to delete.")
        return
    
    print("\n=== Delete Expense ===")
    view_all_expenses()
    
    try:
        exp_id = int(input("\nEnter the ID of the expense to delete: ").strip())
        
        if exp_id not in expenses:
            print(f"Error: Expense ID {exp_id} not found.")
            return
        
        # Show expense details
        expense = expenses[exp_id]
        print(f"\nExpense to delete:")
        print(f"  Date: {expense['date']}")
        print(f"  Category: {expense['category']}")
        print(f"  Amount: ${expense['amount']:.2f}")
        print(f"  Description: {expense['description']}")
        
        # Confirm deletion
        confirm = input("\nAre you sure you want to delete this expense? (yes/no): ").strip().lower()
        
        if confirm == 'yes' or confirm == 'y':
            del expenses[exp_id]
            print("✓ Expense deleted successfully.")
            save_expenses()
        else:
            print("Deletion cancelled.")
    
    except ValueError:
        print("Error: Please enter a valid expense ID (number).")


def generate_expense_summary():
    """
    Generate expense summaries by week, month, or year.
    Extension feature for advanced analysis.
    
    Team Member: Extension feature
    """
    if not expenses:
        print("\nNo expenses to summarize.")
        return
    
    print("\n=== Expense Summary ===")
    print("1. Weekly summary")
    print("2. Monthly summary")
    print("3. Yearly summary")
    
    choice = input("\nSelect summary type (1-3): ").strip()
    
    if choice not in ['1', '2', '3']:
        print("Error: Invalid choice.")
        return
    
    # Group expenses by time period
    summaries = defaultdict(lambda: {'total': 0, 'count': 0, 'categories': defaultdict(float)})
    
    for expense in expenses.values():
        date = datetime.strptime(expense['date'], '%Y-%m-%d')
        
        if choice == '1':  # Weekly
            week_start = date - timedelta(days=date.weekday())
            key = week_start.strftime('%Y-W%U')
            label = week_start.strftime('%Y Week %U (starting %b %d)')
        elif choice == '2':  # Monthly
            key = date.strftime('%Y-%m')
            label = date.strftime('%Y %B')
        else:  # Yearly
            key = date.strftime('%Y')
            label = key
        
        summaries[key]['label'] = label
        summaries[key]['total'] += expense['amount']
        summaries[key]['count'] += 1
        summaries[key]['categories'][expense['category']] += expense['amount']
    
    # Display summaries
    print("\n" + "="*80)
    for key in sorted(summaries.keys(), reverse=True):
        summary = summaries[key]
        print(f"\n{summary['label']}")
        print("-" * 40)
        print(f"Total spent: ${summary['total']:.2f}")
        print(f"Number of expenses: {summary['count']}")
        print(f"Average expense: ${summary['total']/summary['count']:.2f}")
        
        if len(summary['categories']) > 1:
            print("\nTop categories:")
            sorted_cats = sorted(summary['categories'].items(), key=lambda x: x[1], reverse=True)
            for cat, amount in sorted_cats[:3]:
                percentage = (amount / summary['total']) * 100
                print(f"  {cat}: ${amount:.2f} ({percentage:.1f}%)")
    
    print("="*80)


def visualize_expenses():
    """
    Create visualizations of spending trends using Matplotlib.
    Extension feature for data visualization.
    
    Team Member: Extension feature
    """
    if not expenses:
        print("\nNo expenses to visualize.")
        return
    
    print("\n=== Expense Visualization ===")
    print("1. Spending by category (pie chart)")
    print("2. Spending over time (line chart)")
    print("3. Category comparison (bar chart)")
    
    choice = input("\nSelect visualization type (1-3): ").strip()
    
    try:
        if choice == '1':
            # Pie chart by category
            category_totals = defaultdict(float)
            for expense in expenses.values():
                category_totals[expense['category']] += expense['amount']
            
            plt.figure(figsize=(10, 8))
            plt.pie(category_totals.values(), labels=category_totals.keys(), 
                   autopct='%1.1f%%', startangle=90)
            plt.title('Expenses by Category')
            plt.axis('equal')
            plt.tight_layout()
            plt.show()
            print("✓ Pie chart displayed.")
        
        elif choice == '2':
            # Line chart over time
            date_totals = defaultdict(float)
            for expense in expenses.values():
                date_totals[expense['date']] += expense['amount']
            
            sorted_dates = sorted(date_totals.items())
            dates = [datetime.strptime(d, '%Y-%m-%d') for d, _ in sorted_dates]
            amounts = [a for _, a in sorted_dates]
            
            plt.figure(figsize=(12, 6))
            plt.plot(dates, amounts, marker='o', linestyle='-', linewidth=2)
            plt.xlabel('Date')
            plt.ylabel('Amount ($)')
            plt.title('Spending Over Time')
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("✓ Line chart displayed.")
        
        elif choice == '3':
            # Bar chart by category
            category_totals = defaultdict(float)
            for expense in expenses.values():
                category_totals[expense['category']] += expense['amount']
            
            categories = list(category_totals.keys())
            amounts = list(category_totals.values())
            
            plt.figure(figsize=(10, 6))
            plt.bar(categories, amounts, color='steelblue')
            plt.xlabel('Category')
            plt.ylabel('Total Amount ($)')
            plt.title('Total Expenses by Category')
            plt.xticks(rotation=45, ha='right')
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.show()
            print("✓ Bar chart displayed.")
        
        else:
            print("Error: Invalid choice.")
    
    except Exception as e:
        print(f"Error: Could not create visualization: {e}")
        print("Make sure matplotlib is installed: pip install matplotlib")


def display_menu():
    """
    Display the main menu of the expense tracker.
    """
    print("\n" + "="*50)
    print("           EXPENSE TRACKER")
    print("="*50)
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Filter expenses by category")
    print("4. Calculate total expenses")
    print("5. Delete expense")
    print("6. Generate expense summary (Week/Month/Year)")
    print("7. Visualize expenses")
    print("8. Save and exit")
    print("="*50)


def main():
    """
    Main function to run the expense tracker program.
    Handles the menu loop and user interaction.
    """
    print("Welcome to the Expense Tracker!")
    load_expenses()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            filter_expenses_by_category()
        elif choice == '4':
            calculate_total_expenses()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            generate_expense_summary()
        elif choice == '7':
            visualize_expenses()
        elif choice == '8':
            save_expenses()
            print("\nThank you for using Expense Tracker! Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 8.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
