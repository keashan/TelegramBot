from datetime import datetime


def sample_response(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "sup"):
        return "Hey! How's it going?"
    if user_message in ("who are you", "who are you?"):
        return "I am a KTKTools Sample bot"
    if user_message in ("time", "time?"):
        return "It's " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return "I don't understand you."
