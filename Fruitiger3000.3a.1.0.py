import tkinter as tk
import random

# Lists of fruits and vegetables with emojis
fruits_with_emojis = {
    "apple": "🍎", "banana": "🍌", "strawberry": "🍓", "raspberry": "🍇",
    "orange": "🍊", "grape": "🍇", "pineapple": "🍍", "kiwi": "🥝",
    "blueberry": "🫐", "blackberry": "🍇", "watermelon": "🍉",
    "peach": "🍑", "plum": "🍑", "mango": "🥭", "melon": "🍈",
    "cherry": "🍒", "coconut": "🥥"
}
vegetables_with_emojis = {
    "carrot": "🥕", "broccoli": "🥦", "cucumber": "🥒", "pepper": "🌶️", "tomato": "🍅",
    "spinach": "🥬", "celery": "🥬", "kale": "🥬", "lettuce": "🥬", "radish": "🌿",
    "onion": "🧅", "pea": "🌱", "zucchini": "🥒", "squash": "🎃", "beet": "🍠",
    "cabbage": "🥬", "pumpkin": "🎃"
}

# Combine fruits and vegetables for easy checking
all_items_with_emojis = {**fruits_with_emojis, **vegetables_with_emojis}

# Messages
sad_messages = [
    "Oh no, you're making me sad! 😢 I want to make a fruit salad, but you didn't enter any fruit! 🍇🍌",
    "Aww, where’s your fruit? Please, I want to make a delicious salad! 😞🍎🍊",
    "Hey, don't leave me hanging! 😞 Where's your fruit for the salad? 🍉🍇🍌",
    "Oh dear, I can't make a fruit salad without fruit! 🍇🍓🍊 Pretty please? 🌸"
]

one_fruit_messages = [
    "Just one? 🥹 It’s a cute little fruit salad! 🍒✨",
    "A single {fruit} salad? Adorable! 🍎💖💫",
    "Looks like a solo star! 🌟 One {fruit} to brighten the day! 🍌🌞",
    "Only one {fruit}? It’s small but mighty! 🍍💥 So cute! 🌼",
    "Just one, but it's special! 🌸 A {fruit} salad with extra love! 💖🍇"
]

happy_messages = [
    "Yay! You've got the best fruit salad ever! 🍓🍌🍇🍍✨",
    "Oh my goodness, what a fruity feast! 🍓🍊🍌 So yummy! 😋",
    "Look at that rainbow fruit salad! 🌈🍍🍒🍇 It's a masterpiece! 🎨",
    "Wowza! Your fruit salad is bursting with flavor! 🍎🍊🍓🍇💖",
    "Such a colorful and delicious fruit mix! 🍍🍒🍉🍊💫",
    "Who needs a fruit bowl when you’ve got this awesome fruit salad? 🍇🍍🍓🍊🌟",
    "This fruit salad is *so* cute! 🍓🍊🍇🍌 It's like a rainbow of happiness! 🌈✨",
    "Yum! A fruit salad that’s as sweet as you! 🍌🍓🍇🍊💖",
    "Wow, look at that amazing fruit combination! 🍎🍇🍊🍍 So fresh and tasty! 😍",
    "Your fruit salad is a party in a bowl! 🎉🍓🍌🍇🍊✨",
]

mixed_messages = [
    "Oh, a mix of fruits and veggies! 🍎🥕 Well, if you like it, I'm happy too! 😊✨",
    "Hmm, a little fruity, a little veggie? 🍍🥦 If it makes you smile, it makes me smile too! 🌸💚",
    "It’s a... unique combo! 🍉🥬 If this is what makes you happy, I'm all in! 😋🌈",
    "A bit of a mystery salad here! 🍊🌶️ But hey, if you're into it, I'm cheering for you! 🎉💖",
    "Well, it’s not exactly a fruit salad... 🍇🥒 But I'm here for your creativity! 🌟😊"
]

# Function to generate a response based on user input
def generate_response(input_text):
    if not input_text:
        return random.choice(sad_messages)
    elif len(input_text) == 1 and input_text[0] in fruits_with_emojis:
        fruit = input_text[0]
        return random.choice(one_fruit_messages).format(fruit=fruit)
    elif all(item in fruits_with_emojis for item in input_text):
        return random.choice(happy_messages)
    elif any(item in fruits_with_emojis for item in input_text) and any(item in vegetables_with_emojis for item in input_text):
        return random.choice(mixed_messages)
    elif any(item in vegetables_with_emojis for item in input_text):
        return f"Oh no! I'm Fruitiger3000, not the VeggieMaster3000! {vegetables_with_emojis[input_text[0]]} How about an apple instead? 🍏"
    else:
        return "Hmm, I don't think that goes in fruit salad! 🍍🍌 Try fruits only!!!"

# Function to display scrambled fruit and veggie emojis
def create_fruit_salad():
    # Get the items from the input field
    items = fruit_entry.get().lower().split()

    # Generate and display the response
    response = generate_response(items)
    result_label.config(text=response, font=("Comic Sans MS", 25), fg="#D5006D", bg="#FFB6C1", padx=10, pady=10)

    # Clear previous emojis
    for widget in image_frame.winfo_children():
        widget.destroy()

    # Show scrambled items with emojis
    scrambled_items = [all_items_with_emojis[item] for item in items if item in all_items_with_emojis]
    random.shuffle(scrambled_items)
    
    for emoji in scrambled_items:
        emoji_label = tk.Label(image_frame, text=emoji, font=("Comic Sans MS", 50), fg="#FF69B4", bg="#FFB6C1")
        emoji_label.pack(side="left", padx=10)  # Changed to pack the emojis horizontally

# Function for rainbow-shifting button text color
def cycle_button_text_color():
    rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]

    def cycle():
        current_color = rainbow_colors[cycle_button_text_color.index % len(rainbow_colors)]
        shuffle_button.config(fg=current_color)
        cycle_button_text_color.index += 1
        root.after(100, cycle)

    cycle_button_text_color.index = 0
    cycle()  # Start the color cycling

# Create main window
root = tk.Tk()
root.title("Fruitiger3000.3a.1.0")
root.config(bg="#FFB6C1")

# Header
input_label = tk.Label(root, text="🌟💖 What do you want in your fruit salad? 💖🌟", font=("Comic Sans MS", 25), fg="#D5006D", bg="#FFB6C1")
input_label.pack(pady=10)

# Entry field
fruit_entry = tk.Entry(root, width=40, font=("Comic Sans MS", 25))
fruit_entry.pack(pady=5)

# Button to create fruit salad
shuffle_button = tk.Button(root, text="Create Your Fruit Salad", command=create_fruit_salad, font=("Comic Sans MS", 25), fg="white")
shuffle_button.pack(pady=10)

# Start the rainbow text cycling
cycle_button_text_color()

# Result label
result_label = tk.Label(root, text="", font=("Comic Sans MS", 25), fg="#D5006D", bg="#FFB6C1", padx=10, pady=10)
result_label.pack(pady=20)

# Frame for emojis
image_frame = tk.Frame(root, bg="#FFB6C1")
image_frame.pack(pady=10)

root.mainloop()
