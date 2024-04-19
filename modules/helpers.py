from flask import session


from modules.globals import app, db

def create_session(user_id, user, role):
    """ Create a session for the user
    """
    session['logged_in'] = True
    session['id'] = user_id
    session['username'] = user
    session['role'] = role
