class SongStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.recently_played = []
    
    def add_song(self, user, song):
        if user in self.store:
            user_songs = self.store[user]
            user_songs.append(song)
            self.recently_played.remove((user, song))
        else:
            user_songs = [song]
            self.store[user] = user_songs

        self.recently_played.append((user, song))

        if len(self.recently_played) > self.capacity:
            oldest_song = self.recently_played.pop(0)
            user_songs = self.store[oldest_song[0]]
            user_songs.remove(oldest_song[1])

    def get_recently_played(self, user):
        if user in self.store:
            return self.store[user]
        else:
            return[]