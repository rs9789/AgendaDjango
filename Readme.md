# Um projeto do meu aprendizado de Django

# Atualizações
## Proteção da `SECRET_KEY`:
No arquivo `settings.py`, foi necessário o uso do módulo `dotenv` e a criação de um arquivo `.env` para armazenar a chave
em seguida utilizar o `.gitignore` adicionando o arquivo `.env` para não ser carregado para o GitHub.

## Adição de `models`:
Adicionado `models` Categoria e Contatos, e incluindo essas `models` no admin do site.

## Mostrando valores nas `views`:
Além da adição dos `models`, foi adicionado os contatos de forma automatica nas `views` baseado nos dados de contatos contidos na base de dados.

## Adicionando mais Campos na base, e criação de outra página:
Adicionado o campo para mostrar ou não um contato e adição de uma pagina para mostrar um contato único ao clicar nele.
