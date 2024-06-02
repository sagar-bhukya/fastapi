from models import Item
from database import Base,engine
print("creating database is successfully")

Base.metadata.create_all(engine)
