from Ipython.display import display, clear_output
import ipywidgets as widgets

responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm a chatbot, so i don't have feelings, but thanks for asking!",
    "what is your name?": "I am a simple chatbot in python",
    "bye": "Goodbye! Have a great day!"
}

def get_response():
    user_input = user_input.lower()
    return response.get(user_input, "Sorry, I don't understand that.")

input_box = widgets.Output()

display(input_box,  output_box)

def on_submit(change):
    user_input = change.value
    with output_box:
        clear_output()
        response = get_response(user_input)
        print(f"You: {user_input}")
        print(f"Chatbot: {response}")
    input_box.value = ''

input_box.on_submit(on_submit)