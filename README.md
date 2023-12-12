# Little Angels
Little Angles is designed to be a social platform for the parents to get together and collaborate with each others. The primary goals of the web are to:
1. Provide parents the ability to share the picture of their little ones with others and make it an unforgetable memory for themselves;
2. Act as an hub for parents to get informed about the events and social activities and book one.
3. Provide a simple and inituitive user experience for parents to use.
4. Offers a minimal set of impactful features chosen in order to deliver a useful app within achieveable development timeframe, while laying a solid foundation for additional features in the future.

The site is showcasing Python (DRF framework), JavaScript (React library), HTML, CSS, Bootstrap, PostgreSQL database, Herokuapp, and Gitpod for Project Portfolio 5.

And can be accessed by this [link.](https://drf-api-littleangels-f86db13e3ae5.herokuapp.com/)

![Responsive Mockup Screenshot](/readme_assets/mockup.png)

## Contents
<a name="contents"></a>

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
  - [Scope](#scope)
    - [Simple and intuitive User Experience](#simple-and-intuitive-user-experience)
    - [Relevant content](#relevant-content)
    - [Features for upgraded experience](#features-for-upgraded-experience)
    - [Different account types for normal users and staff member/admin](#different-account-types-for-normal-users-and-staff-member--admin)
    - [Responsiveness](#responsiveness)
  - [Structure](#structure)
  - [Skeleton](#structure)
    - [Wireframes](#wireframes)
    - [Database](#database)
  - [Surface(Design)](#surface-design)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Typography](#typography)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Re-use of Components](#re-use-of-components)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Python Packages](#python-packages)
  - [JavaScript Packages](#javascript-packages)
  - [Programs Used](#programs-used)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Fork the repository](#fork-the-repository)
  - [Making a Local Clone](#making-a-local-clone)  
- [Testing](#testing)
  - [Google Chrome Lighthouse](#google-chrome-lighthouse)
  - [Validator Testing](#validator-testing)
    - [Python Validator - PEP8](#python-validator-pep8)
    - [HTML W3C Validator](#html-w3c-validator)
    - [CSS Jigsaw Validator](#css-jigsaw-validator)
    - [ESLint Validator](#eslint-validator)
  - [Manual Testing](#manual-testing)
    - [Front-end](#front-end)
    - [Back-end / API](#back-end-or-api)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Bugs / Issues](#bugs-or-issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgements](#Acknowledgements)


## UX
### Strategy
The objective of the site is to provide a social platform for all users especially parents to register an account, post pictures of the thier litte ones, express their feelings and thoughts through like/unlike a post or leave comment on a post, get informed about events and other social activities and book an event, and follow other users.

#### User Stories
- **User Goals**:<br>
  *Navigation & Authentication*
    - Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages
    - Routing: As a user I can navigate through pages quickly so that I can view content seamlessly without page refresh
    - Authentication - Sign up: As a user I can create a new account so that I can access all the features for signed up users
    - Authentication - Sign in: As a user I can sign in to the app so that I can access functionality for logged in users
    - Authentication - Logged in Status: As a user I can tell if I am logged in or not so that I can log in if I need to
    - Authentication - Refreshing access tokens: As a user I can maintain my logged-in status until I choose to log out so that my user experience is not compromised
    - Navigation: Conditional rendering - As a logged out user I can see sign in and sign up options so that I can sign in/sign up
    - Avatar: As a user I can view user's avatars so that I can easily identify users of the application

  *Adding & Liking Posts*
    - Create posts: As a logged in user I can create posts so that I can share my images with the world!
    - View a post: As a user I can view the details of a single post so that I can learn more about it
    - Like a post: As a logged in user I can like a post so that I can show my support for the posts that interest me

  *The Posts Page*
    - View most recent posts: As a user I can view all the most recent posts, ordered by most recently created first so that I am up to date with the newest content
    - As a user, I can search for posts with keywords, so that I can find the posts and user profiles I am most interested in.
    - View liked posts: As a logged in user I can view the posts I liked so that I can find the posts I enjoy the most
    - View posts of followed users: As a logged in user I can view content filtered by users I follow so that I can keep up to date with what they are posting about
    - Infinite scroll: As a user I can keep scrolling through the images on the site, that are loaded for me automatically so that I don't have to click on "next page" etc

  *The Post Page*
    - Post page: As a user I can view the posts page so that I can read the comments about the post
    - Edit post: As a post owner I can edit my post title and description so that I can make corrections or update my post after it was created
    - Create a comment: As a logged in user I can add comments to a post so that I can share my thoughts about the post
    - Comment date: As a user I can see how long ago a comment was made so that I know how old a comment is
    - View comments: As a user I can read comments on posts so that I can read what other users think about the posts
    - Delete comments: As an owner of a comment I can delete my comment so that I can control removal of my comment from the application
    - Edit a comment: As an owner of a comment I can edit my comment so that I can fix or update my existing comment

  *Adding Events*
    - View an event: As a user, I can view the details of a single event so that I can learn more about it

  *The Events Page*
    - View published events: As a user, I can view all the most recent events, ordered by most recently published so that I am up to date with the newest content
    - Infinite scroll: As a user, I can keep scrolling through the images on the site, that are loaded for me automatically so that I don't have to click on "next page" etc

  *The Event Page*
    - Event page: As a user I can view the event page so that I can take more actions
    - Book an event: As a logged in user I can book an event so that I can reserve a seat for my little one
    - View bookings: As a user I can view my total bookings that I have
    - Delete bookings: As an owner of a booking I can delete my booking so that I can control removal of my booking from the application

  *The Profile Page**
    - Profile page: As a user I can view other users profiles so that I can see their posts and learn more about them
    - Most followed profiles: As a user I can see a list of the most followed profiles so that I can see which profiles are popular
    - User profile - user stats: As a user I can view statistics about a specific user: bio, number of posts, follows and users followed so that I can learn more about them
    - Follow/Unfollow a user: As a logged in user I can follow and unfollow other users so that I can see and remove posts by specific users in my posts feed
    - View all posts by a specific user: As a user, I can view all the posts by a specific user so that I can catch up on their latest posts, or decide I want to follow them
    - Edit profile: As a logged-in user I can edit my profile so that I can change my profile picture and bio
    - Update username and password: As a logged-in user I can update my username and password so that I can change my display name and keep my profile secure
<br>

- **Site Administrator Goals**:
  *Event Category*
    - Create, READ, Update, Delete Category: As as Site Admin I can perform CRUD operation on event category so that I can manage the event category content.

  *Events*
  - Create, READ, Update, Delete Event: As a Site Admin I can perform CRUD operation on events so that I can manage the event content.
  - As a Site Admin I can create draft events so that I can finish writing the content later.

  *Handle Errors and Secure Sensitive Information*
  - To handle any potential errors appropriately and consistently.
  - To keep security-sensitive information hidden.

### Scope
#### Simple and intuitive User Experience
 - Ensure the site title and logo provide first-hand information regarding the site;
 - Ensure the navigation menu is visible and functional at every step;
 - Ensure every page has a suggestive name/ icon that fits its content;
 - Ensure the design matches the theme of the event and does not confuse the user.

 #### Relevant content
 - Add information about the post such as user, title, description, image and image_filter, created_at, modified_at;
 - Add information about the event such as category, title, description, event_image, alt_tag, venue, published, status, eventobjects, start_date, end_date, created_at, modified_at;
 - Create relevant navigation buttons for each section;
 - Create a section for like/unlike, comments, booking, and profiles.

 #### Features for upgraded experience
- Create a scrolled list of posts and events that allows the user to view all posts and events along with all their details;
- Create a post detail page that allows users to update and delete the post, like/unlike the post, leave, edit, and delete comments;
- Created an event detail page that allows users to book an event.
- Created a like page that allows users to view the scrolled list of liked posts.
- Created a feed page that allows users to view the scrolled list of followed and following profiles.
- Created 
- Create a profile page that allows the user to view and edit his profile content. The user can also view its number and scrolled list of its posts, number of followed user and number of following users ;
- The search bar on the home page gives the user the ability to search for posts quickly and easily.

#### Different account types for normal users and staff member/admin
- User can perform CRUD operation on its posts, profile, comment, like, and booking;
- User can view and book events while the admin can add, update, and delete events, and categories;
- Participants have access only to their Profile page for managing it;
- Staff members/ admin has access to the admin panel to manage events, comments, category, and both types of accounts.

#### Responsiveness
- Create a responsive design for desktop, tablet, and mobile devices.

### Structure
It is a single-page website with different sections which navigate the user from one section to another seamlessly but the content depends on authentication and authorization of users.
- **Register/Login** sections give the user the possibility to create an account and authenticate for accessing different features;
- **Logout** feature is a modal that helps user to exit the site securely;
- **Home** page is open and visible to all types of user irrespective of registeration and authorization and includes list of all posts;
- **Post Detail** section is visible only to logged-in users and can be accessed by clicking on the post_image_url. It allows the user to read the details of the post, like/unlike a post, leave, edit, and delete a comment.
- **Add Post** section is visible only to logged-in user and allows the user to add a new post;
- **Event** section is visible only to logged-in user and allows the user to view the scrolled list of events;
- **Event Detail** section is visible only to logged-in user and can be accessed by clicking on the event_image_url. It allows the user to read the details of the event, and book/unbook an event;
- **Feed** section is visible only to logged-in user and allows the user to view the scrolled list of posts posted by the users followed or following him/her profile;
- **Like** section is visible only to logged-in user and allows the user to view the scrolled list of posts liked by him/her;
- **Profile** section is visible only to logged-in users and allows the user to view and update its contents. The user can also view its posted posts, the number of its posts, followers, and following profiles;
- **The Admin Panel** page is visible only to staff members with admin rights/admin to manage the posts, events, comments, category, booking, profile, and user accounts.

### Skeleton
#### Wireframes
Wirefram is used to plan and sketch the website.

#### Database
PostgreSQL relational database is used to store the website data. The database model diagram is designed using [Miro](https://miro.com/).
<details>
  <summary>Database Schema</summary>
<img src="readme_assets/entity_relationships_diagram.jpg"><br>
</details>

### Surface (Design)
#### Color Scheme
The clean and energetic color pallete is selected and used for the website back and text colors.
![#color-pallete](/readme_assets/color-palette.png)
- (#5680e9) color is used as hover and active color for links and icons. The color is also used for buttons.<br>
![#5680e9](/readme_assets/5680e9.png)
- (#84ceeb) is used as background color along with(#c1c8e4). It is also used as links and icons colors.<br>
![#84ceeb](/readme_assets/84ceeb.png)
- (#c1c8e4) is used as background color along with(#84ceeb).<br>
![#84ceeb](/readme_assets/c1c8e4.png)
- (#000) is used as the text color for the website.<br>
![#000](/readme_assets/000.png)
- (#FFFFFF) is used as the main background color for header and Cards.<br>
![#FFF](/readme_assets/fff.png).<br>
A few other limited colors are used as border and shading colors.

#### Imagery
- The website logo that describes the website's purpose is taken from [Zarla](https://www.zarla.com/).
- The fictitious pictures used in the website are taken from [Pexcels](https://www.pexcels.com/).

#### Typography
- Poppins font is used as the main font for the website.<br>
![Poppins](/readme_assets/poppins.png)
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Agile Methodology
This project was developed using the Agile methodology.
All user stories implementation progress was registered using [littleangels_project](https://github.com/users/Ahmad-Hazrati/projects/8/views/1). As the user stories were accomplished, they were moved from the kanban board **To Do**, to **Progress** and finally to **Done** lists.

## Features 
### Existing Features
- __Home Page__ 
  - When the website loads, the home page will load as well as the default page to all users whether authenticated or not. 
  - The home page contains the most followed profiles, a search bar, and a scrolled list of all posts posted by the users. 
  - The user name, number of posts, number of followers, and number of followed users are displayed on the page.
  - The search bar will display a filtered scrolled list of posts based on the user inputs.
  - The post's title, description, image, date created, number of likes, and number of comments are displayed on the home page. 
  - The post image acts as an active navigational link to the post detail section.
  ![Home](/readme_assets/home.png)<br><br>
- __Post detail__ 
  - This section is visible to all users and contains all details of the post including number of likes and comments functionalities. 
  - If the user is not logged in then s/he is restricted and alerted to log in to use like or comment functionalities otherwise, can only view the number of likes and comments.
  - If the user is logged in and is the owner of the like then s/he can unlike the post and edit or delete his/her comments.
  - If the user is logged in and is the owner of the comment then s/he can edit and delete the comment through a dropdown menu.
  ![Post detail](/readme_assets/post_detail.png)<br><br>
- __Add post__
  - This section is only visible to authenticated users and users can add a post.
  - The section contains an image field, 2 input fields, and 2 buttons.
  - To increase the page loading speed and utilize the hosting file server space effectively the image size is controlled and the user cannot upload an image exceeding 2MB, 4096px in width or height. 
  ![Add post section](/readme_assets/add_post.png)<br><br>
- __Event__ 
  - The event section is only visible to authenticated users and contains the scrolled list of all events.
  - The event creation is maintained by the site admin.
  - The event section contains the most followed profiles and a scrolled list of all events posted by the user with admin rights from the admin panel. 
  - The event's title, image, description, event objects, venue, start date, end_date and published date areare displayed in this section. 
  - The event image acts as an active navigational link to the event detail section.
  ![Home](/readme_assets/event.png)<br><br>
- __Event detail__ 
  - This section is only visible to authenticated users and contains all details of the event including booking functionality. 
  - The user can book the event by clicking the book button.
  - If the user is the owner of the booking then s/he can delete his/her bookings through a drop down menu.
  - If the booking is blocked by the admin then the user will be notified with a warning message.
  ![Post detail](/readme_assets/event_detail.png)<br><br>
  - __Feed__ 
  - The feed section is visible to authenticated users.
  - This section contains the most followed profiles, a search bar, and a scrolled list of posts posted by the user followed by the current user logged in. 
  - The user name, number of posts, number of followers, and number of followed users are displayed on the page.
  - The search bar will display a filtered scrolled list of posts based on the user inputs.
  - The post's title, description, image, date created, number of likes, and number of comments are displayed in this section. 
  ![Home](/readme_assets/feed.png)<br><br>
  - __Like__ 
  - The like section is visible to authenticated users.
  - This section contains the most followed profiles, a search bar, and a scrolled list of posts liked by the current user logged in. 
  - The user name, number of posts, number of followers, and number of followed users are displayed on the page.
  - The search bar will display a filtered scrolled list of posts based on the user inputs.
  - The post's title, description, image, date created, number of likes, and number of comments are displayed in this section. 
  ![Home](/readme_assets/liked.png)<br><br>
- __Profile__ 
  The profile section is visible to authenticated users.
  - This section contains the most followed profiles, current user profile details, and a scrolled list of posts posted by the current user logged in. 
  - The user name, number of posts, number of followers, and number of followed users are displayed on the page.
  - The user can edit his profile, change the username, and change the password by clicking the dropdown menu.
  ![Profile](/readme_assets/profile.png)<br><br>
- __Signout__ 
  - The signout section is only visible to logged-in users and allows the user to log out securely from the website.
  - When the user clicks the sign out button, he securely logged-out and the home page loads.
  ![Signout](/readme_assets/signout.png)<br><br>
- __Signup__ 
  - The sign up section is visible to unauthenticated users and allows the user to create an account and securely access the website.
  - This allows the user to fill out the form and sign up. It includes a login button to navigate the user to login section in case already has an account.
  ![Signup](/readme_assets/signup.png)<br><br>
- __Signin__ 
  - The login section is visible to unathenticated users and allows the user to sign in and securely access the website.
  - The page allows the user to fill out his/her username and password to sign in. It also comprises a signup button to navigate the user to signup section in case not have created an account yet.
  ![Login](/readme_assets/signin.png)<br><br>
- __Builtin Admin Panel__ 
  - The builtin admin panel is only visible to authorized user and allows the user with admin rights to log in and securely access the website administration panel.
  - The page allows the admin to create, read, update, and delete the contents of the event, and category. 
  - The page allows the admin to stop booking functionality for normal users.
  ![Builtin Admin Panel](/readme_assets/admin_panel.png)<br><br>
  
  #### Re-use of Components
  - **Asset.js**
  Asset component has been extensively used in other components to display spinner and message while the data loads and display the message in case of any error or notification. It is used in NavBar.js, NotFound.js, EventsPage.js, PostCreateForm.js, PostPage.js, PostsPage.js, PopularProfiles and ProfilePage.

  - **Avatar.js**
  The Avatar component has been used in other components to display the user avatar. It is used almost on all pages.

  - **MoreDropdown.js**
  This component has been used in Booking.js, comment.js, Post.js and ProfilePage.js to provide the Dropdownmenu for edit, delete and udpate icons.

  - **CurrentUserContext.js**
  This component has been almost in all components to authenticate current user.

  - **ProfileDataContext.js**
  ProfileDataContext.js has been used extensively in PopularProfiles.js, Profile.js, and ProfilePage.js to provide follow/unfollow functionalities.

  - **useRedirect.js**
  This component has been used to provide redirect functionality for SignInForm.js, SignUpForm.js, and PostCreateForm.js.

  - **utils.js**
  The utils.js component has embedded a set of functionalities that are used in other components, such as fetchMoreData, followHelper, unFollowHelper, and TokenTimestamps. 


### Features Left to Implement
Initially, the idea was that the event section should have "like" functionality as the post section. The booking of the event should be based on the number of seats available and one user could book only one seat but due to limited time constraints couldn't implemented.
Further features inclusive (cited above) to implement are:
- Another feature to add could be a chat functionality. 
- a review page will be a better feature to be added to the app.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Technologies Used
### Languages Used
- **Python (Rest Framework), JavaScript (React Library), HTML, and CSS** are used extensively during the project.
- **Markdown**: Used exclusively for README.

### Python Packages
- **django** : Django is a high-level web framework for building web applications in Python. It provides a clean and pragmatic design for developing web applications and follows the model-view-controller (MVC) architectural pattern.
- **djangorestframework** : This is a powerful and flexible toolkit for building Web APIs in Django. It adds features like authentication, serialization, and viewsets to make it easier to build RESTful APIs.
- **django-allauth** : Django Allauth is a Django-based authentication system that handles everything from user registration to account management. It provides a customizable set of views, forms, and templates for handling authentication-related tasks.
- **django-filter** : Django Filter is used for allowing users to filter down the queryset based on model fields. It simplifies the process of creating dynamic querysets by providing a simple yet powerful way to filter down data based on parameters a user provides.
- **Pillow** : It is an updated fork of the Python Imaging Library (PIL) and provides easy-to-use methods for opening, manipulating, and saving many different image file formats.
- **gunicorn** : Gunicorn (Green Unicorn) is a WSGI HTTP server for Python web applications. It is commonly used to deploy Django applications in production, providing a stable and efficient server for handling HTTP requests.
- **psycopg2** : psycopg2 is a PostgreSQL adapter for Python. It enables Python applications to connect to a PostgreSQL database and perform various database operations.
- **PyJWT** : PyJWT is a Python library for encoding and decoding JSON Web Tokens (JWT). It is commonly used in web authentication and authorization mechanisms.
- **dj-cloudinary-storage** : This is a Django storage backend for Cloudinary, a cloud-based image and video management service. It allows you to easily integrate Cloudinary with your Django project for handling media files.
- **whitenoise** : WhiteNoise is a lightweight WSGI middleware for serving static files directly from Django application. It simplifies the process of serving static files in production without relying on a separate web server.
- **autopep8** : autopep8 is a tool that automatically formats Python code to comply with the PEP 8 style guide. It helps maintain a consistent coding style and can be integrated into development workflows to ensure code consistency.

### JavaScript Packages
- **react** : The core library for building user interfaces in React. It provides the foundational elements and APIs for creating components, managing state, and handling the rendering of UI elements in a React application.
- **react-dom** : A package that provides the DOM-specific methods that are used to interact with the DOM (Document Object Model). It's responsible for rendering React components into the DOM, updating them, and handling events.
- **axios** : A promise-based HTTP client for making asynchronous HTTP requests. It simplifies the process of sending requests to a server and handling responses. Used for communicating with RESTful APIs.
- **react-scripts** : A set of scripts and configurations used by Create React App (CRA) to build and run a React application.
- **jwt-decode** :  A library for decoding JSON Web Tokens (JWT). Useful for working with authentication tokens in client-side applications.
- **react-bootstrap** : A set of Bootstrap components implemented as React components. It is to provide pre-designed, responsive UI components, making it easier to create visually appealing and consistent user interfaces.
- **react-infinite-scorll-component** : It enables loading additional content as the user scrolls down a page, providing a seamless and continuous user experience for large datasets.
- **ESLint** : A tool for identifying and fixing problems in JavaScript code. It enforces coding standards, identifies potential issues, and helps maintain a consistent code style within a project.

### Programs Used
[React-Bootstrap4](https://react-bootstrap-v4.netlify.app/): used to add predefined styled elements and responsiveness.<br>
[Git](https://git-scm.com/): used for version control.<br>
[GitHub](https://github.com/): used to host the source code of the program.<br>
[Gitpod](https://gitpod.io/): used to write and test the code.<br>
[Heroku](https://dashboard.heroku.com/): used to deploy the project.<br>
[Cloudinary](https://cloudinary.com/): used to store static files.<br>
[PostgreSQL](https://www.elephantsql.com/): used to store the website data.<br>
[Balsamiq](https://balsamiq.com/wireframes/): used to sketch the project contents.<br>
[Miro](https://miro.com/): used to design the database model.<br>
[iLoveIMG](https://www.iloveimg.com/): used to crop and compress the images.<br>
[Zarla](https://www.zarla.com/): used to generate the website favicon and logo.<br>
[Font Awesome](https://fontawesome.com/): used for creating attractive UX with icons.<br>
[Google Fonts](https://fonts.google.com/): used for project typography.<br>
[ESLint](https://eslint.org/): used to validate the JSX codes.<br>
[CI Python Linter](https://pep8ci.herokuapp.com/#/): used to perform check of Python code.<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options): used to valid the HTML pages.<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri): used to valid the CSS.<br>
[Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): used for project debugging purpose.<br>
[React Developer Tools](https://chromewebstore.google.com/detail/fmkadmapgofadopljbjfkapdkoienihi): used for project debugging purpose.<br>
[Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=de): used to test the website performance, accessibility, best practices, and SEO.<br>
[W.A.V.E.](https://wave.webaim.org/): used for testing accessibility.<br>
[Pexels](https://www.pexels.com/): used to generate the website images.<br>
[Color-HEX](https://www.color-hex.com): used to generate the webiste colors.<br>
<br><a href="#contents">BACK TO CONTENTS 🔼</a>


## Deployment

### Deploying to Heroku
* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Next select your region.
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter the following variables and values:
    - Add "ALLOWED_HOST" and its value (excluding the https:// and trailing /);
    - Add "CLIENT_ORIGIN" and its value;
    - Add "CLOUDINARY_URL" and its value;
    - Add "DATABASE_URL" and its value;
    - Add "DISABLE_COLLECTSTATIC" and its value;
    - Add "SECRET_KEY" and its value;
8. Next, scroll down to the Buildpack section click Add Buildpack select Python, and click Save Changes.
9. Scroll to the top of the page and choose the Deploy tab.
10. Select Github as the deployment method.
11. Confirm you want to connect to GitHub.
12. Search for the repository name and click the connect button.
13. Scroll to the bottom of the deploy page and select the preferred deployment type.
14. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

### Fork the repository
To create a copy of the repository on your account and change it without affecting the original project, use **Fork** directly from GitHub:
1. On [My Repository Page](https://github.com/Ahmad-Hazrati/drf_api_littleangels), press Fork in the top right of the page
2. A forked version of my project will appear in your repository

### Making a Local Clone

1. Log in to Github and locate the [Github Repository.](https://github.com/Ahmad-Hazrati/drf_api_littleangels)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Testing 
Testing has taken place continuously throughout the development of the project. Each section, function and component was tested regularly. When the outcome was not as expected, debugging took place at that point.

### Google Chrome Lighthouse
Google Chrome lighthouse checks and generates a comprehensive report regarding the website's performance, accessibility, best practices, and SEO.<br>
![Lighthouse Report](/readme_assets/lighthouse.png)


### Validator Testing 
#### Python Validator - PEP8
- Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files were entered into the online checker and no errors were found in any of the custom codes.<br>
- **bookings app** <br>
**bookings admin.py** : No errors or warnings to show.<br>
![bookings admin.py PEP8](/readme_assets/bookings_admin.png)<br>
**bookings apps.py** : No errors or warnings to show.<br>
![bookings apps.py PEP8](/readme_assets/bookings_apps.png)<br>
**bookings models.py** : No errors or warnings to show.<br>
![bookings models.py PEP8](/readme_assets/bookings_models.png)<br>
**bookings serializers.py** : No errors or warnings to show.<br>
![bookings serializers.py PEP8](/readme_assets/bookings_serializers.png)<br>
**bookings tests.py** : No errors or warnings to show.<br>
![bookings tests.py PEP8](/readme_assets/bookings_tests.png)<br>
**bookings urls.py** : No errors or warnings to show.<br>
![bookings urls.py PEP8](/readme_assets/bookings_urls.png)<br>
**bookings views.py** : No errors or warnings to show.<br>
![bookings views.py PEP8](/readme_assets/bookings_views.png)<br>
**bookings admin.py** : No errors or warnings to show.<br>
![bookings admin.py PEP8](/readme_assets/bookings_admin.png)<br>

- **comments app** <br>
**comments admin.py** : No errors or warnings to show.<br>
![comments admin.py PEP8](/readme_assets/comments_admin.png)<br>
**comments apps.py** : No errors or warnings to show.<br>
![comments apps.py PEP8](/readme_assets/comments_apps.png)<br>
**comments models.py** : No errors or warnings to show.<br>
![comments models.py PEP8](/readme_assets/comments_models.png)<br>
**comments serializers.py** : No errors or warnings to show.<br>
![comments serializers.py PEP8](/readme_assets/comments_serializers.png)<br>
**comments tests.py** : No errors or warnings to show.<br>
![comments tests.py PEP8](/readme_assets/comments_tests.png)<br>
**comments urls.py** : No errors or warnings to show.<br>
![comments urls.py PEP8](/readme_assets/comments_urls.png)<br>
**comments views.py** : No errors or warnings to show.<br>
![comments views.py PEP8](/readme_assets/comments_views.png)<br>

- **drf_api_littleangels**<br>
**drf_api asgi.py** : No errors or warnings to show.<br>
![drf_api asgi.py PEP8](/readme_assets/drf_api_asgi.png)<br>
**drf_api permissions.py** : No errors or warnings to show.<br>
![drf_api permissions.py PEP8](/readme_assets/drf_api_permissions.png)<br>
**drf_api serializers.py** : No errors or warnings to show.<br>
![drf_api serializers.py PEP8](/readme_assets/drf_api_serializers.png)<br>
**drf_api settings.py** : The line too long is showing and since it is not recommended to edit the settings sentences which affect the project, so it is left unchanged.<br>
![drf_api settings.py PEP8](/readme_assets/drf_api_settings.png)<br>
**drf_api urls.py** : No errors or warnings to show.<br>
![drf_api urls.py PEP8](/readme_assets/drf_api_urls.png)<br>
**drf_api views.py** : No errors or warnings to show.<br>
![drf_api views.py PEP8](/readme_assets/drf_api_views.png)<br>
**drf_api wsgi.py** : No errors or warnings to show.<br>
![drf_api wsgi.py PEP8](/readme_assets/drf_api_wsgi.png)<br>

- **events app**<br>
**events admin.py** : No errors or warnings to show.<br>
![events admin.py PEP8](/readme_assets/events_admin.png)<br>
**events apps.py** : No errors or warnings to show.<br>
![events apps.py PEP8](/readme_assets/events_apps.png)<br>
**events models.py** : No errors or warnings to show.<br>
![events models.py PEP8](/readme_assets/events_models.png)<br>
**events serializers.py** : No errors or warnings to show.<br>
![events serializers.py PEP8](/readme_assets/events_serializers.png)<br>
**events tests.py** : No errors or warnings to show.<br>
![events tests.py PEP8](/readme_assets/events_tests.png)<br>
**events urls.py** : No errors or warnings to show.<br>
![events urls.py PEP8](/readme_assets/events_urls.png)<br>
**events views.py** : No errors or warnings to show.<br>
![events views.py PEP8](/readme_assets/events_views.png)<br>

- **followers app**<br>
**followers admin.py** : No errors or warnings to show.<br>
![followers admin.py PEP8](/readme_assets/followers_admin.png)<br>
**followers apps.py** : No errors or warnings to show.<br>
![followers apps.py PEP8](/readme_assets/followers_apps.png)<br>
**followers models.py** : No errors or warnings to show.<br>
![followers models.py PEP8](/readme_assets/followers_models.png)<br>
**followers serializers.py** : No errors or warnings to show.<br>
![followers serializers.py PEP8](/readme_assets/followers_serializers.png)<br>
**followers tests.py** : No errors or warnings to show.<br>
![followers tests.py PEP8](/readme_assets/followers_tests.png)<br>
**followers urls.py** : No errors or warnings to show.<br>
![followers urls.py PEP8](/readme_assets/followers_urls.png)<br>
**followers views.py** : No errors or warnings to show.<br>
![followers views.py PEP8](/readme_assets/followers_views.png)<br>

- **likes app**<br>
**likes admin.py** : No errors or warnings to show.<br>
![likes admin.py PEP8](/readme_assets/likes_admin.png)<br>
**likes apps.py** : No errors or warnings to show.<br>
![likes apps.py PEP8](/readme_assets/likes_apps.png)<br>
**likes models.py** : No errors or warnings to show.<br>
![likes models.py PEP8](/readme_assets/likes_models.png)<br>
**likes serializers.py** : No errors or warnings to show.<br>
![likes serializers.py PEP8](/readme_assets/likes_serializers.png)<br>
**likes tests.py** : No errors or warnings to show.<br>
![likes tests.py PEP8](/readme_assets/likes_tests.png)<br>
**likes urls.py** : No errors or warnings to show.<br>
![likes urls.py PEP8](/readme_assets/likes_urls.png)<br>
**likes views.py** : No errors or warnings to show.<br>
![likes views.py PEP8](/readme_assets/likes_views.png)<br>

- **posts app**<br>
**posts admin.py** : No errors or warnings to show.<br>
![posts admin.py PEP8](/readme_assets/posts_admin.png)<br>
**posts apps.py** : No errors or warnings to show.<br>
![posts apps.py PEP8](/readme_assets/posts_apps.png)<br>
**posts models.py** : No errors or warnings to show.<br>
![posts models.py PEP8](/readme_assets/posts_models.png)<br>
**posts serializers.py** : No errors or warnings to show.<br>
![posts serializers.py PEP8](/readme_assets/posts_serializers.png)<br>
**posts tests.py** : No errors or warnings to show.<br>
![posts tests.py PEP8](/readme_assets/posts_tests.png)<br>
**posts urls.py** : No errors or warnings to show.<br>
![posts urls.py PEP8](/readme_assets/posts_urls.png)<br>
**posts views.py** : No errors or warnings to show.<br>
![posts views.py PEP8](/readme_assets/posts_views.png)<br>

- **profiles app**<br>
**profiles admin.py** : No errors or warnings to show.<br>
![profiles admin.py PEP8](/readme_assets/profiles_admin.png)<br>
**profiles apps.py** : No errors or warnings to show.<br>
![profiles apps.py PEP8](/readme_assets/profiles_apps.png)<br>
**profiles models.py** : No errors or warnings to show.<br>
![profiles models.py PEP8](/readme_assets/profiles_models.png)<br>
**profiles serializers.py** : No errors or warnings to show.<br>
![profiles serializers.py PEP8](/readme_assets/profiles_serializers.png)<br>
**profiles tests.py** : No errors or warnings to show.<br>
![profiles tests.py PEP8](/readme_assets/profiles_tests.png)<br>
**profiles urls.py** : No errors or warnings to show.<br>
![profiles urls.py PEP8](/readme_assets/profiles_urls.png)<br>
**profiles views.py** : No errors or warnings to show.<br>
![profiles views.py PEP8](/readme_assets/profiles_views.png)<br>

- **manage**<br>
**manage.py** : No errors or warnings to show.<br>
![manage.py PEP8](/readme_assets/manage.png)<br>

#### HTML W3C Validator
The index.html has been checked and no errors were found when passing through the official WC3 Validator<br>
**index.html**: No errors or warnings to show.<br>
![Index](/readme_assets/w3c_validator_index.png)<br><br>

#### CSS Jigsaw Validator
All css modules are checked and no errors were found when passing through the official JIGSAW CSS.<br>
![Styles Modules](/readme_assets/jigsaw_css_validator.png)<br>


#### ESLint JSX Validator
All JSX codes were tested for potential errors with ESLint. Most of the errors are rectified except the below ones which are addressed here. Worth to mention that these codes were refactored based on the resources availabe in the stackoverflow but as it doesn't rectify the error, so left as it is. Nevertheless, these codes are mostly the same as were addressed in the P5 Walkthrough Project.<br>
![MoreDropdown](/readme_assets/eslint_moredropdown.png)<br>
![ProfilePage](/readme_assets/eslint_profilepage.png)<br>
![PostPage](/readme_assets/eslint_postpage.png)<br>
![PostsPage](/readme_assets/eslint_postspage.png)<br>


  ### Manual Testing

- __Front-end__
  - The frontend works properly, displaying the components and sections in the expected place. The components are working just fine and communicate with the API to get or post data.
  - The home page loads normally and functions properly. The website favicon and title load as expected.
  - The header section works properly both for desktop and mobile. The logo is at its correct place, and the home, sign-in, and sign-up buttons are showing and functioning properly. 
  - The navbar icons are displayed at the top in the desktop view but are hidden in the mobile view. The icon can be accessed through the hamburger menu. The hamburger menu opens when clicked on the hamburger icon and closes when clicked inside or outside the header section.
  - The landing page loads normally and displays the most followed profiles at the top in desktop view and at the right side in mobile view. As expected the user name and profile image are showing in the most followed profiles sections.
  - The search bar loads and functions normally. It returns the posts matched with the user inputs.
  - The posts are loading and displaying normally based on the created date. 
  - The scroll function works as expected in the deployed version and loads more posts as the user scrolls down.
  - The like and comment functionalities are working as expected. 
  - The functionality to display the number of likes and comments is active only for authenticated users.
  - The navigation links such post image url, like and comment icon are working fine and navigates the user to the post detail section. 
  - In the post detail section the dropdown menu component loads as expected based on the ternary condition applied. If the user is not the owner of the post then the menu doesn't show up.
  - The condition to like/unlike a post is also working fine. It checks if the user has already liked the post, if so, then unlikes it otherwise it likes it. 
  - The comments functionality is working without any issues. The user can view all comments written by other users and can update or delete his comments.
  - The scroll function functions as expected in the deployed version and loads more comments as the user scrolls down.
  - The sign-in section loads normally and authenticates the user as expected. It checks and controls the fields and all functions are working without any issues. The user can sign in, if s/he already has an account, otherwise, he can access the sign-up section with the provided link.
  - The sign-up section loads normally and displays all the required fields. The control function to check the fields such as empty fields, possible same username in the database, not matching passwords are alerted to the user for correction.
  - Post Creation button loads normally and functions without any issues. It provides the post creation form and controls the image size properly.
  - The event button works and navigates the user to the event section normally. The event details are displaying without any issue. 
  - The scroll function functions properly in the deployed version and fetch more events as the user scrolls down.
  - The url set on the event image navigates the user to the event detail section without any issues.
  - The event details are displaying as expected. 
  - The buttons to book or go back to the event section are working fine.
  - The booking function works without any issues. The fuctionality to check the current user and display the dropdown menu to delete the booking is working properly. 
  - The function to stop more booking from admin panel is working without any issue. The warning message is displaying.
  - The alert message for deletion of the booking is working properly.
  - The feed button works and navigates the user to the feed section as expected. The follower and following users' posts are loading without any issues. The scroll function functions in the deployed version as expected and loads more posts as the user scrolls down.
  - The like button works and navigates the user to the liked section without any issues. The posts liked by the user are fetching and loading properly. 
  - The profile button works and navigates the user to the profile section. 
  - The profile details including the number of posts, number of followers, and number of following users are loading properly.
  - The function to check the current user and load the dropdown menu if the user is the owner of the profile is working fine.
  - The edit button works as expected and loads the profile edit section.
  - The fields in the profile edit section are loading and working as expected.
  - The change username button works as expected and loads the edit page.
  The change username field loads and works just fine.
  - The change password button works and loads the password change section properly. The functionality to accept new passwords and confirm both password matches are working properly.
  - The sign-out button works as expected and securely logs out the user and loads the home page.

- __Back-end / API__
  - The API models, serializers, apps, URLs, and views are working and functioning as expected. 
  - It controls the execution of the data based on the provided models and methods.
  - It serializes the data and parses it as JSON to the frontend.
  - The performs the expected CRUD operation based on the API View Models.
  - The admin panel has been tested repeatedly without any issues. 
  - All models are working properly.
  - The admin user can perform CRUD operation on event and category models without any issues.
  - The admin user can publish events.

### Testing User Stories
User Stories are fully achieved and project is closed.<br>
![Little Angels Project](/readme_assets/closed_project.png)<br>
They are discussed in [**User Stories**](#user-stories) section under **Strategy** and for more details please refer to [Github Repository](https://github.com/users/Ahmad-Hazrati/projects/8/views/1).

<a href="#contents">BACK TO CONTENTS 🔼</a>

### Bugs / Issues

<table  width = 100% cellspacing="0" cellpadding="0">
   <tr>
   <th>Issue/Bug</th>
   <th>Solution</th>
   </tr>
   <tr>
   <td>
   The user was not passing as prop in Booking.js, therefore, the delete booking functionality was not working.
   </td>
   <td>
   The issue has been rectified by adding the user attribute as a foreign key to the event model and serializer.
   </td>
   </tr>
   <tr>
   <td>ImportError: Could not import 'restframework.renderers.JSONRenderer' for API setting 'DEFAULT_RENDERER_CLASSES'. ModuleNotFoundError: No module named 'restframework'.
   </td>
   <td>The issue is rectified by adding the below code to settings.py taken from django-rest-framework official website.
   `(REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]},)`
   </td>
   </tr>
   
   <tr>
   <td>CurrentUserContext.js:23 AxiosErrorcode: "ERR_BAD_REQUEST"config: {transitional: {…}, adapter: Array(2), transformRequest: Array(1), transformResponse: Array(1), timeout: 0, …}message: "Request failed with status code 401"name: "AxiosError"request: XMLHttpRequest {onreadystatechange: null, readyState: 4, timeout: 0, withCredentials: true, upload: XMLHttpRequestUpload, …}response: {data: {…}, status: 401, statusText: '', headers: AxiosHeaders, config: {…}, …}stack: "AxiosError: Request failed with status code 401\n    at settle (https://8080-ahmadhazrat-drfapilittl-ldkf5dv9gvn.ws-eu106.gitpod.io/static/js/0.chunk.js:4291:12)\n    at XMLHttpRequest.onloadend (https://8080-ahmadhazrat-drfapilittl-ldkf5dv9gvn.ws-eu106.gitpod.io/static/js/0.chunk.js:2992:70)"[[Prototype]]: Errorconstructor: ƒ AxiosError(message, code, config, request, response)toJSON: ƒ toJSON()isAxiosError: true[[Prototype]]: Objectconstructor: ƒ Error()message: ""name: "Error"toString: ƒ toString()[[Prototype]]: Object</td>
   <td>The issue is rectified by resetting the databases, clearing the browser caches, and remigrating the models.
   </td>
   </tr>
   <tr>
   <td>
   Get the error [27/Nov/2023 17:18:54] "POST /api/likes/ HTTP/1.1" 400 37
   </td>
   <td>
   Reset the likes model and remove the likes element from the model.
   </td>
   </tr>   
  </table>

### Unresolved Bugs or Issues

<table  width = 100% cellspacing="0" cellpadding="0">
   <tr>
   <th>Issue/Bug</th>
   <th>Debugging measures taken</th>
   </tr>   
   <tr>
   <td>The posts and comments are not loading when exceeding 10 in numbers and displaying the error message "Failed to load response data: No data found for resource with given identifier.
   </td>
   <td>The issue has been tackled severals times and with the support of the tutors but could not find the real cause to rectify it. As recommended downgraded the react and react-dom version to ^17.02 but still the issue persists and added to the un-resolved bugs.
   Worth to mention that in the deployed version it is working completely fine.
   </td>
   </tr>
   <tr>
   <td>While validating the JSX codes by ESLint, 4 JSX components were not successfully passed and raised below errors.
  1. `ProfilePage (122:11  error  Do not pass children as props. Instead, nest children between the opening and closing tags  react/no-children-prop)`<br>
  2. `PostsPage (70:17  error  Do not pass children as props. Instead, nest children between the opening and closing tags  react/no-children-prop)`<br>
  3. `PostPage (65:15  error  Do not pass children as props. Instead, nest children between the opening and closing tags  react/no-children-prop)`<br>
  4. `MoreDropdown (9:22  error  Component definition is missing display name  react/display-name)`
   </td>
   <td>Checked in Slack and Stackoverflow for a possible suitable solution, but unfortunately, the solutions do not work for these errors. The errors have also been followed with tutors, but since there was no issue in the codes and comply with the Walkthrough project, therefore, left as it is.
   </td>
   </tr>
   
  </table>

 <br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>


## Credits 
### Content 
- The idea of the project and most of the contents were taken from P5 walkthrough project. 
- The other contents are fictitious.

### Media
- The site logo image is taken from the [Zarla](https://www.zarla.com/) and the other site images are taken from [Pexels](https://www.pexels.com/).

### Code
- The code used for most parts of the website is taken from the [PP5 Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+RA101+2021_T3/courseware/70a8c55db0504bbdb5bcc3bfcf580080/953cd4e5015f483bb05263db3e740e19/).
- The code used for events and bookings api are written with the support of the mentor.

## Acknowledgements
- Thanks to my Code Institute mentor Ms. Juliia Konovalov for her guidance, insight, and constant confidence boost to help me in the right direction.
- Thanks to Code Institute for material and support (Tutor Assistance), Slack Community, and other valuable online resources.
- Some insight and help also taken stack overflows.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>