from flask import render_template, redirect, url_for
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """
    Gère les 404
    :return:
    """
    print_error(error)
    return render_template('errors/404.html', title="Page not found"), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Gère les 500
    :return:
    """
    db.session.rollback()
    print_error(error)
    return render_template('errors/500.html', title="Internal server error"), 500

@app.errorhandler(KeyError)
def key_error(error):
    """
    Gère les KeyError
    :return:
    """
    print_error(error)
    return redirect(url_for('logout', error=True))


def print_error(error):
    """
    Affiche en console la nature de l'erreur
    :return:
    """
    print('*** ERROR HANDLER : ***')
    print(error)
    print('***********************')