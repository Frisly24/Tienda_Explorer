FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN mkdir /code 

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt 


CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "proyectov3", "proyectov3.wsgi:application"]