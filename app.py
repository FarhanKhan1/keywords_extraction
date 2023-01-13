from rake_nltk import Rake
r = Rake()
text = "i need a house of two rooms with one washroom"

r.extract_keywords_from_text(text)

print(r.get_ranked_phrases())
