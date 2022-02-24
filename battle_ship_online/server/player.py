"""
Represents a player object on the server side.
"""

class Player(object):
    def __init__(self, ip, name, hits):
        """
        init the player object on the server

        :param ip: ip address of player
        :type ip: str
        :param name: name of player
        :type name: str
        """

        self.game = None
        self.ip = ip
        self.name = name
        self.hits = hits

    def set_game(self, game):
        """
        sets the player game association

        :param game: Game
        :type game: Game object
        """
        self.game = game

    def update_score(self, hits):
        """
        updates the players hits

        :param hits: hits
        :type score: int
        """
        self.hits += hits

    def guess_ship_pos(self, row, col):
        """
        Makes a player guess where the enemy ship could be located

        :param row: int
        :type row: [type]
        :param col: column
        :type col: int
        """

        pass

    def disconnect(self):
        """
        call to disconnect player
        """
        pass

    def get_ip(self):
        """
        Gets players ip address
        :return: str
        """
        return self.ip

    def get_name(self):
        """
        Gets players name
        :return: str
        """

        return self.name

    def get_hits(self):
        """
        Get player hits
        :return: int
        """