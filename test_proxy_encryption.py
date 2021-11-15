from protocols import *

encrypter = UniqueProtocol(' abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><.,:"?{}+=\/-', 'utf-8')

message = 'https://hinduism-indian.herokuapp.com'
print(message)

print('ENCRYPTING MESSAGE:')
encrypted_message = encrypter.encrypt(message)
print(encrypted_message)
print('DECRYPTING MESSAGE:')
print(encrypter.decrypt(encrypted_message))