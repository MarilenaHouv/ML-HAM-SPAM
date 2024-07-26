import spacy
#used for lemmatizaiton?
import textacy
import textacy.extract

#used to visualize data
from spacy import displacy

import re #regex


# READING DATA AND CREATING MODEL
with open("./data/alice.txt","r") as f:
    text = f.read()
    #print(text)
    chapters = text.split("CHAPTER")[1:]
    chapter1 = chapters[0]
    #small model (_sm) medium is md and large is lg
    nlp = spacy.load("en_core_web_sm")

    #create spacy object and analyze chapter 1
    doc = nlp(chapter1)
    #make a list of sentences
    sentences = list(doc.sents)
    sentence = sentences[2]

    #named entities - has specific name corresponding to it
    ents = list(doc.ents)
    # print(ents)
    # print(ents[0].label)
    # print(ents[0].label_)
    # print(ents[0].text)

# EXTRACTING ENTITIES WITH NER
    people = []
    for ent in ents:
        # print(ent.label_)
        if ent.label_ == "PERSON":
            people.append(ent)

# GET EACH TOKEN OF TEXT
    sentence2 = sentences[2]
    #breaking down text by each token (character)
    # pos for part of speech
        # for token in sentence:
        #     print (token.text,token.pos_)

# GET CHUNKS
    #nouns governed by other words in sentence, useful for chunks that have specific string in them
    chunks =(list(doc.noun_chunks))
    # for chunk in chunks:
    #     if "watch" in str(chunk):
    #         print(chunk)

# FIND ALL OCCURENCES OF SPECIFIC SENTENCE PATTERN
    patterns = [{"POS": "NOUN"}, {"POS":"VERB"},{"POS": "ADV"}]
    #can also have two lists so a patter with noun, verb, adv and a pattenr with pron verb adv
    patterns2 = [[{"POS": "NOUN"}, {"POS":"VERB"},{"POS": "ADV"}],[{"POS": "PRON"}, {"POS":"VERB"},{"POS": "ADV"}]]
    # look for any matches of patterns in doc
    verb_phrases = textacy.extract.matches.token_matches(doc,patterns=patterns2)

    # for verb_phrase in verb_phrases:
        # print (verb_phrase)


# LEMMATAZATION - REDUCING VERBS DOWN TO THEIR LEMMA (AKA THEIR ROOT), so you dont have to look for all forms of word 
    # for word in doc:
    #     if word.pos_ =="VERB":
    #         print (word, word.lemma_)

# VISUALIZING DATA WITH DISPLACY
    #personalizing vizualization
    colors = {"PERSON": "#4E0000"}
    #only highlight person entities and make the highlight color marroon
    options = {"ents":["PERSON"], "colors":colors}

    sentence8 = (sentences[8])
    # style can be dep (words broken down individually and rleationship of words) or ent (for named entity)
    html = displacy.render(doc,style="ent", options=options)
    #two ways to create data visualization .serve(create local server) or .render (creates html file and saves it)
    # with open ('data_vis.html',"w") as f:
    #     f.write(html)

# REGEX TO FIND QUOTES
    # finding quotes in sentences (Doesnt work dont know why)
    def find_sents(text=chapter1):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        sentences = list(doc.sents)
        return (sentences)
    
    def get_quotes(text):
        quotes = re.findall(r'["\'](.*?)["\']', text)
        return (quotes)
    
    # found_sents = find_sents() #gets all sentences in chapter
    # for sent in found_sents:
    #     str_sent = str(sent)
    #     found_quotes = get_quotes(str_sent) # gets all sentences with quotes in chapter
    #     if len(found_quotes)>0:
    #         print(found_quotes)


# NAMED ENTITY RECOGNITION SERIES 

