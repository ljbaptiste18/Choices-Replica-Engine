init python:

    def ArrowsMessage():
        return "Tap the left and right arrows to see \nother options!"

    def RaceDevon():
        if devon_race == 1 or devon_race == 5:
            return "FACE 1"
        elif devon_race == 2 or devon_race == 6:
            return "FACE 2"
        elif devon_race == 3 or devon_race == 7:
            return "FACE 3"
        else:
            return "FACE 4"

    def DevonHair():
        if devon_hair == 1:
            return "close shave"
        elif devon_hair == 2:
            return "curl power"
        elif devon_hair == 3:
            return "pixie perfect"
        elif devon_hair == 4:
            return "pretty in pastel"
        elif devon_hair == 5:
            return "makin' waves"
        elif devon_hair == 6:
            return "lavender love"
        elif devon_hair == 7:
            return "faded"
        elif devon_hair == 8:
            return "close shave"
        elif devon_hair == 9:
            return "classic cut"
        elif devon_hair == 10:
            return "makin' waves"
        elif devon_hair == 11:
            return "lilac value"
        elif devon_hair == 12:
            return "scalped Rowan"
        else:
            return "irresistible"

    def DevonHairDescription():
        if devon_hair == 1:
            return "Long and short, best of both worlds."
        elif devon_hair == 2:
            return "Long and curly."
        elif devon_hair == 3:
            return "Short and edgy."
        elif devon_hair == 4:
            return "Turn heads with this vibrant and \nunique hair color."
        elif devon_hair == 5:
            return "Classic brunette waves."
        elif devon_hair == 6:
            return "Turn heads with this vibrant and \nunique hair color."
        elif devon_hair == 7:
            return "Curly and short."
        elif devon_hair == 8:
            return "Long and short, best of both worlds."
        elif devon_hair == 9:
            return "Traditional and clean."
        elif devon_hair == 10:
            return "Long and casual."
        elif devon_hair == 11:
            return "The color suits you."
        elif devon_hair == 12:
            return "Hey, didn't this hair used to be blue?"
        else:
            return "All the baddies pulling the most bitches \nhave this wig."

    def DevonOutfit():
        global devon_female, devon_outfit;

        if devon_female:
            if devon_outfit == 1:
                return "paint it black"
            elif devon_outfit == 2:
                return "rock 'n roll"
            elif devon_outfit == 3:
                return "da bomb"
            elif devon_outfit == 4:
                return "sweater weather"
            elif devon_outfit == 5:
                return "leisure wear"
            else:
                return "a vision in leather"
        else:
            if devon_outfit == 1:
                return "paint it black"
            elif devon_outfit == 2:
                return "popped collar"
            elif devon_outfit == 3:
                return "who's got spirit"
            elif devon_outfit == 4:
                return "sweater weather"
            elif devon_outfit == 5:
                return "rock 'n roll"
            else:
                return "a vision in leather"

    def DevonOutfitDescription():
        global devon_female, devon_outfit;

        if devon_female:
            if devon_outfit == 1:
                return "Nothing says monster hunter like \nfishnets and skulls."
            elif devon_outfit == 2:
                return "Rage against the machine and look \ngood while you do it."
            elif devon_outfit == 3:
                return "Make a bold impression in this trendy \nand sleek ensemble."
            elif devon_outfit == 4:
                return "Don't sweat it in this casual and \ncomfortable look."
            elif devon_outfit == 5:
                return "Feel comfy, look good, and get shit \ndone. Win win win."
            else:
                return "Cassandra had the gift of prophecy. \nYou have the gift of slay."
        else:
            if devon_outfit == 1:
                return "Nothing says monster hunter like \nfishnets and skulls."
            elif devon_outfit == 2:
                return "Show off your preppy side in this classy \npolo and slacks."
            elif devon_outfit == 3:
                return "Show your Westchester pride in this \nslick letterman jacket."
            elif devon_outfit == 4:
                return "Don't sweat it in this casual and \ncomfortable look."
            elif devon_outfit == 5:
                return "Rage against the machine and look \ngood while you do it."
            else:
                return "Cassandra had the gift of prophecy. \nYou have the gift of slay."
