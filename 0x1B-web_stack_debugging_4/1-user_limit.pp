# Puppet manifest to adjust file descriptor limits for user 'holberton' in limits.conf

# Increase file descriptor limits for user 'holberton'
exec { 'adjust_file_descriptor_limits':
  command => "sed -i 's/5/4096/g; s/4/1024/g' /etc/security/limits.conf",
  path    => [ '/bin/', '/sbin/', '/usr/bin', '/usr/sbin/' ]
}
