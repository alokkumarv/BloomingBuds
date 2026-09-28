from Model import Tenant,Base,User,Role
from sqlalchemy import create_engine
import os
print("Metadata:", Base.metadata.tables.keys())
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

print("Tables created successfully!")