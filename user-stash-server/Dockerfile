FROM python:3.10

WORKDIR /app

COPY . .

RUN pip3 install -e .

EXPOSE 5000

WORKDIR "/user_stash"

CMD ["flask", "db", "upgrade"]

CMD ["user_stash_server"]
