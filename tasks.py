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

@task
def test(ctx, args=''):
    '''
    Run tests
    '''
    manage_instance(ctx, './manage.py test %s' % args)

@task
def clean(ctx):
    '''
    Cleans instances
    '''
    ctx.run("docker rm $(docker ps -a | awk '/Exited/ {print $1}')")


@task
def deploy(ctx):
    '''
    Deploys to staging
    '''
    ctx.run('ansible-playbook -i ./ansible/staging_inventory.ini -u root --tags "deploy" --extra-vars="docker_user=$DOCKER_USER docker_password=$DOCKER_PASS docker_email=$DOCKER_EMAIL" ./ansible/playbook.yml')



