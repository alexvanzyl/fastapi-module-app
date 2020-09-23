from fastapi import FastAPI

from . import auth, user

app = FastAPI(title='FastAPI-Module-App')

# register application modules
auth.init_app(app)
user.init_app(app)
