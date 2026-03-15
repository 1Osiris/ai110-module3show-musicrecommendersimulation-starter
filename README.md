# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.


This version recommends songs based on user preferences for genre, mood, and energy. It scores each song using these features and returns the top matches. The system is simple and designed for classroom learning.

---

## How The System Works


Each Song uses genre, mood, and energy. UserProfile stores the user's preferred genre, mood, and energy. The Recommender scores songs by matching genre (+1.0), mood (+0.7), and energy similarity (closer is better). The top k songs are recommended.


Real-world recommendation systems like Spotify and Apple Music combine numerical similarity and categorical matching into a unified scoring framework, then apply a separate ranking layer to ensure the final list is diverse and engaging rather than just a stack of near-identical songs. Our recommendation system uses a two-layer approach inspired by real-world platforms like Spotify and Apple Music. First, we apply a Scoring Rule that combines both categorical and numerical features into a single composite score for each song:

Genre Match: If a song’s genre matches the user’s preferred genre, it receives a bonus of +1.0 point.
Mood Match: If a song’s mood matches the user’s preferred mood, it receives a bonus of +0.7 points.
Energy Similarity: We calculate how close the song’s energy value is to the user’s target energy using the formula:
energy_score = 1 - abs(song_energy - user_energy)
This value ranges from 0 (least similar) to 1 (most similar).
The final composite score for each song is the sum of these three components. This balanced weighting ensures that no single feature dominates the recommendations, allowing both categorical preferences (like genre and mood) and nuanced numerical similarity (energy) to influence the results.

After scoring, we apply a Ranking Rule: all songs are sorted by their composite scores in descending order. The top results are selected as recommendations. This ranking step can also be extended to promote diversity and avoid recommending near-duplicate songs.

Our Song class encapsulates all relevant song attributes, while the UserProfile class stores the user’s preferences. For each song, we compare its attributes to the user’s profile, compute a score, and then rank all songs to produce the final recommendations.

### Potential Biases

1. **Genre & Mood Popularity** — Common genres/moods dominate recommendations, crowding out underrepresented ones.
2. **Feature Weighting** — Chosen weights are subjective and may not reflect every user's true preferences.
3. **Energy Range** — The similarity formula assumes energy matters equally to all users across all genres.
4. **Cold Start** — New or niche songs are less likely to surface since the system favors common preference matches.
5. **Lack of Diversity** — Without explicit diversity enforcement, top results may be repetitively similar in artist or sub-genre.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried


I tried changing the genre and mood weights, and tested edge cases like empty or unknown preferences. The system worked well for common profiles but gave zero scores for missing or rare preferences.

---

## Limitations and Risks


The system only works on a small catalog, does not use lyrics or tempo, and can over-favor common genres or moods. It does not handle missing or unknown preferences well.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)


I learned that recommenders use simple rules to turn data into predictions, but these rules can create bias or filter bubbles. I was surprised by how strict the system is and how it can miss good recommendations for unusual users. Human judgment is still important in real systems.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

