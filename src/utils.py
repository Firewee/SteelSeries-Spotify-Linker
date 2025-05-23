from os import path, getenv
from OpenSSL import crypto

import logging

logger = logging.getLogger("SpotifyLinker")

def fetch_app_data_path(content=''):
    return path.abspath(getenv('APPDATA') + '/SpotifyLinker/' + content)

def fetch_content_path(content):
    return path.abspath(path.join(path.dirname(path.abspath(__file__)), '../', content))

"""
This function generates a self-signed certificate and private key for HTTPS communication.
It saves the certificate and key to the specified paths in the app data directory.
"""
def generate_cert():
    cert_file = fetch_app_data_path('cert.pem')
    key_file = fetch_app_data_path('key.pem')

    # Private key generation
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Certificat generation
    cert = crypto.X509()
    cert.get_subject().C = "FR"
    cert.get_subject().ST = "France"
    cert.get_subject().L = "Localhost"
    cert.get_subject().O = "Spotify Linker"
    cert.get_subject().CN = "localhost"

    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60)

    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Save private key
    with open(key_file, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    # Save certificate
    with open(cert_file, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    logger.info("Certificate and key generated at %s and %s", cert_file, key_file)
