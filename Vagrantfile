Vagrant.configure("2") do |config|

    config.vm.box_url = "ubuntu/xenial64"
    # Only needed cause of bug in vagrantfile for xenial
    config.vm.provider "virtualbox" do |vb|
        vb.name = "calorie_find"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "./ansible/playbook.yml"
        ansible.tags = "deploy"
        ansible.extra_vars = {
            'docker_user': "#{ENV['DOCKER_USER']}",
            'docker_password': "#{ENV['DOCKER_PASSWORD']}",
            'docker_email': "#{ENV['DOCKER_EMAIL']}",
        }
    end

    config.vm.define "calorie_find" do |calorie_find|
        calorie_find.vm.box = "ubuntu/xenial64"
    end

end

