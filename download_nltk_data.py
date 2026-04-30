import nltk

packages = [
    "punkt",
    "stopwords",
    "punkt_tab",
    "wordnet",
    "omw-1.4",
    "inaugural",
    "maxent_ne_chunker",
    "words",
    "movie_reviews",
    "treebank"
]

for pkg in packages:
    print(f"Downloading {pkg}...")
    nltk.download(pkg)

print("All downloads complete.")