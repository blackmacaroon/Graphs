from util import Queue
import random

# make friends along the way until we have enough
# need to do something about already existing relationships (collisions)
# or if you try to be friends with yourself
# catch the warnings somehow


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # Add users
        # loop through and add one for range of numUsers
        for i in range(numUsers):
            self.addUser(f"User{i}") # NOTE debug function
        # Create friendships
        possible_friendships = []
        # List all possible combos, requires a nested for loop, connect every user to every friend
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possible_friendships.append((userID, friendID))
        
        random.shuffle(possible_friendships)
        for i in range(numUsers * avgFriendships // 2):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])
        

        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        qq = Queue()
        qq.enqueue([userID]) # so we can build all the possible paths and return the best one
        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]
            # if neighbor has already been visited, it skips this 
            if vertex not in visited: #regardless of list or tuple or dictionary, you can ask "is this in here or not"
                #builds a queue of paths for each visited node
                visited[vertex] = path # this is the spot in the traversal where we've found an unvisited node. DO THE THING - adding this path to the discionary as A shortest way here
                
                for friend in self.friendships[vertex]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    qq.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print("print friendships")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("print connections")
    print(connections)
    print(f"users in extended social network: {len(connections) - 1}")

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])
    print(f"average length of social path: {total_social_paths/len(connections)}")

# how realistic is this, how random is it. Is this a good model of what sonething like facebook uses (obviously bigger)
# flaws in our random generation:  uniform probability, even distribution, everyone is connected to everyone
# according to google, FB have 2.4 billion active users that average 155 friends
# make use of other people's work expecially if that work is good and free