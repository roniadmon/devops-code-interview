FROM python:3
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD main.py main.py

CMD python main.py 'https://5dbf2fb9e295da001400b4cc.mockapi.io' '/api/v1/snapshots/'