# -*- coding: utf-8 -*-
"""

"""


#Hashing  Table Algorithm Provides O(1) for Insert , Search & Deletion
#Hash number maps a big number / string to a small integer that can be used as 
# index in hash table
# Collision resolve technique for hashing

class Hashmap:
    
    def __init__(self):
        self.size= 18
        self.map= [None] *self.size
        
    def _get_hash(self,key):
        hash=0
        for char in str(key):
            hash+= ord(char)
        return hash % self.size
        
        
    def add(self,key,value):
        key_hash= self._get_hash(key)
        key_value= [key,value]
        
        if self.map[key_hash] is None:
            self.map[key_hash]=list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    pair[1]==value
                    return True
            self.map[key_hash].append(key_value)
            return True
        
    def get(self,key):
        key_hash=self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    return pair[1]
        return None
    
        
    def delete(self,key):
        key_hash=self._get_hash(key)
        
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            
            if self.map[key_hash][i][0]==key:
                
                self.map[key_hash].pop(i)
                return True
            
    def print(self):
        print("-------Details")
        for item in self.map:
            if item is not None:
                print(str(item))
            
h=Hashmap()
h.add('sam','8643289463248')
h.add('Div','82364832432')
h.add('nae','3234557')
h.add('sam','523103133')
h.add('sam','12485889')
h.print()
h.delete('Div')
h.print()
print('Loh'+ h.get('Loh'))