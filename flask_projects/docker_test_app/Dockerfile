FROM python:stretch


LABEL maintainer="Asqaraliyev Faxriyor"
LABEL description="Learning docker further before the django so i maybe deploy django app without problems"
LABEL date="2021-10-20"

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", ":8080", "app:app"]
