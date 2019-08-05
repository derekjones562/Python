import random

from db import db


class GT1SelectedException(Exception):
    pass


class OutofRangeException(Exception):
    pass


class GameOutOfSyncException(Exception):
    pass


class MontyHallGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipAddress = db.Column(db.String)
    doors = db.relationship('Door')

    def __init__(self):
        self.save()
        self._createDoors()
        self.put_money_in_random_door()

    def __str__(self):
        return "MontyHallGame {}: ipAdress: {}, doors: {}".format(self.id, self.ipAddress, self.doors)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def reset(self):
        for door in self.doors:
            door.selected = False
            door.opened = False
            door.contains_money = False
            door.save()
        self.put_money_in_random_door()

    def _createDoors(self):
        for i in range(3):
            door = Door()
            door.montyHallGame = self.id
            door.save()

    def _get_random_door(self):
        random.seed()
        i = random.randint(0, 2)
        if i < 0 or i >3:
            raise OutofRangeException
        doors = Door.query.filter_by(montyHallGame=self.id).all()
        return doors[i]

    def put_money_in_random_door(self):
        door = self._get_random_door()
        door.contains_money = True
        door.save()

    def get_selected_door(self):
        selected_door = None
        for door in self.doors:
            if door.selected:
                if selected_door != None:
                    raise GT1SelectedException
                selected_door = door
        return selected_door

    def unselect_door(self):
        door = self.get_selected_door()
        if not door:
            return
        door.selected = False
        door.save()

    def is_winner(self):
        door = self.get_selected_door()
        if not door:
            raise GameOutOfSyncException
        if door.contains_money:
            return True
        return False

    def switch_doors(self):
        unopened_doors = []
        for door in self.doors:
            if not door.opened:
                unopened_doors.append(door)
        if len(unopened_doors) != 2:
            raise GameOutOfSyncException
        for door in unopened_doors:
            door.selected = not door.selected
            door.save()


class Door(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    opened = db.Column(db.Boolean, nullable=False)
    contains_money = db.Column(db.Boolean, nullable=False)
    selected = db.Column(db.Boolean, nullable=False)
    montyHallGame = db.Column(db.Integer, db.ForeignKey("monty_hall_game.id"))

    def __init__(self):
        self.opened = False
        self.contains_money = False
        self.selected = False

    def __str__(self):
        return "Door {}: opened:{}, $: {}, selected: {}".format(self.id, self.opened, self.contains_money, self.selected)

    def save(self):
        db.session.add(self)
        db.session.commit()


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")