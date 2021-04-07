FROM python:3
COPY . .
RUN pip install discord python-dotenv
CMD ["python3", "src/main.py"]
