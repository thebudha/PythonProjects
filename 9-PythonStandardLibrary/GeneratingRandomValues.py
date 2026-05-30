import random
import string

print (random.random()) #Returns a random float between 0.0 and 1.0
print (random.randint(1, 10)) #Returns a random integer between 1 and 10 (inclusive)
print (random.choice(['apple', 'banana', 'cherry'])) #Returns a random element from the list
print (random.sample([1, 2, 3, 4, 5], 3)) #Returns a list of 3 unique random elements from the list
print (random.shuffle([1, 2, 3, 4, 5])) #Shuffles the list in place and returns None
print (random.uniform(1.0, 10.0)) #Returns a random float between 1.0 and 10.0
print (random.seed(42)) #Sets the seed for the random number generator to ensure reproducibility
print (random.choices([1,2,3,4,5], k=3)) #Returns a list of 3 random elements from the list, allowing duplicates
print (random.choices("abcdefghijllmnop!@#$%^&*()", k=20)) #Returns a list of 20 random characters from the string, allowing duplicates 
print ("".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=20))) #Returns a string of 20 random characters from the string, allowing duplicates 