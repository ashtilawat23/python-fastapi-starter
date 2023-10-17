from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.validation import User, UserQuery, UserUpdate
from app.validation import default_query, default_update, default_user

# Constants
VERSION = "0.0.1"

# Load the API description from README.md
with open("README.md", "r") as file:
    next(file)  # Skipping the first line (presumably a title)
    description = file.read()

# Create FastAPI app instance
API = FastAPI(
    title='Outreach API',
    description=description,
    version=VERSION,
    docs_url='/',
)

# Middleware setup for CORS
API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@API.get("/version", tags=["General"])
async def version():
    """
    <h3>Version</h3>
    Returns the current version of the API
    <pre><code>
    @return: String </code></pre>
    """
    return VERSION

# Route to create a new user
@API.post("/create-user")
async def create_user(user: User = default_user):
    """
    Creates one user.
    
    @param user: User
    @return: Boolean indicating success
    """
    return API.db.create(user.dict(exclude_none=True))

# Route to read users based on query criteria
@API.put("/read-users")
async def read_users(user_query: UserQuery = default_query):
    """
    Returns array of all matched users.
    
    @param user_query: UserQuery
    @return: Array of User objects
    """
    return API.db.read(user_query.dict(exclude_none=True))

# Route to update users based on query criteria and update data
@API.patch("/update-users")
async def update_users(user_query: UserQuery = default_query,
                       user_update: UserUpdate = default_update):
    """
    Updates all matched users.
    
    @param user_query: UserQuery
    @param user_update: UserUpdate
    @return: Boolean indicating success
    """
    return API.db.update(
        user_query.dict(exclude_none=True),
        user_update.dict(exclude_none=True),
    )

# Route to delete users based on query criteria
@API.delete("/delete-users")
async def delete_users(user_query: UserQuery = default_query):
    """
    Deletes all matched users.
    
    @param user_query: UserQuery
    @return: Boolean indicating success
    """
    return API.db.delete(user_query.dict(exclude_none=True))
