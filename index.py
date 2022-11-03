from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return "Selamat Datang di server Python Flask"


@app.route('/check-cluster', methods=['POST'])
@cross_origin()
def check_cluster():
    data = request.json
    bb = data['bb']
    tb = data['tb']
    lk = data['lk']

    dataset = pd.read_csv("Dataset Balita.csv")
    X = dataset.loc[:, ["NBB", "NTB", "NLK"]]

    kmeans = KMeans(n_clusters=5)
    kmeans.fit(X)
    my_array = np.array([[bb, tb, lk]])
    test = pd.DataFrame(my_array, columns=['NBB', 'NTB', 'NLK'])
    predict = kmeans.predict(test)[0]
    return jsonify({'cluster': int(predict)})


if __name__ == '__main__':
    app.run(debug=False)
