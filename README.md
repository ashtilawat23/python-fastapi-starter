# Python FastAPI Starter API

---

# Tech Stack

This starter template provides a robust backend setup using the following technology stack:

## Logic: Python

- **Python**: A versatile, high-level programming language that's widely used for various applications, from web development to data analysis. Python is known for its simplicity and readability, which makes it an excellent choice for quick development cycles and collaborative environments.

## API Framework: FastAPI

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. Some advantages of FastAPI include:
  - **Performance**: Ranks among the fastest web frameworks available, on par with NodeJS or Go.
  - **Automatic Interactive Docs**: With FastAPI, you automatically get interactive API documentation (using Swagger UI and ReDoc) that lets you call and test your API directly from the browser.
  - **Easy to Use**: Designed to be easy to use, while also enabling new, high-level features not available before.

## Validation: Pydantic

- **Pydantic**: A data validation and settings management tool using Python type annotations. Pydantic's main features include:
  - **Validation**: Provides an easy way to validate data to ensure it meets specific constraints and formats.
  - **Serialization**: Converts complex types, such as ORM objects, into JSON-serializable formats.
  - **Type Safety**: Ensures data consistency and reduces runtime errors by using Python type hints.

## Database: MongoDB

- **MongoDB**: A popular, NoSQL database known for its scalability and flexibility. With MongoDB, you can:
  - **Flexibly Structure Data**: Unlike relational databases, MongoDB allows for a more flexible data model, which can adapt over time.
  - **Scale Out**: Distribute data across many servers easily, with automatic load balancing.
  - **Store Large Volumes**: Handle massive volumes of data without compromising on speed and efficiency.

# Getting Started

Follow the steps below to set up the project on your local machine:

## 1. Set Up Virtual Environment (venv)

Before you begin, ensure you have Python installed on your machine. Then, create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## 2. Give Permission to Install Script

Make the install.sh script executable:

```bash
chmod +x install.sh
```

## 3. Install Dependencies

Run the install.sh script to install necessary dependencies:

```bash
./install.sh
```

## 4. Create .env File

In the root directory of the project, create a new .env file and add your MongoDB connection URL:

```bash
echo "MONGO_URL=your_mongo_connection_url" > .env
```

Replace your_mongo_connection_url with your actual MongoDB connection URL.

## 5. Update Collection Name

Open the file `app/database.py` and update the `collection_name` on line 77 to match the specific collection you intend to use.

## 6. Give Permission to Run Script

Make the run.sh script executable:

```bash
chmod +x run.sh
```

## 7. Run the Application

Execute the run.sh script to start the application:

```bash
./run.sh
```

Your application should now be up and running!




