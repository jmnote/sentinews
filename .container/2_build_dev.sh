set -x
cd $(dirname "$0")/..

IMAGE=jmnote/sentinews:2021.0615.2345

docker build -t $IMAGE -f Dockerfile.dev . && docker push $IMAGE

