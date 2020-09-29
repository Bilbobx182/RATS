FROM tiangolo/meinheld-gunicorn-flask:python3.7

WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
# Copy the project codes into the Work Directory
COPY . /backend
COPY /backend/ssl/ /etc/nginx/ciaranssl/
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 3000
EXPOSE 5000
CMD ["python", "app.py", "runserver"]