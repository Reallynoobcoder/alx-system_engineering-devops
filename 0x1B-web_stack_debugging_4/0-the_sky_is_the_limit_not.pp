# Puppet manifest to increase the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file for Nginx
exec { 'increase_nginx_ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Restart Nginx to apply changes
-> exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
