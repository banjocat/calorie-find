from fabric.api import local


def deploy():
    '''
    Deploys to staging
    '''
    local(
            'ansible-playbook -i '
            './ansible/staging_inventory.ini '
            '-u root '
            '--tags "deploy" '
            '--extra-vars="'
            'docker_user=$DOCKER_USER '
            'docker_password=$DOCKER_PASS '
            'docker_email=$DOCKER_EMAIL" '
            './ansible/playbook.yml')



