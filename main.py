from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import *

from api.api_router import router
from add_models import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Eastvantage" )


app.include_router(router, tags=["Address book"])