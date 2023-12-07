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
    - [Different account types for Participants and staff members / Admin](#different-account-types-for-participants-and-staff-members--admin)
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
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Python Packages](#python-packages)
  - [Programs Used](#programs-used)
- [Testing](#testing)
  - [Google Chrome Lighthouse](#google-chrome-lighthouse)
  - [Validator Testing](#validator-testing)
    - [Python Validator - PEP8](#python-validator-pep8)
    - [HTML W3C Validator](#html-w3c-validator)
    - [CSS Jigsaw Validator](#css-jigsaw-validator)
    - [Jshint Validator](#jshint-validator)
  - [Manual Testing](#manual-testing)
    - [Frontend](#frontend)
    - [Backend / Admin Panel](#backend--admin-panel)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Bugs / Issues](#bugs--issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Fork the repository](#fork-the-repository)
  - [Making a Local Clone](#making-a-local-clone)
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
 - Add information about the event such as category, title, excerpt, description, event_image, alt_tag, venue, published, status, eventobjects, max_seats, registered_seats, start_date, end_date, created_at, modified_at;
 - Create relevant navigation buttons for each section;
 - Create a section for like/unlike, comments, booking, and profiles.

 #### Features for upgraded experience
- Create a scrolled list of posts and events that allows the user to view all oosts and events along with all their details;
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
<img src="readme_assets/entity_relationship_diagram.png"><br>
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