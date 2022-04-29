# -*- coding: utf-8 -*-

#[START imports]
import os
import urllib
import webapp2
import datetime
import logging
import ssl

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def init_tcp_connection_engine(db_config):
        # [START cloud_sql_postgres_sqlalchemy_create_tcp]
        # Remember - storing secrets in plaintext is potentially unsafe. Consider using
        # something like https://cloud.google.com/secret-manager/docs/overview to help keep
        # secrets secret.
        db_user = os.environ["postgres"]
        db_pass = os.environ["1mp0c4l1C5"]
        db_name = os.environ["co-impocali-cld-01:us-east1:bd-compras-project"]
        db_host = os.environ["10.167.240.3"]

        # Extract port from db_host if present,
        # otherwise use DB_PORT environment variable.
        host_args = db_host.split(":")
        if len(host_args) == 1:
            db_hostname = db_host
            db_port = os.environ["5432"]
        elif len(host_args) == 2:
            db_hostname, db_port = host_args[0], int(host_args[1])

        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,  # e.g. "my-database-user"
                password=db_pass,  # e.g. "my-database-password"
                host=db_hostname,  # e.g. "127.0.0.1"
                port=db_port,  # e.g. 5432
                database=db_name  # e.g. "my-database-name"
            ),
            **db_config
        )
        # [END cloud_sql_postgres_sqlalchemy_create_tcp]
        pool.dialect.description_encoding = None
        return pool

    def get(self):
        """Return a friendly HTTP greeting."""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(pool)


# [END main_page]

# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
# [END app]
