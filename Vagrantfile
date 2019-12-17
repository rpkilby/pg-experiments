Vagrant.configure("2") do |config|
    config.vm.box = "bento/centos-7.7"
    config.vm.synced_folder '.', '/home/vagrant/pg-experiments'

    config.ssh.insert_key = false
    config.ssh.forward_agent = true
end
