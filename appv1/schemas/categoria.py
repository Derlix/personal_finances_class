from pydantic import BaseModel, StringConstraints
from typing import Annotated

class CategoryBase(BaseModel):
    category_name: Annotated[str, StringConstraints(max_length=50)]
    category_description: Annotated[str, StringConstraints(max_length=120)]
    
class CategoryCreate(CategoryBase):
    category_name: Annotated[str, StringConstraints(max_length=50)]
    category_description: Annotated[str, StringConstraints(max_length=120)]
    
class CategoryResponse(CategoryBase):
    category_id: int
    category_status: bool = True