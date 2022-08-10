print("")
course = 'python for beginners'
print(course.upper())
print(course)
print("")
work = 'python for intermediates'
print(work.find('y'))
print(work.upper())
print("")
play = 'PYTHON FOR ADVANCED'
print(play.find('A')) #.find will only find the first occurence
print(play.count('A')) #.count is for the total occurences of the letter or word
print(play.lower())
print("")
dull = 'python is cool'
print(dull)
print(dull.replace('cool','average')) #.replace - self explanatory
print("")
boy = 'Python for beginners'
print('Python' in boy)
print("")
print('python' in course, 'intermediates' in work, 'ADVANCED' in play, 'cool' in dull, 'for' in boy)
print("")