FROM python:3.12.8-alpine3.21

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

WORKDIR /src
COPY /src /src

CMD ["python", "main.py"]