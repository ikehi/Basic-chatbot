import random
import tkinter as tk
from tkinter import ttk


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        # Configure style for widgets
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#b1b3b3", font=("Arial", 12))
        self.style.configure("TEntry", font=("Arial", 12))

        self.response_text = tk.StringVar()
        self.response_text.set("Chatbot: Hello! How can I assist you?")

        self.chat_frame = ttk.Frame(master, padding=10)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.response_label = ttk.Label(self.chat_frame, textvariable=self.response_text)
        self.response_label.pack(pady=10)

        self.user_label = ttk.Label(self.chat_frame, text="User:")
        self.user_label.pack()

        self.user_entry = ttk.Entry(self.chat_frame, width=40)
        self.user_entry.pack(pady=10)
        self.user_entry.bind("<Return>", self.get_response)

        self.exit_button = ttk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=10)

        self.responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you?": ["I'm good, thanks for asking.", "I'm doing well.", "All is well."],
    "what's your name?": ["I'm a chatbot.", "You can call me Chatbot.", "I don't have a name."],
    "tell me a joke": ["Why don't scientists trust atoms?\n\nBecause they make up everything!",
                       "What did one wall say to the other wall?\n\nI'll meet you at the corner!"],
    "tell me about yourself": ["I am an AI chatbot designed to assist users in various tasks.",
                               "I'm here to provide information and engage in conversation."],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "how old are you?": ["I don't have an age. I'm an AI.", "I'm timeless.", "Age is just a number for me."],
    "what's the weather like today?": ["I'm sorry, I don't have access to real-time weather information.",
                                       "You can check a weather website or app for the latest forecast."],
    "tell me a fun fact": ["A strawberry is not a berry, but a banana is.",
                           "Cows have best friends and get stressed when separated from them."],
    "what is the meaning of life?": ["The meaning of life is subjective and can vary for each individual.",
                                    "It's a philosophical question with no definitive answer."],
    "thank you": ["You're welcome!", "No problem.", "Glad I could help!"],
    "how can I contact you?": ["I'm a chatbot, so you can interact with me right here.",
                              "I don't have a personal contact information. What can I assist you with?"],
    "what's your favorite color?": ["I don't have the ability to see or perceive colors.",
                                    "Colors are a human perception, and I'm an AI without visual capabilities."],
    "can you help me with programming?": ["Of course! I can help you with programming questions.",
                                         "I have knowledge about various programming languages and concepts."],
    "what's the capital of France?": ["The capital of France is Paris.",
                                     "Paris is the capital and largest city of France."],
    "what's the largest country in the world?": ["The largest country in the world by land area is Russia.",
                                               "Russia holds the title for being the largest country."],
    "what's the square root of 16?": ["The square root of 16 is 4.",
                                      "The square root of 16 is a whole number, which is 4."],
    "tell me a famous quote": ["The only way to do great work is to love what you do. - Steve Jobs",
                               "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln"],
    "what's your favorite book?": ["As an AI, I don't have personal preferences like humans do.",
                                   "I don't read books, but I can recommend some popular ones if you're interested."],
    "do you like pizza?": ["I don't have taste buds, so I don't have preferences for food.",
                           "I don't eat, but many people enjoy pizza!"],
    "tell me a riddle": ["I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\n\nThe answer is an echo.",
                         "I have keys but no locks. I have space but no room. You can enter, but can't go outside. What am I?\n\nThe answer is a keyboard."],
    "what's the distance from the Earth to the Moon?": ["The average distance from the Earth to the Moon is about 238,855 miles (384,400 kilometers).",
                                                       "The average distance from the Earth to the Moon is roughly 384,400 kilometers (238,855 miles)."],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?",
                "I'm still learning, can you try again?"]
}


    def get_response(self, event):
        user_input = self.user_entry.get()
        self.user_entry.delete(0, tk.END)
        self.update_response(user_input)

    def update_response(self, user_input):
        response = self.generate_response(user_input)
        self.response_text.set("Chatbot: " + response)

    def generate_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return random.choice(self.responses[user_input])
        else:
            return random.choice(self.responses["default"])


def main():
    # Create the Tkinter GUI window
    root = tk.Tk()

    # Set window dimensions and position
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set window background color
    root.configure(bg="#f0f0f0")

    # Create an instance of the ChatbotGUI class
    chatbot_gui = ChatbotGUI(root)

    # Center the items inside the GUI
    root.pack_propagate(0)
    chatbot_gui.chat_frame.pack(fill=tk.BOTH, expand=True)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
