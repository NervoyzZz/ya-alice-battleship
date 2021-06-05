# Copyright 2021 Daniil O. Nepryakhin [NervoyzZz]
# Licensed under the Apache License, Version 2.0

import json
import random

import utils

from flask import Flask
from flask import request


app = Flask(__name__)
game_obj = type('Game', (), {'game_state': None,
                             'alice_field': None,
                             'player_field': None})


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
    if not (request_text := req['request']['original_utterance']):
        # The first entry
        possible_responses = (
            'Здравствуйте! Это игра морской бой. Хотите сыграть?',
            'Приветствую вас! Это игра морской бой. Она еще разрабатывается. '
            'Хотите попробовать?'
        )
        game_obj.game_state = utils.GameStateEnum.NOT_STARTED
    else:
        # there is user text
        request_text = request_text.lower()
        if request_text == 'старт':
            game_obj.game_state = utils.GameStateEnum.SHIP_PLACEMENT
            possible_responses = ('Это тестовая версия игры. Начертите два '
                                 'поля размером пять на пять. Одно из них '
                                 'для расположения ваших кораблей, а другое для '
                                 'отслеживания ваших выстрелов по моим кораблям. '
                                 'Затем расположите на вашем поле четыре однопалубных '
                                 'кораблей. Как будете готовы, скажите "готов".',)
            game_obj.alice_field = utils.Field(5)
            game_obj.player_field = utils.Field(5)
            for i in range(4):
                game_obj.alice_field.place_ship(1)
        elif (request_text == 'готов'
              and game_obj.game_state == utils.GameStateEnum.SHIP_PLACEMENT):
            # decide who will start with coin throw
            player_turn = random.random() >= 0.5
            if player_turn:
                game_obj.game_state = utils.GameStateEnum.PLAYER_TURN
                possible_responses = ('Я подбросила монетку, и она показала,'
                                      ' что первый ход за вами.'
                                      ' Скажите "ХОД" и координаты выстрела.',)
            else:
                game_obj.game_state = utils.GameStateEnum.ALICE_TURN
                possible_responses = (f'Я подбросила монетку, и она показала,'
                                      f' что первый ход за мной.'
                                      f' ХОД: {random.randint(1, 5)},'
                                      f' {random.randint(1, 5)}'
                                      f' Скажите "Попала", "Убила" или "Мимо".', )

        else:
            possible_responses = (
                f'Вы сказали: {request_text}',
                f'Повторяю: {request_text}'
            )
    # result Alice response
    res['response']['text'] = random.choice(possible_responses)


if __name__ == '__main__':
    app.run()
