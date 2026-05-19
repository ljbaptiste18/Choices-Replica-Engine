init python:
    #Devon

    def NextDevonRace():
        global devon_female, devon_race;

        if devon_female:
            if devon_race < 4:
                devon_race += 1
            else:
                devon_race = 1
        else:
            if devon_race < 8:
                devon_race += 1
            else:
                devon_race = 5

    def PrevDevonRace():
        global devon_female, devon_race;

        if devon_female:
            if devon_race > 1:
                devon_race -= 1
            else:
                devon_race = 4
        else:
            if devon_race > 5:
                devon_race -= 1
            else:
                devon_race = 8

    def NextDevonHair():
        global devon_hair;

        if devon_hair < 13:
            devon_hair += 1
        else:
            devon_hair = 1

    def PrevDevonHair():
        global devon_hair;

        if devon_hair > 1:
            devon_hair -= 1
        else:
            devon_hair = 13

    def NextDevonOutfit():
        global devon_female, devon_outfit;

        if devon_outfit < 6:
            devon_outfit += 1
        else:
            devon_outfit = 1

    def PrevDevonOutfit():
        global devon_female, devon_outfit;

        if devon_outfit > 1:
            devon_outfit -= 1
        else:
            devon_outfit = 6

    def NextLI():
        global current_LI, li_message
        order = ["Luis", "Devon"]
        messages = {
            "Luis": luis_message,
            "Devon": mc_message
        }
        available_flags = {
            "Luis": luis_available,
            "Devon": mc_available
        }
        available = [li for li in order if available_flags[li]]
        current_index = available.index(current_LI)
        next_li = available[(current_index + 1) % len(available)]
        current_LI = next_li
        li_message = messages[next_li]

    def PrevLI():
        global current_LI, li_message
        order = ["Luis", "Devon"] #you can always add more!
        messages = {
            "Luis": luis_message,
            "Devon": mc_message
        }
        available_flags = {
            "Luis": luis_available,
            "Devon": mc_available
        }
        available = [li for li in order if available_flags[li]]
        current_index = available.index(current_LI)
        next_li = available[(current_index - 1) % len(available)]
        current_LI = next_li
        li_message = messages[next_li]

#####SCREEN BOTTOM OPTION TABS NUMBER
    def get_devon_race():
        if devon_female:
            return [ 1, 2, 3, 4 ]
        else:
            return [ 5, 6, 7, 8 ]

    def get_devon_outfit_options():
        return [ 1, 2, 3, 4, 5, 6 ]

    def get_devon_hair_options():
        return [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]

#####HIGHLIGHT CURRENT OPTION TAB
    def devon_race_selected():
        return devon_race

    def devon_hair_selected():
        return devon_hair

    def devon_outfit_selected():
        return devon_outfit

    def get_available_LIs():
        options = []

        if luis_available:
            options.append("Luis")
        if mc_available:
            options.append("Devon") #you can add as many as you like

        return options
