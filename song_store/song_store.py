class SongStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        
    
    def add_song(self, user, song):
        if user not in self.store:
            self.store[user] = []

        user_songs = self.store[user]

        if song in user_songs:
            user_songs.remove(song)
        
        user_songs.append(song)

        if len(user_songs) > self.capacity:
            user_songs.pop(0)
        
    def get_recently_played(self, user):
        if user in self.store:
            return self.store[user][::-1]
        else:
            return[]
         