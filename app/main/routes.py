from app.main import bp
from flask import render_template

@bp.route('/expenses', methods=['GET', 'POST'])
def expenses():
    """
    Route and method for rendering the expenses page.
    """
    return render_template('internal/expenses.html', title='Expenses')

@bp.route('/income', methods=['GET', 'POST'])
def income():
    """
    Route and method for rendering the income accounts page.
    """
    return render_template('internal/income.html', title='Income Accounts')

@bp.route('/deposit-accounts', methods=['GET', 'POST'])
def depositAccounts():
    """
    Route and method for rendering the deposit accounts page.
    """
    return render_template('internal/deposit-accounts.html', title='Deposit Accounts')