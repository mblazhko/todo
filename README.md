# Todo app

This app can help you create a tasks to manage your time perfectly

## Local deployment instruction

>To deploy the Task Manager project locally, please follow the steps below:

1. Clone the repository to your local machine:
   ```git clone https://github.com/neostyle88/todo.git```

2. Navigate to the project directory:
   ```cd todo```

3. Create a virtual environment:
   ```python -m venv env```

4. Activate the virtual environment:
   - For Windows:
   ``` .\env\Scripts\activate```
   - For macOS and Linux:
   ```source env/bin/activate```

5. Install the project dependencies:
   ```pip install -r requirements.txt```

6. Apply database migrations:
   ```python manage.py migrate```

7. Run the development server:
   ```python manage.py runserver```

8. Open your web browser and access the Task Manager application at http://localhost:8000/.

> You can use test user made during migration:

   - Username ```admin```
   - Password ```test```

## Environment Variables

>The following environment variables should be set in the `.env` file:

- `DJANGO_SECRET_KEY`: Your Django secret key

**Note:** Before starting the project, make a copy of the `.env_sample` file and rename it to `.env`. Replace the sample values with your actual environment variable values.