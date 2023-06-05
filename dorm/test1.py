
def encode_text(text, key):
    encoded_text = ""
    for char in text:
        encoded_char = chr(ord(char) + key)
        encoded_text += encoded_char
    return encoded_text

def decode_text(encoded_text, key):
    decoded_text = ""
    for char in encoded_text:
        decoded_char = chr(ord(char) - key)
        decoded_text += decoded_char
    return decoded_text

# 获取用户输入
text = input("请输入要编码的文本：")
key = int(input("请输入编码密钥（整数）："))

# 编码文本
encoded_text = encode_text(text, key)
print("编码后的文本：", encoded_text)

# 解码文本
decoded_text = decode_text(encoded_text, key)
print("解码后的文本：", decoded_text)

