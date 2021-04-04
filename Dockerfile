FROM ubuntu
COPY . .
RUN pip install discord python-dotenv
CMD ["python" "src/main.py"]
