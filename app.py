import ssl
import socket
from datetime import datetime
from OpenSSL import crypto

def get_ssl_expiry_date(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert_der = ssock.getpeercert(True)
            cert = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_der)
            not_after = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')

    return not_after

# 使用例子：检查taobao.com的SSL证书到期日期
expiry_date = get_ssl_expiry_date('taobao.com')
print('SSL Certificate Expiry Date:', expiry_date)
