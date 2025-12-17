# My Portfolio Website
_My portfolio website built using Django and hosted on Google Cloud Services (GCP)._


## Technologies Used
* Backend: Django (Python web framework)
* Hosting: Google Cloud Platform (GCP)
* Optional: Swiperjs

## Features
* Responsive design
* Project showcase with descriptions and links
* Skills and experience section
* Contact form or email address

## How to Run Locally

### Prerequisites
* Python 3.8 or higher
* pip (Python package installer)
* Virtual environment (recommended)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AlvajoyAsante/My-Portfolio.git
   cd My-Portfolio/personal_portfolio
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```
   The website will be available at `http://127.0.0.1:8000/`

## Deployment on GCP
1. Ensure you have a Dockerfile in the root directory of your project
2. Cloud Build will automatically trigger on pushes to the main branch
3. The build process:
   - Matches the `main` branch using the regex pattern `^main$`
   - Builds a Docker image from the Dockerfile located at `/Dockerfile`
   - Automatically deploys to Cloud Run
4. Access your deployed application via the Cloud Run URL provided in the console

## Additional Notes
* Feel free to personalize this template with details specific to your website and development process.
* Add screenshots or diagrams to showcase your website's design and functionality.
* Update the technologies and features section based on your actual implementation

___
Alvajoy Asante (c) 2023
