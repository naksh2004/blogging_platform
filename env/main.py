from fastapi import FastAPI, HTTPException
from models import Post, Comment
from crud import create_post, read_post, update_post, delete_post,create_comment
from pydantic import BaseModel  # Import BaseModel class from pydantic
from typing import Optional
from bson import ObjectId 

app = FastAPI()

# Create a new post
@app.post("/posts/")
def create_new_post(post: Post):
    return create_post(post)

# Retrieve a post by its ID
@app.get("/posts/{post_id}")
def get_post(post_id: str):
    post = read_post(post_id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

class UpdatePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

@app.put("/posts/{post_id}")
def update_existing_post(post_id: str, post: UpdatePost):
    updated_count = update_post(post_id, post)
    if updated_count:  # Check if the update was successful
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Delete an existing post
@app.delete("/posts/{post_id}")
def delete_existing_post(post_id: str):
    deleted = delete_post(post_id)
    if deleted:  # Check if the delete operation was successful
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
# Add a comment to a post
@app.post("/posts/{post_id}/comments/")
def add_comment_to_post(post_id: str, comment: Comment):
    # Check if the post exists
    post = read_post(post_id)
    if post:
        # Create the comment and associate it with the post
        if create_comment(post_id, comment):
            return {"message": "Comment added successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to add comment")
    else:
        raise HTTPException(status_code=404, detail="Post not found")


# Like a post
@app.post("/posts/{post_id}/like/")
def like_post(post_id: str):
    post = read_post(post_id)
    if post:
        post_id_obj = ObjectId(post_id)  # Convert post_id to ObjectId
        post['likes'] += 1
        # Ensure the post is of type Post before passing it to update_post
        post_obj = Post(**post)
        update_post(str(post_id_obj), post_obj)  # Update post using ObjectId
        return {"message": "Post liked successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Dislike a post
@app.post("/posts/{post_id}/dislike/")
def dislike_post(post_id: str):
    post = read_post(post_id)
    if post:
        post_id_obj = ObjectId(post_id)  # Convert post_id to ObjectId
        post['dislikes'] += 1
        # Ensure the post is of type Post before passing it to update_post
        post_obj = Post(**post)
        update_post(str(post_id_obj), post_obj)  # Update post using ObjectId
        return {"message": "Post disliked successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
