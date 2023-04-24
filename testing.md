DESK HQ - Testing

Visit the deployed site: [DESK HQ](https://desk-hq.herokuapp.com/)

# CONTENTS

 * [User Story Testing](#user-story-testing)
  * [Manual Testing](#manual-testing)
  * [Unit Testing](#unit-testing)
    * [Python unit tests](#python-unit-tests)
    * [JS unit tests](#js-unit-tests)
  * [Automated Testing](#automated-testing)
      * [Code Validation](#code-validation)
      * [Lighthouse](#lighthouse)


## User Story Testing

| Expectations                                                                                 | Realisation                                                                                                                                                                                                                                                                                                                                                                                                                          |
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

- - - 