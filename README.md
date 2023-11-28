# run docker
```
docker-compose up --build  
docker-compose up --build -d 在背景跑
```
# 上傳資料
```
curl -X POST "localhost:9200/law_test_data/_bulk" -H 'Content-Type: application/json' --data-binary @law_test.json
```
# 搜尋
```
curl -X GET "localhost:9200/law_test_data/_search" -H 'Content-Type: application/json' -d '{
  "query": {
    "match": {
      "content": "繼承人"          
    }
  }
}'
```
# port
| Service       | Port |
| ------------- | ---- |
| Elasticsearch | 9200 |
| Kibana        | 5601 |
| Web           | 8080 |
