FROM jmnote/sentinews:base

COPY . /app
WORKDIR /app
RUN  set -xe \
&& cd /app/backend/ \
&& pip install --no-cahe-dir -r requirements.txt


