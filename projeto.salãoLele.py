import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

def conecta():
    conn = sqlite3.connect('salão')
    conn.row_factory = sqlite3.Row
    return conn

def pegaLista():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT nome_clientes, numero_cliente , serviço, data FROM Clientes ")
    infos = cursor.fetchall()
    conn.close()
    return infos
app = Flask(__name__)
@app.route('/')
def listaAtendimento():
    a = pegaLista()
    return render_template('horarios.html', a = a)

@app.route('/agendar')
def agendamento():
    return render_template('Cliente.html')
@app.route('/agendado', methods=['POST'])
def guardaAgendamento():
    nome = request.form.get('nome')
    numero= request.form.get('numero')
    serviço= request.form.get('serviço')
    data = request.form.get('data')

    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes(nome_clientes, numero_cliente , serviço, data)
        VALUES ( ? ,?, ?,?)""" ,(nome , numero, serviço, data))

    conn.commit()
    conn.close()

    return redirect(url_for("listaAtendimento"))

app.run(debug=True)
