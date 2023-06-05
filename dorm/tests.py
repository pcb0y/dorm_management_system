import os
import base64
import hashlib

def generate_code_verifier():
    # 随机生成一个长度为 32 的 code_verifier
    token = os.urandom(32)
    code_verifier = base64.urlsafe_b64encode(token).rstrip(b'=')
    return code_verifier.decode('utf-8')

def generate_code_challenge(code_verifier):
    # 对 code_verifier 进行哈希处理，然后再进行 base64url 编码，生成 code_challenge
    m = hashlib.sha256()
    m.update(code_verifier.encode('utf-8'))
    code_challenge = base64.urlsafe_b64encode(m.digest()).rstrip(b'=')
    return code_challenge.decode('utf-8')

code_verifier = generate_code_verifier()
code_challenge = generate_code_challenge(code_verifier)

print("code_verifier: ", code_verifier)
print("code_challenge: ", code_challenge)