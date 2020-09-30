tag="Test123"
echo($tag)

cd ../backend
cp ~/.ssh/onuallaic.dev.key ./ssl
sudo docker build --tag $tag .
rm ./ssl/onuallaic.dev.key
sudo docker run -d -p 5000:5000 $tag