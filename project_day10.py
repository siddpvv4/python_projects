import random

# Lists of story elements
names = ["Arjun", "Maya", "A mysterious hacker", "An old wizard", "A brave astronaut"]
places = ["in a dark forest", "on Mars", "inside a secret lab", "in an abandoned school", "under the ocean"]
problems = ["found a hidden portal", "accidentally activated a robot army", 
            "discovered a magical sword", "received a strange message", 
            "opened a forbidden book"]
actions = ["saved the world", "unlocked a hidden power", 
           "traveled through time", "defeated an evil villain", 
           "changed history forever"]

while True:
    print("\n📖 Generating your story...\n")

    name = random.choice(names)
    place = random.choice(places)
    problem = random.choice(problems)
    action = random.choice(actions)

    story = f"One day, {name} was {place}. Suddenly, they {problem}. In the end, they {action}!"

    print(story)

    again = input("\nDo you want another story? (yes/no): ").lower()
    if again != "yes":
        print("✨ Thanks for using the Story Generator!")
        break