# Restaurant Booking System

## Table of Contents
- [About The Project](#about-the-project)
- [Objectives](#objectives)
- [Built With](#built-with)
- [Key Features](#key-features)
- [Authentication](#authentication)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Screenshots](#screenshots)
  - [Reservation Page](#reservation-page)
  - [Reservation List](#reservation-list)
  - [Contact Page](#contact-page)
- [Error and Success Messages](#error-and-success-messages)
- [Validator Testing](#validator-testing)
- [Code Style](#code-style)
- [Accessibility](#accessibility)
- [Manual Testing](#manual-testing)
- [Automated Testing and Code Coverage](#automated-testing-and-code-coverage)
- [Wireframes](#wireframes)
- [Agile Sprints](#agile-sprints)
  -[Agile & Kanban Process](#agile--kanban-process)
- [Database Model](#database-model)
- [Deployment](#deployment)
- [User Stories](#user-stories)
- [Bug Fixes](#bug-fixes)
- [Future Enhancements](#future-enhancements)
- [References](#references)
- [Inspiration and Learning Resources](#inspiration-and-learning-resources)
- [Acknowledgements](#acknowledgements)

![Home Page](https://github.com/BadrAlioui/forthProject/blob/master/media/images/home-page-presentation.png)

## About The Project

The Restaurant Booking System is a web application that allows users to easily book tables. Our goal is to simplify reservations and user experience.

## Objectives

-   To provide an easy-to-use platform for making reservations.
-   To engage customers with a friendly interface.
-   To ensure a pleasant user experience on all devices.
-   To allow users to manage their reservations easily.

## Built With

This project uses basic web technologies:

-   **Python**: Provides the functionality for the site.
-   **HTML5**: For structuring content.
-   **CSS3/Bootstrap**: For styling and responsive design.
-   **Django**: For back-end and data management.
-   **JavaScript**: For interactive features.

## Key Features

-   **Easy Reservations**: Users can select the date, time, and number of people for their booking.
-   **Admin-Only Menu Creation**: Only the administrator can add new menus to ensure everything stays consistent and accurate.
-   **Login Required for Reservations**: Users need to log in to book, edit, or cancel a table reservation.
-   **Message Confirmation**: Users receive a confirmation message after making a reservation.
-   **Reservation Management**: Users can cancel or change their reservations easily.
-   **Responsive Design**: Ensures a smooth experience on mobile and desktop.

### Authentication

This project uses Django's built-in authentication system to let users log in and log out.
When logged in, users can access features like managing their reservations or viewing personalized content.
Logging out securely ends the user session.
Django's authentication makes it easy to handle these features while keeping everything secure and reliable.

## Getting Started

### Prerequisites

-   A modern web browser that supports HTML5 and CSS3.
-   Python 3.x and Django installed.

### Installation

1. Clone the repository: `git clone [https://github.com/BadrAlioui/forthProject]`
2. Navigate to the project folder: `cd forthProject`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the Django server: `python manage.py runserver`

---

## Screenshots

Here are some screenshots of the application:

### Reservation Page

![Reservation Page](https://github.com/BadrAlioui/forthProject/blob/master/media/images/reservation_page.png?raw=true)

### Reservation List

![Reservation List](https://github.com/BadrAlioui/forthProject/blob/master/media/images/reservation_list_page.png?raw=true)

### Contact Page

![Contact Page](https://github.com/BadrAlioui/forthProject/blob/master/media/images/contact_presentation_page.png?raw=true)

---

## Error and Success Messages

This section showcases the feedback messages displayed by the application:

- **Registration Error Message:**  
  Displays when a user submits an invalid registration form, clearly indicating what went wrong so that the user can correct their input.

  ![Registration Error](https://github.com/BadrAlioui/forthProject/blob/master/media/images/no_reservation_past.png)


- **Reservation Success Message:**  
  Appears after a successful reservation, confirming that the booking has been successfully recorded and providing reassurance to the user.

  ![Reservation Success](https://github.com/BadrAlioui/forthProject/blob/master/media/images/reservation_success.png?raw=true)


- **Contact Form Error Message:**  
  Shows when the contact form submission fails due to invalid or missing input, guiding the user to make the necessary corrections.

  ![Contact Form Error](https://github.com/BadrAlioui/forthProject/blob/master/media/images/contact_error.png?raw=true)

These messages are designed to enhance user experience by providing clear and immediate feedback for both errors and successful actions.

---


## Validator Testing

**HTML Validation (W3C Validator)**:

-   No errors or warnings on all pages.

-page signup:

![signup validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/signup_validator.png?raw=true)

-page reservation:

![reservation validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/reservation_validator.png?raw=true)

-page list of reservation:

![reservation_list validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/reservation_list_validator.png?raw=true)

-menu page:

![menu_page validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/menu_page_validator.png?raw=true)

-login page:

![login validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/login_page_validator.png?raw=true)

-home page:

![home_page validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/home_page_validator.png?raw=true)

-Edit reservation:

![edir_reservation validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/edit_reservation_validator.png?raw=true)

-contact page:

![contact validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/contact_page_validator.png?raw=true)
**CSS Validation**:

-   All CSS files passed without errors:
s
-   css validator in styles.css:

![css validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/css_validator.png?raw=true)

**JavaScript Validation**:

![Javascript validator](https://github.com/BadrAlioui/forthProject/blob/master/media/images/javascript_validator.png?raw=true)

---
## Code Style

This project adheres to the [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines for Python code style. All Python files (e.g., `models.py`, `forms.py`, etc.) have been formatted accordingly.  
We used [pep8ci](https://pep8ci.herokuapp.com/) to validate our code, and the following screenshots demonstrate the compliance:

![PEP8CI Screenshot 1](/media/images/validator_reservation_test_view.png)
![PEP8CI Screenshot 2](/media/images/validator_reservation_view.png)

---

## Accessibility

We are committed to ensuring accessibility for all users. Our platform has been tested, with Lighthouse, to provide an inclusive user experience.

**Accessibility Mobile**

![Accessibility Mobile](https://github.com/BadrAlioui/forthProject/blob/master/media/images/mobile_accessibility.png)

**Accessibility Desktop**

![Accessibility Desktop](https://github.com/BadrAlioui/forthProject/blob/master/media/images/desktop_accessibility.png)

## Manual Testing:

[Manual Testing Documentation](https://github.com/BadrAlioui/forthProject/blob/master/TESTING.md)

## Automated Testing and Code Coverage

To ensure the application runs smoothly and reliably, extensive automated tests were written for key components like forms, views, and models. These tests help maintain the overall quality of the project.

### Code Coverage

Using the `coverage.py` tool, I measured the test coverage of the project. The results show an overall coverage of **over or equal to 90%**, highlighting that the most critical parts of the application are well-tested.

| Component | Coverage |
| --------- | -------- |
| Views     | 90%      |
| Models    | 100%     |
| Forms     | 100%     |
| Overall   | 96%      |

![coverage report](https://github.com/BadrAlioui/forthProject/blob/master/media/images/coverage.png)

### Helpful Resources

The course [Unit Testing in Django](https://netninja.dev/courses/unit-testing-in-django/) by [Net Ninja](https://netninja.dev/) was incredibly helpful in improving my understanding of testing in Django. It provided practical guidance on how to write better tests and achieve high coverage.

## Wireframes

#### Home Page

![wireframe home_page](https://github.com/BadrAlioui/forthProject/blob/master/media/images/wireframes.png)

#### User flows

![user flows](https://github.com/BadrAlioui/forthProject/blob/master/media/images/User-flow.png)

---

## Agile Sprints

Here are some screenshots from our agile sprints:

![Sprint 1](/media/images/spring1.png)
![Sprint 2](/media/images/spring2.png)
![Sprint 3](/media/images/spring3.png)
![Sprint 4](/media/images/spring4.png)

### Agile & Kanban Process

To better manage our project, we've implemented a structured Agile and Kanban workflow. Our board uses clear labels to prioritize tasks:

- **Must Do:** Critical tasks that must be completed.
- **High Priority:** Tasks that are critical and need immediate attention.
- **Medium Priority:** Tasks that are important but not urgent.
- **Low Priority:** Tasks that can be addressed later.
- **Should Do:** Tasks that are planned and expected to be completed in the current sprint.
- **Could Do:** Tasks that are optional and may be addressed if time allows.

Below is a snapshot of our Kanban board displaying these labels:

![Kanban Board](/media/images/label.png)


---
## Database Model

The database model has been designed using [drawSQL](https://drawsql.app/). The application utilizes a relational database architecture, with **SQLite3** used during development and **PostgreSQL** for deployment in production.

The model supports essential user interactions: users can make reservations and have the ability to modify or delete them. Additionally, if a user is an administrator, they have the capability to create and manage the restaurant menu.

![Database Model](/media/images/database_model.png)

---

## Deployment

The booking system is hosted on Heroku. To deploy your own version, follow these steps:

#### Deploying a Django Project on Heroku

Heroku is a cloud platform that lets you build, run, and operate applications entirely in the cloud. Here's how to deploy this project:

1. **Create an account or log in to Heroku.**
2. **Create a new app:**  
   On the Heroku dashboard, click **"New"** and select **"Create new app"**.  
   Give your app a unique name and select the region closest to you, then click **"Create app"**.
3. **Set up environment variables:**  
   For security and proper functioning of the application, you must set the following environment variables:
   ```bash
   heroku config:set SECRET_KEY="your_secret_key"
   heroku config:set EMAIL_HOST_USER="your_email@example.com"
   heroku config:set EMAIL_HOST_PASSWORD="your_email_password"
   heroku config:set CLOUDINARY_CLOUD_NAME="your_cloud_name"
   heroku config:set CLOUDINARY_API_KEY="your_api_key"
   heroku config:set CLOUDINARY_API_SECRET="your_api_secret"```

**Important Security Note:**  
Sensitive data is stored in a `.env` file, and a `.gitignore` file is used to ensure that this file is not pushed to GitHub. This approach keeps your credentials and other confidential information secure.

Your `requirements.txt` file must include essential packages for a successful deployment on Heroku, such as:

- **Django**: The web framework.
- **dj-database-url**: For easy database configuration.
- **gunicorn**: The WSGI server recommended for Heroku.
- **psycopg2** or **psycopg2-binary**: To work with PostgreSQL on Heroku.
- **django-heroku**: For configuring Django with Heroku settings.
- **whitenoise**: For efficient static file management.
- **cloudinary**: (If used) For managing images.



#### Settings

##### Update `settings.py`

##### 1. Set `ALLOWED_HOSTS`:

ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com', 'localhost']

##### 2. Set `Debug = False` for production:

It is important to turn off debug mode before deploying to ensure the app is secure and runs efficiently.

##### 3. Error Handling:

With Debug = False, Django will serve custom error pages(e.g., 404 or 500 pages) instead of showing technical debug information.

You can access the live version here: [Restaurant Booking System](https://quiet-crag-61811-4fb808af66c6.herokuapp.com/)

## User Stories

You can access the user stories, organized by different levels of priority, here: [User Stories](https://github.com/BadrAlioui/forthProject/issues), or here: [Kanban](https://github.com/users/BadrAlioui/projects/2)

| User Story | Description                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1          | As a user, I want to easily book a table so that I can reserve a spot for my desired date and time.                                 |
| 2          | As a user, I want to provide my personal details such as my name, email, and number of persons when making a reservation.           |
| 3          | As a user, I want to select the date and time for my reservation so that I can plan my visit accordingly.                           |
| 4          | As a user, I want to receive a confirmation message after submitting the reservation form so that I know my booking was successful. |
| 5          | As a user, I want to be informed if the restaurant is fully booked on my selected date to avoid confusion about my reservation.     |
| 6          | As a user, I want to edit my reservation details if my plans change, while I am still logged in.                                    |
| 7          | As a user, I want to cancel my reservation if I can no longer make it, but only while I am logged in.                               |
| 8          | As a user, I want to view a list of all my past reservations so that I can keep track of my dining history.                         |
| 9          | As a user, I want to access the menu page to see the available dishes before making a reservation.                                  |
| 10         | As a user, I want to view the details of a specific menu item so that I can learn more about what I will be ordering.               |
| 11         | As a user, I want to create new menu items as an admin to keep the restaurant's offerings up-to-date.                               |
| 12         | As a user, I want to see images of the menu items so that I can make my choices based on the presentation of the food.              |
| 13         | As a user, I want to have a contact form so that I can reach out to the restaurant for inquiries or feedback.                       |
| 14         | As a user, I want to access the home page easily so that I can quickly navigate to other parts of the website.                      |
| 15         | As a user, I want to receive error messages if I make a mistake in the reservation form to correct my input.                        |
| 16         | As a user, I want to have a visually appealing interface that makes my experience enjoyable while browsing the website.             |
| 17         | As a user, I want the website to work well on mobile devices so that I can make reservations on the go.                             |
| 18         | As a user, I want to easily find the option to log in or sign up so that I can manage my reservations.                              |
| 19         | As a user, I want the website to load quickly so that I do not have to wait long to see the content.                                |
| 20         | As a user, I want the navigation bar to be clear and organized so that I can find what I am looking for without confusion.          |

## Bug Fixes

1. **Image Loading Issues**: Added Cloudinary to prevent images from disappearing after each deployment.
2. **Reservation Past Date Bug**: Added validation to prevent users from making reservations for past dates.
3. **CSS Issues**: Consolidated all CSS into `styles.css` to avoid confusion caused by inline styles.
4. **Cloudinary Environment Variables Bug**: We encountered an issue on Heroku where the static files collection failed because the Cloudinary environment variables were missing. This was fixed by setting `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET` directly in the Heroku config using the `heroku config:set` command.


## Future Enhancements

-   **Online Payment**: Not available for now, but could be added later.
-   **Comments**: Add a feature to allow user comments about the restaurant.
-   **Add a notification**: This is would make communication faster and ensure the restaurant can respond to users quickly.
-   **Add Opening and Closing Hours**: To let users know when the restaurant is open and when they can make reservations.

## References

-   Images sourced from [Pexels](https://www.pexels.com/), [Google](https://www.google.com/).
-   Bootstrap for styling: [Bootstrap Documentation](https://getbootstrap.com/).
-   Django documentation: [Django Framework](https://www.djangoproject.com/).

## Inspiration and Learning Resources

-   **Modification and Deletion Features**: Inspired by the course [Push Django & Python Apps to Heroku](https://www.udemy.com/course/push-django-python-apps-to-heroku/) on Udemy.
-   **Adding Menus**: Learned from the course [Python Django - Full Stack Web Developer Training](https://www.udemy.com/course/python-django-formation-developpeur-web-full-stack/) on Udemy.
-   **Tooltips and Other Bootstrap Features**: Inspired by the course [Bootstrap 5 - The Ultimate Training](https://www.udemy.com/course/bootstrap-5-la-formation-ultime/) on Udemy.
-   **Contact Page Creation**: Based on the tutorial from [GeeksforGeeks](https://www.geeksforgeeks.org/create-a-contact-form-using-html-css-javascript/).

## Acknowledgements

-   My Mentor Rahul for his ongoing support and feedback
-   The Code Institute's Tutor Support with Marco
