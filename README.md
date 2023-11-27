# 上傳資料
curl -X POST "localhost:9200/law_test_data/_bulk" -H 'Content-Type: application/json' --data-binary @law_test.json
# run docker
docker-compose up --build