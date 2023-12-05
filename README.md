# Little Angels
Little Angles is designed to be a social platform for the parents to get together and collaborate with each others. The primary goals of the web are to:
1. Provide parents the ability to share the picture of their little ones with others and make it an unforgetable memory for themselves;
2. Act as an hub for parents to get informed about the events and social activities and book one.
3. Provide a simple and inituitive user experience for parents to use.
4. Offers a minimal set of impactful features chosen in order to deliver a useful app within achieveable development timeframe, while laying a solid foundation for additional features in the future.

The site is showcasing Python (DRF framework), JavaScript (React library), HTML, CSS, Bootstrap, PostgreSQL database, Herokuapp, and Gitpod for Project Portfolio 5.

And can be accessed by this [link.](https://drf-api-littleangels-f86db13e3ae5.herokuapp.com/)

![Responsive Mockup Screenshot](/readme_assets/mockup.png)

## Table of Contents
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
    - View all posts by a specific user: As a user I can view all the posts by a specific user so that I can catch up on their latest posts, or decide I want to follow them
    - Edit profile: As a logged in user I can edit my profile so that I can change my profile picture and bio
    - Update username and password: As a logged in user I can update my username and password so that I can change my display name and keep my profile secure
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