from fastapi import APIRouter
from schemas.blog_schema import BlogSchema

router = APIRouter( 
    prefix="/blogs",
    tags=["user"])

@router.post("/create-blog")
def CreateBlog(blog: BlogSchema):
    return  create_blog(blog)


@router.get("/")
def GetAllBlog():
    return get_All_blog()


@router.get("single-blog/{id}")
def GetSingleBlog(id):
    return get_single_blog(id)



@router.get("/update-blog/{id}")
def UpdateBlog(id, blog:BlogSchema):
    return upload_blog(id,blog)

@router.get("delete-blog/{id}")
def DeleteBlog(id):
    return delete_blog(id)

