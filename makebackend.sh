
cd backend
backend="backendrats"
sudo docker build --tag $backend .
docker tag $backend gcr.io/rats-290113/$backend
docker push gcr.io/rats-290113/$backend
