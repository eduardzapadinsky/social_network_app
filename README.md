# Social Network App

This is a sample social network app built with Django and Django REST framework.

## Installation

To run this app, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/eduardzapadinsky/social_network_app.git
cd social_network_app
```

### 2. Create a Virtual Environment (Optional but Recommended)

We recommend using a virtual environment to isolate your project's dependencies. You can create and activate a virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Edit the `settings.py` file to configure your database settings. By default, the app is configured to use SQLite.

### 5. Migrate the Database

Run the database migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

You can create a superuser (admin) account to manage the app:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin account.

### 7. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

The app should now be running locally at `http://127.0.0.1:8000/`.

## Usage

You can access the main functionality of the app through the following URLs:

- Sign Up: `http://127.0.0.1:8000/api/signup/`
- Authentication: `http://127.0.0.1:8000/api/auth/`
- Create a Post: `http://127.0.0.1:8000/api/post/create/`
- Like a Post: `http://127.0.0.1:8000/api/post/<int:pk>/like/`
- Dislike a Post: `http://127.0.0.1:8000/api/post/<int:pk>/dislike/`
- Get User Activity: `http://127.0.0.1:8000/api/users/<int:user_id>/get_activity/`
- Analytics: `http://127.0.0.1:8000/api/analytics/`

## Testing with the Bot

You can use the provided bot for testing the app. Follow the instructions in the [demo_for_social_network_app](https://github.com/eduardzapadinsky/demo_for_social_network_app) repository to set up and run the bot.

