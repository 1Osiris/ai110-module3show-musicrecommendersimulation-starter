
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs


    def recommend(self, user: UserProfile, k: int = 5) -> List[Tuple[Song, float, list]]:
        """Return top k recommended songs with scores and reasons."""
        scored = []
        for song in self.songs:
            score, reasons = self._score_song(user, song)
            scored.append((song, score, reasons))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return explanation string for a song recommendation."""
        _, reasons = self._score_song(user, song)
        return "; ".join(reasons)

    def _score_song(self, user: UserProfile, song: Song) -> Tuple[float, list]:
        """Score a song for a user and return score and reasons."""
        score = 0.0
        reasons = []
        # Genre match (+1.0)
        if song.genre == user.favorite_genre:
            score += 1.0
            reasons.append("Genre match (+1.0)")
        # Mood match (+0.7)
        if song.mood == user.favorite_mood:
            score += 0.7
            reasons.append("Mood match (+0.7)")
        # Energy similarity (1 - abs(song_energy - user_energy))
        if song.energy is not None and user.target_energy is not None:
            energy_sim = 1 - abs(song.energy - user.target_energy)
            score += energy_sim
            reasons.append(f"Energy similarity (+{energy_sim:.2f})")
        return score, reasons

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file as dictionaries."""
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numeric fields
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, list]:
    """Score a song for a user and return score and reasons."""
    score = 0.0
    reasons = []
    # Genre match (proposed: +1.0)
    if song.get('genre') == user_prefs.get('genre'):
        score += 1.0
        reasons.append("Genre match (+1.0)")
    # Mood match (proposed: +0.7)
    if song.get('mood') == user_prefs.get('mood'):
        score += 0.7
        reasons.append("Mood match (+0.7)")
    # Energy similarity (proposed: 1 - abs(song_energy - user_energy))
    song_energy = song.get('energy')
    user_energy = user_prefs.get('energy')
    if song_energy is not None and user_energy is not None:
        energy_sim = 1 - abs(song_energy - user_energy)
        score += energy_sim
        reasons.append(f"Energy similarity (+{energy_sim:.2f})")
    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return top k recommended songs with scores and explanations."""
    # Score all songs
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    # Version 1: Using sorted() (does NOT modify the original list)
    top_k_sorted = sorted(scored, key=lambda x: x[1], reverse=True)[:k]

    # Version 2: Using .sort() (modifies the list in place)
    scored.sort(key=lambda x: x[1], reverse=True)
    top_k_sort = scored[:k]

    # Key difference:
    # - sorted() returns a new sorted list, leaving the original list unchanged.
    # - .sort() sorts the list in place, modifying the original list object.

    # You can return either version; here we return the sorted() version for safety.
    return top_k_sorted