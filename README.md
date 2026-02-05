# Expense Tracker

A Python-based expense tracking system that manages and analyzes personal expenses using dictionaries for data organization.

## Features

### Core Features
- Add new expenses with category, amount, date, and description
- View all expenses in organized format
- Filter expenses by category
- Calculate total expenses with category breakdown
- Delete specific expenses
- Automatic data persistence (JSON)

### Extension Features
- Generate weekly, monthly, or yearly expense summaries
- Data visualization (pie charts, line graphs, bar charts)
- Spending trend analysis
- Category spending analysis

## Installation

**Prerequisites:**
- Python 3.7+
- pip

**Setup:**

1. Clone the repository:
```bash
git clone https://github.com/coolrack/expense.git
cd expense
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python expense_tracker.py
```

## Usage

### Main Menu

1. Add new expense
2. View all expenses
3. Filter by category
4. Calculate totals
5. Delete expense
6. Generate summary (week/month/year)
7. Visualize expenses
8. Save and exit

## Team Roles & Tasks

This project was initially developed collaboratively with another group, where I learned about team-based coding practices and Git workflows. When the original group finished early, I decided to rebuild the project independently to apply what I learned and ensure I gained hands-on experience with all components.

**Development responsibilities covered:**
- Data entry and validation (add expense functionality)
- Analysis and calculations (total expenses, breakdowns)
- Data management (filtering, deletion, viewing)
- Extension features (summaries and visualizations)
- Documentation and testing

## Project Functionalities

**1. Adding Expenses**
- User input for category, amount, date, and description
- Input validation
- Unique ID assignment
- Immediate data saving

**2. Viewing Expenses**
- Tabular format display
- Sorted by date
- Total count included

**3. Filtering by Category**
- Category selection
- Filtered display with subtotal
- Spending percentage

**4. Calculating Totals**
- Total sum calculation
- Category breakdown
- Percentages and averages

**5. Deleting Expenses**
- ID-based deletion
- Confirmation required
- Data updates

**6. Expense Summaries**
- Weekly/monthly/yearly reports
- Top categories per period
- Period averages

**7. Data Visualization**
- Pie charts (category distribution)
- Line graphs (trends over time)
- Bar charts (category comparison)

## Technical Details

**Data Structure:**
```python
expenses = {
    1: {'category': 'Food', 'amount': 45.50, 'date': '2026-02-05', 'description': 'Grocery shopping'},
    2: {'category': 'Transport', 'amount': 15.00, 'date': '2026-02-04', 'description': 'Bus fare'}
}
```

**File Structure:**
```
expense/
├── expense_tracker.py
├── expenses_data.json (auto-generated)
├── requirements.txt
├── README.md
└── Expense Tracker Collab Project.md
```

**Error Handling:**
- Invalid date formats
- Non-numeric/negative amounts
- Empty categories
- Invalid expense IDs
- File I/O errors
- Missing dependencies

**Code Organization:**
- Modular functions
- Comprehensive docstrings
- PEP 8 formatting
- Input validation
- Clear error messages

## Challenges & Solutions

**Challenge 1: Data Persistence**
- Problem: Expenses lost when program closed
- Solution: JSON file storage with auto-save/load

**Challenge 2: Input Validation**
- Problem: Program crashed with invalid inputs
- Solution: Validation functions and try-except blocks

**Challenge 3: Date Handling**
- Problem: Inconsistent date comparison and sorting
- Solution: Python datetime module, YYYY-MM-DD standard format

**Challenge 4: Category Management**
- PReflection on Collaborative Coding

Working with my initial group taught me valuable lessons about collaborative development:

**What I learned from collaboration:**
- Git workflows (branches, pull requests, merge conflicts)
- Code review practices and constructive feedback
- Dividing tasks and coordinating work
- Communication importance in team projects

**Why I rebuilt independently:**
When the original group completed the project early, I recognized an opportunity to solidify my understanding by implementing everything myself. This allowed me to:
- Gain hands-on experience with every feature
- Understand the full codebase deeply
- Practice problem-solving independently
- Apply collaborative coding principles I learned

**Did I enjoy collaborative coding?**
Yes, but with important caveats. Working with others provided learning opportunities and exposed me to different approaches. However, rebuilding independently gave me confidence that I truly understood the material rather than just contributing to isolated features. The ideal approach combines both: collaborate to learn best practices, then independently practice to ensure mastery.

## roblem: Inconsistent category capitalization
- Solution: .title() method for standardization

**Challenge 5: User Experience**
- Problem: Unclear outputs
- Solution: Formatted tables, visual separators, confirmation messages

**Challenge 6: Visualization Dependencies**
- Problem: matplotlib not universally installed
- Solution: Optional visualization with clear error messages

## Future Enhancements

- Budget limits with alerts
- Export to CSV/Excel
- Multi-user support
- Mobile app integration
- Recurring expense tracking
- Receipt photo attachment
- Cloud synchronization
- Email expense reports

## License

MIT

---

**Project Due Date**: February 18th, 2026, 11:59 PM
