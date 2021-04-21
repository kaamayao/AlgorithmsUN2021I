from flask import Flask, render_template, make_response, request
import urllib.request
import json
import io
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    with app.app_context():
        return render_template('home.html', name="home")

def makeImgResponse():
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    response=make_response(img.getvalue())
    response.headers['Content-Type'] = 'image/png'
    img.close()
    return response

@app.route('/arboles-plot')
def plot_arboles():
    URL_STRING = 'https://www.datos.gov.co/resource/gt2j-8ykr.json'
    SAMPLE_SIZE = int(request.args.get('sampleSize')[:-1])
    with urllib.request.urlopen(URL_STRING) as url:
        data = json.loads(url.read())
        edades = [int(x['edad']) for x in data]
        plt.rcdefaults()
        fig, ax = plt.subplots()
        x_pos = np.arange(SAMPLE_SIZE)
        ax.bar( edades[0:SAMPLE_SIZE], x_pos )
        ax.set_title('Edad de los arboles de Bogota')
        ax.set_xlabel('Edad')
        ax.set_ylabel('Cantidad de arboles')
        return makeImgResponse()

@app.route('/agricultura-plot')
def plot_agricultura():
    URL_STRING = 'https://www.datos.gov.co/resource/2pnw-mmge.json'
    SAMPLE_SIZE = int(request.args.get('sampleSize')[:-1])
    with urllib.request.urlopen(URL_STRING) as url:
        data = json.loads(url.read())
        edades = [int(x['a_o']) for x in data]
        plt.rcdefaults()
        fig, ax = plt.subplots()
        x_pos = np.arange(SAMPLE_SIZE)
        ax.bar( edades[0:SAMPLE_SIZE], x_pos )
        ax.set_title('Rendimiento Agricultura Colombiana')
        ax.set_xlabel('Año')
        ax.set_ylabel('Area sembrada')
        return makeImgResponse()

@app.route('/software-plot')
def plot_software():
    URL_STRING = 'https://www.datos.gov.co/resource/dubk-bq6v.json'
    SAMPLE_SIZE = int(request.args.get('sampleSize')[:-1])
    with urllib.request.urlopen(URL_STRING) as url:
        data = json.loads(url.read())
        edades = [(x['tipo_de_aplicaci_n']) for x in data]
        plt.rcdefaults()
        fig, ax = plt.subplots()
        x_pos = np.arange(SAMPLE_SIZE)
        ax.hist( edades[0:SAMPLE_SIZE], x_pos )
        ax.set_title('Numero de software hecho en colombia segun su tipo del año 2013 a 2018')
        ax.set_xlabel('Tipo de software')
        ax.set_ylabel('Cantidad de software')
        return makeImgResponse()

@app.route('/arboles',methods=['GET', 'POST'])
def arboles():
    sampleSize = ""
    if request.method == 'POST':
        sampleSize = request.form['sampleSize']
    else:
        sampleSize = "10"
    return render_template('arboles.html', name="Arboles",sampleSize=sampleSize)

@app.route('/agricultura',methods=['GET', 'POST'])
def agricultura():
    sampleSize = ""
    if request.method == 'POST':
        sampleSize = request.form['sampleSize']
    else:
        sampleSize = "100"
    return render_template('agricultura.html', name="Rendimiento agricultura",sampleSize=sampleSize)

@app.route('/Software',methods=['GET', 'POST'])
def software():
    sampleSize = ""
    if request.method == 'POST':
        sampleSize = request.form['sampleSize']
    else:
        sampleSize = "40"
    return render_template('Software.html', name="Software en Colombia",sampleSize=sampleSize)