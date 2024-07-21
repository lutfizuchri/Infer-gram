from collections import Counter
import math

# Sample text data for two languages
english_text = "This is a sample English text. It contains common English words and bigrams."
spanish_text = "Este es un texto de ejemplo en español. Contiene palabras comunes en español."

# Function to calculate bigram frequencies
def bigram_frequencies(text):
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    return Counter(bigrams)

# Create language profiles
english_profile = bigram_frequencies(english_text)
spanish_profile = bigram_frequencies(spanish_text)

# Function to calculate cosine similarity
def cosine_similarity(profile1, profile2):
    all_bigrams = set(profile1.keys()).union(set(profile2.keys()))
    vec1 = [profile1.get(bigram, 0) for bigram in all_bigrams]
    vec2 = [profile2.get(bigram, 0) for bigram in all_bigrams]
    
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a*a for a in vec1))
    magnitude2 = math.sqrt(sum(a*a for a in vec2))
    
    if not magnitude1 or not magnitude2:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

# Analyze a new input string
input_string = "This is a test string in English."

input_profile = bigram_frequencies(input_string)

# Compare with language profiles
similarity_with_english = cosine_similarity(input_profile, english_profile)
similarity_with_spanish = cosine_similarity(input_profile, spanish_profile)

print(f"Similarity with English: {similarity_with_english}")
print(f"Similarity with Spanish: {similarity_with_spanish}")

# Determine the language
if similarity_with_english > similarity_with_spanish:
    print("The input string is likely in English.")
else:
    print("The input string is likely in Spanish.")
