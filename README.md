# yip20betasite
This is the website for YIP 2020

If you are using Ubuntu and clone this repo in your Desktop. Then to get the Django project running, open the terminal and enter following commands. Before doing this make sure you have python3 and django installed on your system.

for installing django, you should use this command-> 
pip install django==3.1.2

cd Desktop/YIP2020betawebsite/yip-project/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

This will open up the server and you will get a link of your website which would look something like this http://127.0.0.1:8000/

Some relevant and nice articles

https://realpython.com/python-virtual-environments-a-primer/#using-virtual-environments

https://www.e2enetworks.com/help/knowledge-base/how-to-install-django-on-ubuntu-18-04-16-04-lts/