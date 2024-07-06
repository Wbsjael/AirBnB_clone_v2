# setting up my web servers for the deployment of web_static

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> exec { 'create directories':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}
-> exec { 'test content':
  command => '/usr/bin/echo "<h1>Welcome to johnalx.tech site</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}
-> exec { 'remove link':
  command => '/usr/bin/rm -rf /data/web_static/current',
}
-> exec { 'create symbolic link':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'grants':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}
-> exec { 'hbnb_static location':
  command => 'sudo sed -i "/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}" /etc/nginx/sites-enabled/default',
  provider => shell,
}
-> exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
