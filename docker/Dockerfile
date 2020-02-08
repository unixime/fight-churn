FROM postgres

#RUN apt-get update && apt-get install postgresql python3-venv python3-pip
#RUN apt-get python3-venv

#COPY requirements.txt /fight_churn/

# RUN pip install -r /fight_churn/requirements.txt

ENV POSTGRES_PASSWORD=dbAdmin 
ENV POSTGRES_DB=churn

COPY data-generation/schema/*create_* /docker-entrypoint-initdb.d/

RUN for item in /docker-entrypoint-initdb.d/create_*.sql; do sed -i 's@x\.@socialnet7\.@g' $item ; done

EXPOSE 5432

