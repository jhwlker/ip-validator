FROM python:3.9

EXPOSE 8080

COPY ./ip_validator /ip_validator

RUN pip install -r /ip_validator/requirements.txt --upgrade

CMD ["uvicorn", "ip_validator.fast_api:app", "--host", "0.0.0.0", "--port", "80"]
