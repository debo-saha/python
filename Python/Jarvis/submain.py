import os 


def say(text):
    os.system(f'say{text}')

if __name__=='__main__':
    say('I am')