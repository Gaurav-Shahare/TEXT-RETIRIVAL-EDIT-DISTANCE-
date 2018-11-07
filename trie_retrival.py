#python 2.7
import numpy as np
import string 
class TrieNode:
    def __init__(self):  #Trie Data Strucuture
        self.children=[None]*26 
        self.endword=False
        self.count=0

class Trie:

    def __init__(self):
        self.root=self.getnode()

    def getnode(self):
        return TrieNode()

    def chartoint(self,temp):  
        return ord(temp)-ord('a')

    def insert(self,word):
    
        temp=self.root

        for i in word: 

            idx=self.chartoint(i)
            if(ord(i)>=65 and ord(i)<=90):
                idx=idx+32

            elif(ord(i)<65 or ord(i)>122 or( ord(i)>90 and ord(i)<97 ) ):
                continue

            if not temp.children[idx]:
                temp.children[idx]=self.getnode()
            temp=temp.children[idx]
        temp.count=temp.count+1
        temp.endword=True

    def search(self,word):
        temp=self.root
        for i in word:
            idx=self.chartoint(i)
            
            if not temp.children[idx]:
                return False
            temp=temp.children[idx]

        return temp.endword

    def find(self,word):
        temp=self.root
        length=0
        for i in word:
            if(ord(i)<65 or ord(i)>122 or  (ord(i)>90 and ord(i)<97 )  ):
                continue
            else:
                length=length+1
        if length==0:
            return

        
        col=np.zeros(length+1)
        for i in range(length+1):
            col[i]=i
        x=""
        for i in range(26):
            self.findrecursively(word,length,temp.children[i],i+97,x,1,2,col)

    def print_all(self,temp,x,i):
        if(temp==None):
            print(x)
            return
        x=x+chr(i)
        if(temp.endword):
            print(x)
        are=False
        for i in range(26):
            if(temp.children[i]!=None):
                self.print_all(temp.children[i],x,97+i)
                are=True
        if(are==False and temp.endword==False):
            print(x)
            

    def findrecursively(self,word,length,temp,i,x,order,max_edit,pre):
        if temp==None:
            return 
        newrow=np.zeros(length+1)
        
        x=x+chr(i)
        y=chr(i)
        

        for k in range(length+1):
            if(k==0):
                newrow[k]=order
            else:
                if(ord(word[k-1])<65 or ord(word[k-1])>122 or  (ord(word[k-1])>90 and ord(word[k-1])<97) ):
                    continue
                if word[k-1]==y:
                    newrow[k]=pre[k-1]
                else:
                    newrow[k]=1+min(pre[k-1],pre[k],newrow[k-1])
        
        if(newrow[length]<=max_edit):
            self.print_all(temp,x[:(len(x)-1)],i)
            return
        
        for i in range(26):
            self.findrecursively(word,length,temp.children[i],i+97,x,order+1,max_edit,newrow)

    def findoccurance(self,x):
        table = string.maketrans("","")
        new_x = x.translate(table, string.punctuation)
        self.find(new_x)


def main():
    x=raw_input("Enter query\n")
    crimefile = open('test.txt', 'r')  #input the stored data
    yourResult = [line.split(',') for line in crimefile.readlines()]
    t=Trie()
    
    for i in yourResult[0]:
        t.insert(i)  #insert stored the data
   # x =input("")
    t.findoccurance(x)
    

if __name__ == '__main__': 
    main() 
