from fastapi import APIRouter
from schemas.blog_schema import BlogSchema
from services.blog_service import create_blog, get_all_blog, get_single_blog, upload_blog, delete_blog  


router = APIRouter( 
    prefix="/blogs",
    tags=["Blogs"])

@router.post("/create-blog")
def CreateBlog(blog: BlogSchema):
    return  create_blog(blog)


@router.get("/")
def GetAllBlog():
    return get_all_blog()


@router.get("/single-blog/{id}")
def GetSingleBlog(id: int):
    return get_single_blog(id)



@router.put("/update-blog/{id}")
def UpdateBlog(id: int  , blog:BlogSchema):
    return upload_blog(id,blog)

@router.delete("/delete-blog/{id}")
def DeleteBlog(id: int):
    return delete_blog(id)

