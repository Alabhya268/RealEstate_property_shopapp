# RealState property shop app

## About project:

This is Django Web App for realstate .User can view and search properties and make an inquery to realtor.

### Sample Images -

![Sample1](https://raw.githubusercontent.com/Alabhya268/RealState_property_shopapp/master/sample_images/project_sample/sample1.png)

![Sample2](https://raw.githubusercontent.com/Alabhya268/RealState_property_shopapp/master/sample_images/project_sample/sample2.png)

## Steps to run locally :

1. Create a Python virtualenv 

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Run the app by running following command -

     ```bash
     python manage.py runserver   
    ```
    That's it. Open web browser and hit the URL http://127.0.0.1:8000/. 

4. Two users will be created by default which are listed below -

    ```
    SUPERUSER- username: admin password: 1234
    USER- username: user password: user@1234
    ```

One property and one realtor will br created by default

If you wish to modify properties and realtors ,You can do so in admin section, Open web browser and hit the URL "http://127.0.0.1:8000/admin" and login with superuser account given above .

If you wish to create your own superuser account, Run the following command-

    ```bash
    python manage.py createsuperuser
    ```
### You can use sample images provided in sample_images folder to add new properties and realtor if you choose.
___

### If you are having trouble with linting, or getting error like: "No object member in class" then follow these steps :

1. In Visual Studio Code press ctr+sft+P to open the the Command Palette.

2. Now in command palette type Preferences: Configure Language Specific Settings.

3. Now select Python and inside the first curly braces. Make sure that pylint-django is also installed if not paste following code in first curly braces -

    ```
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
    ]
    ```
