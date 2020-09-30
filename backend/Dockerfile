FROM tiangolo/meinheld-gunicorn-flask:python3.7

WORKDIR /api
RUN apt-get update && apt-get install -y git ca-certificates
COPY . /api
COPY ./ssl /ssl
COPY ./ssl /api
RUN pip3 install -r requirements.txt

Run python -c "import nltk; nltk.download(['punkt', 'wordnet'])"

EXPOSE 3000
EXPOSE 5000
CMD ["python", "app.py", "runserver"]