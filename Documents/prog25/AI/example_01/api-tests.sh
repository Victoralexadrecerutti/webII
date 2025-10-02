echo "POST test"
curl -X POST http://localhost:5000/persons \
-H "Content-Type: application/json" \
-d '{"name":"Alice","email":"alice@example.com","phone":"1234567890","dob":"1990-01-01"}'

echo "GET all test"
curl http://localhost:5000/persons

echo "UPDATE test"
curl -X PUT http://localhost:5000/persons/1 \
-H "Content-Type: application/json" \
-d '{"phone":"0987654321"}'

echo "GET specific record test"
curl http://localhost:5000/persons/1

echo "DELETE test"
curl -X DELETE http://localhost:5000/persons/1

echo "GET all test"
curl http://localhost:5000/persons

