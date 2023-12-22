# Executes a bash command: kills killmenow process
exec { 'killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}
