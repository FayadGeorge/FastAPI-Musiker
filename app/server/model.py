from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int= Field(default=None)
    title: str= Field(default=None)
    content: str= Field(default=None)
    class Config:
        schema_extra={
            "post_demo":{
                "title":"animals",
                "content":"some content about animals"
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default = None)
    email : EmailStr = Field(default = None)
    password : str = Field (default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "name":"George",
                "email": "George@fayad.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default = None)
    password : str = Field (default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "email": "George@fayad.com",
                "password": "123"
            }
        }