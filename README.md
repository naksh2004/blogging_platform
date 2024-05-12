#Steps to run this project

#Prerequisites:
Python installed on your system.
MongoDB installed and running locally or accessible via a URL.

Step 1: Clone the Repository
Clone the repository containing your FastAPI application code to your local machine.
code
git clone <repository_url>
cd <repository_directory>

Step 2: Set Up Virtual Environment
Create a virtual environment to isolate your project dependencies.

Copy code
python -m venv env
Activate the virtual environment:

On Windows:
Copy code
env\Scripts\activate

On macOS/Linux:
Copy code
source env/bin/activate

Step 3: Install Dependencies
Install the required dependencies for your FastAPI application.
Copy code
pip install -r requirements.txt

Step 4: Configure MongoDB Connection
Edit your FastAPI application configuration file to specify the MongoDB connection details (e.g., host, port, database name).

MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "blogging_platform"

Step 5: Run the FastAPI Application
Run your FastAPI application using the uvicorn server.

Copy code
uvicorn main:app --reload

Step 6: Access the API
Once the FastAPI application is running, you can access the API endpoints locally using a web browser or tools like curl or Postman.

Base URL: http://localhost:8000

Step 7: Test Endpoints
You can test the endpoints by making HTTP requests to the appropriate URLs using tools like curl or Postman. Here are some example requests:

Create a Post:
bash
Copy code
curl -X POST "http://localhost:8000/posts/" -H "Content-Type: application/json" -d '{"title": "First Post", "content": "This is my first post!", "author": "John Doe"}'

Get a Post:
bash
Copy code
curl -X GET "http://localhost:8000/posts/{post_id}/"

Update a Post:
bash
Copy code
curl -X PUT "http://localhost:8000/posts/{post_id}/" -H "Content-Type: application/json" -d '{"title": "Updated Title", "content": "Updated content", "author": "John Doe"}'

Delete a Post:
bash
Copy code
curl -X DELETE "http://localhost:8000/posts/{post_id}/"

Add a Comment:
bash
Copy code
curl -X POST "http://localhost:8000/posts/{post_id}/comments/" -H "Content-Type: application/json" -d '{"text": "Great post!", "author": "Jane Doe"}'

Like a Post:
bash
Copy code
curl -X POST "http://localhost:8000/posts/{post_id}/like/"

Dislike a Post:
bash
Copy code
curl -X POST "http://localhost:8000/posts/{post_id}/dislike/"


Step 8: Deactivate Virtual Environment
After you're done testing, deactivate the virtual environment.
Copy code
deactivate
