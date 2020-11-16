from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:devsecops@localhost/agenda'


db = SQLAlchemy(app)


class time(db.Model):
    __tablename__ = 'cadastrar_time'
    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(60))
    historia = db.Column(db.String(2500))
    atacante = db.Column(db.String(60))
    meia = db.Column(db.String(60))
    zaga = db.Column(db.String(60))
    goleiro = db.Column(db.String(60))
    tecnico = db.Column(db.String(60))
    def __init__(self, nome, historia, atacante, meia, zaga, goleiro, tecnico):
        self.nome = nome
        self.historia = historia
        self.atacante = atacante
        self.meia = meia
        self.zaga = zaga
        self.goleiro = goleiro
        self.tecnico = tecnico


class cadatrar_partida(db.Model):
    __tablename__ = 'cadastrar_partida'
    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nometime1 = db.Column(db.String(60))    
    nometime2 = db.Column(db.String(60))
    datadapartida = db.Column(db.String(10))
    horariodapartida = db.Column(db.String(10))
    def __init__(self, nometime1, nometime2, datadapartida, horariodapartida):
        self.nometime1 = nometime1       
        self.nometime2 = nometime2
        self.datadapartida = datadapartida
        self.horariodapartida = horariodapartida


db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pagina_inicial")
def pagina_inicial():
    return render_template("pagina_inicial.html")


@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")


@app.route("/cadastrar_partida")
def cadastrar_partida():
    return render_template("cadastrar_partida.html")


@app.route("/cadastrar_time")
def cadastrar_time():
    return render_template("cadastrar_time.html")  


@app.route("/listar_time")
def listar_time():
    return render_template("listar_time.html")  


@app.route("/atletico_nacional")
def atletico_nacional():
    return render_template("atletico_nacional.html")


@app.route("/new_york_city")
def new_york_city():
    return render_template("new_york_city.html")


@app.route("/palmeiras")
def palmeiras():
    return render_template("palmeiras.html")


@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")


@app.route("/resultado")
def resultado():
    return render_template("resultado.html") 


@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        telefone = (request.form.get("telefone"))
        if nome:
            f = agenda(nome, telefone)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem.html"))


@app.route("/cadastrar_time",methods=['GET', 'POST'])
def cadastrar_time():
    if request.method =="POST":
        nome = (request.form.get("nometime"))
        historia = (request.form.get("historia"))
        atacante = (request.form.get("atacante"))
        meia = (request.form.get("meia"))
        zaga = (request.form.get("zaga"))
        goleiro = (request.form.get("goleiro"))
        tecnico = (request.form.get("tecnico"))
        if nome:
            f = time(nome, historia, atacante, meia, zaga, goleiro, tecnico)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem.html"))


@app.route("/cadastrar_partida",methods=['GET', 'POST'])
def cadastrar_partida():
    if request.method =="POST":
        nometime1 = (request.form.get("nometime1"))
        nometime2 = (request.form.get("nometime2"))
        datadapartida = (request.form.get("datadapartida"))
        horariodapartida = (request.form.get("horariodapartida"))        
        if nome:
            f = cadastrar_partida(nometime1, nometime2, datadapartida, horariodapartida)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem.html"))


@app.route("/listar")
def listar():
    agendas = agenda.query.all()
    return render_template("listar.html", agenda = agendas)


if __name__ == "__main__":
    app.run(debug=True)
    

app.run()