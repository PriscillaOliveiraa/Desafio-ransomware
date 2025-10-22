Scripts de Criptografia e Descriptografia Simples

Este repositório contém dois scripts Python simples (codigo1 e codigo2) que demonstram a criptografia e descriptografia de um arquivo usando o algoritmo AES 
(Advanced Encryption Standard) no modo CTR (Counter Mode), implementado pela biblioteca pyaes.

⚠️ ATENÇÃO: Os códigos simulam a ação básica de um ransomware ao criptografar um arquivo e remover o original. Ele é para fins educacionais/demonstrativos. 
Não o utilize em arquivos importantes ou sistemas de produção.

🎯​ Objetivo
Criptografar um arquivo especificado (teste.txt), remover o arquivo original e salvar a versão criptografada com uma nova extensão (.ransomwaretroll).

​⚙️​ Como Funciona
  1. Importações: Importa os módulos os (para manipulação de arquivos do sistema) e pyaes (para criptografia AES).
  2. Abertura e Leitura: Abre o arquivo com o nome "teste.txt" no modo de leitura binária ("rb") e lê todo o seu conteúdo para a memória.
  3. Remoção do Original: Usa os.remove(file_name) para deletar o arquivo original não criptografado. Esta é a etapa que simula a ação de destruição do
     original de um ransomware.

  4. Chave e Inicialização AES:
   .Define a chave de criptografia como b"testeransomwares" (uma string de bytes).
   .Cria uma instância de pyaes.AESModeOfOperationCTR usando a chave. O modo CTR é usado para esta operação.

  5. Criptografia:
     O método aes.encrypt(file_data) criptografa os dados do arquivo.
  
  6.Salvando:
    Cria um novo nome de arquivo, anexando a extensão ".ransomwaretroll" (ex: "teste.txt.ransomwaretroll").
    Abre o novo arquivo no modo de escrita binária ("wb") e escreve os dados criptografados.

  Script de Descriptografia

  🎯​ Objetivo
  Descriptografar um arquivo previamente criptografado (teste.txt.ransomwaretroll), remover o arquivo criptografado e restaurar o arquivo original com o 
  nome original (teste.txt).

  ​⚙️​ Como Funciona
    1. Importações: Importa os módulos os e pyaes.
    2. Abertura e Leitura: Abre o arquivo criptografado ("teste.txt.ransomwaretroll") no modo de leitura binária ("rb") e lê seu conteúdo.
    3. Chave e Inicialização AES:
      Define a MESMA chave de criptografia/descriptografia: b"testeransomwares". É crucial que esta chave seja idêntica à usada na criptografia.
      Cria uma instância de pyaes.AESModeOfOperationCTR com a chave. O modo CTR é simétrico, usando a mesma lógica para criptografar e descriptografar.
    4.Descriptografia: O método aes.decrypt(file_data) descriptografa os dados.
    5.Remoção do Criptografado: Usa os.remove(file_name) para deletar o arquivo criptografado.

   6. Restauração
    Define o nome do arquivo restaurado como "teste.txt".
    Abre o novo arquivo no modo de escrita binária ("wb") e escreve os dados descriptografados, restaurando o arquivo original.
