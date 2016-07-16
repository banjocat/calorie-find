from invoke import task


@task
def db(ctx):
    '''
    Bring up postgres
    '''
    ctx.run('docker-compose -d  db')


@task
def migrate(ctx):
    '''
    makemigrations and migrate
    '''
    ctx.run('docker-compose run backend ./manage.py makemigrations')
    ctx.run('docker-compose run backend ./manage.py migrate')


@task
def fixture(ctx):
    '''
    Load food calorie data fixture in backend
    '''
    ctx.run('docker-compose run backend ./manage.py loaddata food_calorie')


@task
def manage(ctx, command):
    '''
    custom manage command - Requires backend to be up
    '''
    ctx.run('docker-compose exec backend ./manage.py %s' %  command, pty=True)


@task
def backend(ctx):
    '''
    starts up backend only
    '''
    ctx.run('docker-compose up backend')



