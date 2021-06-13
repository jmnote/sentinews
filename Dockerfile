FROM jmnote/sentinews:base

COPY . /app
WORKDIR /app
RUN  set -xe \
&& npm install --global yarn \
&& yarn global add @vue/cli \
&& cd /app/backend/ \
&& pip install --no-cache-dir -r requirements.txt \
&& echo done...

