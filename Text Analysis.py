givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class textanalyzer(object):

    def __init__(self,text):
        formattedtext=text.replace(".","").replace("!","").replace("?","").replace(",","")
        formattedtext=formattedtext.lower()
        self.fmttext=formattedtext
    def freqall(self):
        wordlist=self.fmttext.split(" ")
        freqmap={}
        for word in set(wordlist):
            freqmap[word]=wordlist.count(word)
            return freqmap
    def freqof(self,word):
            freqdict=self.freqall()
            if word in freqdict:
                return freqdict[word]
            else:
                return 0
analyzed=textanalyzer(givenstring)
print("formatted text:",analyzed.fmttext)
freqmap=analyzed.freqall()
print(freqmap)
word="lorem"
frequency=analyzed.freqof(word)
print("the word",word,"appears",frequency,"times.")
