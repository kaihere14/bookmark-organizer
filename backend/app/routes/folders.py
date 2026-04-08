from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

# Import database dependency and models
from app.database import get_db
from app.models import Folder as FolderModel
from app.schemas import Folder, FolderResponse

# Create API router for folder endpoints
# Prefix: /folders
# Tags: folders (for API documentation)
router = APIRouter(
    prefix="/folders",
    tags=["folders"],
)

@router.get("/", response_model=list[FolderResponse])
def get_folders(db: Session = Depends(get_db)):
    """
    Get all folders from the database.
    
    Args:
        db: Database session dependency
        
    Returns:
        List of all folders in the database
    """
    folders = db.query(FolderModel).all()
    return folders

@router.get("/{folder_id}", response_model=FolderResponse)
def get_folder(folder_id: int, db: Session = Depends(get_db)):
    """
    Get a specific folder by ID.
    
    Args:
        folder_id: The ID of the folder to retrieve
        db: Database session dependency
        
    Returns:
        The requested folder
        
    Raises:
        HTTPException: If folder with given ID is not found
    """
    folder = db.query(FolderModel).filter(FolderModel.id == folder_id).first()
    if not folder:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"folder with id: {folder_id} not found",
        )
    return folder

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FolderResponse)
def create_folder(folder: Folder, db: Session = Depends(get_db)):
    """
    Create a new folder in the database.
    
    Args:
        folder: Folder data from request body
        db: Database session dependency
        
    Returns:
        The created folder with generated ID
    """
    db_folder = FolderModel(**folder.dict())
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

@router.put("/{folder_id}", response_model=FolderResponse)
def update_folder(folder_id: int, folder: Folder, db: Session = Depends(get_db)):
    """
    Update an existing folder.
    
    Args:
        folder_id: The ID of the folder to update
        folder: Updated folder data from request body
        db: Database session dependency
        
    Returns:
        The updated folder
        
    Raises:
        HTTPException: If folder with given ID is not found
    """
    update_query = db.query(FolderModel).filter(FolderModel.id == folder_id)
    existing_folder = update_query.first()
    if existing_folder is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"folder with id: {folder_id} not found",
        )
    update_query.update(folder.dict(), synchronize_session=False)
    db.commit()
    return update_query.first()

@router.delete("/{folder_id}")
def delete_folder(folder_id: int, db: Session = Depends(get_db)):
    """
    Delete a folder by ID.
    
    Args:
        folder_id: The ID of the folder to delete
        db: Database session dependency
        
    Returns:
        Empty response with 204 No Content status
        
    Raises:
        HTTPException: If folder with given ID is not found
    """
    folder_query = db.query(FolderModel).filter(FolderModel.id == folder_id)
    folder = folder_query.first()
    if folder is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"folder with id: {folder_id} not found",
        )
    folder_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)