# A simple script to generate humorous, random fake news headlines.

import random 

def generate_headline():
    subjects = ["ShahRukh Khan", "Salman Khan", "Akshay Kumar ", "Hritik Roshan", "Deepika Padukone", "Priyanka Chopra"]
    
    
    actions = ["riding a buffalo", "riding a horse", "scolding a dog", 
               "doing a prank", "practicing kung fu", "eating an ant"]
    
    locations = ["at the Red Fort", "at the India Gate", "at the airport", 
                 "at a local market", "on a film set", "in their hometown"]

    subject = random.choice(subjects)
    action = random.choice(actions)
    location = random.choice(locations)
    
   
    headline = f"{subject} caught {action} {location}!"
    return headline


if __name__ == "__main__":
    print("Welcome to the Fake News Generator!")
    print("Here is your headline:\n")
    print(generate_headline())
    