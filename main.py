# Copyright 2021 Daniil O. Nepryakhin [NervoyzZz]
# Licensed under the Apache License, Version 2.0

import json
import random

from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/post', methods=['POST'])
def main():
    """Entry point of the application."""
    response = {
            'session': request.json['session'],
            'version': request.json['version'],
            'response': {'end_session': False}
     }

    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res, req):
    """
    Function to handle user requests.

    Parameters
    ----------
    res: dict
        Response. Necessary argument to make Alice work.
        Set `text` field to make Alice say it.
    req: dict
        Request. User request with necessary data.
        Contains text of user Speech in `original_utterance`.

    Returns
    -------
    None
    """
    if req['request']['original_utterance']:
        request_text = req['request']['original_utterance'].lower()
        possible_responses = (
            f'Вы сказали: {request_text}',
            f'Повторяю: {request_text}'
        )
    else:
        possible_responses = (
            'Здравствуйте! Это игра морской бой. Хотите сыграть?',
            'Приветствую вас! Это игра морской бой. Она еще разрабатывается. '
            'Хотите попробовать?'
        )
    res['response']['text'] = random.choice(possible_responses)


if __name__ == '__main__':
    app.run()
