FROM python:3.7
WORKDIR /app
COPY . /app
COPY /ssl /app/
RUN apt-get update && apt-get install -y git ca-certificates && apt-get install nano
RUN pip3 install -r requirements.txt
RUN python -c "import nltk; nltk.download(['punkt', 'wordnet'])"
RUN ls /app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0","--port=5000","--cert=onuallainc_dev.crt", "--key=onuallaic.dev.key"]