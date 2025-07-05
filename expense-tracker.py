import argparse, os, sys
from storage.engine import JSONDatabase, Expense

db = JSONDatabase()

def add_expense(**kwargs):
    amount: int = None
    description: str = ''
    for k, v in kwargs.items():
        match k:
            case 'amount': amount = v
            case 'description': description = v
    if amount is None or amount < 0: raise ValueError('Amount must be positive number')

    expense = Expense(amount=amount, description=description)
    db.add(expense)
    print(f'Expense added successfully (ID={expense.id})')

def list_expenses(**kwargs):
    month: int = None
    year: int = None
    for k, v in kwargs.items():
        match k:
            case 'month': month = v
            case 'year': year = v
    expenses = []
    for expense in db._objects:
        if month is not None and int(expense.date.split('.')[1]) != month: continue
        if year is not None and int(expense.date.split('.')[2]) != year: continue
        expenses.append(expense)
    if not len(expenses): print("No expenses found!")
    else:
        print("ID  Date        Description  Amount")
        print("--  ----        -----------  ------")
        print(*expenses, sep='\n')

def summary(**kwargs):
    month: int = None
    year: int = None
    for k, v in kwargs.items():
        match k:
            case 'month': month = v
            case 'year': year = v
    expenses = []
    for expense in db._objects:
        if month is not None and int(expense.date.split('.')[1]) != month: continue
        if year is not None and int(expense.date.split('.')[2]) != year: continue
        expenses.append(expense.amount)
    if not len(expenses): print("No expenses found!")
    else: print(f"Total expenses: ${sum(expenses)}")
    

def delete_expense(**kwargs):
    id: int = None
    for k, v in kwargs.items():
        match k:
            case 'id': id = v-1
    if id < 0: raise ValueError('Id must be more or equal to 1')
    db.remove(id)
    print('Expense deleted successfully!')

actions = {
    'add': add_expense,
    'list': list_expenses,
    'summary': summary,
    'delete': delete_expense
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(type=str, dest='action')
    parser.add_argument('--id', type=int)
    parser.add_argument('--amount', type=int)
    parser.add_argument('--month', type=int)
    parser.add_argument('--year', type=int)
    parser.add_argument('--description', type=str)
    args = parser.parse_args()

    if args.action in actions:
        actions[args.action](**args.__dict__)
    