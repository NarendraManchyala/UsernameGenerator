import random as rd
def generate_username(choice, first_name="", last_name = "",nick_name=""):
    if choice == "1":
        usernames = [f"{first_name}.{last_name}".lower(),
                    f"{first_name}{last_name}123".lower(),
                    f"{first_name}_{last_name}".lower()]
    elif choice == "2":
        number = str(rd.randint(10,99))
        usernames = [f"{nick_name}_xx",f"Xx{nick_name}_Xx",f"{nick_name}_{number}"]
    elif choice == "3":
        words = ["cool","happy","lazy","boy","enjoy","blue","sun","cat","star","sky"]
        word1 = rd.choice(words)
        word2 = rd.choice(words)
        number = str(rd.randint(100,999))
        usernames = [f"{word1}.{word2}{number}",f"{word1}.{number}",f"{word2}.{number}",f"{word1}.{word2}"]
    elif choice == "4":
       usernames = [f"user_{rd.randint(1000,9999)}",f"anon_{rd.randint(100,999)}",
                    f"mystery{rd.randint(100,999)}"]
    else :
        return "Invalid choice"
    return usernames