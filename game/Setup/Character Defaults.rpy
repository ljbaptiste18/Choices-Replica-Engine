init python:
    def get_character_defaults():
        return {
            #image name for call back , image you are manipulating, side on the screen 
            "LUIS":         ("luis", "right"),

            #ILITW
            "DEVON": (
                "devflip" if playing_as == capsDevon else "devon",
                "left"  if playing_as == capsDevon else "right",
            ), ##automatic switch for if playing_as or not playing_as
        }
