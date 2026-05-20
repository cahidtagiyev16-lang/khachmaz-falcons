from flask import Flask, render_template, abort

app = Flask(__name__)

# Khachmaz Falcons - Son Yenilənmiş Real Verilənlər Bazası
PLAYERS_DB = {
    "qapicilar": [],
    "mudafieciler": [],
    "yarimmudafieciler": [
        {
            "id": 1,
            "number": 17,
            "name": "Cahid",
            "surname": "Tağıyev",
            "role": "Kapitan",
            "birth_date": "30.06.2010",
            "citizenship": "Azərbaycan",
            "height_weight": "178sm / 71kq",
            "foot": "sağ",
            "position": "CM (Mərkəz Yarımmüdafiəçi)",
            "image": "cahid.jpeg"
        },
        {
            "id": 3,
            "number": 11,
            "name": "Fərid",
            "surname": "Rəhimov",
            "role": "Oyunçu",
            "birth_date": "11.11.2010",
            "citizenship": "Azərbaycan",
            "height_weight": "175sm / 55kq",
            "foot": "sağ",
            "position": "CAM (Ofensiv Yarımmüdafiəçi)",
            "image": "ferid.jpeg"
        },
        {
            "id": 6,
            "number": 8,
            "name": "Rafael",
            "surname": "Qasımov",
            "role": "Oyunçu",
            "birth_date": "06.10.2009",
            "citizenship": "Azərbaycan",
            "height_weight": "177sm / 60kq",
            "foot": "sağ",
            "position": "CM (Orta Sahə)",
            "image": "rafael.jpeg"
        }
    ],
    "hucumcular": [
        {
            "id": 2,
            "number": 7,
            "name": "Ramal",
            "surname": "Yusifli",
            "role": "2. Kapitan",
            "birth_date": "Məlumat yoxdur",
            "citizenship": "Azərbaycan",
            "height_weight": "180sm / 64kq",
            "foot": "sağ",
            "position": "LW (Sol Hücumçu)",
            "image": "ramal.jpeg"
        },
        {
            "id": 4,
            "number": 9,
            "name": "Müşfiq",
            "surname": "Məhsimli",
            "role": "Oyunçu",
            "birth_date": "Məlumat yoxdur",
            "citizenship": "Azərbaycan",
            "height_weight": "171sm / 75kq",
            "foot": "sağ",
            "position": "ST (Santrafor)",
            "image": "musfiq.jpeg"
        },
        {
            "id": 5,
            "number": 99,
            "name": "x",
            "surname": "x",
            "role": "Oyunçu",
            "birth_date": "x",
            "citizenship": "Azərbaycan",
            "height_weight": "172sm / Məlumat yoxdur",
            "foot": "sağ",
            "position": "RW (Sağ Hücumçu)",
            "image": "default.jpeg"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', categories=PLAYERS_DB)

@app.route('/player/<int:player_id>')
def player_detail(player_id):
    target_player = None
    for position_group in PLAYERS_DB.values():
        for player in position_group:
            if player["id"] == player_id:
                target_player = player
                break
    
    if target_player:
        return render_template('player.html', player=target_player)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)