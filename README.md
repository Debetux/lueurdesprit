Python 3.4.
```
apt-get install libsqlite3-dev
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

That's it !