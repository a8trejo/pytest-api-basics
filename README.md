### PYTHON API BASICS + WORDPRESS
----------------------------------------------------------------------
#### LOCAL SET UP

- To set up MySQL and Wordpress locally follow these steps:
  - Execute the command `cp secrets-example.env.sh secrets.env.sh` and replace the content on `secrets.env.sh` with your proper credentials
  - Run the following commands in order:
    ```
    cd my_wordpress
    docker compose up -d
    docker exec -ti wordpress_db bash
    mysql -u root -p
    UPDATE mysql.user SET host = '%' where user='wordpress';
    UPDATE mysql.user SET host = '%' where user='root';
    FLUSH PRIVILEGES;
    ```
  - Configure and Install plugin WooCommerce and add sample data as seen in:
  https://woocommerce.com/document/importing-woocommerce-sample-data/

  - Run the command `python setup.py develop`
  
  - Finally, to run the tests execute `pytest -v -s -m "not basics" --junitxml reports/testing-results.xml`
  
  - More notes and comments on `notes.sh`