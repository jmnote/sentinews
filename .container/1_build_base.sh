set -x
rm -rf /tmp/docker_build
mkdir /tmp/docker_build
cd /tmp/docker_build

IMAGE=jmnote/sentinews:base

cat <<'EOF' > Dockerfile
FROM python:3.9-slim
RUN set -x \
&& apt-get update && apt-get install -y \
  git \
  curl \
  nginx \
  libmariadbclient-dev gcc \
&& curl -sL https://github.com/krallin/tini/releases/download/v0.19.0/tini -o /tini \
&& chmod +x /tini \
&& curl -sL https://deb.nodesource.com/setup_14.x | bash - \
&& apt-get install -y \
	nodejs \
&& rm -rf /var/lib/apt/lists/* \
&& npm install --global yarn \
&& yarn global add @vue/cli
EOF

docker build -t $IMAGE . && docker push $IMAGE

