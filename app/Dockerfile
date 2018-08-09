From python:3

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
WORKDIR /home/app

CMD ["python3", "-m", "flask", "run", "--port", "80", "--host", "0.0.0.0"]
