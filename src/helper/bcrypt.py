from bcrypt import hashpw, checkpw, gensalt

def hash(password):
    return hashpw(password.encode('utf-8'), gensalt(rounds = 10))

def is_the_same(password, hashed_password):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
