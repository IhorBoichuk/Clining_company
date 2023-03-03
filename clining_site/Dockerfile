FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /clining_site

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /clining_site

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]