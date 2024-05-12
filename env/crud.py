from pymongo import MongoClient
from bson import ObjectId
from models import Post
from models import Comment

client = MongoClient("mongodb://localhost:27017/")
db = client["blogging_platform"]
collection = db["posts"]

def create_post(post: Post):
    result = collection.insert_one(post.dict())
    return {"id": str(result.inserted_id)}  # Return the ID of the newly created post

def read_post(post_id: str):
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Query the database to find the post by its ObjectId
        post = collection.find_one({"_id": post_obj_id})
        if post:
            # Convert ObjectId to string for JSON serialization
            post["_id"] = str(post["_id"])
            return post
        else:
            return None  # Return None if post not found
    except Exception as e:
        # Handle any exceptions (e.g., invalid ObjectId format)
        print(f"Error while reading post: {e}")
        return None


def update_post(post_id: str, post: Post):
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Update the post in the database
        result = collection.update_one({"_id": post_obj_id}, {"$set": post.dict()})
        if result.modified_count > 0:
            return True  # Return True if the post was updated successfully
        else:
            return False  # Return False if the post was not found
    except Exception as e:
        # Handle any exceptions (e.g., database update error)
        print(f"Error while updating post: {e}")
        return False


def delete_post(post_id: str):
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Delete the post from the database
        result = collection.delete_one({"_id": post_obj_id})
        if result.deleted_count > 0:
            return True  # Return True if the post was deleted successfully
        else:
            return False  # Return False if the post was not found
    except Exception as e:
        # Handle any exceptions (e.g., database deletion error)
        print(f"Error while deleting post: {e}")
        return False

def create_comment(post_id: str, comment: Comment):  # Change the type of 'comment' parameter to 'Comment'
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Update the post with the new comment
        result = collection.update_one({"_id": post_obj_id}, {"$push": {"comments": comment.dict()}})
        if result.modified_count > 0:
            return True  # Return True if the comment was added successfully
        else:
            return False  # Return False if the post was not found
    except Exception as e:
        # Handle any exceptions (e.g., database update error)
        print(f"Error while creating comment: {e}")
        return False

def like_post(post_id: str):
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Increment the like count for the post
        result = collection.update_one({"_id": post_obj_id}, {"$inc": {"likes": 1}})
        if result.modified_count > 0:
            return True  # Return True if the like was incremented successfully
        else:
            return False  # Return False if the post was not found
    except Exception as e:
        # Handle any exceptions (e.g., database update error)
        print(f"Error while liking post: {e}")
        return False

def dislike_post(post_id: str):
    try:
        # Convert post_id string to ObjectId
        post_obj_id = ObjectId(post_id)
        # Increment the dislike count for the post
        result = collection.update_one({"_id": post_obj_id}, {"$inc": {"dislikes": 1}})
        if result.modified_count > 0:
            return True  # Return True if the dislike was incremented successfully
        else:
            return False  # Return False if the post was not found
    except Exception as e:
        # Handle any exceptions (e.g., database update error)
        print(f"Error while disliking post: {e}")
        return False

