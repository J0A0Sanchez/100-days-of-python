def calculate_love_score(name1, name2):
    checker1 = "TRUE"
    checker2 = "LOVE"
    upper1 = name1.upper()
    upper2 = name2.upper()
    c1 = 0
    c2 = 0


    for letter in checker1:
        if letter in upper1:
            
            print(f"{letter} occurs {upper1.count(letter)} times")  
            c1 = c1 + upper1.count(letter)

        else:
            print(f"{letter} occurs 0 times")
    
    print(f"Total: {c1}")

    

    for letter in checker2:
        if letter in upper2:
           
            print(f"{letter} occurs {upper2.count(letter)} times")
            c2 = c2 + upper2.count(letter)

        else:
            print(f"{letter} occurs 0 times")    
        
    print(f"Total: {c2}")

    
    print(f"Love Score = {c1}{c2}")

    
calculate_love_score("Kanye West", "Kim Kardashian")

