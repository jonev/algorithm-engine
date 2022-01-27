# exit when any command fails
set -e

echo "Building app"
docker build -f Dockerfile.organizer -t jonev/home-hosting:algorithm-engine-organizer .
docker push jonev/home-hosting:algorithm-engine-organizer
docker build -f Dockerfile.worker -t jonev/home-hosting:algorithm-engine-worker .
docker push jonev/home-hosting:algorithm-engine-worker
echo "Successfully pushed the app"