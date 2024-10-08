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

-page signup:

![signup validator](https://github.com/BadrAlioui/forthProject/blob/master/media/signup_validator.png?raw=true)

-page reservation:

![reservation validator](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_validator.png?raw=true)

-page list of reservation:

![reservation_list validator](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_list_validator.png?raw=true)

-menu page:

![menu_page validator](https://github.com/BadrAlioui/forthProject/blob/master/media/menu_page_validator.png?raw=true)

-login page:

![login validator](https://github.com/BadrAlioui/forthProject/blob/master/media/login_page_validator.png?raw=true)

-home page:

![home_page validator](https://github.com/BadrAlioui/forthProject/blob/master/media/home_page_validator.png?raw=true)

-Edit reservation:

![edir_reservation validator](https://github.com/BadrAlioui/forthProject/blob/master/media/edit_reservation_validator.png?raw=true)

-contact page:

![contact validator](https://github.com/BadrAlioui/forthProject/blob/master/media/contact_page_validator.png?raw=true)
**CSS Validation**:
- All CSS files passed without errors:

- css validator in styles.css:

![css validator](https://github.com/BadrAlioui/forthProject/blob/master/media/css_validator.png?raw=true)


**JavaScript Validation**:

![Javascript validator](https://github.com/BadrAlioui/forthProject/blob/master/media/javascript_validator.png?raw=true)

**Python Validation**:

***Reservation***

-Reservation Views:

![reservation_views validator](https://github.com/BadrAlioui/forthProject/blob/master/media/view_reservation.png?raw=true)

-Reservation Urls:

![reservation_urls validator](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_urls.png?raw=true)

-Reservation Models:

![reservation_urls validator](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_model.png?raw=true)

-Reservation Forms:

![reservation_forms validator](https://github.com/BadrAlioui/forthProject/blob/master/media/reservation_form.png?raw=true)

***Mysite***

-Mysite Views:

![mysite_views validator](https://github.com/BadrAlioui/forthProject/blob/master/media/mysite_view.png?raw=true)

-Mysite Urls:

![mysite_urls validator](https://github.com/BadrAlioui/forthProject/blob/master/media/mysite_urls.png?raw=true)

-Mysite Forms:

![mysite_forms validator](https://github.com/BadrAlioui/forthProject/blob/master/media/mysite_forms.png?raw=true)

***Menu***

-Menu Views:

![menu_views validator](https://github.com/BadrAlioui/forthProject/blob/master/media/menu_views.png?raw=true)

-Menu Forms:

![menu_forms validator](https://github.com/BadrAlioui/forthProject/blob/master/media/media_forms.png?raw=true)

-Menu Urls:

![menu_urls validator](https://github.com/BadrAlioui/forthProject/blob/master/media/media_urls.png?raw=true)

-Menu Models:

![menu_models validator](https://github.com/BadrAlioui/forthProject/blob/master/media/media_models.png?raw=true)

## Accessibility
We are committed to ensuring accessibility for all users. Our platform has been tested to provide an inclusive user experience.

**Accessibility Mobile**

![Accessibility Mobile](https://github.com/BadrAlioui/forthProject/blob/master/media/mobile_accessibility.png?raw=true)

**Accessibility Desktop**

![Accessibility Desktop](https://github.com/BadrAlioui/forthProject/blob/master/media/desktop_accessibility.png?raw=true)



## Deployment
The booking system is hosted on Heroku. To deploy your own version:
1. Upload the necessary files to your Heroku repository.
2. Set up the configuration for your app to be online.

You can access the live version here: [Restaurant Booking System](https://quiet-crag-61811-4fb808af66c6.herokuapp.com/)

## User Stories

| User Story | Description |
|------------|-------------|
| 1 | As a user, I want to easily book a table so that I can reserve a spot for my desired date and time. |
| 2 | As a user, I want to provide my personal details such as my name, email, and number of persons when making a reservation. |
| 3 | As a user, I want to select the date and time for my reservation so that I can plan my visit accordingly. |
| 4 | As a user, I want to receive a confirmation message after submitting the reservation form so that I know my booking was successful. |
| 5 | As a user, I want to be informed if the restaurant is fully booked on my selected date to avoid confusion about my reservation. |
| 6 | As a user, I want to edit my reservation details if my plans change, while I am still logged in. |
| 7 | As a user, I want to cancel my reservation if I can no longer make it, but only while I am logged in. |
| 8 | As a user, I want to view a list of all my past reservations so that I can keep track of my dining history. |
| 9 | As a user, I want to access the menu page to see the available dishes before making a reservation. |
| 10 | As a user, I want to view the details of a specific menu item so that I can learn more about what I will be ordering. |
| 11 | As a user, I want to create new menu items as an admin to keep the restaurant's offerings up-to-date. |
| 12 | As a user, I want to see images of the menu items so that I can make my choices based on the presentation of the food. |
| 13 | As a user, I want to have a contact form so that I can reach out to the restaurant for inquiries or feedback. |
| 14 | As a user, I want to access the home page easily so that I can quickly navigate to other parts of the website. |
| 15 | As a user, I want to receive error messages if I make a mistake in the reservation form to correct my input. |
| 16 | As a user, I want to have a visually appealing interface that makes my experience enjoyable while browsing the website. |
| 17 | As a user, I want the website to work well on mobile devices so that I can make reservations on the go. |
| 18 | As a user, I want to easily find the option to log in or sign up so that I can manage my reservations. |
| 19 | As a user, I want the website to load quickly so that I do not have to wait long to see the content. |
| 20 | As a user, I want the navigation bar to be clear and organized so that I can find what I am looking for without confusion. |

## Bug Fixes
1. **Image Loading Issues**: Modified the path to access images using relative or absolute paths to fix image loading issues.
2. **Reservation Past Date Bug**: Added validation to prevent users from making reservations for past dates.
3. **CSS Issues**: Consolidated all CSS into `styles.css` to avoid confusion caused by inline styles.

## Future Enhancements
- **Filtering Feature**: Possibility to add menus.
- **Online Payment**: Not available for now, but could be added later.
- **Comments or Contact**: Add a feature contact about restaurant.

## References
- Images sourced from [Pexels](https://www.pexels.com/), [Google](https://www.google.com/).
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
