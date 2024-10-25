# Binomial Nomenclature Project
## Distinctiveness and Complexity

The Binomial Nomenclature Project aims to provide a comprehensive web application for managing and cataloging scientific names of organisms, aligning with the principles of biological classification. Unlike typical projects such as social networks or e-commerce sites, this application focuses on the specialized domain of taxonomy, serving a unique audience of researchers, educators, and students.

This project showcases its complexity through various features, including user authentication, CRUD (Create, Read, Update, Delete) operations for managing scientific names, and a user-friendly interface that leverages JavaScript for dynamic interactions. The backend is built using Django, ensuring robust data management and security, while the front-end is designed to be mobile-responsive, catering to users on various devices.

The application incorporates multiple models to represent different entities, such as organisms, families, and classifications, allowing for intricate relationships and data integrity. The distinctiveness of this project lies in its focus on an academic subject, which is rarely covered in standard course projects, thus making it a unique contribution to the field.


## Project Structure

- manage.py: The command-line utility for interacting with the Django project.
- requirements.txt: A list of Python packages required to run the project, including Django and any additional dependencies.
- nomenclature/: The main application directory containing:
    - models.py: Defines the data models for organisms and classifications.
    - views.py: Contains the logic for handling user requests and rendering templates.
    - urls.py: Defines the URL patterns for the application.
    - templates/: Contains HTML templates for rendering pages.
        - nomenclature/: Subdirectory for app-specific templates.
        - admin/: Contains templates for the admin panel, including admin_panel.html.


## How to Run the Application
To run the Binomial Nomenclature Project locally using Docker, follow the steps below:

##### Prerequisites:
- Docker and Docker Compose must be installed on your machine.
- You need to have a Docker Hub account to pull necessary images.

**Step 1.**
clone the repo and then enter the directory with `cd binomial_nomenclature` command.

**Step 2: Build and Start Containers**

1. Build the Docker images and start the containers using Docker Compose:

```
docker-compose up --build
```

This will:

- Build the web application image.
- Pull the PostgreSQL image from Docker Hub.
- Set up and run the containers for the web application and the database.

**Step 3: Database Migrations**

After the containers are up and running, you need to apply the Django migrations to set up your database schema.

Open a new terminal window, and run:

```
    docker-compose run web python nomencletureproject/manage.py makemigrations
```

Then this command:

```
    docker-compose run web python nomencletureproject/manage.py migrate
```

**Step 5: Create a Superuser (for Admin Access)**

To access the Django admin panel, create a superuser by running the following command:

```
    docker-compose run web python nomencletureproject/manage.py createsuperuser
```

Follow the prompts to create a superuser account.

**Step 6: Access the Application**

Once everything is set up and the containers are running, you can access your application at:

   - Web Application: http://127.0.0.1:8000/
   - Django Admin Panel: http://127.0.0.1:8000/admin/
   - Custom Admin Panel: http://127.0.0.1:8000/admin-panel/

Login using the superuser credentials you created earlier.

**Step 7: Stopping the Application**

To stop the running containers, press CTRL + C in the terminal where docker-compose is running, or run:

```
docker-compose down
```

## Additional Information

  -  This project utilizes Django's built-in admin interface for easy data management.
  -  The application is designed to be mobile-responsive, ensuring usability across different devices.
  -  Future enhancements may include user roles, advanced search functionalities, and integration with external databases for biological data.
  -  Improve the custom admin panel and make it more user friendly.