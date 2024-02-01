from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configurando a aplicação Flask
app = Flask(__name__)

# Configurando o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

# Definindo o modelo Movie para representar filmes no banco de dados
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)

    def to_dict(self):
        """Converte um objeto Movie para um dicionário."""
        return {'id': self.id, 'title': self.title, 'rating': self.rating}

# Rota para criar um novo filme
@app.route('/movies', methods=['POST'])
def create_movie():
    """Cria um novo filme a partir dos dados fornecidos."""
    data = request.get_json()
    new_movie = Movie(title=data['title'], rating=data.get('rating'))
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201

# Rota para listar todos os filmes
@app.route('/movies', methods=['GET'])
def list_movies():
    """Retorna uma lista de todos os filmes no banco de dados."""
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

# Rota para atualizar as informações de um filme
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Atualiza as informações de um filme existente."""
    movie = Movie.query.get_or_404(movie_id)
    data = request.get_json()
    movie.title = data['title']
    movie.rating = data.get('rating')
    db.session.commit()
    return jsonify(movie.to_dict())

# Rota para excluir um filme
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Exclui um filme do banco de dados."""
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'})

# Rota para avaliar um filme
@app.route('/movies/<int:movie_id>/rate', methods=['POST'])
def rate_movie(movie_id):
    """Avalia um filme existente."""
    movie = Movie.query.get_or_404(movie_id)
    data = request.get_json()
    movie.rating = data['rating']
    db.session.commit()
    return jsonify(movie.to_dict())

# Rota para recomendar um filme não avaliado
@app.route('/movies/recommend', methods=['GET'])
def recommend_movie():
    """Recomenda um filme não avaliado aleatoriamente."""
    unrated_movies = Movie.query.filter_by(rating=None).all()

    import random
    recommended_movie = random.choice(unrated_movies) if unrated_movies else None

    if recommended_movie:
        return jsonify(recommended_movie.to_dict())
    else:
        return jsonify({'message': 'No unrated movies available'})

# Inicializando o banco de dados e iniciando a aplicação Flask
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
s