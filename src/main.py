"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    """Run the music recommender simulation from the command line."""
    songs = load_songs("../data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # Additional user preference dictionaries
    user_prefs_rock = {"genre": "rock", "mood": "energetic", "energy": 0.9}
    user_prefs_chill = {"genre": "electronic", "mood": "chill", "energy": 0.4}
    user_prefs_jazz = {"genre": "jazz", "mood": "relaxed", "energy": 0.6}


    # Adversarial / edge case user profiles
    user_prefs_classical_angry = {"genre": "classical", "mood": "angry", "energy": 1.0}  # Genre-mood mismatch
    user_prefs_impossible_energy = {"genre": "pop", "mood": "happy", "energy": 2.0}     # Impossible energy value
    user_prefs_empty = {}  # Empty preferences
    user_prefs_unknown_genre = {"genre": "alienwave", "mood": "mysterious", "energy": 0.5} # Unknown genre/mood
    user_prefs_contradictory = {"genre": "jazz", "mood": "calm", "energy": 1.0}           # Contradictory mood/energy

    rec_lst = [
        user_prefs_classical_angry, user_prefs_impossible_energy, user_prefs_empty,
        user_prefs_unknown_genre, user_prefs_contradictory
    ]

    print("\nTop recommendations:\n")

    for recc in rec_lst:
        recommendations = recommend_songs(recc, songs, k=5)
        for idx, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print("=" * 40)
            print(f"#{idx}: {song['title']} by {song['artist']}")
            print(f"Score: {score:.2f}")
            # Print each reason on its own line
            for reason in explanation.split(";"):
                print(f"- {reason.strip()}")
            print("=" * 40 + "\n")


if __name__ == "__main__":
    main()
