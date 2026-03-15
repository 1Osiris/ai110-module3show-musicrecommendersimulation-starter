# 🎧 Model Card: Music Recommender Simulation


## 1. Model Name

VibeFinder 1.0

---


## 2. Intended Use

This recommender suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy. It assumes users know their preferences and is intended for classroom exploration, not real-world deployment.

---


## 3. How the Model Works

The model uses each song's genre, mood, and energy. It compares these to the user's stated preferences. Songs get points for matching genre (+1.0), mood (+0.7), and for having similar energy (closer is better). The top-scoring songs are recommended. No major changes were made from the starter logic.

---


## 4. Data

The dataset contains 20 songs with genres like pop, rock, lofi, jazz, synthwave, indie pop, and ambient. Moods include happy, chill, intense, relaxed, moody, and focused. No songs were added or removed. Some genres and moods are missing, so the catalog is limited.

---


## 5. Strengths

The system works well for users with common preferences, like pop/happy or jazz/relaxed. It captures genre and mood matches clearly, and the top results usually make sense for typical user profiles.

---


## 6. Limitations and Bias

The system ignores features like tempo, valence, and lyrics. It struggles with rare or unknown genres and moods, and only recommends songs that closely match the user's input. This can create filter bubbles and miss out on diverse or unexpected recommendations.


## 7. Evaluation

I tested typical and edge case user profiles, including empty and out-of-bounds preferences. I looked for reasonable matches and checked for zero or odd scores. I was surprised that empty or unknown preferences led to all zero scores and no explanations.

---


## 8. Future Work

I would add more features like tempo and valence, improve explanations, and add diversity to the recommendations. Handling missing or unknown preferences and supporting more complex user tastes would make the system better.



## 9. Personal Reflection

My biggest learning moment was realizing how even simple rules can create both useful and biased recommendations. Using AI tools helped me move faster, but I often needed to double-check their suggestions for accuracy and clarity. I was surprised that such basic algorithms could still "feel" like real recommendations, even though they miss a lot of nuance. If I extended this project, I would experiment with adding more features, improving diversity, and making the system more robust to unusual or missing user preferences.
