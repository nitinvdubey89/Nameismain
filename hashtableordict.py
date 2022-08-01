class Hashtable:

    def __init__(self):
         # under the hood hashtable or dictionary is relying heavily on a list

         # based on the load factor we may change the size of the unerlying data structure
         # this resizing is called dynamic  resizing
         self.capacity = 10
         self.keys = [None]*self.capacity
         self.values = [None]*self.capacity


    def insert(self,key,data):

        # we have to find a valid location for the value or data.
        index = self.hash_function(key)
        #print(self.keys[index])
        #print(self.values[index])

        # there may be collisions i.e. index is already occupied
        # while we do not find an empty array slot
        while self.keys[index] is not None:
            #print(self.keys[index])
            # sometime we ahve to update the vlaue if the key is already presebnt
            if self.keys[index] == key:
                print(data)
                self.values[index] = data
                print(self.values[index])
                return

            # do linear probing (try the next slot in the array )
            # becasue we may increment the index suh that we are outside the range
            # of the  underlying list

            index = (index+1) % self.capacity
        # we have foynd the valid slot of the item

        self.keys[index] = key
        self.values[index] = data
        #print(data)



    def get(self,key):

        # we have to find a valid location for the value (data)
        index = self.hash_function(key)


        while self.keys[index] is not None:
            # this is whemn we find the item we are looking for
            if self.keys[index] == key:
                #print(self.values[index])
                return self.values[index]


            index = (index + 1) % self.capacity

        # the given key value pair with the key does not exist in the hash table
        return None

    # has valye based on the key i.e. index of the array
    def hash_function(self, key):
        hash_sum = 0

        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity

#print(ord('a')) # ord function gives the value of the character w.r.t the ascii code


if __name__ == '__main__':
    table = Hashtable()
    #print(table.hash_function('adam'))
    #table.insert('Adam', 23)
    #table.insert('kevin', 45)
    table.insert('Daniel', 34)
    table.insert('Daniel', 33)  # value wil be updated in hashtable
    #table.insert('Daniel', 32)

    print(table.get('Daniel'))





