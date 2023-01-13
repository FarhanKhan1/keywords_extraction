from keybert import KeyBERT

text = """I need 2 bedroom house with 2 washrooms and 1 kitchen"""

model = KeyBERT()
keywords = model.extract_keywords(text, keyphrase_ngram_range=(1, 2))
print(keywords)




