geek = {"404": "Clueless.  From the web error message 404, meaning page not found.",
        "Googling": "Searching the Internet for background information on a person.",
        "Keyboard Plaque" : "The collection of debris found in computer keyboards.",
        "Link Rot" : "The process by which web page links become obsolete.",
        "Percussive Maintenance" : "The act of striking an electronic device to make it work.",
        "Uninstalled" : "Being fired.  Especially popular during the dot-bomb era."}

while True:
    choice= raw_input ("    GEEK TRANSLATOR\n\
    1 - Look Up a Geek Term\n\
    2 - Add a Geek Term\n\
    3 - Redefine a Geek Term\n\
    4 - Delete a Geek Term\n\
    5 - Quit\n\nChoice: ")
    if choice == "1":
        term= raw_input ("Enter your term: ")
        if geek.has_key(term):
            print geek[term]
            continue
        else:
            print ("Sorry, I dont know that term.")
            continue
    elif choice == "2":
        term= raw_input ("Enter your term: ")
        if geek.has_key(term):
            print "That term already exists!  Try redefining it."
            continue
        else:
            definition= raw_input("Please enter the definition: ")
            geek[term]=definition
            continue
            
    elif choice == '3':
        term= raw_input ("Enter your term: ")
        if geek.has_key(term):
            print geek[term]
            new_definition= raw_input ("Please enter your new definition: ")
            geek[term]=new_definition
            continue
        else:
            print "That term doesn't exist! Try adding it."
            continue
            
    elif choice == '4':
        term= raw_input ("Enter your term: ")
        if geek.has_key(term):
            del geek[term]
            print "Okay, I deleted the term."
            continue
        else:
            print "Sorry, I don't know that term."
            continue
        
    elif choice == '5':
        break
    else:
        print "That isn't an option"
        continue
    
            
            
            
            
    