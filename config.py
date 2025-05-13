from os import environ 
from dotenv import load_dotenv

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI="mysql://root:root@localhost:3306/sispar_t2"
    SQLALCHEMY_DATABASE_TRACK_MOSFICATIONS = False
