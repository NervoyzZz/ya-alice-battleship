# Yandex Alice skill: Battleship Game

## What is it?
It is an implementation of Yandex Alice skill that 
makes it possible to play the battleship game with
Alice.

The classic paper-game is ported to Alice station. 
You will play the well known game as usual - using
your piece of paper and a pen. The difference is that
your opponent will be an electronic friend.

## How to run
To run the application it is enough to run `main.py` as
```
python3 main.py
```

For local development and tests it is possible to use
`alice-nearby` Go package For local test.
[Source](https://github.com/azzzak/alice-nearby).
```
go/bin/alice-nearby --webhook=http://localhost:5000/post --port=3456
```
And go to your browser to `localhost:3456`

To make your application visible from the net you can
use `ngrok` as:
```
ngrok http 5000
```
Create your skill in Yandex 
[dialogs](https://dialogs.yandex.ru/developer/).
Copy https link and paste it to the dialog
settings as webhook and publish the skill. The private
skills are not needed in moderation.