# Spec A Console!

A Django Capstone project

[Link to deployed site](https://spec-a-console-448d20442e38.herokuapp.com/)

[Link to project KanBan](https://github.com/users/lratcli/projects/12)

Spec A Console is a fun website whose purpose is to allow people to create and share alternate-history games consoles. It's a chance to re-live plaground argunments about would could be, what should be, and what definitely shouldn't be.

Create an account and create a system for others to view or leave a review of.

Mobile example screenshot (actual mobile):

![Mobile example screenshot](readme-assets/introduction/mobile-sceenshot.webp)

Example of tablet resolution scaling:

![Tablet example screenshot](readme-assets/introduction/tablet-example.webp)

Example of desktop resolution scaling:

![Desktop example screenshot](readme-assets/introduction/desktop-example.webp)


# Table of Contents

- [User Experience and Design](#user-experience-and-design)
    - [Agile Methodology](#agile-methodology)
        - [User Stories](#user-stories)
        - [MoSCoW Prioritisation](#moscow-prioritisation)
        - [Project KanBan Board](#project-kanban-board)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Wireframes](#wireframes)
    - [Colour](#colour)
    - [Fonts](#fonts)
- [Features](#features)
    - [Admin](#admin)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Main page](main-page)
    - [Create System page](#create-system-page)
    - [System Detailed page](#system-detailed-page)
    - [My Systems](#my-systems)
    - [Create Account](#create-account)
    - [Log In](#sign-in)
    - [Log Out](#log-out)
    - [User Notifications](#user-notifications)
- [Technologies and Languages](#technologies-and-languages)
- [Deployment](#deployment)
- [Testing](#testing)
- [Bugs](#bugs)
- [Use of AI](#use-of-ai)
- [References and Credits](#references-and-credits)


# User Experience and Design

<details>
  <summary>Click to expand section</summary>

The site goal is to create a website where people can come and share their ideas on what might have made a good console or not, and others can give feedback on that in the form of a "review". It is important that users can 'own' their systems by posting them from a user account, and that they can modify and also delete any console idea that they have created.

As a layer of protection against misuse, all reveiws must be approved by an administrator after creation or modification before anyone other than the user-creator can see them on the site. Reviews must also be approved before anyone other than the user-creator can see them.

## Agile Methodology ##

In keeping with the principles of **Agile Development**, following ideation User Stories were created and then assigned to appropriate Epics.

The four Epics that User stories are split are:

- Epic: Admin - core administration capability
- Epic: User General - features common to all user activities
- Epic: User Proposed-System - create and view hypothetical gaiming systems
- Epic: User Review - attach user created reviews of a hypothetical gaming system to that system

These Epics are represented by labels on respective user stories on the Kanban board.

## User Stories

The User Stories created to guide this project, and their respective Epics, are as follows:

**Epic: Admin**

- *Admin full control*: As an admin, I can add, modify, or delete "proposed-systems" and "reviews" associated with regular users, so that I can handle any issues that occur on the site, including after a proposed gaming-system or review has gone live on the site.

- *Admin Content Approval*: As a site admin, I approve "proposed-systems" and their "reviews" before they appear on the site, so that I can maintain the integrity of the site.

**Epic: User General**

- *Create user account*: As a site user, I can create a user account, so I can own my hypothetical systems and reviews of others’.

- *Responsive, mobile first design*: As a site user, I want the site to be responsive across devices, so that I can browse the site on my phone on lunch break, or write a detailed explanation on my laptop or desktop.

- *Dedicated proposed-system pages*: As a site user, I want to be able to read about people’s proposed gaming systems on a page dedicated to that system, so that I can see in detail what ideas other people are coming up with.

- *Home page content*: As a site user, I want to be presented with a collection of the latest fantasy systems on the home page, so I can easily dip into some of the latest content on the site

- *Message Admin*: As a site user with an account, I want to be able to message admin directly, so I can engage them directly from the site as a known user.

**Epic: User Proposed-System**

- *Create hypothetical gaming system*: As a user I want to be able to create my own custom, hypothetical a gaming-system to be displayed on the site, so I can share my ideas or thoughts with others.

- *User-owner edit system*: As a user creating a gaming-system, I want to be able to edit and update my proposed console, so that I can add additional detail or respond to feedback.

- *Delete proposed system*: As a user creating a gaming-system, I want to be able to delete gaming-systems that I no longer wish to propose, so that I can curate my proposed systems and remove ones that no longer feel deserving of a place in my collection

- *Detailed description of proposed gaming system*: As a user creating a gaming-system, I can leave a detailed description and rationale for a system I’ve created, so I can explain or justify my ideas as fully as I wish to.

- *Detail sections for proposed system*: As a user creating a gaming system, I want to have dedicated areas to enter brief details about a system in key categories: CPU, Graphics processor, memory, price, proposed year. This is so that I can quickly get across the idea for the system without readers having to go into a more detailed description first.

- *Proposed-system image*: As a user creating a gaming-system, I want to be able to upload an image representing the system, so I can make my entry on the site unique or distinctive.

**Epic: User Review**

- *User review of others' proposed-systems*: As a user I want to be able to leave reviews or feedback on console ideas, so I can be part of a larger discussion in the community.

- *Review scores*: As a site user, I want to see an average review score along with each proposed system on the home page, so I can decide which systems to look at first.

- *Reviewer edit own reviews*: As a user creating creating reviews for other users' systems, I want to be able to modify my reviews, so I can keep my reviews up to date with edits to the system I am reviewing or changes in how I feel about a system.

- *Reviewer delete own reviews*: As a user who has created reviews for other users' systems, I want to be able to fully delete my review data from the database, so I can be sure that my review is no longer attached to a proposed system in any way.

## MoSCoW Prioritisation ##

In keeping with the Agile Development approach, Stories were prioritised based on the value they added to the site.

Initially there were no *Won't Have* User Stories as all were deemed to be of some degree of desireability, and at the start of developement it seemed that it might potentially be possible to implement all of them.

Towards the end of the project, it was deemed that three user stories that had been **Could Have** were unrealistic in the time left and were changed to **Won't Have**. They were then moved back into the **"Backlog"** column on the KanBan board to indicate that they were not being implemented in this round of development, but that were still desireable for a future iteration.

## Project KanBan board ##

The User Stories along with their Epic and MoSCoW catagorisation via labels can be seen on the project KanBan board.

[Link to project KanBan](https://github.com/users/lratcli/projects/12)

This screenshot shows the current state of the KanBan board at the time of finalising the Readme.

![KanBan board at time of finishing up](readme-assets/kanban/kanban.webp)

## Entity Relationship Diagram (ERD) ##

The ERD for the database is as follows:

![Database Entity Relationship Diagram](readme-assets/erd/erd.webp)

In addition to the Allauth user account model, there are models for the Gaming System and the Review.

The relationship between User and GamingSystem is one to many, as is User to Review. The relationship between GamingSystem and Review is also one to many, as one instance of GamingSystem can have many reviews.

As this is a Django/PostreSQL project, the GamingSystem and Review models inherit from the Django Model.

The GamingSystem model is used to support full end-user CRUD funtionality.

## Wireframes ##

Wireframes for the site design are below. They were initially sketched on paper then recreated using Balsamiq. Wireframes were created for the home page, the detailed page for each system, and for the "create a system" page containing the form used to create a system.

**Home page & My Systems:**

The home page has an almost identical layout to the "My Systems" page, which differs only in some of the text above the listed systems.

![Home page wireframe](readme-assets/wireframes/capstone-home.webp)

**Detailed page for each system:**

![Detailed system page](readme-assets/wireframes/capstone-detailed.webp)

**Create a System page:**

![Create a System page wireframe](readme-assets/wireframes/capstone-create.webp)

## Colour ##

In keeping with the theme of the site, the colour scheme chosen was influenced by the first level of a classic video game, Green Hill Zone from Sonic the Hedgehog on the Sega Megadrive.

![Colour palette](readme-assets/colour/colours.webp)

## Fonts ##

The site uses a primary and a seconday font, sourced from Google Fonts. These are Orbitron and Quantico, as they were determined to be be a good fit for retro focused games-system based site, while still offering a high degree of legibility.

![Google Fonts used](readme-assets/fonts/fonts.webp)

</details>
<br>

# Features #

<details>
  <summary>Click to expand section</summary>

## Admin  ##

The site allows for designated administrators to sign in, and from there administer the site using the Django admin panel. Approval of Gaming Systems and Reviews that have been submitted by users are done through the admin panel. 

![Admin panel](readme-assets/features/admin.webp)

## Navbar ##

The site features a responsive navbar, that collapses into a hamburger menu at tablet or lower screen sizes.

As a logged in user, navigation options are Home, Create System, My Systems, and Logout.

As a visitor who is not logged in, navigation options are Home, Sign Up, and Login.

![Navbar on mobile](readme-assets/features/navbar-mobile.webp)

![Navbar on desktop](readme-assets/features/navbar-full.webp)

## Footer ##

The footer contains contact and social media links, and a "Back to Top" link for easier navigation.

![footer](footer.webp)

## Main page ##

The main page features brief outlines of the six most recently added and approved gaming systems created by users. When more than six systems are on the site, pagination controls are displayed allowing the user to navigate back through more systems.

![Main page](readme-assets/features/main-page.webp)

![Pagination controls](readme-assets/features/main-page-pagination.webp)

## Create System page ##

The Create System page allows a logged in user to create a system using a form. The form fields are:

This form allows a user to upload an representative image with the submission, so it can be displayed along with the system details.


![Create System page](readme-assets/features/create-system.webp)


Fields for release year and price are validated to ensure year of release is between 1972 and 2025, and that price is not negative.

![Release year validation](readme-assets/features/year-validation.webp)

![Price validation](readme-assets/features/price-validation.webp)

## System Detailed page ##

The System: Detailed page in a full page focusing on only one of the user submitted systems. It present in full all details that the creator entered on the Create System page. It also shows an average score of reviews from other users.

If the person viewing is also the creator, they have the option to modify or delete their System.

![System Detailed](readme-assets/features/system-detailed.webp)

If the user choses to delete their System, they are presented with a delete confirmation modal.

![Delete confirmation modal](readme-assets/features/delete-confirmation-modal.webp)

Below the System is a form which allows another logged-in user to review the system. Users can only post one review per system, and the creator cannot review their own creation.

![Review section](readme-assets/features/reviews.webp)

## Edit system ##

The Edit System page is very similar to the Create System page.

![Edit System](readme-assets/features/edit-system.webp)

## My Systems ##

Very similar to the the main page, this shows all the systems that a logged in user has created, including ones that are not yet approved. They are displayed in the order of newest to oldest.

Like the main page, this displayed up to six systems, after which pagination controls appear to allow navigation to their older systems.

![My Systems](readme-assets/features/my-systems.webp)

## Create Account ##

The site has a simple sign up form with an optional email field. The site uses django-allauth.

![Sign Up](readme-assets/features/sign-up.webp)

## Log In ##

The site has a simple login page.

![Log in](readme-assets/features/login.webp)

## Log Out ##

![Log Out](readme-assets/features/log-out.webp)

## User Notifications ##

The site always has the username of the currently logged in user near the top of the page, directly under the navbar. 

![Username](readme-assets/features/username.webp)

The site also features confirmation notifications for key actions, including those involved with data creation, modification and deletion. These notifications are displayed near the top of the screen, directly under the username.

Confirmation notifications appear after:
- Sign In
- Sign Out
- Creating a system
- Editing a system
- Deleting a system
- Creating a review

![Signed In Notification](readme-assets/features/notification-singed-in.webp)

![Review Submitted Notification](notification-review-submitted.webp)

</details>
<br>

# Technologies and Languages

