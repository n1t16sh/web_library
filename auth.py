from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)
    #if this(wraps) is not used the decorator return wrappper with this it returns dashboard 
    def wrappper():
        if "user_id" not in session:
            return redirect(url_for("login_page"))
        return func()
    
    return wrappper