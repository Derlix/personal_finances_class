from sqlalchemy import Boolean, Column,String,SMALLINT
from base_class import Base

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(SMALLINT(3),autoincrement=True,primary_key=True)
    category_name = Column(String(50))
    category_description = Column(String(120))
    category_status = Column(Boolean, default=True)