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
    - [User Stories](#user-stories)
    - [MoSCoW Prioritisation](#moscow-prioritisation)
    - [Project KanBan Board](#project-kanban-board)
- [Design](#design)
- [Features](#features)
- [Technologies and Languages](#technologies-and-languages)
- [Deployment](#deployment)
- [Testing](#testing)
- [Bugs](#bugs)
- [Use of AI](#use-of-ai)
- [References and Credits](#references-and-credits)


# User Experience and Design

The site goal is to create a website where people can come and share their ideas on what might have made a good console or not, and others can give feedback on that in the form of a "review". It is important that users can 'own' their systems by posting them from a user account, and that they can modify and also delete any console idea that they have created.

As a layer of protection against misuse, all reveiws must be approved by an administrator after creation or modification before anyone other than the user-creator can see them on the site. Reviews must also be approved before anyone other than the user-creator can see them.

In keeping witth the principles of **Agile Development**, following ideation User Stories were created and then assigned to appropriate Epics.

The four Epics that User stories are split are:

- Epic: Admin
- Epic: User General
- Epic: User Proposed-System
- Epic: User Review

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

-*User review of others' proposed-systems*: As a user I want to be able to leave reviews or feedback on console ideas, so I can be part of a larger discussion in the community.

-*Review scores*: As a site user, I want to see an average review score along with each proposed system on the home page, so I can decide which systems to look at first.

-*Reviewer edit own reviews*: As a user creating creating reviews for other users' systems, I want to be able to modify my reviews, so I can keep my reviews up to date with edits to the system I am reviewing or changes in how I feel about a system.

-*Reviewer delete own reviews*: As a user who has created reviews for other users' systems, I want to be able to fully delete my review data from the database, so I can be sure that my review is no longer attached to a proposed system in any way.

## MoSCoW Prioritisation ##

Stories were prioritised based on the value they added to the site.

Initially there were no *Won't Have* User Stories as all were deemed to be of some degree of desireability, and at the start of developement it seemed that it might potentially be possible to implement all of them.

*Agile 
Towards the end of the project, it was deemed that three user stories that had been **Could Have** were unrealistic in the time left and were changed to **Won't Have**. They were then moved back into the **"Backlog"** column on the KanBan board to indicate that they were not being implemented in this round of development, but that were still desireable for a future iteration.

## Project KanBan board ##

The User Stories along with their Epic and MoSCoW catagorisation via labels can be seen on the project KanBan board.

[Link to project KanBan](https://github.com/users/lratcli/projects/12)

This screenshot shows the current state of the KanBan board at the time of finalising the Readme.

![KanBan board at time of finishing up](readme-assets/kanban/kanban.webp)

## Entity Relationship Diagram (ERD) ##

The ERD for the database is as follows:

![Database Entity Relationship Diagram](readme-assets/erd/erd.webp)


## Wireframes ##

Wireframes for the site design are below. They were initially sketched on paper then recreated using Balsamiq. Wireframes were created for the home page, the detailed page for each system, and for the "create a system" page containing the form used to create a system.

**Home page:**

![Home page wireframe](readme-assets/wireframes/capstone-home.webp)

**Detailed page for each system**

![alt text](readme-assets/wireframes/capstone-detailed.webp)

**Create a System page:**

![Create a System page wireframe](readme-assets/wireframes/capstone-create.webp)
