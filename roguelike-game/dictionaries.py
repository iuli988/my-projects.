# PLAYER -------------------------

player = {
    'player_icon': '😋',
    'position_x': 4,
    'position_y': 3,
    'player_life': 1,
    'player_power': 1,
    'used_code': False,
    'wins': 0,
    'loss': 0,
    'levels': 1
    }

# BOARD -------------------------

BOARD = {
    'BOARD_1': {
        'BRICK': '🧱',
        'COLOR': 'green',
        'WIDTH': 70,
        'HEIGHT': 40,
        'NEXT_LEVEL': 'BOARD_2',
        'PREVIOUS_LEVEL': None,
        'GATES': {
            'GATE_UP': {
                'GATE_POSITION_Y': 15,
                'GATE_POSITION_X': 69},
            'GATE_DOWN': {
                'GATE_POSITION_Y': None,
                'GATE_POSITION_X': None}
                }
    },

    'BOARD_2': {
        'BRICK': '🧱',
        'COLOR': 'yellow',
        'WIDTH': 70,
        'HEIGHT': 40,
        'GATE_POSITION_X': 0,
        'GATE_POSITION_Y': 10,
        'NEXT_LEVEL': 'BOARD_3',
        'PREVIOUS_LEVEL': 'BOARD_1',
        'GATES': {
            'GATE_UP': {
                'GATE_POSITION_Y': 15,
                'GATE_POSITION_X': 69},
            'GATE_DOWN': {
                'GATE_POSITION_Y': 15,
                'GATE_POSITION_X': 0}
        }
    },

    'BOARD_3': {
        'BRICK': '🧱',
        'COLOR': 'yellow',
        'WIDTH': 70,
        'HEIGHT': 40,
        'GATE_POSITION_X': 60,
        'GATE_POSITION_Y': 0,
        'NEXT_LEVEL': 'WIN',
        'PREVIOUS_LEVEL': 'BOARD_2',
        'GATES': {
            'GATE_UP': {
                'GATE_POSITION_Y': 15,
                'GATE_POSITION_X': 69},
            'GATE_DOWN': {
                'GATE_POSITION_Y': 15,
                'GATE_POSITION_X': 0
                }
            }
        }
    }


# ITEMS -------------------------

items = {
        'Chocolate': {
            'type': 'ingridient',
            'item_icon': '🍫',
            'position_x': 4,
            'position_y': 4,
            'number': 1,
            'board': 1,
            'added_power': 1,
            'added_protection': 0
            },
        'Watermelon': {
            'type': 'ingridient',
            'item_icon': '🍉',
            'position_x': 2,
            'position_y': 8,
            'number': 1,
            'board': 3,
            'added_power': 0,
            'added_protection': 1
            },
        'Pot of Food': {
            'type': 'ingridient',
            'item_icon': '🍲',
            'position_x': 5,
            'position_y': 5,
            'number': 1,
            'board': 3,
            'added_power': 0,
            'added_protection': 10
            },
        'gate': {
            'type': 'ingridient',
            'item_icon': '⛩️',
            'position_x': 9,
            'position_y': 8,
            'number': 1,
            'board': 1,
            'added_power': 0,
            'added_protection': 10
            },
        'Wine Glass': {
            'type': 'ingridient',
            'item_icon': '🍷',
            'position_x': 6,
            'position_y': 7,
            'number': 2,
            'board': 2,
            'added_power': 2,
            'added_protection': 0
            },
        'Syringe': {
            'type': 'ingridient',
            'item_icon': '💉',
            'position_x': 4,
            'position_y': 3,
            'number': 2,
            'board': 2,
            'added_power': 5,
            'added_protection': 0
            },
        'Sword': {
            'type': 'ingridient',
            'item_icon': '🗡️',
            'position_x': 3,
            'position_y': 3,
            'number': 2,
            'board': 2,
            'added_power': 7,
            'added_protection': 0
            },
        'Bow': {
            'type': 'ingridient',
            'item_icon': '🏹',
            'position_x': 4,
            'position_y': 6,
            'number': 3,
            'board': 1,
            'added_power': 12,
            'added_protection': 0
            },
        'Armor': {
            'type': 'ingridient',
            'item_icon': '🛡️',
            'position_x': 4,
            'position_y': 7,
            'number': 2,
            'board': 3,
            'added_power': 0,
            'added_protection': 30
            },
        'Tower': {
            'type': 'ingridient',
            'item_icon': '🗼',
            'position_x': 5,
            'position_y': 2,
            'number': 2,
            'board': 1,
            'added_power': 7,
            'added_protection': 0
            },
        'gate_2': {
            'type': 'ingridient',
            'item_icon': '🌁',
            'position_x': 9,
            'position_y': 8,
            'number': 1,
            'board': 2,
            'added_power': 0,
            'added_protection': 10
            },
        'gate_3' : {
            'type': 'ingridient',
            'item_icon': '🚪',
            'position_x': 9,
            'position_y': 8,
            'number': 1,
            'board': 3,
            'added_power': 0,
            'added_protection': 10
            }
    }


# OTHER CHARACTERS --------------

others = {
    'other': {
        'other_type': "quiz",
        'other_name': "HATZ.UL SUPREM",
        'other_icon': "👨🏼",
        'position_x': 5,
        'position_y': 5,
        'step': 1,
        'other_health': 3,
        'goal_quiz': "Syringe",
        'questions':   [["What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n", "b", False],
                        ["Which river passes through Bucharest?\n(a) Tisa\n(b) Dâmbovița\n(c) Danube\n", "c", False],
                        ["What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n", "c", False],
                        ["What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n", "b", False],
                        ["Which European country shares a border with Brazil?\n(a) Germany\n(b) Belgium\n(c) France\n", "b", False]],
        'width': 1,
        'other_power': 3,
        'board': 1
        },
    'boss': {
        'other_type': "enemy",
        'other_name': "Boss",
        'other_icon': "",
        'position_x': 30,
        'position_y': 15,
        'step': 1,
        'other_health': 3,
        'goal_quiz': "winning",
        'questions': [],
        'width': 5,
        'other_power': 1,
        'board': 3
        }
    }


# INVENTORY ---------------------

inventory = {}


# CODES ---------------------

codes = {
    "kill_others": "killemall",
    "last_board": "desparate",
    "extra_lives": "showmustgoon"
}
