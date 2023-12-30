FROM python:3.11.6
WORKDIR /server
COPY . ./

RUN pip install --user -r requirements.txt

EXPOSE 8080

CMD ["python3","./main.py"]