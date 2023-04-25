[<< Back to main ReadMe](README.md)


# DESK HQ - Testing

Visit the deployed site: [DESK HQ](https://desk-hq.herokuapp.com/)

---

## CONTENTS

  * [Manual Testing](#manual-testing)
    * [User Story Testing](#user-story-testing)
    * [Full Testing](#full-testing)
    <!-- * [JS unit tests](#js-unit-tests) -->
  * [Automated Testing](#automated-testing)
    * [Python Unit Tests](#python-unit-tests)
    * [Code Validation](#code-validation)
    * [Lighthouse](#lighthouse)
- - -

## Manual Testing

* ### User Story Testing


| Expectations                                                                                 | How are they achieved?                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a **first time user**                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I want to be able to access the website from any device. | The website is fully responsible and accessible on all screen sizes, starting at 360px.|
| I want to easily Understand what the site is for.                           | The Home and the about page describes the goals of the site, and a Contact Form is included in case the user has any other questions.                       |
| I want to be able to easily navigate and find content.  | The navbar with a fixed top position is always present on the screen and allows for navigating the website from any point on the website.                      |
| I want to create account to make booking.                                                                     | The user can register a new account.                                                                                                                                                                 | I want to Contact somebody via the contact form or contact details for enquiry.                    | The website provides a contact form.                                        |
| Quickly understand the benefits of co-working and how the space can help me grow my business, so that I am motivated to sign up.               | The description of the site on the home and about us page encourages new users to register for an account.                                                                                                                                                            |                     ||                                                                                                ||                                            |       | I want to learn more about the project on github. | A github link and a link to social media are available in the footer and accessible from every page. |
| I want to receive feedback from my intaraction with the website. | 1. Django messages inform the user about the status of their actions. <br>2. Error messages notify the user if something goes wrong. |
|  As a **Returning user**                                                                               |                                                                                |                                                              ||                            ||
| I want to Log in to my account..          | A login link is provided on the navbar.          ||
| I want to be able to easily make my workspace booking. | The book a space button is displayed prominently on the hero image of the home page. |
| I want to be able to Edit my workspace booking |  When a user views their booking on the space booking page, they are given the option to edit their booking.
| I want to be able to Delete my workspace booking. | When a user views their booking on the space booking page, they are given the option to delete their booking. When the user selects delete, a modal will pop up to confirm deletion, then redirected to confirmation page. |
| As an **Admin user**                |
| I want to be able to manage or approve booking contents. |The admin panel provides CRUD functionalities, which allows for the management and modification of user authentication, contents, users, groups, and permissions.   |


[<< Back to main ReadMe](README.md)
- - - 


* ### Full Testing

  The app was manually tested in the following browsers:

  * Chrome
  * Safari
  * Firefox
  * Edge
  * Opera

Full manual testing were performed on defferent devices and screen sizes, using [Media Gensis](https://responsivedesignchecker.com/) & [Browser Stack](https://www.browserstack.com/).

BrowserStack is a cloud-based web and mobile testing platform that provides testing on a variety of browsers, operating systems, and mobile devices. It allows running automated and manual tests on real devices and browsers, which helps to ensure that web applications are compatible with different browsers, operating systems, and devices.

Futher testing were done by friends and family on a variety of devices and screen sizes. 





| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|Test responsiveness of website on all screen sizes, on and browsers | 1. Open website in browser: https://desk-hq.herokuapp.com/ <br>2. Right click and inspect <br>3. Click the toggle device toolbar <br>4. Set the zoom <br>5. Click and drag the responsive window down to resize between 300px to 2900px, checking contents layout. <br>6. Repeat steps on all pages| Website is responsive, all elements contained, and images not distorted| Website is responsive, all elements contained, and images not distorted. | Pass |
| `Navbar` |
|  |  |  |  |  |
| DESK HQ Logo & Title | When clicked the user will be redirected to the home page. | Clicked Logo and title | Redirected to the home page. | Pass |
| Home Page Link | When clicked the user will be redirected to the home page.| Clicked link | Redirected to the home page. | Pass |
| About Us Page Link | When clicked the user will be redirected to the about us page. | Clicked link | Redirected to the about us page. | Pass | 
| Services Page Link | When clicked the user will be redirected to the services page. | Clicked link | Redirected to the services page | Pass | 
| Booking Details Page Link (Logged in users only) | When clicked the user will be redirected to the booking page. | Clicked link | Redirected to the booking page | Pass | 
| Sign Up Link (Only shown if user not in session) | When clicked the user will be redirected to the sign up in page. | Clicked link | Redirected to the sign up in page | Pass | 
| Log in Link (Only shown if user not in session) | When clicked the user will be redirected to the log in page. | Clicked link | Redirected to the log in page | Pass | 
| Log out Link (Logged in users only) | When clicked the user will be redirected to the home page and a flash message displayed to let the user know they have been logged out successfully. | Clicked link |Redirected to the home page and a flash message displayed to let me know I have been logged out | Pass | 
| `Footer` |
|  |  |  |  |  |
| DESK HQ Title | When clicked the user will be redirected to the home page. | Clicked title | Redirected to the home page. | Pass | 
| Copyright year | The copyright should display the correct year - this is a JavaScript function that checks what the current year is, and injects it into the footer | Checked the year | Displaying the correct year | Pass |
| `Home Page` |
|   |   |   |   |
| Book a space button on the hero image carousel| When clicked the user will be redirected to the space booking page. | Clicked button | Redirected to the space booking page | Pass | 
| Our Services button on the image card | When clicked the user will be redirected to the services page. | Clicked link | Redirected to services page | Pass | 
| Enquire Now button | When clicked the user remains on home page. Flash message informs user message received | Clicked button | User remains on home page | Pass | 
| `Log in Page` |
| Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass | 
| Password input empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | tooltip tells me this field is required |  Pass | 
| Log in button | Saves the user to session and redirects to home, or the booking page, if user tries to book without log in. Flash message is displayed to user as user’s name | Submitted form | Redirected to the home or the booking page, if user tries to book without log in first and flash message shown | Pass | 
| Incorrect username or password used | A message should display saying username/password incorrect - not letting user know which input is incorrect | Incorrect username and/or password entered | Message display to let the user know they have entered an incorrect username and/or password | Pass | 
| Link to Sign up page |  This should redirect the user to the sign up page | Clicked link | Redirected to the sign up page | Pass |
| `Sign Up Page` |
| | | | | | |
| Username input | The username should not include space| Entered username with space | tooltip lets the user know they have entered invalid username | Pass | 
| Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass | 
| Username input | If username is in use, message should displayed to user | username already exist | Message displayed username already in exist | Pass| 
| Email input | The email input should include an email address  | Entered plain text | Tooltip tells user to use an email address here | Pass | 
| Email input - empty | The email is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass | 
| Password input | This field should contain at least 8 characters long | Entered password too short | Tooltip tells user the password should be at least 8 characters long | Pass | 
| Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass | 
| Sign up button | Should redirect user to home page and a log in successful message is displayed | Created new user and submitted form | Redirected to home page and a flash message is displayed | Pass |
| `About us Page` | 
|   |   |   |   |  | 
| About us Page | Validate navigation to the correct page from the navbar when clicked | Link navigate to about us page | Link navigate correctly | Pass | 
| Contact us button | When user clicks redirect user to the contact form on the home page  | Link navigate to contact form on home page | Element behaves as expected | Pass | 
| `Services Page` |
|   |   |   |   |  |
| Services Page | Validate navigation to the correct page from the navbar when clicked | Link navigate to services page | Link navigate correctly | Pass |
| `Space Booking Page` | 
| Book a workspace button ((Only accessible if user is logged in)) | User can make booking. Users choose from choice of drop down options in the space booking services. | Clicked button | Booking saved to database, and user is redirected to home page with a flash message | Pass |
| Location dropdown | This should be a choice field with the location address. <br>2. User should be able to select a location of their choice. <br>3. Selection saved saved | Clicked location address | Location saved to the database | Pass | 
| Space Booking dropdown | This should be a choice field with the space booking type. <br>2. User should be able to select a space booking of their choice. <br>3. Selection saved | Clicked space booking | space booking saved to the database | Pass | 
| Booking Date | This should be a date selection field with the calendar. <br>2. User should be able to select a date of their choice. <br>3. Selection saved | Clicked booking date | booking date saved to the database | Pass | 
| Booking Date Validation | This should be a date selection field with the calendar. <br>2. User cannot select a past date or same day. <br>3. User get an error message Date cannot be in the past or the same day. Booking is not saved and redirects the user to the  space booking page and a flash error message to let the user know booking has not been successful. | Clicked booking date button | Booking is not saved to database and redirects the user to the space booking page and a flash error message to let the user know booking has not been successful | Pass | 
| Booking Duration dropdown | This should be a choice field with the booking duration. <br>2. User should be able to select a duration of their choice. <br>3. Selection saved | Clicked booking duration | booking duration saved to the database | Pass | 
| Booking Start dropdown | This should be a choice field with the booking start time. <br>2. User should be able to select a booking start of their choice. <br>3. Selection saved | Clicked booking start | booking start saved to the database | Pass | 
| Booking end dropdown | This should be a choice field with the booking end time. <br>2. User should be able to select a booking end of their choice. <br>3. Selection saved | Clicked booking end | booking end saved to the database | Pass | 
| `Booking Details Page` | 
|   |   |   |   |  | 
| Highlight Booking Details in the navbar (Only shown if user is logged in) | When the user clicks this link they should be taken to the booking details page to view their booking if any previously made. | Click button | Redirected to the booking details page | Pass | 
| Edit booking button | The user should be taken to the edit booking page with the selected space booking pre-populated in the input | Clicked button | Taken to the edit space booking page. Input pre-populated with the current booking field | Pass | 
| Delete button | When the user clicks the delete button a modal should pop up asking the user to confirm they wish to cancel the booking, user is redirected to a confirm delete page | Clicked button | Modal popped up and displayed the confirm deletion message | Pass | 
| Delete Button on Deletion modal| When the user clicks the delete button the user is redirected to a confirm delete page. A flash message will confirm deletion and the user is redirected to space booking page | Clicked button | Booking Details is deleted from the page and a flash message displayed success. Redirected to the booking details page | Pass | 
| Cancel button on deletion modal | When the user clicks the cancel button the modal should close | Clicked button | Modal closed | Pass | 
| `Error Page` | 
|   |   |   |   |   | 
| Home page link | Redirects the user to the home page | Clicked link | Redirected to home page | Pass | 
| `Pagination` | 
|   |   |   |   |   | 
| Pagination element | The element should navigate the booking details page. <br>2. Ensure the pagination block is present. <br>3. Ensure it works when clicked| The pagination block is present when needed | Element behaves as expected | Pass | 
| `Back to top button` | 
| Back to top button| This element should appear when user scroll down the page. <br>2. It should take user back to the top of the page when clicked. <br>3. It should be repeated across all pages.| Button appears when scrolled down and takes you back to the top of the page.| Button behaves as expected. | Pass | 
| `Django Messages work correctly` | 
| Flash/Display messages| Messages should be displayed at the top when user sign in. <br>2. User make booking/update/delete. <br>3. User logout | A message appears at the top and disappear after 3.5 seconds | Elements behave as expected | Pass | 
| `Hover color change on buttons` | 
| Hover over buttons | This button should change color when user hover on the buttons on the home page. <br>2. Hover over links and social icons in the footer. <br>3. Hover over the contact us on the about us page. <br>4. Hover over sign in and logout page and navigate to booking bookings page. | Button changed color when hovered over. | Elements behave as expected. | Pass |


[Back to the Top](#contents)

- - -


## Automated Testing

### Python Unit Tests

This project uses the [Django’s unit tests](https://docs.djangoproject.com/en/4.1/topics/testing/overview/).

* Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach.

* The tests solely rely on database access such as creating or querying the models. Hence, the test were created using 'test classes' as subclasses of django.test.TestCase rather than unittest.TestCase. Leading to unit tests that pass when run in isolation but fail when run in a suite.





[<< Back to main ReadMe](README.md)