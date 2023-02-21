import os
import pyaes

## abrir o arquivo  com criptografia
file_name = "comum.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## criando chave para descriptografia
key = b"comumransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## removendo o arquivo criptografado
os.remove(file_name)

## criando o arquivo descriptografado
new_file = "comum.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
