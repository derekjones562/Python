#!/usr/bin/python
from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('create_rms_retailer.html', **request.args)


@app.route('/create_rms_retailer', methods=['POST'])
def create_rms_retailer():
    r = request
    URL = "https://sandbox.doba.com/api/20110301/xml_partner_api.php"
    str_request = render_template('add_retailer_xml.txt', **request.form)
    try:
        response = requests.post(url=URL, data=str_request)
        print("Response: {}   Http code: {}".format(response.content, response.status_code))
    except requests.exceptions.ConnectionError as e:
        raise
        print(e.message)
    except Exception as e:
        raise
        print(e.message)

    success_url_param = ""
    if response.status_code == 200:
        raise
        success_url_param = "?success=True"

    redirect_url = "{}{}".format(url_for('index'), success_url_param)
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run(debug=True)
