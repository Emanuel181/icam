import ssl
from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def get_handler(self, *args, **options):
        handler = super().get_handler(*args, **options)
        self.stdout.write("Starting HTTPS server with SSL certificates...")
        return handler

    def run(self, *args, **options):
        addr, port = self.addr, int(self.port)
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="localhost+1.pem", keyfile="localhost+1-key.pem")
        self.stdout.write(f"Starting HTTPS server at https://{addr}:{port}/")
        super().run(*args, **options, extra_options={"ssl_context": ssl_context})
