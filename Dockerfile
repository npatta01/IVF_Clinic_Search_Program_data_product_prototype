FROM python:3.6

WORKDIR /app
ADD ivf/requirements.txt .

RUN pip install -r requirements.txt

COPY ivf/* ./

ENV DEBUG False
#CMD ["python", "app.py"]
CMD ["gunicorn","-w 2", "app:app.server","--preload"]
