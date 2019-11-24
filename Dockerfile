FROM python:3

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY mlsvc.py .

CMD python3 mlsvc.py