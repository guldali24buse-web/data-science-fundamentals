#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:36:29 2026

@author: buseguldalii
"""

#“Data! Data! Data!” he cried impatiently. “I can’t make bricks without clay.”
#Social Network Example 
#Finding Key Connectors

users = [
  { "id": 0,"name": "Hero"},
  { "id": 1,"name": "Dunn"},
  { "id": 2,"name": "Sue"}, 
  { "id": 3,"name": "Chi"}, 
  { "id": 4,"name": "Thor"}, 
  { "id": 5,"name": "Clive"},
  { "id": 6,"name": "Hicks" },
  { "id": 7,"name": "Devin" },
  { "id": 8,"name": "Kate" },
  { "id": 9,"name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#arama yapmanın (lookup) yavaş ve verimsiz olmasıdır.
#let’s create a dict where the keys are user ids and the values are lists of friend ids

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i,j in friendship_pairs:
    friendships[i].append(j) # Add j as a friend of user i
    friendships[j].append(i) # Add j as a friend of user i
    
# we find the total number of connections

def number_of_friends(user) :
    """How many friends does _user_ have"""
    user_id=user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids) #fonksiyonun ürettiği değeri hafızada tutar.

total_connections = sum(number_of_friends(user) for user in users)

#And then we just divide by the number of users:

num_users = len(users) # length of the users list
avg_connections = total_connections / num_users 

# Create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse =True)

#reverse=True büyükten küçüğe
#key=lambda id_and_friends: id_and_friends[1] ikinci elemana bakar 
#network metric degree centrality

#users might know the friends of their friends
#suggestor for making more friends
#kiminle kaç ortak noktamız olduğunu sayan bir yapı

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(foaf_id for friend_id in friendships[user_id]   # For each of my friends,
                   for foaf_id in friendships[friend_id]    # find their friends
                   if foaf_id != user_id                    # who aren't me
                   and foaf_id not in friendships[user_id]  # and aren't my friends.
                   )

print(friends_of_friends(users[3]))  # Counter({0: 2, 5: 1})

#MACHING ALGORİTHM
#meeting users with similar interests.
#list of pairs (user_id, interest):

interests = [(0,"Hadoop"), (0,"Big Data"), (0,"HBase"), 
             (0,"Java"),(0,"Spark"), (0,"Storm"), (0,"Cassandra"),
             (1,"NoSQL"), (1,"MongoDB"), (1,"Cassandra"), (1,"HBase"),
             (1,"Postgres"), (2,"Python"), (2,"scikit-learn"), (2,"scipy"),
             (2,"numpy"), (2,"statsmodels"), (2,"pandas"), (3,"R"), (3,"Python"),
             (3,"statistics"), (3,"regression"), (3,"probability"),(4,"machine learning"), 
             (4,"regression"), (4,"decision trees"),(4,"libsvm"), 
             (5,"Python"), (5,"R"), (5,"Java"), (5,"C++"),(5,"Haskell"),
             (5,"programming languages"), (6,"statistics"),(6,"probability"),
             (6,"mathematics"), (6,"theory"),(7,"machine learning"), (7,"scikit-learn"), 
             (7,"Mahout"),(7,"neural networks"), (8,"neural networks"), (8,"deep learning"),
             (8,"Big Data"), (8,"artificial intelligence"), (9,"Hadoop"),(9,"Java"), 
             (9,"MapReduce"), (9,"Big Data")
             ]
'''
#function that finds users with a certain interest
def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return[user_id
           for user_id , user_interest in interests 
           if user_interest == target_interest]
'''

from collections import defaultdict

#Keys are interests , values are list of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#Keys are user_ids,values are list of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

#Iterate over the user’s interests.
#For each interest, iterate over the other users with that interest.
#Keep count of how many times we see each other user.

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
        )


#find the most popular interests / word frequency
words_and_counts = Counter(word for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
        










