GATEWAY_FQDN = "hospital-reader-gateway.local"
DB_FQDN = "hospital-database.local"
# yes, these should be environment variables,
# but, since we're not deploying this on the internet we'll keep it like
# this for simplicity
DB_PASSWORD = "root"
DB_USER = "root"
MYSQL_CONNECT_OPTIONS = {
    "host": DB_FQDN,
    "user": "root",
    "passwd": "root",
}