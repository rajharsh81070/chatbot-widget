# Chat Widget Backend

## Table of Contents

- [Chat Widget Backend](#chat-widget-backend)
  - [Table of Contents](#table-of-contents)
  - [Tech Stack](#tech-stack)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)
  - [API Endpoints](#api-endpoints)
  - [Docker](#docker)

## Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- PostgreSQL (or SQLite for development)
- OpenAI API (optional)
- Poetry (for dependency management)

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Poetry
- PostgreSQL (optional, SQLite can be used for development)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/rajharsh81070/chatbot-widget.git
   cd chat-widget-backend/server
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file with your configuration.

## Running the Application

To run the application locally:

```
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Running Tests

To run the tests:

```
poetry run pytest
```

## API Endpoints

For a detailed list of API endpoints and their request/response structures, please refer to the [API Documentation](API_DOCUMENTATION.md).

## Docker

To build and run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t chat-widget-backend .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 chat-widget-backend
   ```

The API will be available at `http://localhost:8000`.