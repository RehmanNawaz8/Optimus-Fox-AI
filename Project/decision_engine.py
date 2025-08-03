

story_tree = {
    "start": {
        "prompt": "Do you want to explore the cave or return to the village?",
        "options": {
            "explore the cave": "cave",
            "return to the village": "village"
        }
    },
    "cave": {
        "prompt": "You enter a dark cave and hear a growl. Do you run or hide?",
        "options": {
            "run": "run_outcome",
            "hide": "hide_path"
        }
    },
    "hide_path": {
        "prompt": "You hide behind a rock. You see a torch on the ground. Do you grab it or stay hidden?",
        "options": {
            "grab it": "torch_path",
            "stay hidden": "monster_attack"
        }
    },
    "torch_path": {
        "prompt": "You grab the torch and scare the creature away. Do you move deeper into the cave or return?",
        "options": {
            "move deeper": "treasure_room",
            "return": "village"
        }
    },
    "treasure_room": {
        "prompt": "You find a treasure chest. Do you open it or leave it?",
        "options": {
            "open it": "open_treasure",
            "leave it": "leave_treasure"
        }
    },
    "open_treasure": {
        "prompt": "Inside is a magical stone. You gain wisdom and return a hero!",
        "options": {}
    },
    "leave_treasure": {
        "prompt": "You leave the chest untouched. A mysterious voice blesses your restraint. You exit safely.",
        "options": {}
    },
    "monster_attack": {
        "prompt": "The creature spots you and attacks. Game over.",
        "options": {}
    },
    "run_outcome": {
        "prompt": "You run and escape safely. You survived!",
        "options": {}
    },
    "village": {
        "prompt": "You return safely. Do you want to rest or speak to the elder?",
        "options": {
            "rest": "rest_outcome",
            "speak to the elder": "elder_path"
        }
    },
    "elder_path": {
        "prompt": "The elder offers you a map to a hidden temple. Do you accept or decline?",
        "options": {
            "accept": "temple_path",
            "decline": "decline_map"
        }
    },
    "temple_path": {
        "prompt": "You follow the map and arrive at a temple gate. Do you enter or wait outside?",
        "options": {
            "enter": "inside_temple",
            "wait outside": "missed_opportunity"
        }
    },
    "inside_temple": {
        "prompt": "Inside, you find ancient scrolls that give you knowledge. You return as a sage.",
        "options": {}
    },
    "missed_opportunity": {
        "prompt": "The temple disappears. You miss your chance and return home.",
        "options": {}
    },
    "decline_map": {
        "prompt": "You choose peace over adventure. You live a quiet life.",
        "options": {}
    },
    "rest_outcome": {
        "prompt": "You feel refreshed. The journey resumes tomorrow.",
        "options": {}
    }
}

def get_next_state(current_state, user_input):
    options = story_tree[current_state]["options"]
    for keyword in options:
        if keyword in user_input:
            return options[keyword]
    return None

