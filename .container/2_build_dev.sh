set -x
cd $(dirname "$0")/..

IMAGE=jmnote/sentinews:2021.0603.1742

docker build -t $IMAGE . && docker push $IMAGE

