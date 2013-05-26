#3

#Assign to a variable in your program a triple-quoted string
#that contains your favorite paragraph of text.

#Write a function which removes al punctuation from the string and counts
#the number of words in your text that contain the letter 'e.'
#Your program should print an analysis of the text like this:

#Your text contains 243 words, of which 109 (44.8%) contain an 'e'.

#my text

#The megalomania of the genes does not mean that benevolence and cooperation cannot evolve, any more than the law of gravity proves that flight cannot evolve. It means only that benevolence, like flight, is a special state of affairs in need of an explanation, not something that just happens.
#-Stephen Pinker

string = """The megalomania of the genes does not mean that benevolence and cooperation cannot evolve,
any more than the law of gravity proves that flight cannot evolve. It means only that benevolence, like flight,
is a special state of affirs in need of an explanation, not something that just happens.
-Stephen Pinker"""

def eCounter(string):
    eSum = 0
    for every word in string:
        if 'e' in word:
            eSum=eSum+1
            
        
