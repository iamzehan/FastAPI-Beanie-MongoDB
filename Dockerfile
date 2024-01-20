FROM python:3.9.0

WORKDIR /code

RUN pip install bcrypt

COPY ./.env /code/.env
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["python", "/code/app/main.py"]
