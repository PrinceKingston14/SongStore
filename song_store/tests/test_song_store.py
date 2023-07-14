import unittest
from song_store import SongStore

class SongStoreTests(unittest.TestCase):
    def test_recently_played_songs(self):
        store = SongStore(3)

        store.add_song('user1', 'S1')
        store.add_song('user1', 'S2')
        store.add_song('user1', 'S3')

        store.add_song('user2', 'S4')
        store.add_song('user2', 'S2')
        store.add_song('user2', 'S1')

        store.add_song('user3', 'S5')
        store.add_song('user3', 'S2')
        store.add_song('user3', 'S6')

        self.assertEqual(store.get_recently_played('user1'), ['S3', 'S2', 'S1'])
        self.assertEqual(store.get_recently_played('user2'), ['S1', 'S2', 'S4'])
        self.assertEqual(store.get_recently_played('user3'), ['S6', 'S2', 'S5'])

        if __name__ == '__main__':
            unittest.main()