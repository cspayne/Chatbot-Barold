from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from nltk.tokenize import word_tokenize
from chatterbot.response_selection import get_random_response
from chatterbot.comparisons import LevenshteinDistance
#import logging

#logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'barold',
    statement_comparison_function=LevenshteinDistance,
    response_selection_method=get_random_response,
    logic_adapters=[
        'chatterbot.logic.BestMatch'
            ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite1'
)

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(
#    'chatterbot.corpus.english.emotion',
#    'barryconvo',
#    'barold',
#    'chatterbot.corpus.english.greetings',
#)


print('Barold: I am Barold the Chatbot. Talk to me or type Goodbye to exit!')

def preprocess(statement):
        import re
        #replace linebreaks and tabs with spaces
        statement= statement.replace('\n', ' ').replace('\r',' ').replace('\t', ' ')
        #remove leading and trailing whitespace
        statement = statement.strip()
        #remove consecutive spaces
        statement = re.sub(' +', ' ', statement)

        #split into words
        tokens = word_tokenize(statement)
        #convert to lower
        tokens = [w.lower() for w in tokens]
        #get rid of punctuation
        words = [word for word in tokens if word.isalpha()]
        #convert list to string
        retval = ' '.join(words)
        return str(retval)


while True:
        message =input('\t\t\tYou: ')
        #print(message)
        final = preprocess(message)
        #print(final)
        if final!='goodbye':
            reply=bot.get_response(final)
            print('Barold: ',reply)
        if final=='goodbye':
              print('Barold: Goodbye')
              break
