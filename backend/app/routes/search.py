from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Bookmark, Folder
from app.schemas import BookmarkResponse

router = APIRouter(
    prefix="/v1/search",
    tags=["search"],
)

@router.get("/bookmarks", response_model=list[BookmarkResponse])
def search_bookmarks(
    folder_name: str = Query(None, description="Search bookmarks by folder name"),
    bookmark_title: str = Query(None, description="Search bookmarks by bookmark title"),
    search_type: str = Query("partial", description="Search type: 'partial' (case-insensitive), 'exact', 'case_sensitive', 'first_letter'"),
    db: Session = Depends(get_db)
):
    """
    Search bookmarks based on folder name and/or bookmark title with different search modes.
    
    Args:
        folder_name: Optional string to search for in folder names
        bookmark_title: Optional string to search for in bookmark titles
        search_type: Type of search to perform:
                    - 'partial': Case-insensitive partial match (default)
                    - 'exact': Exact case-sensitive match
                    - 'case_sensitive': Case-sensitive partial match
                    - 'first_letter': Match only first letter (case-sensitive)
        db: Database session dependency
        
    Returns:
        List of bookmarks matching the search criteria
        
    Raises:
        HTTPException: If no search criteria are provided or invalid search_type
    """
    if not folder_name and not bookmark_title:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one search parameter (folder_name or bookmark_title) must be provided"
        )
    
    valid_search_types = ["partial", "exact", "case_sensitive", "first_letter"]
    if search_type not in valid_search_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid search_type. Must be one of: {', '.join(valid_search_types)}"
        )
    
    # Start with base query joining bookmarks with folders
    query = db.query(Bookmark).join(Folder)
    
    # Apply filters based on provided parameters and search type
    if folder_name:
        if search_type == "partial":
            query = query.filter(Folder.name.ilike(f"%{folder_name}%"))
        elif search_type == "exact":
            query = query.filter(Folder.name == folder_name)
        elif search_type == "case_sensitive":
            query = query.filter(Folder.name.like(f"%{folder_name}%"))
        elif search_type == "first_letter":
            query = query.filter(Folder.name.startswith(folder_name))
    
    if bookmark_title:
        if search_type == "partial":
            query = query.filter(Bookmark.title.ilike(f"%{bookmark_title}%"))
        elif search_type == "exact":
            query = query.filter(Bookmark.title == bookmark_title)
        elif search_type == "case_sensitive":
            query = query.filter(Bookmark.title.like(f"%{bookmark_title}%"))
        elif search_type == "first_letter":
            query = query.filter(Bookmark.title.startswith(bookmark_title))
    
    # Execute query and return results
    bookmarks = query.all()
    return bookmarks
