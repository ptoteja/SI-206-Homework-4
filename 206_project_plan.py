## Your name: PRASHANT TOTEJA
## The option you've chosen: OPTION 2

# Put import statements you expect to need here!

import unittest
import itertools
import collections
import requests
import tweepy
#import twitter_info    --    twitter_info needed in folder in order for this line to run
import json
import sqlite3



#Create your caching set up:


#--------calling APIs---------

#Define a function Tweet() that takes an input string and returns a dictionary of 20+ tweets on that input


#Define a function called Twitterusers() that takes a user screen name that is found in any given tweet and returns a dictionary of all that user's info
#Hint: use api.get_user() to get the dictionary of user info

#Define a function called OMDB() that takes and input of a movie name and returns a dictionary of all of that movie's info from the OMDB API




#---------Movie Class------------

#Define a class Movie that will have the info representing any given movie


#Create the __init__ constructor here:


#Define a __str__ method within the movie class that returns a readable output for the user that gives us the name of the movie, by whom it was directed, and the IMDB rating it received


#Define a method within the movie class called listactors() that returns a list of actors that were in that movie


#Define a method within the movie class called numlanguages() that returns the number of languages that were in that movie



#---------------------------------


#Create 3 sql tables: Tweets, Users, Movies 
#Tweets will have the following columns: text, tweet_id(primary key), username(reference the user table), movie_search, num_fav, num_retweets

#Users will have the following columns: user_id(primary key), username, num_fav 

#Movies will have the following columns:  movie_id (primary key), title, director, num_languages, IMDB_rating, top_actor

#Load your info into the database and create two queries, one utilizing JOIN INNER, on your new table


#Find the frequencies of all the actors across all of the movie we iterate over. Save the dictionary in a variable called actor_frequency

 
#Did you find anything interesting? Create a quick summary about your findings and write it into a .txt file for your users!













# Write your test cases here.

class Sqltask(unittest.TestCase):
	def test_users1(self):
		conn = sqlite3.connect('finalproject_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Users');
		result = cur.fetchall()
		self.assertTrue(len(result) >= 2, "There should be 2 or more distinct users in the User table!!")
		conn.close()

	def test_users2(self):
		conn = sqlite3.connect('finalproject_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		result = cur.fetchall()
		self.assertTrue(len(result[0]) == 6, "Testing that there are 6 columns in the Tweets table")
		conn.close()

class Moretests(unittest.TestCase):
	def test_tweeter(self):
		self.assertTrue(type(tweeter('Tom Cruise')), type({"hi","bye"}), "Testing that the tweeter function returns a type dictionary of tweets")

	def test_twitterusers(self):
		self.assertTrue(type(twitterusers('Tome Cruise')), type({"hi","bye"}), "Testing that the twitterusers function returns a type dictionary of users")
	def test_Movie1(self):
		x = omdb('Titanic')
		mymovie = Movie(dict = x)
		self.assertTrue(type(mymovie.listactors()), type([]), "Testing that the listactors function returns a type list when called on a movie")
	def test_Movie2(self):
		x = omdb('Titanic')
		mymovie = Movie(dict = x)
		self.assertTrue(type(mymovie.numlanguages()), type(1), "Testing that the numlanguages function returns a type integer when called on a movie")
	def test_actor_frequency(self):
		self.assertEqual(type(actor_frequency),type({}),"Testing that mostcommon_actor across inputed movies is of type dictionary")


	def test_movielist(self):
		self.assertEqual(len(movielist) >= 3,"Testing that we will be running the ombd function on a list that contains 3 or more movie names")




## Remember to invoke all your tests...

if __name__ == "__main__":
	unittest.main(verbosity = 2)