FROM python:3.7-slim

ENV SRC_DIR /usr/local/src/secret-injector
RUN pip3 install pipenv

WORKDIR ${SRC_DIR}

COPY Pipfile Pipfile.lock ${SRC_DIR}/

RUN pipenv install --system --dev

COPY ./ ${SRC_DIR}

CMD ["pytest", "./tests"]
