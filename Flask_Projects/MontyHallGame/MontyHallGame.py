#!/usr/bin/python
from flask import Flask, render_template, redirect, url_for, request
import requests
from flask_migrate import Migrate
from db import db
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()


def get_images():
    pass

def create_new_game(ipAddress):
    game = models.MontyHallGame()
    game.ipAddress = ipAddress
    db.session.add(game)
    db.session.commit()
    return game


def get_game_by_ip(ipAddress):
    game = models.MontyHallGame.query.filter_by(ipAddress=ipAddress).first()
    if not game:
        game = create_new_game(ipAddress)
    return game


def get_game_by_id(game_id):
    return models.MontyHallGame.query.get(game_id)


def get_doors_by_game(game):
    doors = models.Door.query.filter_by(montyHallGame=game.id).all()
    return doors


def get_door_by_id(door_id):
    return models.Door.query.get(door_id)


def door_previously_selcted(game):
    for door in game.doors:
        if door.selected:
            return True
    return False


def find_goat_door(game):
    for door in game.doors:
        if not door.selected and not door.contains_money:
            return door


@app.route('/')
def index():
    get_images()
    game = get_game_by_ip(request.remote_addr)
    try:
        selected_door = game.get_selected_door()
        if selected_door:
            return redirect(url_for('choose_door', door=selected_door.id))
    except models.GT1SelectedException as e:
        pass
    return redirect(url_for('new_game'))



@app.route('/choose_door', methods=['GET'])
def choose_door():
    # mark door as selected
    door_id = request.args.get("door")
    if not door_id:
        return redirect(url_for('index'))
    door = get_door_by_id(door_id)
    game = get_game_by_id(door.montyHallGame)
    if door_previously_selcted(game):
        game.reset()
    door.selected = True
    door.save()
    # open door with goat
    goat_door = find_goat_door(game)
    goat_door.opened = True
    goat_door.save()

    game = get_game_by_ip(request.remote_addr)
    data = {
        "game": game,
        "change_door_url": url_for('change_door'),
        "end_game_url": url_for('end_game')
    }
    return render_template('SwitchDoors.html', **request.args, **data)


@app.route("/change_door", methods=['GET'])
def change_door():
    # change selected door
    game = get_game_by_ip(request.remote_addr)
    try:
        game.switch_doors()
    except models.GameOutOfSyncException as e:
        return redirect(url_for('index'))
    return redirect(url_for('end_game'))


@app.route("/end_game", methods=['GET'])
def end_game():
    # reveal door with money
    game = get_game_by_ip(request.remote_addr)
    try:
        winner = game.is_winner()
    except models.GameOutOfSyncException as e:
        return redirect(url_for('index'))
    game.unselect_door()
    # save win/lose and if changed or not
    # winner variable = True/False
    data = {
        "game": game,
        "win": winner
    }
    return render_template('EndGame.html', **request.args, **data)


@app.route("/new_game", methods=['GET'])
def new_game():
    # flush game state
    game = get_game_by_ip(request.remote_addr)
    game.reset()
    # Set the game associated with the ip to the cookie
    data = {
        "game": game,
        "url": url_for('choose_door')
    }
    return render_template('Doors.html', **request.args, **data)


if __name__ == '__main__':
    app.run(debug=True)
