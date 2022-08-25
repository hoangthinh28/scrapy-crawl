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
```
