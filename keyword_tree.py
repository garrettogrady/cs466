# Python program for insert and search 
# operation in a Trie 
import time


class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie:
      
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        return TrieNode()
  
    def insert(self,key): 
          
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = ord(key[level])-ord('a')
  
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index]
  
        pCrawl.isEndOfWord = True
  
    def search(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = ord(key[level])-ord('a') 
            print(index)
            print('hello')
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
  
        if pCrawl != None and pCrawl.isEndOfWord:
            #print("found in trie at ", index)
            return True
  
# driver function 
def keyword_main(patterns, sequence): 
  
   # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"]


  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in sequence: 
        t.insert(key)

    for word in patterns:
        #print(word)
        t.search(word)


  
if __name__ == '__main__': 
    main() 