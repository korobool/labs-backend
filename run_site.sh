sudo uwsgi -y classifier/uwsgi.yaml 
sudo /etc/init.d/nginx restart 

python ./xml-rpc/classifier_daemon.py restart
