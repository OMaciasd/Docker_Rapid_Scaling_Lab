ARG PYTHON_VERSION=3.19
FROM python:${PYTHON_VERSION}-alpine

WORKDIR /app

LABEL Name="MiApp" \
      Version="1.0"

COPY myapp /app/myapp

ENV PYTHONPATH=/app

# Actualiza pip, urllib3, e instala dependencias desde requirements.txt
RUN pip3 install --upgrade pip3 \
      && pip3 install --upgrade urllib3 \
      && pip3 install --no-cache-dir -r /app/myapp/requirements.txt \
      && rm -rf /var/cache/apk/*

EXPOSE 5000

CMD ["python3", "-m", "myapp"]
