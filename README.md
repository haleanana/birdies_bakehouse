<h2 align = "center">Birdies Bakehouse</h2>

<p align ="center">An online bakery<br>
This website was inspired by my mums passion for baking. I wanted to create a simple online store where people can browse and purchase delicious treats.
</p>

## Table of Contents

[**Demo**](#demo)

[**UX**](#ux)

[**Technologies Used**](#technologies-used)

[**Information Architecture**](#information-architecture)

[**Testing**](#testing)

[**Bugs and Fixes**](#bugs-and-fixes)

[**Deployment**](#deployment)

[**Credits**](#credits)

## Demo

<a href= "https://our-recipe.herokuapp.com/" target= "_blank">Live Demo</a>


[**back to top**](#table-of-contents)
## UX

### Goals

The goal of this website is to create a user friendly online dessert store. The website should be easy to navigate but also able to convert visitors into customers.

### Target audience goals

This website is catered for people who wants to browse or purchase delicious treats/desserts for any type of occassion.

User needs:
- Be able to purchase items in the store.
- Be able to create and login to their own profile.
- Simple and clean design.
- See their order history via their profile.
- Submit comments on the desserts they have purchased.

How this website meets their needs:
- Users are able to check out via stripe. 
- Use of allauth module which is a nice and simple way to create and manage user profiles.
- Design is simple and clean but still visually appealing.
- All order history will show on their profile when logged in.
- The ability to submit comments.

### Goals as a developer

- Expand my portfolio.
- Practice my Python , JS , CSS and modules involved in this project.
- An online dessert store where people can purchase items.
- Capture customer data.

### User stories

As a user, what I would want in an online store
1. Direct and easy way to navigate.
2. A number of items to choose and purchase.
3. Easy and direct way to purchase.
4. Own profile to see my order history.
5. Access the website from any device.
6. Able to purchase items without having to register.

### Research

I visited a few online bakeries for inspiration and to discover what works and what doesnt. One thing I noticed is that most websites make it easy to navigate and purchase their items.
Most if not all, also has the feature to let the users purchase without making a profile.

### Design choices

**Colour scheme**

- The primary colours for this website are #fff , #FF7291 and black. The colours are chosen because they compliment each other well.
- The colour combination also presents a clean and simple looking website because the colours do not conflict with each other.

**Fonts**

- I'm using Roboto and Abhaya Libre as my main Fonts as this presents a much simpler and cleaner feel which is one of my design goals.

**Ease of use**
- Navbar is fixed at the top so users will always have access to the main/important pages.

**Product page**
- Cards are used to showcase the products in a neat and organised manner.
- Cards also provide a cleaner and less cluttered look which reflects the "clean" look goal.
- Search bar added so users can quickly search items.


### Wireframes

Figma was used to create my mock ups.


## Features

- [x] Users are able to purchase items.
- [x] Users are able to create their own profile.
- [x] Search bar for items where users can search any keyword related to the item that they want.
- [x] Comment section for registerd users.
- [x] Easy check out process.
- [x] Form validation.
- [x] Collapsible navbar on mobile view.


## Features to add


## Technologies used

**HTML** - To create the foundation and structure of my website. <br>
**CSS** - To add styles and make my website visually appealing.<br>
**Figma** - To create the wireframe of my website.<br>
**Javascript** - To expand the capability and interactivity of my website.<br>
**Python** - The core language used in this project.<br>
**Flask, Jinja, Pymongo** - Frameworks used for this project to help tie everything together.<br>
**Bootstrap CDN** - Components from BS library heavily used in this website.<br>
**MongoDB/Atlas** - To store and grab user submitted data for my website.<br>
**GitHub**- To store and share this project.<br>
**Heroku** - To deploy my website.<br>
**Font Awesome**- To access the icons that I wanted for this website.<br>
**Gitpod**- To write my code using their IDE.<br>

## Testing 

### Validated through:

- [W3C Markup Validation]( https://validator.w3.org/) for HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) for CSS.
- [JSHint](https://jshint.com/) for JavaScript.
- [Autoprefixer CSS]( https://autoprefixer.github.io/) for browser compatibility.

### Tested through 

- Google Lighthouse
- [Mobile Friendly Test - Result](https://search.google.com/test/mobile-friendly?id=9Plrf2ZSoX8vpdkyxBGLeA)
- Chrome developer tools
- [BrowserStack](https://www.browserstack.com/)


## Deployment ##

This project was built using Gitpod IDE , commited and published using GitHub.

### To run this project locally ###

1. Follow this <a href="https://github.com/haleanana/birdies_bakehouse" target = "_blank"> link </a>
2. Click "Clone or Download". 
3. Copy the clone URL under the HTTPs section.
4. Run the files in your local IDE.
5. Upgrade PIP with 
```
$ pip install -U pip
```
6. Install dependancies using 
```
$ pip3 install -r requirements.txt
```
7.  Create a env.py file with the data that matches my code. Place your own values.
```