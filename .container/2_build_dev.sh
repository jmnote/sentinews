set -x
cd $(dirname "$0")/..

IMAGE=jmnote/sentinews:2021.0615.0210

docker build -t $IMAGE -f Dockerfile.dev . && docker push $IMAGE

