# Fix 500 Internal Server Error returned by the Apache server.
exec { 'replace':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
