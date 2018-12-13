From python:3

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /home/app

CMD ["python3", "-m", "flask", "run", "--port", "80", "--host", "0.0.0.0"]
