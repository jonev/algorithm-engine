# exit when any command fails
set -e

echo "Building app"
docker build -f Dockerfile.organizer -t jonev/home-hosting:algorithm-engine .
docker push jonev/home-hosting:algorithm-engine
echo "Successfully pushed the app"