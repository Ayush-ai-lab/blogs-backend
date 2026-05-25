from fastapi import APIRouter,UploadFile,File,Form 
from schemas.blog_schema import BlogSchema
from services.blog_service import create_blog, get_all_blog, get_single_blog, update_blog, delete_blog  
from sqlalchemy.orm import Session
from core.database import get_db
from fastapi import Depends

router = APIRouter( 
    prefix="/blogs",
    tags=["Blogs"])

@router.post("/create-blog")
def CreateBlog(
    title: str = Form(...),
    slug: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return create_blog(
        title,
        slug,
        short_description,
        description,
        image,
        db
    )


@router.get("/")
def GetAllBlog(
    db: Session = Depends(get_db)):
    return get_all_blog(db)


@router.get("/single-blog/{id}")
def GetSingleBlog(id: int,
    db: Session = Depends(get_db)):
    return get_single_blog(id, db)



@router.put("/update-blog/{id}")
def UpdateBlog(

    id: int,

    title: str = Form(...),

    slug: str = Form(...),

    short_description: str = Form(...),

    description: str = Form(...),

    image: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    return update_blog(

        id,

        title,

        slug,

        short_description,

        description,

        image,

        db
    )

@router.delete("/delete-blog/{id}")
def DeleteBlog(id: int,
    db: Session = Depends(get_db)):
    return delete_blog(id,db)

