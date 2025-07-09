import random as rd
def generate_username(choice, first_name="", last_name = "",nick_name=""):
    if choice == "1":
        return "_".join([first_name,last_name])
    elif choice == "2":
        number = str(rd.randint(10,99))
        return "_".join([nick_name,number])
    elif choice == "3":
        words = ["cool","happy","lazy","boy","enjoy","blue","sun","cat","star","sky"]
        word1 = rd.choice(words)
        word2 = rd.choice(words)
        number = str(rd.randint(100,999))
        return "_".join([word1,word2,number])
    elif choice == "4":
        letters = "abcdefghijklmnopqrstuvwxyz1234567890"
        return "user_" + ''.join(rd.choice(letters) for _ in range (6))
    else :
        return "Invalid choice"