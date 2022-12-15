import requests
from flask import Flask, request

from Responses import sample_response
from config.get_keys import Config

app = Flask(__name__)

token = Config.API_KEY


def welcome_msg(item):
    msg = sample_response(item["text"])
    chat_id = item["chat"]["id"]
    user_id = item["from"]["id"]
    user_name = item["from"].get("username", user_id)
    welcome_msg = '''{}'''.format(msg)
    to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                    welcome_msg)
    resp = requests.get(to_url)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return {'statusCode': 200, 'body': 'Success', 'data': data}
    else:
        return {'statusCode': 200, 'body': 'Success'}


if __name__ == '__main__':
    app.run(debug=True)
