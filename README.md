### PYTHON API BASICS + WORDPRESS
----------------------------------------------------------------------
#### LOCAL SET UP


#### MYSQL SetUp
- To set up MySQL locally run the following commands:
```
cd my_wordpress
docker compose up -d
docker exec -ti wordpress_db bash
mysql -u root -p
UPDATE mysql.user SET host = '%' where user='wordpress';
UPDATE mysql.user SET host = '%' where user='root';
FLUSH PRIVILEGES;
```
