from fastapi import APIRouter,Depends,status
from database import get_db
from schemas.add_schemas import *
from sqlalchemy.orm import Session
from crud.add_crud import *


# creating an instance of APIRouter
router = APIRouter()


# End point to create an user
@router.post("/",status_code=status.HTTP_201_CREATED)
def Create_User(createBody: CreateUser , db: Session = Depends(get_db)):
    # calling create_user function to create a user
    response = create_user(createBody, db)
    return response


# End point to show  user by id
@router.get("/user_details{id}", status_code=status.HTTP_200_OK)
def Get_user_address(id: int, db : Session = Depends(get_db)):
            # calling get_user function to show user details
            response = get_user(id, db)
            return response


# End point to update a user by id
@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def Update_user(id : int, updateBody: CreateUser , db: Session = Depends(get_db)):
    updateBody = updateBody.__dict__
    # calling update_user function to update user details
    response = put(id, updateBody, db)
    return response


# End point for hard delete a user by id
@router.delete("/hard_delete{id}", status_code=status.HTTP_200_OK)
def Delete_user(id : int, db: Session = Depends(get_db)):
    # calling delete function to delete a user details 
    response = delete(id,db)
    return response

