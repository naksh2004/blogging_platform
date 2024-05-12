Running FastAPI Application Locally

Prerequisites:

Python installed on your system.
MongoDB installed and running locally or accessible via a URL.
Step 1: Clone the Repository
Clone the repository containing your FastAPI application code to your local machine.

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Step 2: Set Up Virtual Environment
Create a virtual environment to isolate your project dependencies.

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:
bash
Copy code
env\Scripts\activate
On macOS/Linux:
bash
Copy code
source env/bin/activate
Step 3: Install Dependencies
Install the required dependencies for your FastAPI application.

bash
Copy code
pip install -r requirements.txt
Step 4: Configure MongoDB Connection
Edit your FastAPI application configuration file to specify the MongoDB connection details (e.g., host, port, database name).

python
Copy code
# config.py

MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "blogging_platform"
Step 5: Run the FastAPI Application
Run your FastAPI application using the uvicorn server.

bash
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
(Similar requests for other endpoints)
Step 8: Deactivate Virtual Environment
After you're done testing, deactivate the virtual environment.

bash
Copy code
deactivate
