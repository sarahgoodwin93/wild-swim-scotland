# [Wild Swim Scotland](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Wild Swim Deployed Page")

![am-i-responsive-image](documentation/readme-images/am-i-responsive.png "am-i-responsive-image")

# Introduction

Wild Swim Scotland is a site for the community of wild swimmers within Scotland to connect and find out about upcoming swims they may wish to participate in. The staff users will post upcoming swims so that their community can join a swim, and site users can go back to the site to view their upcoming swims.

The site is aimed at all wild swimmers around Scotland and hopes to help build a sense of community for these lovers of the cold!

[Live Site Here](https://wild-swim-scotland-47f727d45ac1.herokuapp.com/ "take you to the Wild Swim Deployed Page")

# Table of Contents

- [Key Project Goals](#key-project-goals)
- [Agile Development](#agile-development)
- [User Stories](#user-stories)
- [User Experience](#user-experience)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Typography](#typography)
    - [Colour Palette](#colour-palette)
    - [Logo](#logo)
    - [Design Choices](#design-choices)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Non logged in user](#non-logged-in-user)
            - [The Landing page And General Site Content](#the-landing-page-and-general-site-content)
            - [Login](#login)
            - [Register](#register)
        - [Logged in User](#logged-in-user)
            - [Logout](#logout)
            - [Your Upcoming Swims](#your-upcoming-swims)
        - [Staff User](#staff-user)
            - [Add Swim](#add-swim)
            - [Edit and Delete buttons](#edit-and-delete-buttons)
            - [Delete Swims](#delete-swim)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Deploying on GitHub Pages](#deploying-on-github-pages)
    - [The ElephantSQL Database](#the-elephantsql-database)
- [Credits](#credits)
    - [Content](#content)
        - [Images](#images)
    - [Education](#education)
- [Acknowledgements](#acknoledgements)

[Back to Top](#wild-swim-scotland)

# Key Project Goals

The goals of the sites functionality are:

- List View: users can see all the swim cards, even if they have not registered or logged in
- Register: users can register to the site so that they can use the sites functionality 
- Logged In: users have the ability to join a swim and view their upcoming joined swims
- Logged Out: users are asked if they wish to sign out of the site
- Staff login: staff users can create a new swims, read, edit and delete the swims they have created from their staff account
- Admin: can create new staff users

# Agile Development

A Kaban board was used in GitHub to create the agile development process – see the board [here]( https://github.com/users/sarahgoodwin93/projects/3 "Kaban board for Wild Swim Scotland Project")

User stories were labelled using the MoSCoW method.

[Back to Top](#wild-swim-scotland)

# User Stories

4 Epics were created broken down into user stories, the epics included:

1. Admin
2. Staff
3. Site Access
4. User Functions

The user stories are as follows:

## Epic - Admin

### Create staff users

- As an admin, I can use the Django admin panel to create new staff users so that they can create new swims
    - AC1 - Admin can access the Django admin panel
    - AC2 - Admin can create staff users in the Django admin panel
    - AC 3 - New staff users can create, read, edit and delete swims

Tasks 
- Create staff users
- Ensure new staff members can create, read, edit and delete swims

## Epic - Staff

### Create Swim Posts (Full CRUD)

- As a site staff member, I can make new swim posts so that my users can see upcoming swims
    - AC1 - Create new swims by filling out the 'Add Swim' form
    - AC2 - Read the new swim that has been created on the homepage
    - AC 3 - Update/ edit the swim that I have created
    - AC 4 - Delete the swim I have created

Tasks
-  Create 'Add Swim' form on user interface for staff members only to be able to add swims
- Create view so that the added swims will be added to the homepage
- Create authenticated users for that specific swim so that only that staff member can edit the swims they have added
- Create a delete warning message so that staff can confirm they want to delete the swim

## Epic - Site Access

### Log-in and log-out

- As a site user, I can log in with my created username and password to access the site and see my previous actions
    - AC1 - Site user can log in with their created username and password after they have registered to the site
    - AC2 - Site users can see the swims they have registered from a previous login
    - AC 3 - Site user can log out when they have finished their session and confirm they want to log out

Tasks
- Link accounts/login template so that users can sign into the site
- Link accounts/logout template so that users can sign out of the site
- Ensure data is saved from previous login so that users can see their previous swim actions

### Register an account

- As a site user I can register an account so that I can return to see the swims I have booked to join
    - AC1 - User can register account and see site functionality

Tasks
- Create a Register nav link button
- Link 'accounts/sign_up.html' template so that new users can register to the site
- Ensure registered users can see site functionality changed from being logged in vs logged out

## Epic - User Functions

### View wild swim list

- As a site user I can view the wild swims around Scotland so that I can decided if I wish to register and sign up to a swim
    - AC1 - When the site loads, the list of swims is visible to the user both logged and not logged in.
    - AC2 - User can view swim detail without logged in
    - AC 3 - User can join the swim once logged in

Tasks
- Create a swim model to pull data from added swims and view to show the swims on the homepage
- Create user authentication so that only logged-in users can join swims

### Join a swim

- As a logged-in site user, I can click to join a swim so I can make sure there is a place for me on that time and date
    - AC1 - The site can be logged into and the join swim button is not visible to users who are not logged in or registered
    - AC2 - The join swim button then moves that swim card to the Upcoming Swims page where users can revisit their upcoming swims
    - AC 3 - Users can cancel their swim reservation

Tasks
- Ensure the 'Join Swim' button is not visible to unauthorised users
- Create model and view for moving joined swim into upcoming swim page
- Create cancel button which removes the swim from the upcoming swim page

## Future Stories

Future user stories were also created for the following:

- Commenting on swims
- Adding reviews to site
- Editing account details


# User Experience

## Wireframes

![Wireframe Image](documentation/readme-images/wireframe.png "wireframe image")

Site structure was created before the site was created to test layout idea.
After testing UX, a different approach was taken for better flow of the site navigation. 
Nav bar was moved to middle of page with clear call to actions.
Main image was removed to create focus on swim card images rather than a header image.
Logo was moved to middle of page to have more impact. 

## Database Schema

For this project the Django User Model was used for user account and one custom models with full CRUD were created for creating swims, this model is available for staff users only. 
A second custom model was created for joining a swim, however this does not have full CRUD as users can only edit and delete their joined swim, rather than create and update.

The data schema was created using [drawSQL](https://drawsql.app/ "drawsql website homepage") before the project was started to get the flow and function of the models. 

Some of the fields in the below image do not reflect the final data types used (such as Cloudinary) – please see the app for the true data types. 

![Data Schema Image](documentation/readme-images/new-data-schema.png " Data Schema Image ")

## Typography

The google font [Oswald](https://fonts.google.com/specimen/Oswald/ "Oswald font") was used throughout the site with different weights for different headings and paragraphs.

I chose this font for its tall height and wide proportions, making it a great choice for readability and also mimicking the swim cards height, making the site flow nicely. Oswald has rounded corners which give it a friendly appearance while still remaining bold and strong.  

## Colour Palette

I chose the colour #0d1a32 as the primary colour to remind people of the water and paired this with a white background for contrast and for a clean look and finish. As the swims will all have an image of a wild swim, either uploaded by the creator or using the default image, the blues in images from the water will help tie in with #0d1a32 as the primary colour. 

Secondary colours #327ab7 and #d6e4f0 were chosen as a continuation of #0d1a32 with an accent colour of #b5e2e0. These blues all represent the water that draws all swimmers to it. 

![Color palette Image](documentation/readme-images/colour-palette.png "Color palette Image ")

### Logo

The wild swim logo was created by Sarah Goodwin using Photoshop and the Oswald font. Waves were added to tie the site user back to the main purpose of the site, wild swimming.

![Logo Image](documentation/readme-images/ws-logo.png " Logo Image ")

## Design Choices

I wanted the design of the site to feel fresh and clean, just like how a wild swim makes you feel. I wanted the user experience to be easy to navigate and for the site to be very functional – users can come in, see the details they need, choose which swims to join and interact with each other. I did not want unnecessary detail about the swims as part of the fun of wild swimming is going into nature and letting that be your experience rather than overloading with information.

This is why I chose to display the swims as swim cards which have a very clean look.  

![Swim Card](documentation/readme-images/swimcard.png " Swim Card Image ")

[Back to Top](#wild-swim-scotland)

# Features

## Existing Features

## Non-Logged in User

### The Landing page And General Site Content

![Homepage](documentation/readme-images/homepage.png " Home page image ")

The landing page of the site shows a non logged in / non registered user the swims cards and gives and explanation of what Wild Swim Scotland is about. 
The text 
*Please see our upcoming swims, with times, dates and difficulty level.
Register an account with us and save your swims so that you can come back to see the details.
There is no limit on the number of swims you can join, or how many people can join them.
We'd love to see you there!*
Gives users a clear indication on what the site offers them and what actions they should next perform.

The landing page has 2 call to actions, Register and Login. 

The landing page is responsive for different screen sizes and scales down for easy mobile or tablet use. 

### Login

![login](documentation/readme-images/login.png " login image ")

The login page welcomes the user back to the site and has 2 clear options, username and password.
The design is friendly and approachable by using rounded corners on the input boxes.

The text at the bottom of the login section lets users know they must be logged into the site to use the full functions, it offers them an action if they have not yet registered by using the sign up link.

If the username and password are not correct this error will show.

![username error](documentation/readme-images/username-error.png " username error image ")

### Register

![register](documentation/readme-images/register-form.png " register form image ")

The register page welcomes users to the site with a friendly greeting. It lets users know that in order to use the site functions they must register an account.

It offers them space for a username, password and then rechecks the password to ensure it matches and there were no errors.
An example of some of the errors:

![register form errors](documentation/readme-images/register-form-errors.png " register form errors image ")

The text at the bottom lets users know who already have an account that they can sign in using the login page.

## Logged in User

### Logout

![logout](documentation/readme-images/logout.png " logout image ")

The logout page checks if the user does wish to sign out of the site.

### Your Upcoming Swims

![joined swims](documentation/readme-images/joined-swim-page.png " joined-swim-page image ")

The 'Your Upcoming Swims' page lets users know what swims they have joined previously and allows them to remove swims from their swim list. 

If the user has not yet joined an upcoming swim they will see the message "No swims joined yet"

![no swims joined](documentation/readme-images/no-swims-yet.png " no-swims-joined image ")

The page is solely for the user themselves and does not link to the staff user section of the site. As stated on the homepage, there is no limit to the number of people who can join a swim so therefore staff do not need to know who exactly will be attending. This section of the site is so that users can come back and quickly see what swims they were interested in and check the details easily. 

## Staff User

### Add Swim

![add swim form](documentation/readme-images/add-swim-form.png " add swim form image ")

The add swim page allows staff users to add new swims to the swim list. If they have not provided an image for their swim, the placeholder image will be added for them.
The Add Swim page has warnings for both the date, time and swim difficulty fields if they are not entered correctly.
To prevent users from enterting the date in the wrong format the placeholder text 'YYYY-MM-DD' has been added.
To prevent users from enterting the time in the wrong format the placeholder text '00:00:00' has been added.
to prevent users from enterting the swim difficulty incorrectly the 'Between 1-5 text' has been added.
If the above fields are not entered correctly a warning will show.

![add swim warnings](documentation/readme-images/add-swim-warnings.png " add swim warnings image ")


## Edit and Delete buttons

![edit and delete buttons](documentation/readme-images/edit-and-delete-button.png " edit and delete button image ")

The edit and delete buttons only appear to a swim that the specific staff user has added, they cannot edit or delete swims other staff members have created.

When clicking on the edit swim button the form has the same functions as the add swim form, however the swim details are already populated so that the staff user can edit them according. The same error warning functions as the add swim form.

## Delete Swim

When clicking the delete swim button the user is asked if they are sure they want to delete the swim before the action is performed. 

![delete warning](documentation/readme-images/delete-swim.png " delete swim image ")

## Future Features

There are some future features that I would like to add to the project to improve user functions.

- Reviews:
I began to create the review feature of the site, where users could come in and add reviews for different swim locations so that others could make a more informed decision on if they wanted to join a particular swim. However this feature was moved to future implementation as it could not be fully realised to the standard of the project at this time.

- Community Board:
It would be good to have a community board for wild swimmers to chat to each other and post stories and photos from their swims and connect together

- Date Picker:
Currently the date picker allows staff users to pick any date, a future implimentation would be to restrict the date picker to only have future dates

- Past Swims:
A section of the community page where past swims would automatically go after their date was passed so users could see what type of swims they had done previously

- Joined Swims saved to staff dashboard:
In the future I would like to have the join swim button log which user has joined which swim and have a staff dashboard area so that staff users could see how many people had signed up to that particular swim. 


[Back to Top](#wild-swim-scotland)

# Technologies Used

- [Lucidchart](https://www.lucidchart.com/ "link to Lucidchart homepage")
Lucidchart was used to create the wireframe in the planning stages of the project
- [drawSQL](https://drawsql.app/ "Drawsql homepage")
Drawsql was used to create the data schema
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "link to html5 wikipedia")
Used to create structure and content for the site.
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html "link to w3")
Used to add custom styles to the site.
- [Django](https://www.djangoproject.com/ "link to django docs homepage")
The python framework used to develop the site.
- [Bootstrap](https://getbootstrap.com/ "link to bootstrap homepage")
The CSS framework used to add styles and structure to the site.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "link to Python wikipedia")
Used to provide functionality to the site.
- [Cloudinary](https://cloudinary.com/ "link to cloudinary homepage")
Used to host images for the swim cards
- [ElephantSQL](https://www.elephantsql.com/ "link to elephantsql homepage")
Used to host the database used for the site.
- [Am I Responsive?](https://ui.dev/amiresponsive "Link to Am I responsive webpage")
Am I Responsive was used to see the responsive design and create screenshots of the final page on different devices.
- [Codeanywhere](https://app.codeanywhere.com/ "Link to Codeanywhere webpage")
Codeanywhere was used for writing code, adding, committing and pushing to GitHub before issues were faced and moved to GitPod.
- [Gitpod](https://www.gitpod.io/#get-started "Link to gitpod webpage")
Used to continue to create code and file structure for the respository.
- [GitHub](https://github.com/ "Link to github webpage")
GitHub was used to store the code files, README files and asset files after pushing
- [Heroku](https://id.heroku.com/login "Link to Heroku login")
Heroku was used to deploy the project. 

# Testing

Testing detail can be found [here](TESTING.md)

# Deployment

This project was developed using [Codeanywhere](https://app.codeanywhere.com/ "Link to Codeanywhere login") to begin with until issues with codeanywhere occurred. It was committed and pushed to GitHub using the Codeanywehere terminals.
After the issues with codeanywhere, the project was moved to [GitPod](https://www.gitpod.io/ "link to gitpod homepage") and continued from there. The projected had deployed at the start so the following is a step by step of how it was first deployed.

## Cloning The Repository

To clone the repository using GitHub the following steps were taken:

1. In the repository, select the "code" tab.
2. Select "HTTPS" in the dropdown menu.
3. Click the 'copy URL to dashboard button.
4. Open your chosen IDE
5. Create a new workspace and paste in the copied URL
6. Press enter

## Deploying on GitHub Pages

To deploy this page to Heroku from its Codeanywhere repository, the following steps were taken:

1. Get Python Essentials Template from Code Institute [P3 Template](https://github.com/Code-Institute-Org/p3-template "p3 template link")
2. Create a new repository using the P3 template
3. Copy the repo URL and copy it into Codeanywhere to create a new workspace
4. Install Django - add to requirements file
5. Create Procfile and add guricorn
6. Log in to Heroku
7. Click 'New' - 'Create new app'
8. Enter a name for the application and select the region
9. Click 'Create App'
10. Go to Settings and connect to GitHub - choose the correct repository
11. Click 'Reveal config vars' and add DISABLE_COLLECTSTATIC as the key with a value of 1
12. Go to Deploy and scroll down, click on 'Deploy Branch' to manually deploy
13. Once the app has deployed, click 'Open App' at the top of the page

## The ElephantSQL Database
ElephantSQL PostgreSQL Database was used for this project, to set up a database the following steps were taken:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance
4. Select "Tiny Turtle (Free)" free plan.
5. Click "Select Region".
6. Select a data centre near you.
7. Click "Review".
8. Ensure that all details are correct and then click "Create instance".
9. Copy the database URL
10. Add the database into the setting.py file

You will also need to add the database to your Django settings.py file:

DATABASES = {

'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

}

[Back to Top](#wild-swim-scotland)

# Credits

## Content

Wording for the site was all created by Sarah Goodwin

### Images

Images for swim posts were taken from google images of the swim location.
The logo image was created by Sarah Goodwin on Photoshop

## Education

*Django models additional learning:*
- [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/ 'django documention for making queries')
To gain more understanding of making queries for my django modules this page was used, especially for the SwimPosts model.

- [Start Ratings for reviews](https://django-star-ratings.readthedocs.io/en/latest/?badge=latest/ 'how to use start ratings in django')
I wanted to incorporate star ratings in the review section of the site so this page was used to learn about star ratings in Django. This has been kept in for future implementation

- [Django Validators](https://studygyaan.com/django/how-to-implement-validators-in-django-models?utm_content=cmp-true 'how to use django validators')
How to use Django validators for the swim difficulty feature 

- [BuyBytes Youtube video on Validators](https://www.youtube.com/watch?v=1x0Zdukpjrs 'BugBytes youtube on Django ORM - Model Field Validators')
To add a 'swim difficulty' to the SwimPost model I used django validators and the above two sources were used to gain that understanding.

- [Date fields and timezones in Django](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/ 'django documentation on timezones')
To gain more understanding about date fields and how they work in django the above page was used.

- [User.is_authenticated](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/ 'django documentation on django.contrib.auth')
To create the logout, upcoming swims and add swim pages, the above page was used to gain understanding on how to add authenticated user sections.

*Django forms additional learning:*
- [Editing an inbuilt django form](https://stackoverflow.com/questions/7769805/editing-django-form-as-p 'stack overflow on how to edit dajngo form')
How to edit inbuilt django forms to be able to style the templates to suit the site better

- [Form Helper](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html 'read-the-docs page on crispy forms')
Reading on form helpers, decieded to use placeholder function instead for time and date in forms

- [Date Picker](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/#:~:text=In%20this%20case%2C%20we%20are,is%20rendered%20in%20the%20template. 'letscodemore date widget page')
To gain more understanding of how to add a date picker widget this site was used

*Django views additional learning:*
- [UpdateViews](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView 'django docoumentation for editing views')
More info on views, how they work and how to use the UpdateView speciffically 

- [Code.my Youtube video using the DeleteView](https://www.youtube.com/watch?v=8NPOwmtupiI&t=580s 'code.my youtube video on deleting blog posts')
To gain more understanding of how to created CRUD functionality, these sources were used, especially for the AddSwimView, EditSwimView and DeleteSwimView

- [Restrict access via url](https://docs.djangoproject.com/en/5.0/topics/auth/default/ "Using the Django authentication system")
How to restrict user from accessing content via the url, for example by typing swim/add to the url without being logged in as a staff member.

*Error Pages*
- [Adding Error Pages, 404 & 500](https://www.makeuseof.com/create-custom-404-error-page-django/ 'make use of us webpage')
How to add 404 and 500 pages

*Additional Education*
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow webpage")
Stack overflow was used to answer questions as to why certain code may not be performing as expected.

- [ChatGPT](https://openai.com/blog/chatgpt "link to chatgpt page")
  ChatGPT was used gain a better understanding of errors faced

- [CluelessBiker/mentoring](https://github.com/CluelessBiker/mentoring "link to CluesslessBiker repo")
  CluelessBiker mentoring github page was used to check examples of projects, access links to resources such as validators and w3schools, Am I Responsive.

# Acknowledgements

- Mentor, Lauren-Nicole, for all her help and support, the useful resources she provided and for being a friendly face throughout! Could not have done this project without her!!
- Friends and family who helped test the site on different devices and give real world user feedback


[Back to Top](#wild-swim-scotland)
