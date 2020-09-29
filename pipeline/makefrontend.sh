cd ../frontend
frontend="frontendrats"
cp ~/.ssh/ssl_onuallainc.key .
sudo docker build --tag $frontend .
docker tag $frontend gcr.io/rats-290113/$frontend
docker push gcr.io/rats-290113/$frontend
rm ssl_onuallainc.key