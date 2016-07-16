# In Development

# Calorie find 
Is a RESTFUL API that finds calorie counts of food
This is primarly a learning project

### How to develop on
http://www.pyinvoke.org/ is used for tasks - very similar to fabric

    sudo pip install invoke

If this is your first time use `invoke setup`
This will get the calorie data, create postgres, migrate and add fixture data.
Running this multiple times will destroy the database and reset everything.

To start up the backend

    invoke backend

To run other manage commands on a running django backend. This requires the backend to actually be running.

Examples:
    invoke manage shell_plus
    invoke manage makemigrations


To see remaining tasks that may be useful

    invoke -l




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

