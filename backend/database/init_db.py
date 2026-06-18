# from connection import engine
# from models import Base

from database.connection import engine
from database.models import Base

Base.metadata.create_all(bind=engine)

print("Tables created successfully")