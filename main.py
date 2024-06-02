from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
app =FastAPI()


# @app.get('/')
# def index():
#     return "Hi sagar"

# @app.get('/about')
# def index():
#     return {'data':{"sagar","bhukya"}}



#path parameters-----------------------------------------------

@app.get('/blog/unpublished') ##gets error because of this path /blog/{id} and /blog/unpublished same instead of int we give unpublished so if we write this to top then only that works
def published():
    return {"data":"all the data are unpublished"}

@app.get('/blog/{id}') # dynamically given  # by default id takes strings if you want give type goto fucntion
def show(id : int): #mention here which type do you want
    #fetch blog with id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id =id
    return {'data':{'1','2'}}


#query parameters---------------------------
#Query parameters in FastAPI allow you to pass additional data to your API endpoints through the URL. They are commonly used for filtering, sorting, or providing additional options to your API.
# @app.get('/limit')#http://127.0.0.1:8000/limit?limit=80 we have to give with ?
# def blog(limit):
#     return {'data':f'{limit}get all the data'}

@app.get('/limit')# http://127.0.0.1:8000/limit?limit=80&published=false
# def blog(limit : int,published : bool):#here we have to give data validation so need to add bool type at published
               #? and & should give in the path 
        # limit and published are required parameters if you miss anything that will give you error
def blog(limit =10,published:bool=True,sort:str|None=None): #we assign for both parameters to thier values
    if published:
        return {'data':f'{limit} published data from db'}
    else:
        return {'data':f'{limit} unpublished data from db'}
    


#request body--------------------we use pydantic models to create fields
class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]

@app.post('/blog')
def Create_Blog(request:Blog):
    return {'data':"this blog is published at this title {request.title}"}

#Body - Nested Models-------------
class address(BaseModel):
    vil:str
    street:str
    state:str
    pin:int
class User(BaseModel):
    name:str
    age:int
    address:address
@app.post('/create_user/')
async def body_nested_models(user:User):
    user_data=user.dict()
    return {"user_details":user_data}

#Declare Request Example Data
class re(BaseModel):
    name:str
    age:int
data={
    "name":"Sagar",
    "designation":"Python Developer",
    "Roll_id":"20079"
}
@app.post('/res_declaration/{item_id}')
async def dec_req(item_id:int,Data:re=data):
    return {"item":item_id,"Data":Data}




class I(BaseModel):
    name: str
    description: str = None
    price: float
    tags: list[str] = []

# Example request data
example_request_data = {
    "name": "Example Item",
    "description": "This is an example item.",
    "price": 19.99,
    "tags": ["example", "test"]
}
@app.post("/create_item")
async def create_item(item: I = example_request_data):
    return {"item": item}





























# #if you want to change the port number you can give 
# if __name__=="__main__":
#     uvicorn.run(app, host="127.0.0.1",port=9000)