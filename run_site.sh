sudo .env/bin/uwsgi -y classifier/uwsgi.yaml 
sudo /etc/init.d/nginx restart 

pypy ./xml-rpc/classifier_daemon.py restart
/home/ubuntu/production/labs-backend/.env/bin/python /home/ubuntu/production/labs-backend/xml-rpc/twitter_queue_svc.py restart
/home/ubuntu/production/labs-backend/.env/bin/python /home/ubuntu/production/labs-backend/xml-rpc/TwitterStreamer.py restart
python /home/ubuntu/production/labs-backend/xml-rpc/reversid.py restart
