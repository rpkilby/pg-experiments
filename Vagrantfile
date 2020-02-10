Vagrant.configure("2") do |config|
    config.vm.box = "bento/centos-8.0"

    config.vm.define "postgres" do |postgres|
        config.vm.synced_folder '.', '/home/vagrant/pg-experiments'
        config.vm.network "forwarded_port", guest: 5432, host: 5432
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "provisioning/playbook.yml"
        ansible.compatibility_mode = "2.0"
        # ansible.verbose = true
    end
end
