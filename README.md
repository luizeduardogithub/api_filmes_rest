# API de Filmes

Esta API permite a gestão de filmes, incluindo a criação, atualização, listagem, exclusão, avaliação e recomendação de filmes não avaliados.

## Estrutura do Projeto

- `app.py`: Script principal contendo a aplicação Flask e definição de rotas.
- `movies.db`: Banco de dados SQLite para armazenar informações dos filmes.
- `README.md`: Documentação do projeto.
- `seed.py`: Script para adicionar dados iniciais ao banco de dados.

## Instalação

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/apifilmes.git
    cd apifilmes
    ```

2. **Crie um Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # no Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Execute o Script Principal:**
    ```bash
    python app.py
    ```

5. **Adicione Dados Iniciais (Opcional):**
    ```bash
    python seed.py
    ```

## Endpoints da API

- **`POST /movies`**: Cria um novo filme.
- **`GET /movies`**: Lista todos os filmes.
- **`PUT /movies/<int:movie_id>`**: Atualiza as informações de um filme existente.
- **`DELETE /movies/<int:movie_id>`**: Exclui um filme.
- **`POST /movies/<int:movie_id>/rate`**: Avalia um filme existente.
- **`GET /movies/recommend`**: Recomenda um filme não avaliado aleatoriamente.

## Exemplos de Uso

- **Criar um Filme:**
  curl -X POST -H "Content-Type: application/json" -d '{"title": "Matrix", "rating": 4.8}' http://127.0.0.1:5000/movies

Listar Filmes:
curl http://127.0.0.1:5000/movies

Atualizar um Filme:
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Matrix Reloaded", "rating": 5.0}' http://127.0.0.1:5000/movies/1

Excluir um Filme:
curl -X DELETE http://127.0.0.1:5000/movies/1

Avaliar um Filme:
curl -X POST -H "Content-Type: application/json" -d '{"rating": 4.5}' http://127.0.0.1:5000/movies/2/rate

Recomendar Filme não Avaliado:
curl http://127.0.0.1:5000/movies/recommend

Modelo de Dados
Movie
id (integer): Chave primária do filme.
title (string): Título do filme.
rating (float): Classificação do filme.

Considerações Finais
Este projeto utiliza Flask e SQLAlchemy para criar uma API simples para gerenciamento de filmes. Certifique-se de consultar a documentação completa no código-fonte e explorar as capacidades da API conforme necessário.

Para contribuir ou relatar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório no GitHub.

Este README fornece uma visão geral do projeto, instruções de instalação e exemplos de uso dos endpoints da API. Personalize conforme a necessidade do seu projeto.





