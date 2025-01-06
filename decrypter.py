from cryptography.fernet import Fernet

# Carrega a chave de um arquivo

def load_key():
	return open("key.key", "rb").read()

# Descriptografa o arquivo

def decrypt_file(file_path):
	key = load_key()
	fernet = Fernet(key)

	with open(file_path, "rb") as file:
		encrypted_data = file.read()

	decrypted_data = fernet.decrypt(encrypted_data)

	with open(file_path, "wb") as file:
		file.write(decrypted_data)

if __name__ == "__main__":
	file_to_decrypt = "/home/userxxxx/projeto-ransomware/teste.txt"  # Coloque o caminho do arquivo que sera decriptografado
	decrypt_file(file_to_decrypt)
	print(f"O arquivo {file_to_decrypt} foi descriptografado.")
