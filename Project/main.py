
from voice_input import get_voice_input
from text_to_speech import speak
from decision_engine import story_tree, get_next_state
from char_profils import characters

def run_chatbot(character_key="guide"):
    char = characters[character_key]
    speak(char["greeting"])
    
    state = "start"
    
    while state:
        prompt = story_tree[state]["prompt"]
        speak(prompt)

        if not story_tree[state]["options"]:
            break 

        user_input = get_voice_input()
        next_state = get_next_state(state, user_input)

        if next_state:
            state = next_state
        else:
            speak("I didn't catch that. Try again.")

if __name__ == "__main__":
    run_chatbot("guide")  
