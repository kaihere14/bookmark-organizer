from pydantic import BaseModel

class Folder(BaseModel):
    name: str
    description: str

class FolderResponse(Folder):
    name: str
    description: str
    
    model_config = {"from_attributes": True}

class Bookmark(BaseModel):
    title: str
    url: str
    description: str
    folder_id: int

class BookmarkResponse(Bookmark):
    id: int
    
    model_config = {"from_attributes": True}