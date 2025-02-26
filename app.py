
import qrcode
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Servir a página HTML e a imagem
@app.route('/')
def index():
    return send_from_directory(os.getcwd(),'index.html')

@app.route('/imagem.jpg')
def imagem():
    return send_from_directory(os.getcwd(),'imagem.jpg')

# Gerar QR Code com o link para o servidor local
def gerar_qr_code():
    url = "https://luis-matheus-br.github.io/Love_Counter/"  # O URL que você acessa localmente
    qr = qrcode.make(url)
    qr.save("qr_code.png")
    print("QR Code gerado com sucesso!")

if __name__ == '__main__':
    gerar_qr_code()  # Gera o QR Code
    app.run(debug=True)


