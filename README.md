# Criando Ransomware para criptografar e descriptografar arquivo

### Ferramentas usadas
* Python
* Kali Linux

### Configurando o ransomware
* Criação de 2 arquivos python
* Criação de 1 arquivo .txt para teste
* Os arquivos .py um será o encrypter e o outro o decrypter

### Explicação do Código

#### Biblioteca Usada: cryptography
* Usamos a classe Fernet para realizar a criptografia simétrica.

#### Funções principais:
* Fernet.generate_key(): Gera uma chave de criptografia.
* Fernet.encrypt(data): Criptografa os dados.
* Fernet.decrypt(data): Descriptografa os dados.

#### Estrutura do Código
##### Funções em encrypt.py
* generate_key():
* Gera uma chave única e a salva em key.key.
* load_key():
* Lê a chave salva em key.key.
* encrypt_file(file_path):
* Criptografa o conteúdo do arquivo especificado.

##### Funções em decrypt.py
* load_key():
* Lê a chave salva em key.key.
* decrypt_file(file_path):
* Descriptografa o conteúdo do arquivo especificado.
