# Using the random module to generate random numbers
#
import random

a = random.random() # random number between 0 and 1
print(f"random number: {a}")

b = random.randint(1, 10) # random integer between 1 and 10
print(f"random int: {b}")

c = random.randrange(1, 10, 2) # random integer between 1 and 10, but skipping even numbers
print(f"random randrange: {c}")

d = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # random element from a list
print(f"random choice: {d}")

e = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) # random sample of 3 elements from a list
print(f"random sample: {e}")

f = random.uniform(1.5, 5.5) # random float between 1.5 and 5.5
print(f"random float: {f}")

g = random.normalvariate(5.5, 1.5) # random float with mean 5.5 and standard deviation 1.5
print(f"random normalvariate: {g}")

# Picking random elements from a list
names = ["Mike","Cheryl", "Kiddo", "Elie", "Sally", "Jill", "Bobby", "Sue", "Jill", "Bobby", "Sue"]
chosen_one = random.choice(names)
print(f"Top guy: {chosen_one}")

chosen_sample = random.sample(names, 2)
print(f"Qualified: {chosen_sample}")

sorted_names = sorted(names)
print(f"Sorted: {sorted_names}")

# Shuffling a list
mixed_up = random.shuffle(names)
print(f"Shuffled: {names}")

# Using seed to set the random number generator
random.seed(1) # seed is 1 so the numbers will always be the same
print(f"Seeded: {random.random()}")
print(f"Seeded: {random.randint(1, 10)}")

random.seed(2) # seed is 12 so the numbers will always be the same
print(f"Seeded: {random.random()}")
print(f"Seeded: {random.randint(1, 10)}")

random.seed(1) # seed is 1 so the numbers will always be the same
print(f"Seeded: {random.random()}")
print(f"Seeded: {random.randint(1, 10)}")

# Note: random.seed() is not the same as random.seed(1)
# random.seed() is a function that sets the seed for the random number generator
# random.seed(1) is a statement that sets the seed for the random number generator

# seed is not recommended for production use, instead use secrets.token_hex()
# to generate a random string of hexadecimal digits
import secrets

# 1. Generate a random string of hexadecimal digits: token_hex()
secret_key = secrets.token_hex(30)
print(f"Secret key: {secret_key}")

# 2. Generate a random string of hexadecimal digits: token_urlsafe()
secret_key = secrets.token_urlsafe(30)
print(f"Secret key: {secret_key}")

# 3. Generate a random string of hexadecimal digits: token_bytes()
secret_key = secrets.token_bytes(30)
print(f"Secret key: {secret_key}")
