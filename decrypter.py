import os
import pyaes
import hashlib

## Função para gerar chave de tamanho adequado a partir da senha

def generate_key(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return hashed

## abrir o arquivo criptografado

file_name = 'ransomwaretroll.teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

print("Dados do arquivo criptografado:")
print(file_data)

## chave de descriptografia

password = 'testeransomware'
key = generate_key(password)
##key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

print("Dados descriptografados:")
print(decrypt_data)

## remover o arquivo criptografado

os.remove(file_name)

## criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
