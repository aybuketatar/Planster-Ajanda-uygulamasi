from flask import Flask, render_template
import random

app = Flask(__name__)

oneriler = [
    {"konu": "Hava", "mesaj": "Bugün hava biraz kapalı, yanına şemsiye almayı unutma! ☔"},
    {"konu": "Mod", "mesaj": "Enerjin düşükse bir kahve molası ver ve derin nefes al. ☕"},
    {"konu": "Giyim", "mesaj": "Bugün mavi tonları sana çok yakışacak! 💙"},
    {"konu": "Aktivite", "mesaj": "Akşam kısa bir yürüyüş zihnini açabilir. 🚶‍♀️"},
    {"konu": "Motivasyon", "mesaj": "Bugün en zor işi en başa al, gerisi çorap söküğü gibi gelir! 💪"}
]

@app.route('/')
def ana_sayfa():
    gunun_onerisi = random.choice(oneriler)
    return render_template('index.html', oneri=gunun_onerisi)

@app.route('/ajanda/<tur>')
def ajanda_goster(tur):
    # Kullanıcının seçtiği türü (minimalist, renkli vs.) alıp ajanda.html'e gönderiyoruz
    return render_template('ajanda.html', tur=tur)

if __name__ == '__main__':

    app.run(debug=True)
