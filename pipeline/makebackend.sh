
cd ../backend
backend="backendrats"
cp ~/.ssh/onuallaic.dev.key ./ssl
sudo docker build --tag $backend .
docker tag $backend gcr.io/rats-290113/$backend
docker push gcr.io/rats-290113/$backend
rm ./ssl/nuallaic.dev.key


#debugname="0310backend"
#sudo docker stop $(sudo docker ps -aq)
#clear_docker
#sudo docker build --tag $debugname .
#sudo docker run -p 5000:5000 $debugname
#curl --insecure https://onuallainc.dev:5000/