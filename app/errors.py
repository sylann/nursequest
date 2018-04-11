from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    print_error(error)
    return render_template('errors/404.html', title="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    print_error(error)
    return render_template('errors/500.html', title="Internal server error"), 500

def print_error(error):
    print('*** ERROR HANDLER : ***')
    print(error)
    print('***********************')