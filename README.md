## Simple REST API on Python

### Technologies
Flask, Python, REST, Python. SQL (PostgreSQL) \
All settings are in the file .env. \
Change the settings for the DB to match your own, the rest can be left unchanged.  

### Current requests GET, PUT, POST, DELETE. Specify ? instead of specific id

### Planets
```sh
curl http://127.0.0.1:5001/planets
curl http://127.0.0.1:5001/planets/?
curl -X POST http://127.0.0.1:5001/add_planet -H "Content-Type: application/json" -d "{\"name\": \"Earth\", \"description\": \"Our home planet\", \"discovered_date\": \"2024-06-17\"}"
curl -X PUT http://127.0.0.1:5001/update_planet/? -H "Content-Type: application/json" -d "{\"name\": \"Mars\", \"description\": \"The red planet\", \"discovered_date\": \"2024-06-18\"}"
curl -X DELETE http://127.0.0.1:5001/delete_planet/?
```

### Governments
```sh
curl http://127.0.0.1:5001/governments
curl http://127.0.0.1:5001/governments/6
curl -X POST http://127.0.0.1:5001/add_government -H "Content-Type: application/json" -d "{\"planet_id\": 1, \"type\": \"Republic\", \"leader\": \"Stalin\", \"established_date\": \"2024-06-17\"}"
curl -X PUT http://127.0.0.1:5001/update_government/? -H "Content-Type: application/json" -d "{\"planet_id\": 6, \"type\": \"Republic\", \"leader\": \"Stalin\", \"established_date\": \"2024-06-18\"}"
curl -X DELETE http://127.0.0.1:5001/delete_goverment/?
```

### States
```sh
curl http://127.0.0.1:5001/states
curl http://127.0.0.1:5001/states/?
curl -X POST http://127.0.0.1:5001/add_state -H "Content-Type: application/json" -d "{\"name\": \"Ohio7\", \"planet_id\": 7, \"population\": 100, \"area\": 85.54}"
curl -X PUT http://127.0.0.1:5001/update_state/? -H "Content-Type: application/json" -d "{\"name\": \"Ohio7\", \"planet_id\": 7, \"population\": 100, \"area\": 100.50}"
curl -X DELETE http://127.0.0.1:5001/delete_state/?
```

### Cities
```sh
curl http://127.0.0.1:5001/cities
curl http://127.0.0.1:5001/cities/?
curl -X POST http://127.0.0.1:5001/add_city -H "Content-Type: application/json" -d "{\"name\": \"city6\", \"state_id\": 7, \"population\": 1000, \"founded_date\": \"2024-06-17\"}"
curl -X PUT http://127.0.0.1:5001/update_city/? -H "Content-Type: application/json" -d "{\"name\": \"city6\", \"state_id\": 7, \"population\": 1000, \"founded_date\": \"2024-06-17\"}"
curl -X DELETE http://127.0.0.1:5001/delete_city/?
```




