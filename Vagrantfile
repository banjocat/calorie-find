Vagrant.configure("2") do |config|

    config.vm.box_url = "ubuntu/xenial64"

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "./ansible/playbook.yml"
    end

    config.vm.define "calorie_find" do |calorie_find|
        calorie_find.vm.box = "ubuntu/xenial64"
    end

end
