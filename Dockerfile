FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache install -r requirements.txt
RUN pip3 install flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]