
WOOCOMMERCE_API = {
    "base_url": {
        "local": "http://localhost:8888",
        "dev": "http://cool-site:dev",
        "test": "http://cool-site:test"
    },
    "api_path": {
        "v3": "/wp-json/wc/v3"
    },
    "endpoints": {
        "customers": "/customers",
        "products": "/products"
    }
}

DB_CONFIG = {
    "WORDPRESS_DB": {
        "db_name": "wordpress-db",
        "base_url": {
            "local": "localhost",
            "dev": "http://cool-site-db:dev",
            "test": "http://cool-site-db:test"
        },
        "port": {
            "local": 3306,
            "dev": 3306,
            "test": 3306
        }
    }
}