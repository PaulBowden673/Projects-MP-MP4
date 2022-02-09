<h1 align="center">Maximum Effort Fitness site</h1> 

<img src="https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/amiRespomsive%20.png" width="100%" alt="Maximum Effort Fitness Website"> 

 

 **Maximum Effort** - is an online gym training community designed to help to and to get help from members to members! 
 
<a href=https://maximum-effort-django.herokuapp.com/" rel="nofollow" target="_blank">Click  here to access the site.</a>

 

## Table of Contents 
 
> 1.  [**UX**](#ux) 
> 2.  [**Scope**](#scope) 
> 3.  [**Structure**](#structure) 
>     - [**Navigation**](#navigation) 
>     - [**Maximum Effort Shop**](#maximum-effort-shop) 
>     - [**Blog**](#blog) 
>     - [**Home Page**](#home-page) 
>     - [**About Page**](#about-page) 
>     - [**Contact Page**](#contact-page) 
> 4.  [**Technologies**](#technologies) 
> 5.  [**Features**](#maximum-effor-shop-features) 
> 6.  [**Testing**](#testing) 
> 7.  [**Deployment**](#deployment) 
> 8.  [**Credits & Acknowledgements**](#credits) 
 
 ## UX 
                                                                                    
 ## <i>Full Stack Frameworks With Django, 4th Milestone Project - Code Institute</i>                                                                                    
 
 My goal is to make an online community web site which contains a small online store where users can by products which can help them progress better and faster. I also intended to add a blog where users can post topics and interact which each other, give or get tips from persons that are on a higher or lower level. 
 
 
 ### User Stories 
 
 #### User 
 
 - As a user, I want to access the website from any device. 
 - As a user, I want to navigate easily through the site. 
 - As a user, I want to create account easily. 
 - As a user, I want to be able to edit my profile, my password, shipping address. 
 - As a user, I want to easy access to web store, sort products by category, price, name. 
 - As a user, I want to be able to read product details, to review and rate them. 
 - As a user, I want to search for products, blog topics and trainings. 
 - As a user, I want to be able to order products from online store. 
 - As a user, I want to be able to Create, Read, Update and Delete own blog topics. 
 - As a user, I want to be able to read, comment and like other blog topics. 
 - As a user, I want to be able to view my past orders. 
 - As a user, I want to link to my social accounts. 
 
#### Admin 
 - As administrator, I want to add, edit, delete products, blogs, and training programs. 
 - As administrator, I want to be able to login from any page. 
 - As administrator, I want to be first who see the blog topic and if it's appropriate allow it to others to view it. 
 - As administrator, I want to see all the orders that have taken place. 
 - As administrator, I expect to see a ‘No Image’ image if there is no image for a product. 
 - As administrator, I want to be able to delete a member if he/she has violated rights of a blog. 
 - As administrator, I want to be able to put products out of stock. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## Scope 
 
- **Maximum Effort** is a totally free gym fitness portal that allows user to be part of community and participate in a blog related to training experiences, advices and tips. Every user can read a blog and use a web store. 
We will be using [Django](<https://www.djangoproject.com/>) web frameworks and the site will be hosted on  [Heroku](https://www.heroku.com/postgres) using [Heroku Postgres](https://www.heroku.com/postgres) for the database. 
 
- **USER** 
Becoming a user, registration is required. When the user is registrated, they are able to log in, edit profile information, see their order history. Main access as a user is to be able to shop and  participate in blog community, write topics, comment, like and review them (in future releases)
 
- **Administration** 
Site will has an admin area which allows Superusers to make changes to the available products.
From admin area, user management, adding, editing or deleting products, also putting them out of stock. 
Collecting all the orders as they are made. 
Control of the blog, admin will be first to read the new topic and decide if it's appropriate publish it.  
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## Structure 
 
The basic structure of the web page is 
 
- _Navigation_ - Top level 
- _Body_ - Main page elements 
- _Footer_ - More navigation, email signup and legal 
 
For a more detailed look at web site structure and page flow see Structure Diagram. 
 
#### Sign Up (Registration) and Login 
 
I have used a 3rd Party package called [Allauth](https://django-allauth.readthedocs.io/en/latest/) to take care of the logic. 
The users are asked to fill in the Registration with fields ‘Email’, ‘Username’, and password, this is done twice to make sure they are both the same. 
 
**Sign Up and Login.** 
The form has two fields, ‘email’ and ‘Password’ and a remember me button and a link to your if you have forgotten your password. 
All of [Allauth](https://django-allauth.readthedocs.io/en/latest/) HTML pages have been customised to fit the themes of the site. 
Full Page background with a center-block design. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
### **Navigation** 
 
#### Navbar 
 
The navbar is fixed to top of each page, This makes navigation easer and quicker. 
 
- **Left – Maximum Effort logo** - Clickable links to the home page from anywhere on the web site. 
- **Center - Page navigation** - This is the main pages navigation, this with change if the users is logged in or not. 
- **Right -User login and Cart** - This changes if the user is a) logged in or B) If the user has access to the admin area. 
 
##### The Footer 
 
The footer stays at the button of each page. 
It contains social media links. 
 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
### **Home Page** 
 
The home page or Index page is the main page for users to interact with. 
It is divided into 3 sections. 
 
#### Section 1 
 
Full-page background, with a container that contains buttons to sign in and register account. 
 
#### Section 2 
 
3 clickable cards each linking to there information they are displaying. 
 
#### Section 3 
 
Will show the latest blog items, the blog is currently under development. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## **Maximum Effort Shop** 
 
- **Product Filtering area** 
  The category selectors are nav links based on the top od products page. 
  Under that is a section which shows which product is currently selected. 
 
- **Product cards** 
  The products are displayed on cards, are positioned side by side in rows. 
  - Picture - is at the top. 
  - Name of the product. 
  - Price of the product is displayed in bold numbers. 
  - Category and stars ratings - The product is rated by the users and the average of all the ratings is displayed here, total out of 5. 
  - There is also view product button from bootstrap that lies od the bottom of the card. 
 
#### Product Details 
 
The Details page is a container-fluid which contains image-container, product-details-container, delete/edit if Superuser,  there are product size selectors where product has sizes and buttons to continue shoping or go to chekcout page. 
 
- Name of the product 
- Category and Rating 
- Price 
- Size selector, (if applicable) 
- Quantity selector 
- Add to Cart button. 
- Product Overview - 
 
#### Shopping Cart 
 
The Cart is where you see a list of all the products that you have added. 
The top horizontal half is a list of all the products and information: 
 
- Image on the left 
- Name 
- Prince 
- Quantity and quantity adjuster - Here you see the quantity of a product, if you want to adjust, or remove the product. 
 
The Order Summary is below the products list and hold all the financial details of the order: 
 
- Cart Total 
- Subtotal 
- Delivery charge 
- Grand Total 
- Keep shopping button - will take you back to the shop. 
- Checkout button - will take to the check out. 
 
#### Checkout 
 
Full page layout with the user order form to complete: 
 
- Contact details and delivery address. 
- Save information to profile button that if pressed the information will be autofilled in next time they use the store. 
- Adjust cart button - If you need to adjust the cart. 
- Complete Order - Sends the card informtion to [Stripe](https://stripe.com/) 
 
#### Stripe Development Card 
> 
> A [Stripe](https://stripe.com/) payment system is inplace and >takes all major cards. 
> The numbers below are used to test the Stripe Payment software. 
> 
> - Card number - 4242 4242 4242 4242 
> - CVC - Any 3 digit number. 
> - Expire date - Any date in the future 
 
#### Checkout Success 
 
- Order Details 
- Stripe Receipt - Clicking the receipt will sent to a new page with you Stripe receipt 
- Contact Details 
- Shipping information 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## **Blog** 
 
Because of time for this project, I wasn't been able to complete the Blog part of the site, but it is the plan to be developed in the future. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## **Your Goals** 
 
Your goals page is where you can find rekomended products which you have in online store. 
Page contains 100% height image where is a container with description. 
Under the image is a block with 3 cards which have buttons on the bottom that links to specific products. 
 
- Lose weight 
- Gain weight 
- Be more endurable 
- Live healthy 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
#### **About Page** 
 
The About page has a centre block format with a heading and information about Maximum Effort fitness Community. 
 
#### **Data Base** 
 
For this Project I used [SQLite](https://www.sqlite.org/index.html) in development because it is integrated as default in [Django](https://www.djangoproject.com/). and [Heroku Postgres](https://www.heroku.com/postgres) in production 
[AWS S3](https://aws.amazon.com/s3/) buckets are used to hold all the Static Files. 
 
#### Images 
 
Images are used extensively. The images chosen are all gym and fitness related. They are used as a background in most of the site. 
All images were found on [Pixabay](https://pixabay.com//) and have a CC licence. 
 
## Technologies 
 
### Core Languages, Frameworks, Editors 
 
- [HTML 5](https://en.wikipedia.org/wiki/HTML) ~ Markup language designed to be displayed in a web browser. 
- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) ~ Style sheet language used for describing the presentation of a document in HTML. 
- [Python 3.8](https://code.jquery.com/) ~ High-level, general-purpose programming language. 
- [Django 3.0.8](https://www.djangoproject.com/) ~ Django is a high-level Python Web framework. 
- [jQuery 3.5](https://code.jquery.com/) ~ lightweight JavaScript library. 
- [Bootstrap 4.5](https://getbootstrap.com/) ~ Design and customize responsive mobile-first sites. 
- [Heroku](https://heroku.com) ~ A cloud based platform - as a service enabling deployment of CRUD applications 
- [Heroku Postgres](https://www.heroku.com/postgres) ~ PostgreSQL's capabilities - as a fast, functional, and powerful data resource. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
#### Third-Party Tools 
 
- [GitHub](https://github.com/) ~ Distributed version control and source code management (SCM) functionality of Git, plus its own features. 
- [Font Awesome](https://fontawesome.com/) ~ Font Awesome icons 
- [Git](https://git-scm.com/) ~ Distributed version control system 
- [Slack](https://slack.com/intl/en-ie/) ~ A workspaces allowing you to organize communications by channels for group discussions and allows for private messages to share information. 
- [W3 Validator](https://validator.w3.org/nu/) ~ The HTML Validation Service. 
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) ~ A CSS validator checks your Cascading Style Sheets to make sure that they comply with the CSS standards set by the W3 Consortium. 
- [Google Fonts](https://fonts.google.com/) ~ A library free licensed font families, an interactive web directory for browsing the library. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
### Maximum Effort Shop Features 
 
- **Product** **Filtering**: 
  You can filter the products in the shop with category selectors: 
  - All products - lets you sort by price, lowest to highest or by category in an alphabetical order. 
 
This makes it quicker to find the product you are looking for. 
 
- **Sort By Selector**: 
  Here you can sort the products by: 
 
  - _Price_ -(low-high) or (high-low). 
  - _Name_ - (A-Z) or (Z-A). 
  - _Category_ (A-Z) or (Z-A). 
  - _Rating_ (low-high) or (high-low). 
 
- **Product cards**: 
  The Product have links on image and on button on bottom and will take you to the details product page. If the product does not have an image a 'No Image' image will take its place (issue with missing images not displaying noimage) 
 
### Future Features 
- Developing the blog 
- Add social accounts log in, 
- Upgrade profile app to add more user details
- Upgrade more of the UX design 
- No image stopped working during the development, tried changing image from png to jpg to no success. 
- Contact page needs more developing, it's not sending emails ( localhost emails are being sent but deployed site gmail provider is not sending emails)
- Upgrading store with more products 
- Developing personal training programs section. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## Testing

I have tested the site adn only found issues with verfy email due to emails not being sent from deployed site.

#### Goals
When I click on "Goals", the dropdown works and the links to Lose Weight, Gain Weight, Live Healthy and Endurance work when clicked amd redirect to the correct pages. All the links back to filtered products on each page work as expected.

#### Create a new user account
I created my main account, as well as a few test accounts to test this functionality. Clicking on the "Register" button in the navbar opens the form, where I can put username and password to create a new account. I tried to input an existing username, not matching passwords in "password" and "confirm password" fields, and input less then 3 or more then 15 charachters. In all cases I got a corresponding error message. As well as that, I tried to leave an empty field and submit the form, but got an error message again asking to fill the field. When the form was successfully submitted, I was given a message telling me to verfy email. The email was not recieved ( issues with using gmail to send emails - not fixed) However on the localhost I was able to verfy the email address by following the link in the terminal and log into the site as well as verify email addresses in the admin

#### Login
Clicking on the "Login" button in the navbar opens the form, allowing me to login to my account. I tried to leave empty fields or input incorrect details, but I was not able to submit the form if something was entered incorrectly. After a successful login I was redirected to the home page, seeing the message that I was logged in.

#### Delete Account
I deleted some testing accounts to test the functionality. This can only be done by Suoerusers logged into the django admin.

#### Add New product
I added several products to check the functionality throughout the development. If I leave some of the required fields empty, I will not be able to submit the form. If the added product does not have an image the page should display moimage.jpg in place of the missing image

#### Edit/Delete product
If I am logged, I can see the button "product management" in the account dropdown. I can then add products or edit them by completing the forms and submitting. the button for delte item on the products page will delete items without the need for a form.



#### Devices
- Samsung S9
- Samsung S21
- Samsung S6 Lte Tablet
- Ipad 
- Iphone 6/7/8
- Desktop with 4K 2056px Monitor
- Dell Inspiron 5405 Laptop 

#### Browsers

- Microsoft Edge
- Chrome
- Firefox
- Safari 

## Issues/Bugs

- Issue with deployed site not linking to bag.html was discovered after deploying. This was fixed by checking the template folders and finding that the folder structure was wrong.
- Issue with emails not being sent on deployed site allowing users to verify email address and log in. This may be due to changes in gmail settings blocking emails being sent ( code was taken and method followed from Boutique Ado mini-project/walkthrough and not changed)
- Further Stripe testing needs to be carried out to put this site into production
- Further Django testing needs to be completed for this site to be put into production as a finished site.

### Validation

All Python files passed validation testing for PEP8 compliance (only remaining errors in files are 'line too long' - not able to shorten some lines further and 2 instances that are populated when user adds items to basket) 

 ###### HTML
 
 - Duplcate id found which is in both the mobile header and main nav and is needed 

  ![HTML Validation](https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/validationHTML.png)


 #### CSS
 
  ![CSS Validation](https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/validationCSS.png)

 #### JS
 
 ![JSHint Validation](https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/validationJShint.png)

- [Lighthouse]

 ###### Lighthouse Validation Desktop
 
![Lighthouse Validation Desktop](https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/validationLighthouseDesktop.png)

###### Lighthouse Validation Mobile

![Lighthouse Validation Mobile](https://github.com/PaulBowden673/Projects-MP-MP4/blob/main/assets/documents/validationLighthouseMobile.png)
 
 
## Deployment 
 
### Local Deployment 
 
To be able to clone this project there are a few things you will need. 
 
- [Git](https://git-scm.com/) - Install Git, installation docs and be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
- [Pip](https://pip.pypa.io/en/stable/installing/) - install pip, installation docs can be found [here](https://pip.pypa.io/en/stable/installing/) 
- A [Gmail](https://www.gmail.com/mail/help/intl/en/about.html?utm_expid=...) account with app secret key. 
 
Once you have [Git](https://git-scm.com/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed. 
 
1. Created app on Heroku 
 
2. Went to the Resources tab in Heroku and searched for Heroku Postgres in the 'Add-Ons' section. 
 
3. Selected the free Hobby level. 
 
4. Updated the .bashrc file within my local workspace with the DATABASE_URL details, and the settings.py to connect to the database using the dj_database_url package. 
 
5. Ran the python3 manage.py makemigrations, python3 manage.py migrate, python3 manage.py createsuperuser commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database. 
 
6. Went to the Settings tab in Heroku and clicked on the Reveal Config Vars button. 
 
7. Copied and pasted all of the .bashrc default variables in Heroku's Config Vars section. 
 
8. Went to the Deploy tab in Heroku, connected my app to my GitHub repository and selected Enable Automatic Deployment as the deployment method. 
 
9. Went to the Developers section in Stripe and clicked on API Keys. 
 
10. Copied and pasted the Publishable Key and Secret Key and set them as the STRIPE_PUBLISHABLE and STRIPE_SECRET environment variables in the .bashrc file within my local workspace. 
 
11. Updated the settings.py with the new Stripe environment variables. 
 
12. Went to the S3 section of AWS and created a new S3 bucket. 
 
13. Within the relevant bucket's permissions, changed the CORS Configuration. 
 
``` 
        { 
    "Version": "2012-10-17", 
    "Statement": [ 
        { 
            "Sid": "PublicReadGetObject", 
            "Effect": "Allow", 
            "Principal": "*", 
            "Action": "s3:GetObject", 
            "Resource": "arn:aws:s3:::<my-bucket-name>/*" 
        } 
    ] 
} 
``` 
 
14. Replaced the <my-bucket-name> in the Resource line with my S3 bucket's name instead. 
 
15. Went to the IAM section of AWS, created a 'New Group' and attached my S3 bucket details to it. 
 
16. Updated the settings.py file in my local workspace with the relevant S3 bucket details: 
``` 
if 'USE_AWS' in os.environ: 
    # Bucket config 
    AWS_STORAGE_BUCKET_NAME = 'maximum-effort-django' 
    AWS_S3_REGION_NAME = 'us-east-1' 
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') 
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' 
 
    # Static and media files 
    STATICFILES_STORAGE = 'custom_storages.StaticStorage' 
    STATICFILES_LOCATION = 'static' 
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage' 
    MEDIAFILES_LOCATION = 'media' 
 
    # Override static and media URLs in production 
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/' 
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/' 
``` 
 
17. Created a custom_storages.py file with classes to route to the relevant location settings for static and media files. 
 
18. Ran the python3 manage.py collectstatic command to push the static files to my S3 bucket. 
 
19. Created a Procfile using the following command in the terminal window. 
 
20. Ran the git add ., git commit -m "<commit-message>" and git push commands to push all changes to my GitHub repository. 
 
#### The app was successfully deployed to Heroku at this stage. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
 
## Credits 
 
### Code 
 
- The project’s code was developed by following the [Code Institute](https://codeinstitute.net/) project Botique Ado, and most of the code to web store comes from that project. 
- The [Django Documentation](https://docs.djangoproject.com/en/3.1/) and [Stack Overflow](https://stackoverflow.com/) have been referred to constantly and super helpful in deciphering the different django debugging error codes. 
- [CSS-Tricks](https://css-tricks.com/snippets/css/media-queries-for-standard-devices/) 
 
 
#### Content and Media 
 
**Content** 
The Supplements section of the shop is all obtained from [proteini.si](proteini.si) 
 
### Special Thanks and Acknowledgements 
 
I would like to say thank you to everyone who has helped me throughout this project. 

 
- My Mentor Nishant Kumar, tips and advice and for pushing me. 
- To the Slack community for their support. 
- Google, my best friend. 
 
<div align="right"> 
 
[Back to Top](#table-of-contents) 
 
</div> 
