
cd ../backend
backend="backendrats_ssl1"
cp ~/.ssh/ssl_onuallainc.key .
sudo docker build --tag $backend .
docker tag $backend gcr.io/rats-290113/$backend
docker push gcr.io/rats-290113/$backend
rm ssl_onuallainc.key