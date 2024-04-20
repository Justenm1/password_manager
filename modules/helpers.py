from flask import session

def create_session(user_id, user, role):
    """ Create a session for the user
    """
    session['logged_in'] = True
    session['id'] = user_id
    session['username'] = user
    session['role'] = role

def logged_in():
    """ Check if the user is logged in
    """
    return 'logged_in' in session