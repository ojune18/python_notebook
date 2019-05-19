FROM python:3.6-alpine
COPY pgsql_connect.py /code/
ENV DB_NAME="con"
ENV TABLE_NAME="mobile"
WORKDIR code
RUN ["pip install psycopg2"]
CMD ["python","pgsql_connect.py"]