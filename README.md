# In Development

# Calorie find 
Is a RESTFUL API that finds calorie counts of food
This is primarly a learning project

### How to develop on
http://www.pyinvoke.org/ is used for tasks - very similar to fabric

To see all tasks.

    invoke -l

To start the database in the background

    invoke db


Next migrate and fixture data

    invoke migrate
    invoke fixture


Then start up the backend in the foreground

    invoke backend

To run other manage commands on a running django backend

    invoke manage shell_plus


### Requirements
* Docker compose for development
* Django restframework for API
* Django swagger for docs
* Ansible and vagrant for deployment simulation
* circle.yml for test and pushing to
* Read ASCII data file into database for calorie data
* 1 API endpoint to send list of data
* User can put in multiple measurement types
* If multiple matches or mispelling send multiple options in JSON

### Extra credit
* UPC support

### Tech used
* django
* postgresql

