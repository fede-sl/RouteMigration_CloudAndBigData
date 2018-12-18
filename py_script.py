from flask import Flask, request, render_template, jsonify 
import sys
import re
import csv
from pandas.io.parsers import read_csv
import json

app = Flask(__name__)
@app.route('/')


def homepage():

	valores = read_csv("reducedData/Swainson's Hawks.csv", sep = ',', header=None).values
	lat = []
	date = []
	lon = []
	year = []
	datos = valores.astype(str)
	for line in datos:
	    if("timestamp" not in line):
	        lat.append(line[3])
	        lon.append(line[2])
	        date.append(line[0])
	        year.append(re.split('-', line[0])[0])
	return render_template("mapsRoutes.html",lat=lat, lon = lon, date = date, year = year)

@app.route('/showBirds', methods=['POST'])
def showBirds():
	bird =  request.form['bird']
	filename = "reducedData/"+bird+".csv"
	valores = read_csv(filename, sep = ',', header=None).values
	lat = []
	date = []
	lon = []
	year = []
	datos = valores.astype(str)
	for line in datos:
	    if("visible" not in line):
	        lat.append(line[3])
	        lon.append(line[2])
	        date.append(line[0])
	        year.append(re.split('-', line[0])[0])
	return jsonify({ 'lat': lat, 'lon': lon, 'year': year, 'date': date})

if __name__ == '__main__':
	app.run(host='localhost', port=9874)