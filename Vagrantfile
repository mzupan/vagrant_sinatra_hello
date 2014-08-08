
$script = <<SCRIPT
mkdir -p /srv/
cd /srv/
git clone https://github.com/arupchak/sinatra_hello.git
mkdir -p sinatra_hello/log
chown -R vagrant: sinatra_hello
start sinatra_hello
apt-get -y install nginx logster
rm -rf /etc/nginx/sites-enabled/default
SCRIPT

Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "phusion-open-ubuntu-14.04-amd64"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"


  config.vm.provision :chef_solo do |chef| 
    chef.cookbooks_path = "./cookbooks" 

    chef.add_recipe "runit"
    chef.add_recipe "apt"   
    chef.add_recipe "git"
    chef.add_recipe "yum"
    chef.add_recipe "build-essential"
    chef.add_recipe "ruby_build"
    chef.add_recipe "rbenv::vagrant"
    chef.add_recipe "rbenv::user"

    chef.json = {
      'rbenv' => {
        'user_installs' => [
          {
            'user'    => 'vagrant',
            'rubies'  => ['2.0.0-p247'],
            'global'  => '2.0.0-p247',
            'gems'    => {
              '2.0.0-p247' => [
                { 'name'    => 'sinatra' },
              ]
            }
          }
        ]
        }
      }
  end
 
  config.vm.provision :shell, :inline => "echo -e '#{File.read("#{Dir.pwd}/upstart-hello.conf")}' > '/etc/init/sinatra_hello.conf'"
  config.vm.provision "shell", inline: $script
  config.vm.provision :shell, :inline => "echo -e '#{File.read("#{Dir.pwd}/nginx-hello.conf")}' > '/etc/nginx/sites-enabled/sinatra_hello'"
  config.vm.provision "shell", inline: "/etc/init.d/nginx restart"
  
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # add a private network interface, to make it easier to
  # plug vagrant instances from formula together (outside of
  # an integration setup)
  config.vm.network "private_network", ip: "192.168.35.20"

end
