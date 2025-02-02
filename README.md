# Bharatfd - Multilingual FAQ Management System

A Django-based multilingual FAQ management system with REST API support, caching, and automated translations using the Google Translate API. The project allows managing FAQs with language-specific translations, WYSIWYG editors for answers, and caching for improved performance.

## Table of Contents
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Configuration](#configuration)
4. [Running the Project](#running-the-project)
5. [Testing](#testing)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

Follow these steps to set up and run the project:

### Prerequisites

1. Python 3.10+ (recommended)
2. Django 4.0+
3. Redis (for caching)
4. Google Translate API key (optional, for automated translations)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/bharatfd.git
    cd bharatfd
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows
    source venv/bin/activate  # For macOS/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database (SQLite or configure Redis):
    ```bash
    python manage.py migrate
    ```

5. (Optional) Set up the Google Translate API:
    - Set up a Google Cloud project and enable the Translate API.
    - Add your API key to the `settings.py` under `GOOGLE_TRANSLATE_API_KEY`.

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Usage

### Endpoints

#### 1. Get FAQ by Language
- **URL**: `/api/faqs/`
- **Method**: `GET`
- **Query Parameters**: `lang` (e.g., `?lang=en`, `?lang=hi`)
- **Response**: Returns a list of FAQs in the specified language.

#### 2. Create FAQ
- **URL**: `/api/faqs/`
- **Method**: `POST`
- **Body Parameters**:
    ```json
    {
        "question": "What is Django?",
        "answer": "Django is a high-level Python web framework.",
        "translations": {
            "hi": "Django क्या है?",
            "bn": "Django কী?"
        }
    }
    ```
- **Response**: Returns the created FAQ object.

#### 3. Update FAQ
- **URL**: `/api/faqs/{id}/`
- **Method**: `PUT`
- **Body Parameters**: Same as `POST`.

#### 4. Delete FAQ
- **URL**: `/api/faqs/{id}/`
- **Method**: `DELETE`
- **Response**: Returns a success message.

## Configuration

- **Cache Configuration**: Make sure to set up Redis for caching in your `settings.py`:
    ```python
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
        }
    }
    ```

- **Google Translate**: Set the API key for automated translation in `settings.py`:
    ```python
    GOOGLE_TRANSLATE_API_KEY = 'your-google-api-key'
    ```

## Running the Project

1. Start the server:
    ```bash
    python manage.py runserver
    ```

2. Visit `http://127.0.0.1:8000/` to access the application.

3. Access the API at `http://127.0.0.1:8000/api/faqs/`.

## Testing

To run the tests, use `pytest`:

```bash
pytest
