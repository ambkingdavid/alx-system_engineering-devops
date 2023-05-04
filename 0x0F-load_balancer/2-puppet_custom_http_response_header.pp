# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# create index.html file that contains the "Hello World!"
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

# Configure Nginx server to add custom HTTP header response
$hostname = $facts['hostname']

$nginx_config = "server {
    listen       80;
    server_name  localhost;
    root         /var/www/html;

    location / {
        add_header X-Served-By ${hostname};
        index  index.html;
    }
}"

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_config,
}

# create symlink to enable virtual host
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

