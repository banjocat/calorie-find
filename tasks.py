from invoke import task


@task
def setup(ctx):
    '''
    Setups develop for the first time
    '''
    ctx.run('cd ./backend && make clean && make')
    ctx.run('docker-compose up -d db')
    ctx.run('docker-compose run backend /tmp/wait-for-it.sh -h db -p 5432')
    manage_instance(ctx, './manage.py makemigrations')
    manage_instance(ctx, './manage.py migrate')
    


@task
def manage(ctx, command):
    '''
    docker-compose exec backend ./manage.py <command>
    '''
    ctx.run('docker-compose exec backend ./manage.py %s' %  command, pty=True)


@task
def manage_instance(ctx, command):
    '''
    docker-compose run web
    '''
    ctx.run('docker-compose run backend %s' % command)


@task
def backend(ctx):
    '''
    starts up backend only
    '''
    ctx.run('docker-compose up backend')



