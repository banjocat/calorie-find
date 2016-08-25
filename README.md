# In Development
[![CircleCI](https://circleci.com/gh/banjocat/calorie-find/tree/master.svg?style=svg)](https://circleci.com/gh/banjocat/calorie-find/tree/master)

# Calorie find 
Is a RESTFUL API that finds calorie counts of food
This is primarly a learning project to get me use of use django with docker.

### How to develop on
If this is your first time just use `docker-compose up`. 

To run other manage commands on a running django backend. This requires the backend to actually be running.
```
docker-compose exec backend ./manage.py shell_plus
docker-compose exec backend ./manage.py migrate
```

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
* UPC support (required to make it a "real" project)

### Tech used
* django
* postgresql


### Vagrant
Vagrant is used for ansible deploy testing. It is not required for general development

