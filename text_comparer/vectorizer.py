from collections import defaultdict
import re

from similarity import similarity


def word_frequencies(word_vector):
   
    num_words = len(word_vector)
    frequencies = defaultdict(float)
    for word in word_vector:
        frequencies[word] += 1.0 / num_words

    return dict(frequencies)


def compare_vectors(word_vector1, word_vector2):
    
    all_words = list(set(word_vector1).union(set(word_vector2)))
    #print all_words
    frequency_dict1 = word_frequencies(word_vector1)
    #print frequency_dict1
    frequency_dict2 = word_frequencies(word_vector2)
    #print frequency_dict2

    frequency_vector1 = [frequency_dict1.get(word, 0) for word in all_words]
    frequency_vector2 = [frequency_dict2.get(word, 0) for word in all_words]
    #print frequency_vector1,frequency_vector2

    return similarity(frequency_vector1, frequency_vector2)


def vectorize_text(text):
    """Takes in text, processes it, and vectorizes it."""

    def remove_punctuation(text):
        """Removes special characters from text."""
        return re.sub('[,.?";:\-!@#$%^&*()]', '', text)

    def remove_common_words(text_vector):
        """source: http://www.bckelk.ukfsn.org/words/uk1000n.html"""
        
        common_words = set(['the', 'and', 'to', 'of', 'a', 'I', 'in', 'was',
            'he', 'that', 'it', 'his', 'her', 'you', 'as', 'had', 'with',
            'for', 'she', 'not', 'at', 'but', 'be', 'my', 'on', 'have', 'him',
            'is', 'said', 'me', 'which', 'by', 'so', 'this', 'all', 'from',
            'they', 'no', 'were', 'if', 'would', 'or', 'when', 'what', 'there',
            'been', 'one', 'could', 'very', 'an', 'who'])
        return [word for word in text_vector if word not in common_words]

    text = text.lower()
    text = remove_punctuation(text)
    #print text
    words_list = text.split()
    #words_list = remove_common_words(words_list)
    #print words_list
    return words_list


def compare_texts(text1, text2):
    
    return compare_vectors(vectorize_text(text1), vectorize_text(text2))


