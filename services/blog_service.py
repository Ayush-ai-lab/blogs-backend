from models.blog import Blog
import shutil
import os 
# CREATE BLOG
def create_blog(

    title,
    slug,
    short_description,
    description,
    image,
    db

):

    file_path = f"uploads/{image.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            image.file,
            buffer
        )


    new_blog = Blog(
        title=title,
        slug=slug,
        short_description=short_description,
        description=description,
        image=file_path
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {
        "message": "Blog created successfully",
        "data": new_blog
    }

# GET ALL BLOGS
def get_all_blog(db):
    blogs = db.query(Blog).all()
    if not blogs:
        return {
            "message": "No blog found"
        }
    blog_data = []

    for blog in blogs:
        blog_data.append({
            "id": blog.id,
            "title": blog.title,
            "slug": blog.slug,
            "short_description": blog.short_description,
            "description": blog.description,
            "image": f"http://127.0.0.1:8000/{blog.image}"
        })  
    return {
        "message": "All blogs fetched successfully",
        "data": blog_data
    }


# GET SINGLE BLOG
def get_single_blog(id, db):

    blog = db.query(Blog).filter(
        Blog.id == id
    ).first()
    if not blog:
        return {
            "message": "Blog not found"
        }

    return {
        "message": "Single blog fetched successfully",
        "data": {
            "id": blog.id,
            "title": blog.title,
            "slug": blog.slug,
            "short_description": blog.short_description,
            "description": blog.description,
            "image": f"http://127.0.0.1:8000/{blog.image}"
        }
    }
# UPDATE BLOG
def update_blog(

    id,
    title,
    slug,
    short_description,
    description,
    image,
    db

):

    blog = db.query(Blog).filter(
        Blog.id == id
    ).first()

    if not blog:

        return {
            "message": "No blog found"
        }

    # UPDATE IMAGE
    if image:

        # DELETE OLD IMAGE
        if blog.image and os.path.exists(blog.image):
            os.remove(blog.image)
        # SAVE NEW IMAGE
        file_path = f"uploads/{image.filename}"

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                image.file,
                buffer
            )

        blog.image = file_path

    # UPDATE OTHER DATA
    blog.title = title
    blog.slug = slug
    blog.short_description = short_description
    blog.description = description

    db.commit()

    db.refresh(blog)

    return {

        "message": "Blog updated successfully",

        "data": {

            "id": blog.id,

            "title": blog.title,

            "slug": blog.slug,

            "short_description": blog.short_description,

            "description": blog.description,

            "image": f"http://127.0.0.1:8000/{blog.image}"
        }
    }


# DELETE BLOG
def delete_blog(id, db):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        return {
            "message": "No blog found"
        }

    # DELETE IMAGE
    if blog.image and os.path.exists(blog.image):

        os.remove(blog.image)

    # DELETE BLOG

    db.delete(blog)

    db.commit()

    return {
        "message": "Blog deleted successfully"
    }