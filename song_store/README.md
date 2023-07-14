#SongStore

SongStore is an in-memory store for recently played songs. It can store a list of song-user pairs, with each song linked to a user. The store has a fixed inital capacity and automatically removes the least recently played song when it becomes full.

## Usage

Clone the repository:

    ```bash
    git clone <https://github.com/PrinceKingston14/SongStore.git>

1. Install the dependencies (none required for this project).
2. Run the tests:
   python -m unittest discover -s song_store
