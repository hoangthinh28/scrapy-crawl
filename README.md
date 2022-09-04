<h3>Learn the first Devops and practice Docker, Jenkins, Aws</h3>

```shell
pip install scrapy
scrapy startproject crawldata
scrapy shell https://stackoverflow.com/questions/tagged/python
scrapy crawl posts -o posts.json
pip install scrapy-xlsx
scrapy crawl posts -o posts.xlsx

docker build -t mycrawler .
docker compose up
docker cp containerID:/crawldata/data.csv D:/MT/Python/crawldata/data.csv

docker ps -a
docker rm ContainerID
docker images
docker image rm ImageID
docker volume ls

dokcer-compose up

sudo systemctl stop docker.socket
sudo systemctl start docker.socket
sudo service docker start
```
