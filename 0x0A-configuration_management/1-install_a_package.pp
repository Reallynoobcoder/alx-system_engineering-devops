# Install Flask version 2.1.0
$python_version = '3.8.10'
$flask_version = '2.1.0'
$werkzeug_version = '2.1.1'

package { 'python3.8':
  ensure => $python_version,
}

package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => $flask_version,
  provider => 'pip',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => $werkzeug_version,
  provider => 'pip',
  require  => Package['python3-pip'],
}
