class directory:
    path:str

class login:
    user:str
    password:str

class database:
    host:str
    port:int
    name:str
    login:login

class Config:
    directory:directory
    database:database
