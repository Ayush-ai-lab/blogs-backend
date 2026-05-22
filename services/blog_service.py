from models.blog import Blog


# CREATE BLOG
def create_blog(blog, db):

    new_blog = Blog(
        title=blog.title,
        short_description=blog.short_description,
        description=blog.description,
        slug=blog.slug
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

    return {
        "message": "All blogs",
        "data": blogs
    }


# GET SINGLE BLOG
def get_single_blog(id, db):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        return {
            "message": "No blog found"
        }

    return {
        "message": "Single blog",
        "data": blog
    }


# UPDATE BLOG
def update_blog(id, updated_blog, db):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        return {
            "message": "No blog found"
        }

    blog.title = updated_blog.title
    blog.short_description = updated_blog.short_description
    blog.description = updated_blog.description
    blog.slug = updated_blog.slug

    db.commit()

    db.refresh(blog)

    return {
        "message": "Blog updated successfully",
        "data": blog
    }


# DELETE BLOG
def delete_blog(id, db):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        return {
            "message": "No blog found"
        }

    db.delete(blog)

    db.commit()

    return {
        "message": "Blog deleted successfully"
    }