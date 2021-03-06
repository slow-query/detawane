FROM python:3.8.3

ENV TZ=Asia/Tokyo

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "detawane", "--file", "/usr/src/app/resource/test.json"]
