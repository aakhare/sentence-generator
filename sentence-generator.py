import random
noun_list = ["dog", "cat", "giraffe", "computer", "donut", "bed", "butterfly", "lion", "school", "table"]
verb_list = ["makes", "dances", "goes", "runs", "jumps", "sleeps", "sings", "eats", "codes", "cries", "laughs"]
adjective_list = ["happy", "amazing", "proud", "cool", "nice", "fierce", "fabulous", "super", "lazy", "energetic"]
adverb_list = ["sadly", "fortunately", "gladly", "generally", "boldly", "excitedly", "carefully", "playfully"]
preposition_list = ["to", "from", "under", "over", "with", "behind", "beneath", "beside"]
article_list = ["a", "an", "the"]

def noun_phrase():
    return random.choice(article_list) + " " + \
    random.choice(adjective_list) + " " + \
    random.choice(noun_list)

def verb_phrase():
    return random.choice(adverb_list) + " " + \
    random.choice(verb_list)

def prepositional_phrase():
    return random.choice(preposition_list) + " " + \
    noun_phrase()

def sentence():
    return noun_phrase() + " " + verb_phrase() + " " + prepositional_phrase()

print(sentence())
