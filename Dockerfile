FROM continuumio/miniconda3

LABEL maintainer="Gaioz Tabatadze <tabatadze@gmail.com>"
LABEL description="Docker image for simple HTTP database using fastpi and file-manipulation"

COPY environment.yml .

RUN conda env create -f environment.yml  -n environment

WORKDIR /app

COPY /src /app/src
COPY .env /app/.env

EXPOSE 6900

#ENTRYPOINT ls src

ENTRYPOINT [ "conda", "run" ]
CMD ["--no-capture-output", "-n", "environment", "fastapi", "dev", "--host", "0.0.0.0", "--port", "6900", "src/main.py"]
