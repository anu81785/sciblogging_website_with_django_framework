# sciblogging_website_with_django_framework
This is a scientific blogging website which adds a richtexteditor integrated with mathjax library to convert the latex equations. The complex equation can be added to blog in latex format and will automatically be processed on frontend as mathematical equations.

## Steps to Run the Website

* Download the github folder to you local server using following command:

  * git clone https://github.com/anu81785/sciblogging_website_with_django_framework.git

* Change the directory to downloaded folder:
   
   * cd sciblogging_website_with_django_framework

* Create a virtual environment using python:
  
  * python -m venv env_name

* Activate the virtual environment:
   
   * source /path/to/venv/bin/activate

* Now download all the required packages inside this virtual environment using following command:
    
   * pip install -r requirements.txt

* Start the following commands to apply the migrations and runserver
    
   * python manage.py migrate
   
   * python manage.py runserver

