FROM gcr.io/distroless/python3-debian10
COPY . /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]