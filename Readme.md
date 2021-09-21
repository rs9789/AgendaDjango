# Um projeto do meu aprendizado de Django

# Atualizações
## Proteção da `SECRET_KEY`:
No arquivo `settings.py`, foi necessário o uso do módulo `dotenv` e a criação de um arquivo `.env` para armazenar a chave
em seguida utilizar o `.gitignore` adicionando o arquivo `.env` para não ser carregado para o GitHub.