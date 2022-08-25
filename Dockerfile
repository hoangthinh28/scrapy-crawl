FROM python:3

WORKDIR /crawldata

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "crawl.py" ]
