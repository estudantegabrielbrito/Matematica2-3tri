senha = "123456"
senha_criptogradada = ""

for numero in senha:
    numero = int(numero) + 1
    senha_criptogradada += str(numero)
       
print(senha_criptogradada)
