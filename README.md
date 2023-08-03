# Documentação do Projeto de E-Commerce em Django

O projeto de E-Commerce em Django é uma aplicação simples que permite realizar operações de CRUD (Create, Read, Update, Delete) de produtos, incluindo o gerenciamento de imagens para cada produto. A aplicação foi desenvolvida utilizando o framework Django e oferece funcionalidades básicas para criar, visualizar, atualizar e remover produtos.

## Requisitos

O projeto de E-Commerce foi desenvolvido com as seguintes dependências:

- Django: Framework web utilizado para desenvolver a aplicação.
- Django Crispy Forms: Biblioteca para facilitar a criação de formulários estilizados.
- Django Debug Toolbar: Ferramenta para depuração e análise de desempenho.
- Pillow: Biblioteca para manipulação de imagens.

## Funcionalidades Principais

O projeto de E-Commerce oferece as seguintes funcionalidades principais:

1. Cadastro de Produtos: Permite criar novos produtos com informações como nome, descrição e preço.
2. Upload de Imagens: Os produtos podem ter imagens associadas, que são armazenadas no sistema.
3. Listagem de Produtos: Exibe uma lista de produtos cadastrados, incluindo suas informações e imagens.
4. Edição de Produtos: Permite atualizar informações e imagens de produtos existentes.
5. Remoção de Produtos: Permite remover produtos do sistema.


## Tecnologias Utilizadas

O projeto de E-Commerce utiliza as seguintes tecnologias e ferramentas:

- Django: Framework web para desenvolvimento de aplicações Python.
- Django Crispy Forms: Biblioteca para estilização de formulários.
- Django Debug Toolbar: Ferramenta para análise de desempenho e depuração.
- Pillow: Biblioteca para manipulação de imagens.

## Execução e Desenvolvimento

Para executar o projeto de E-Commerce e iniciar o desenvolvimento, siga os passos abaixo:

1. Clone o repositório do projeto para o seu ambiente local.
2. Navegue até a pasta raiz do projeto e crie um ambiente virtual (opcional, mas recomendado).
3. Execute `pip install -r requirements.txt` para instalar as dependências do projeto.
4. Execute `python manage.py migrate` para aplicar as migrações do banco de dados.
5. Execute `python manage.py runserver` para iniciar o servidor de desenvolvimento e visualizar a aplicação no navegador.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com melhorias ou adicionar novos recursos ao projeto, sinta-se à vontade para criar um fork do repositório e abrir um pull request.

## Licença

Este projeto é disponibilizado sob a licença MIT. Desenvolvido por **Erick Staviasz** como parte do curso de Django ministrado por Otávio Miranda.
