sudo uwsgi -y classifier/uwsgi.yaml 
sudo /etc/init.d/nginx restart 

pypy ./xml-rpc/classifier_daemon.py restart
