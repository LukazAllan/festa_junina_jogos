__author__ = "LukazAllan"
__version__ = "0.1.alpha"

from flask import Flask, render_template, request, redirect, url_for
from gerar_fase import *
from os.path import isfile, join
from os import listdir

# Definindo o caminho para os sprites e gráficos
SPRITES = []
imagens = [f for f in listdir('static/images') if isfile(join('static/images', f))]
for file in imagens:
    if ".png" in file:
        SPRITES.append({"nome":f"{file.split('.')[0]}", "image": f"static/images/{file}", "description": f"Uma {file.split('.')[0]}"})

# Criando a aplicação Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerte-a-palavra', methods=['GET', 'POST'])
def acerte_a_palavra():
    """
    Rota para o jogo 'Acerte a Palavra'
    """
    if request.method == 'POST':
        palavra = request.form.get('palavra')
        if palavra:
            # Aqui você pode adicionar lógica para verificar a palavra
            return redirect(url_for('index'))
    return render_template('acerte_a_palavra.html')

@app.route('/jogo-da-memoria')
def jogo_da_memoria():
    """
    Rota para o jogo da memória
    """
    return render_template('jogo_da_memoria.html')

@app.route('/tudo')
def tudo():
    """
    Rota para devolver sprites e gráficos e visuais
    """
    return render_template('tudo.html', sprites=SPRITES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

