# WARNING: Not production ready
# Not cache friendly
# produces huge image

FROM python:3.7

RUN pip install pipenv

WORKDIR /build
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . ./
RUN pip install .

CMD ["hanuka"]
