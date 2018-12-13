# backend-coding-challenge

There are 5 failed tests so please fix them to pass.

You only have to write sql code and it's better to add some test cases too.

If you have questions, feel free to drop us an email at engineering@sourcesage.co

## Setup

```bash
docker-compose build
docker-compose up
```

## Run tests

```bash
docker exec -it backend-coding-challenge py.test 
```

## Go to mysql repl

```bash
docker exec -it backend-coding-challenge-mysql mysql db -ppasswd
```
