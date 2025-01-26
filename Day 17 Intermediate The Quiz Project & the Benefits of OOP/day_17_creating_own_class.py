# Day 17 - Creating Classes Example
# This module demonstrates basic class creation and usage in Python

#--------------------
# Basic Class Example
#--------------------

# Simple class definition (commented out for reference)
# class User:
#     pass
#
# # Manual attribute assignment
# user1 = User()
# user1.id = "001"
# user1.username = "angela"
#
# print(user1.username)

#--------------------
# Improved Class
#--------------------

class User:
    """
    A class representing a social media user.
    
    Attributes:
        id (str): User's unique identifier
        username (str): User's display name
        followers (int): Number of followers
        following (int): Number of users being followed
    """
    
    def __init__(self, user_id, username):
        """
        Initialize a new User.
        
        Args:
            user_id (str): User's unique identifier
            username (str): User's display name
        """
        self.id = user_id
        self.username = username
        self.followers = 0  # Start with 0 followers
        self.following = 0  # Start with 0 following

    def follow(self, user):
        """
        Follow another user.
        
        Args:
            user (User): The user to follow
        """
        user.followers += 1  # Increase their followers
        self.following += 1  # Increase our following

#--------------------
# Usage Example
#--------------------

# Create users
user1 = User("001", "angela")
user2 = User("002", "jack")

# Display user info
print(user1.id, user1.username)

# Test follow functionality
user1.follow(user2)
print(f"User1 followers: {user1.followers}")
print(f"User1 following: {user1.following}")
print(f"User2 followers: {user2.followers}")
print(f"User2 following: {user2.following}")
