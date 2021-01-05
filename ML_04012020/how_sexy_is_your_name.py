# A dictionary of scores for each letter
scores = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
              'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
              'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
              'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

# Python can access to each character in a string so try typing name[0] it will return the first character in your name
def sexy_name(name):
    # Initial score is 0
    score = 0
    # rannking
    rank = ""

    for i in range(0,len(name)):
        score = score + scores[name[i]]

    if(score <= 60):
        rank = 'NOT TOO SEXY'
    elif(score >= 61 and score <=300):
        rank = 'PRETTY SEXY'
    elif(score >= 301 and score <=599):
        rank = 'VERY SEXY'
    elif(score >= 600):
        rank = 'THE ULTIMATE SEXY'
    return rank

example_name = 'DONALD TRUMP'
# remove all spaces in string
example_name = example_name.replace(" ", "")
# uppercase everything in string
example_name = example_name.upper()
print(example_name)

print(sexy_name(example_name))


