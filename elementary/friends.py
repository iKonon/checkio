'''
For the mission "How to find friends" (http://www.checkio.org/mission/find-friends/share/3061fec1b35588e4bae8ad69db073aab/), 
it's nice to have access to a specially made data structure. 
In this mission we will realize a data structure which we will use to store and work with a friend network.

The class "Friends" should contains names and the connections between them. 
Names are represented as strings and are case sensitive. 
Connections are undirected, so if "sophia" is connected with "nikola", then it's also correct in reverse.

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Friends class.
Output: The behaviour as described.

How it is used: Here you will implement a class with mutable states. 
This is not a simple structure with a couple of functions, but object representation with more complex structure.
Precondition: All data is correct.
'''

class Friends: # connections

    def __init__(self, connections):
        # Returns a new Friends instance. "connections" is an iterable of sets with two elements in each. 
        # Each connection contains two names as strings. 
        # Connections can be repeated in the initial data, but inside it's stored once. Each connection has only two states - existing or not.
        self.__friends = list(connections)
        
    def add(self, connection):
        # Add a connection in the instance. "connection" is a set of two names (strings). 
        # Returns True if this connection is new. Returns False if this connection exists already.
        if connection in self.__friends:
            return False
        else:
            self.__friends.append(connection)
            return True

    def remove(self, connection):
        # Remove a connection from the instance. "connection" is a set of two names (strings). 
        # Returns True if this connection exists. Returns False if this connection is not in the instance.
        if connection in self.__friends:
            self.__friends.remove(connection)
            return True
        else:
            return False

    def names(self):
        # Returns a set of names. The set contains only names which are connected with somebody.
        return set().union(*self.__friends)

    def connected(self, name):
        # Returns a set of names which is connected with the given "name". 
        # If "name" does not exist in the instance, then return an empty set.
        return {x for x in self.names() if {x, name} in self.__friends}
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
