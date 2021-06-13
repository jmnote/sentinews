set -x
cd $(dirname "$0")/..

IMAGE=jmnote/sentinews:dev

docker build -t $IMAGE . && docker push $IMAGE

