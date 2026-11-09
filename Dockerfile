FROM python
WORKDIR /app
COPY ./app
run pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD["python","app.py"]
