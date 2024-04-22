# SSLExpiryChecker
```
pip install pyOpenSSL
```

直接使用 `OpenSSL.crypto` 模块来处理从服务器获取的DER格式证书，并转换为PEM格式，然后再解析它(将下面代码命名为app.py)：

```python
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
```

这段代码做了以下修改：

1. **连接和获取证书**：通过建立SSL连接，获取证书的DER编码。
2. **转换证书**：使用`OpenSSL.crypto`的`load_certificate`方法将DER格式证书转换为`X509`对象。
3. **解析日期**：提取证书的到期时间并将其转换为Python的`datetime`对象。

## 运行脚本
你可以尝试运行这段代码。它应该能够成功连接到指定的服务器（例如`taobao.com`），获取SSL证书信息，并打印出证书的到期日期。

```
python3 app.py
```
## 运行结果
![内容](https://pbs.twimg.com/media/GLxwniLaAAAVpBg?format=png&name=900x900 "Optional title")


