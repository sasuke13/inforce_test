FROM ubuntu:latest
LABEL authors="User"

ENTRYPOINT ["top", "-b"]
FROM python:3.10

WORKDIR / code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3" ,"Restaurant/manage.py", "migrate", "&&", "python3" ,"Restaurant/manage.py", "runserver"]