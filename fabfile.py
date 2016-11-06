from fabric.api import env, run, put, hosts, cd

env.user = 'root'

@hosts('giantgreendinosaur.com')
def deploy():
    '''
    Deploy it
    '''
    run('mkdir -p /app/caloriefind')
    put('./production-compose.yml', '/app/caloriefind/docker-compose.yml')
    with cd('/app/caloriefind'):
        run('docker-compose pull')
        run('docker-compose down')
        run('docker-compose up -d')
