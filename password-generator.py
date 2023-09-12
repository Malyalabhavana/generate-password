import random

lower = "abcdefghijklmnoprqstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(string, length))

print("Your new Password Is:" + password)
