
from sqlalchemy.orm import Session
from add_models.models import *
from fastapi import status,HTTPException
from schemas.add_schemas import *


# function to create user
def create_user(request: CreateUser, db: Session):
    # defining empty dictionary for structuring futhur response body  
    response_data = {}
    #<--- getting all data from request body in db_user variable--->
    db_user = User_address(**request.dict())
    # adding data to the database and commiting
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # response body
    response_data.update({
                "status_code": status.HTTP_201_CREATED,
                "message": "Saved successfully.",
                "success": True,
                "id": db_user.id
                })
    return response_data


# function to update user
def put(id, request: CreateUser, db: Session):
     # defining empty dictionary for structuring futhur response body  
    response_data = {}
    #< -- QUERY TO CHECK USER  WITH THIS id EXIST OR NOT --->
    Update_user_details = db.query(User_address).filter(User_address.id == id)

    #< --Condition to check data in user with this id exist or not --->
    if not Update_user_details.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=  ({
                        "status_code": status.HTTP_404_NOT_FOUND,
                        "message": f"user with id {id} not found"
                        }))
    # getting all data from request body and update user details 
    Update_user_details.update(request)
    # commiting the updated data to the database
    db.commit()
    # response body
    response_data.update({
                        "status_code": status.HTTP_202_ACCEPTED,
                        "message": "Updated successfully."
                    })
    return response_data


# function to delete user
def delete(id, db: Session):
    # defining empty dictionary for structuring futhur response body 
    response_data = {}
    #< -- Query to check user with this id exit or not--->
    user_delete = db.query(User_address).filter(User_address.id == id).first()
    #< --Condition to check data in user with this id exist or not --->
    if not user_delete:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=  ({
                        "status_code": status.HTTP_404_NOT_FOUND,
                        "message": f"user with id {id} not found"
                        }))
    # delete data from database and commiting
    db.delete(user_delete)
    # db.delete(usr_city)
    db.commit()
    # response body
    response_data.update({
                        "status_code": status.HTTP_200_OK,
                        "message": "Deleted successfully."
                    })
    return response_data


# function to get single user details by user_id
def get_user(id: int, db: Session):
    # defining empty dictionary for structuring futhur response body  
    response_data = {}
    #< -- QUERY TO CHECK USER  WITH THIS id EXIST OR NOT --->
    user = db.query(User_address).filter(User_address.id == id).first()
    #< --Condition to check data in user with this id  exist or not --->
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail={
            "status_code" : status.HTTP_404_NOT_FOUND,
            "message" :  f"No user found with {id}"
        })
    # response body
    response_data.update({  "data": user, 
                            "message": "Data retrieved successfully.", 
                            "status_code": status.HTTP_200_OK
                        })
    return response_data