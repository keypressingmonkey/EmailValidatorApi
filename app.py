# list of whitelisted IPs from RapidApi here: https://docs.rapidapi.com/docs/firewall-ip-security
# helpers.py
from flask import request, current_app, Blueprint


# routes.py
index = Blueprint('index ', __name__)
@index.route('/', methods=['POST'])
def hello_world():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if ip:
        if 1==1: #ip in whitelistedIpAddresses:
            email = request.form.get('email')
            if email is None:
                return "No email address passed with call"
            else:
                domain = email.split("@")[-1]
                return "Congratulations, you received an API response: "+ domain
    else:
        return 'invalid authentification IP address'


whitelistedIpAddresses = [
    '107.23.255.128',
    '107.23.255.129',
    '107.23.255.131',
    '107.23.255.132',
    '107.23.255.133',
    '107.23.255.134',
    '107.23.255.135',
    '107.23.255.137',
    '107.23.255.138',
    '107.23.255.139',
    '107.23.255.140',
    '107.23.255.141',
    '107.23.255.142',
    '107.23.255.143',
    '107.23.255.144',
    '107.23.255.145',
    '107.23.255.146',
    '107.23.255.147',
    '107.23.255.148',
    '107.23.255.149',
    '107.23.255.150',
    '107.23.255.151',
    '107.23.255.152',
    '107.23.255.153',
    '107.23.255.154',
    '107.23.255.155',
    '107.23.255.156',
    '107.23.255.157',
    '107.23.255.158',
    '107.23.255.159',
    '35.162.152.183',
    '52.38.28.241',
    '52.35.67.149',
    '54.149.215.237',
    '13.127.146.34',
    '13.127.207.241',
    '13.232.235.243',
    '13.233.81.143',
    '13.112.233.15',
    '54.250.57.56',
    '18.182.156.77',
    '52.194.200.157',
    '3.120.160.95',
    '18.184.214.33',
    '18.197.117.10',
    '3.121.144.151',
    '13.239.156.114',
    '13.238.1.253',
    '13.54.58.4',
    '54.153.234.158',
    '18.228.167.221',
    '18.228.209.157',
    '18.228.209.53',
    '18.228.69.72',
    '13.228.169.5',
    '3.0.35.31',
    '3.1.111.112',
    '52.220.50.179',
    '34.250.225.89',
    '52.30.208.221',
    '63.34.177.151',
    '63.35.2.11'
]
