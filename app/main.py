from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
