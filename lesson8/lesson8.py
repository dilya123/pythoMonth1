import datetime

today = datetime.date.today()

file = open("score.txt", "w")  # write permission

file.write("Hello, World!\n")
file.write("I love Python!")

file.close()
