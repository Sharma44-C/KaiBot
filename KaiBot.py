import random

# Chatbot variables
name = "Kai"
mood = ["happy", "sad", "angry"]
greetings = ["Hi! How can I help you?", "Hello! What's up?", "Hey! What's on your mind?", "Wassup! How may i help?"]
goodbyes = ["Goodbye! Have a great day!", "See you later!", "Bye for now!"]
thanks = ["You're welcome!", "No problem!", "It was my pleasure to help!"]
motivational_phrases = ["You can do it!", "Don't give up!", "Keep going!"]
jokes = ["Why did the computer go to the doctor? It had a virus!", "What did one traffic light say to another? Don't look at me, I'm changing!"]
colors = ["Blue", "Green", "Gold", "Black", "Pink", "White"]
hobies = ["gaming", "coding", "sports", "TV shows","anime", "music"]

# Anime knowledge
anime = {
    "naruto shippuden": ["Naruto Uzumaki", "Sasuke Uchiha", "Kakashi Hatake", "The Will of Fire"],
    "dbz": ["Goku", "Vegeta", "Dragon Balls"],
    "dbs": ["Goku", "Vegeta", "Jiren"],
    "atlab": ["Aang", "Katara", "Sokka", "Avatar State"]
    }

# Minecraft knowledge
minecraft = {
    "blocks": ["Grass", "Dirt", "Stone", "Diamond"],
    "items": ["Sword", "Pickaxe", "Axe", "Shovel"],
    "mobs": ["Creeper", "Zombie", "Skeleton", "Enderman"]
}

# School subjects
school = {
    "math": ["Algebra", "Geometry", "Calculus", "Statistics"],
    "science": ["Biology", "Chemistry", "Physics", "Earth Science"],
    "english": ["Reading", "Writing", "Grammar", "Literature"],
    "history": ["World History", "US History", "Ancient Civilizations", "Medieval Times"]
}

# Introduction
print(f"{name}: Hello! I'm {name}.")
print(f"Here is what i can provide:")
print(f" -info about minecraft")
print(f" -tell you some jokes")
print(f" -motivate you")
print(f" -info about anime")
print(f" -info about school")
print(f" -tell you my favourite color")
print(f" -tell you my hobies")
print(f" -tell you who my owner is")

while True:
    # Get user input
    user_input = input("You: ")

    # Check user input
    if user_input.lower() in ["how are you", "how are you doing", "hud"]:
        print(f"{name}: I'm feeling {random.choice(mood)} thanks for asking.")
    elif user_input.lower() in ["hi", "hello", "hey", "wassup", "yo"]:
        print(f"{name}: {random.choice(greetings)}")
        print(f"{name}: Here is what i can provide:")
        print(f" -info about minecraft")
        print(f" -tell you some jokes")
        print(f" -motivate you")
        print(f" -info about anime")
        print(f" -info about school")
        print(f" -tell you my favourite color")
        print(f" -tell you my hobies")
        print(f" -tell you who my owner is")
    elif user_input.lower() in ["what do you like to do", "what are your hobies", "what do you enjoy", "tell me ur hobies", "tell me your hobies"]:
        print(f"{name}: i enjoy {random.choice(hobies)}")
    elif "bye" in user_input.lower():
        print(f"{name}: {random.choice(goodbyes)}")
        break
    elif "thank" in user_input.lower():
        print(f"{name}: {random.choice(thanks)}")
    elif user_input.lower() in ["motivate", "motivation"]:
        print(f"{name}: {random.choice(motivational_phrases)}")
    elif "joke" in user_input.lower():
        print(f"{name}: {random.choice(jokes)}")
    elif "anime" in user_input.lower():
        anime_choice = random.choice(list(anime.keys()))
        print(f"{name}: Did you know that {random.choice(anime[anime_choice])} is a main character in {anime_choice}?")
    elif "minecraft" in user_input.lower():
        minecraft_choice = random.choice(list(minecraft.keys()))
        print(f"{name}: In Minecraft, {random.choice(minecraft[minecraft_choice])} is a type of {minecraft_choice}.")
    elif user_input.lower() in ["who's ur owner", "who created you", "who made you", "who's ur boss"]:
        print(f"{name}: I was created by Sharma Zambara he used coding skills he's my owner and my boss .")
    elif "school" in user_input.lower():
        school_choice = random.choice(list(school.keys()))
        print(f"{name}: In {school_choice} class, you might learn about {random.choice(school[school_choice])}.")
    elif "color" in user_input.lower():
            print(f"{name}: My favourite color is {random.choice(colors)}")            
    else:
        print(f"{name}: I didn't understand that. Please try again!")
        