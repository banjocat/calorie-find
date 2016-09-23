# In Development
[![CircleCI](https://circleci.com/gh/banjocat/calorie-find/tree/master.svg?style=svg)](https://circleci.com/gh/banjocat/calorie-find/tree/master)

# Calorie find 
Is a RESTFUL API that finds calorie counts of food
This is primarly a learning project to get me use of use django with docker.

My progress can be seen at http://www.giantgreendinosaur.com:8020 (assuming I have it up at this time)

### How to develop on
If this is your first time just use `docker-compose up`. 

To run other manage commands on a running django backend. This requires the backend to actually be running.
```
docker-compose exec backend ./manage.py shell_plus
docker-compose exec backend ./manage.py migrate
```

### Requirements
* ~~Docker compose for development~~
* ~~Django restframework for API~~
* Django swagger for docs (swagger couldn't determine the POST schema)
* ~~Ansible and vagrant for deployment simulation~~
* ~~circle.yml for test and pushing to~~
* ~~Read ASCII data file into database for calorie data~~
* ~~1 API endpoint to send list of data~~
* ~~If multiple matches or mispelling send multiple options in JSON~~

### Extra credit
* Make a basic frontend
* Figure out way to do lazy matching
* UPC support (required to make it a "real" project)

### Tech used
* django
* postgresql


### Vagrant
Vagrant is used for ansible deploy testing. It is not required for general development

