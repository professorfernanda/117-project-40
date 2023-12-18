Create the Experience section

1. Create an app named experience:
    python3 manage.py startapp experience 

2. Install the app in setting.py under config folder
    INSTALLED_APPD = [
        'pages',
        'projects',
        'experience',
    ]

3. Create a folder named experience under templates folder

4. Create a template named list.html
    4.1 Add <h2>My experence section here</h2>

5. Create a view named experience_list
    5.1 Render the list.html

6. Create the urls.py file under experience app

7. Create the urlpattern to for the experience_list view

8. Include the urls of the experience app to the urls under config folder

9. Run the server