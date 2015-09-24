Vagrant.configure("2") do |config|
  config.vm.box = "precise64"

  config.vm.define :udp_sender do |node|
    node.vm.box = "precise64"
    node.vm.hostname = "udp-sender"
    node.vm.network :private_network, ip: "192.168.3.2"
    node.vm.synced_folder ".", "/vagrant/"
    node.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.sudo = true
      ansible.inventory_path = "vagrant.inv"
      ansible.limit = "all"
      ansible.verbose = "true"
      ansible.extra_vars = { }
    end
  end
end
