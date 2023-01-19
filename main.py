import uvicorn
from fastapi import FastAPI, Body, Depends
from app.server.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [   
    {
        "id": 1,
        "title": "penguins",
        "content":"Penguins are from the arctic and are elegant."
    },  
    {
        "id": 2,
        "title": "tigers",
        "content":"tigers are tigers"
    },
        {
        "id": 3,
        "title": "koalas",
        "content":"koalas are marsupials"
    }
]

users=[]

app=FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"hola": "mundo"}

#Get Posts
@app.get("/posts", tags = ["posts"])
def get_posts():
    return {"data":posts}

#Get Posts by ID
@app.get("/posts/{id}", tags=["posts"])
def get_post_by_id(id:int):
    if id > len(posts):
        return {
            "error":
            "Your element does not exist!"
            }
    for post in posts:
        if post["id"] == id:
            return{
                "data":post
            }
#Post a blog pos [A handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearer())],tags=["posts"])
def add_posts(post: PostSchema):
    post.id= len(posts) + 1
    posts.append(post.dict())#Append the data to the dictionary of the posts
    return{
        "info":
        "Post successfully added!"
    }

#5 User Signup [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup (user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

#User Login
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default = None)):
    if check_user(user):
        return signJWT(user.email)
    else: 
        return{
            "error":"Invalid login details!"
        }
