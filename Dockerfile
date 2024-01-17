FROM python:3.9.0-alpine
WORKDIR /code
COPY ./.env /code/.env
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN ["python", "/code/app/main.py"]
#RUN ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "80"]
