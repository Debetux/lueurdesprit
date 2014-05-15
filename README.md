Python 3.4.
```
apt-get install libsqlite3-dev libmysqlclient-dev
virtualenv-3.4 -p /usr/local/bin/python3.4 develop
```

To set up the project :
```
pip install -r stable-req.txt
npm install
bower install
grunt build
```

If bower fail to install dependencies, it's because of the firewall, so allow git :
```
iptables -A OUTPUT -o eth0 -p tcp --dport 9418 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 9418 -m state --state ESTABLISHED -j ACCEPT
```

In order to use the sources in production, with gunicorn, don't forget to :
```
python manage.py collectstatic
python manage.py run_gunicorn
```
(and look at the nginx.conf if you want to use nginx)

That's it !