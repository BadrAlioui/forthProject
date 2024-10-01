# Restaurant Booking System

## About The Project
The Restaurant Booking System is a web application that allows users to easily book tables. Our goal is to make the reservation process simple and provide a good experience for users.

## Objectives
- To provide an easy-to-use platform for making reservations.
- To engage customers with a friendly interface.
- To ensure a pleasant user experience on all devices.
- To allow users to manage their reservations easily.

## Built With
This project uses basic web technologies:
- **HTML5**: For structuring content.
- **CSS3/Bootstrap**: For styling and responsive design.
- **Django**: For back-end and data management.
- **JavaScript**: For interactive features.

## Key Features
- **Easy Reservations**: Users can select the date, time, and number of people for their booking.
- **Message Confirmation**: Users receive a confirmation message after making a reservation.
- **Reservation Management**: Users can cancel or change their reservations easily.
- **Responsive Design**: Ensures a smooth experience on mobile and desktop.

## Getting Started

### Prerequisites
- A modern web browser that supports HTML5 and CSS3.
- Python 3.x and Django installed.

### Installation
1. Clone the repository: `git clone [https://github.com/BadrAlioui/forthProject]`
2. Navigate to the project folder: `cd forthProject`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the Django server: `python manage.py runserver`

## Screenshots
Here are some screenshots of the application:

### Home Page
![Home Page](https://github.com/BadrAlioui/forthProject/blob/master/media/home-presentation.png?raw=true)

### Reservation Page
![Reservation Page](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_page.png?raw=true)

### Reservation List
![Reservation List](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_list_page.png?raw=true)

### Contact Page
![Contact Page](https://github.com/BadrAlioui/forthProject/blob/master/media/contact_presentation_page.png?raw=true)


## Validator Testing

**HTML Validation**:
- No errors or warnings on all pages.

**CSS Validation**:
- All CSS files passed without errors:

- css validator in style.css:

![css validator](https://github.com/BadrAlioui/forthProject/blob/master/media/css_validator.png?raw=true)

-home page:

![css home](https://github.com/BadrAlioui/forthProject/blob/master/media/home_css_validator.png?raw=true)

-contact page:

![css contact](https://github.com/BadrAlioui/forthProject/blob/master/media/contact_css_validator.png?raw=true)

-reservation page:

![css reservation](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_css_validator.png?raw=true)

## Accessibility
We are committed to ensuring accessibility for all users. Our platform has been tested to provide an inclusive user experience.

**Accessibility Mobile**

![Accessibility Mobile](https://github.com/BadrAlioui/forthProject/blob/master/media/mobile_accessibility.png?raw=true)

**Accessibility Mobile**

![Accessibility Desktop](https://github.com/BadrAlioui/forthProject/blob/master/media/desktop_accessibility.png?raw=true)


## Unfixed Bugs
Currently, there are no known bugs in the project.

## Deployment
The booking system is hosted on Heroku. To deploy your own version:
1. Upload the necessary files to your Heroku repository.
2. Set up the configuration for your app to be online.

You can access the live version here: [Restaurant Booking System](https://quiet-crag-61811-4fb808af66c6.herokuapp.com/)

## Manual Testing User Stories

## User Stories

### As a User, I Want to Make a Reservation
I can access the reservation page from the home page. The reservation form allows me to enter my details such as first name, last name, email, number of persons, date, and time. Upon submitting the form, I receive a confirmation message, indicating that my reservation has been successfully recorded.

### As a User, I Want to View My Reservations
I can view a list of all my reservations by navigating to the reservation management page. Each entry displays essential details such as the reservation date, time, and number of persons. This feature allows me to keep track of my bookings easily.

### As a User, I Want to Edit My Reservation
If I need to change any details regarding my reservation, I can click on the "Edit" button next to my reservation entry. This takes me to a pre-filled form where I can update my information. Once I submit the changes, I receive a success message confirming that my reservation has been updated.

### As a User, I Want to Delete My Reservation
If my plans change, I can delete my reservation directly from the reservation management page. After confirming the deletion in a pop-up modal, the reservation is removed from the system, and I receive a notification indicating that my reservation has been successfully deleted.

### As a User, I Want to Contact the Restaurant
The contact page provides a form where I can send messages or inquiries to the restaurant. After filling out my name, email, and message, I can submit the form. I receive a confirmation message indicating that my message has been sent successfully.

### As a User, I Want to Browse the Menu
I can view the menu items by navigating to the menus page. Each menu item includes an image, title, description, and price, giving me an overview of what the restaurant offers. This feature allows me to decide what I would like to order before making a reservation.

### As a User, I Want a Mobile-Friendly Experience
When accessing the website on my mobile device, the layout adjusts seamlessly, ensuring that I can easily navigate through the pages and fill out forms without any hassle. The responsive design enhances my overall experience, making it convenient to use on various devices.

### As a User, I Want to Ensure My Data is Secure
I trust that my personal information and reservations are securely handled. The application has measures in place to protect my data, and I can manage my reservations safely through the user interface.

### As a User, I Want Easy Navigation
The navigation bar at the top of the page helps me quickly access different sections of the website, such as home, menus, reservations, and contact. This feature simplifies my journey through the application.

### As a User, I Want to Receive Error Messages
If I make a mistake while filling out a form, I want clear error messages to help me correct the issue. This ensures that I can successfully complete my tasks without frustration.

### As a User, I Want to Access the Application Anytime
The application is hosted online, allowing me to access it at any time from anywhere, as long as I have an internet connection. This accessibility makes it convenient for me to make reservations whenever needed.

### As a User, I Want to See Validation Messages
When I submit forms, I want to see validation messages confirming my inputs are correct or alerting me to any errors. This helps ensure that my information is accurately captured.

---

## Unfixed Bugs
During development, I encountered a few bugs:

1. **Image Loading Issues**: Some images did not load correctly when accessed through external links due to CORS restrictions.
2. **Form Submission Errors**: Occasionally, users received error messages even when valid inputs were provided, which required thorough validation checks.
3. **Responsiveness on Older Browsers**: The website sometimes did not display correctly on older browser versions, affecting user experience.


### Browser Compatibility
The application has been tested on various browsers, including Firefox, Chrome, and Microsoft Edge, to ensure a consistent user experience.

## Future Enhancements
- **Filtering Feature**: Possibility to add menus.
- **Online Payment**: Not available for now, but could be added later.
- **Comments or Contact**: Add a feature contact about restaurant.

## References
- Images sourced from [Pexels](https://www.pexels.com/).
- Bootstrap for styling: [Bootstrap Documentation](https://getbootstrap.com/).
- Django documentation: [Django Framework](https://www.djangoproject.com/).

## Inspiration and Learning Resources
- **Modification and Deletion Features**: Inspired by the course [Push Django & Python Apps to Heroku](https://www.udemy.com/course/push-django-python-apps-to-heroku/) on Udemy.
- **Adding Menus**: Learned from the course [Python Django - Full Stack Web Developer Training](https://www.udemy.com/course/python-django-formation-developpeur-web-full-stack/) on Udemy.
- **Tooltips and Other Bootstrap Features**: Inspired by the course [Bootstrap 5 - The Ultimate Training](https://www.udemy.com/course/bootstrap-5-la-formation-ultime/) on Udemy.
- **Contact Page Creation**: Based on the tutorial from [GeeksforGeeks](https://www.geeksforgeeks.org/create-a-contact-form-using-html-css-javascript/).


## Acknowledgements
- My Mentor Rahul for his ongoing support and feedback
- The Code Institute's Tutor Support with Marco