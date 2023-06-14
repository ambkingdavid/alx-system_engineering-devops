# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx1':
  command => 'sed -i "/^ULIMIT/d" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'fix--for-nginx2':
  command => 'sed -i "$ a\ULIMIT=4096" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
