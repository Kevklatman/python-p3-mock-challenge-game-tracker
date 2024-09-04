class Game:
    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise TypeError("Title must be a non-empty string")
        
    @property
    def title(self):
        return self._title
    
    def results(self):
        return [result for result in Result.all if result.game == self]
    
    def players(self):
        return list(set([result.player for result in self.results()]))
    
    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        return 0

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else:
            raise ValueError("Username must be a string between 2 and 16 characters")
    
    def results(self):
        return [result for result in Result.all if result.player == self]
    
    def games_played(self):
        return list(set(result.game for result in self.results()))
    
    def played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:
    all = []
    
    def __init__(self, player, game, score):
        if isinstance(player, Player) and isinstance(game, Game) and isinstance(score, int) and 1 <= score <= 5000:
            self._player = player
            self._game = game
            self._score = score
            Result.all.append(self)
        else:
            raise ValueError("Invalid arguments for Result initialization")
    
    @property
    def player(self):
        return self._player
    
    @property
    def game(self):
        return self._game
    
    @property
    def score(self):
        return self._score