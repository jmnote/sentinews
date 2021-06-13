FROM jmnote/sentinews:base

COPY . /app
WORKDIR /app
RUN  set -xe \
&& cd /app/backend/ \
&& pip install --no-cache-dir -r requirements.txt


