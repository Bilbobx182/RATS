
cd ../backend
backend="backendrats"
cp ~/.ssh/onuallaic.dev.key .
cp ~/.ssh/onuallaic.dev.key ./ssl
sudo docker build --tag $backend .
docker tag $backend gcr.io/rats-290113/$backend
docker push gcr.io/rats-290113/$backend
rm ./ssl_onuallainc.key


# debugname="brrrrfn"
# sudo docker stop $(sudo docker ps -aq)
# clear_docker
# sudo docker build --tag $debugname .
# sudo docker run -d -p 5000:5000 78db27b4626c
# curl --insecure https://localhost:5000/
