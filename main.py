from jarvis import *

if __name__ == "__main__":
    i=0
    while True:        
        query = wakecommand().lower()
        if 'jarvis' in query:
            i=main(i)