# --- STEP 1: Security Check ---
password = input("Hello! Enter security code to wake me up: ")

if password == "python123":
    # --- STEP 2: Getting to know the User ---
    name = input("\nAccess Granted! I'm your AI. What's your name? ").strip().title()
    print(f"Nice to meet you, {name}! Let's chat.")

    # --- STEP 3: Real Person Emotion Logic ---
    mood = input(f"\nSo {name}, how are you feeling right now? ").lower()

    if "not" in mood:
        print("Oh no... I'm just a code, but I'm here for you. Stay strong! ❤️")
    elif "happy" in mood or "good" in mood or "fine" in mood:
        print("That's what I like to hear! Keep smiling! 😊")
    else:
        print("I hear you. Thanks for sharing that with me.")

    # --- STEP 4: Smart Number Game ---
    print("\nLet's test my brain power!") # \n adds a nice gap
    try:
        num = int(input("Give me any number, and I'll tell you its secret: "))
        
        if num % 2 == 0:
            print(f"The number {num} is EVEN. It's perfectly balanced!")
        else:
            print(f"The number {num} is ODD. It's unique, just like you!")
    except ValueError:
        print("Hey, that wasn't a number! You're trying to prank me, huh? 😂")

    # Final Goodbye with spacing
    print(f"\nAlright {name}, it was great talking to you. See you later!:)")

else:
    print("Wrong code! I only talk to authorized legends. Bye!")
