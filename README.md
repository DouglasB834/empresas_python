## Como Rodar com VENV (Ambiente Virtual Python)
Este projeto foi inicialmente desenvolvido para rodar utilizando um ambiente virtual Python. Abaixo, forneceremos um guia completo de instalação para rodar sua API em qualquer sistema operacional:
## Windows(CMD/Powershell):
1. Criando o VENV

    Primeiro, você deve abrir este projeto no seu terminal e executar os seguintes comandos na pasta raiz do seu projeto.
 Abaixo está o comando para criar um ambiente virtual Python (venv):

    ```commandline
    python -m venv venv
    ```
2. Ativando o Ambiente Virtual

    Execute o comando abaixo para ativar o seu venv na sessão atual do terminal:
    ```commandline
    .\venv\Scripts\activate
    ```
    O comando acima funciona bem para CMD ou Powershell. Se você estiver utilizando o Git Bash para rodar esses comandos, execute o seguinte comando:

      ```bash
      source venv/Scripts/activate
      ```  
4. Rodar o app.py

   Após a instalação das bibliotecas ser concluída, você pode utilizar o comando abaixo para rodar o projeto:
    ```bash
    python app.py
    ```