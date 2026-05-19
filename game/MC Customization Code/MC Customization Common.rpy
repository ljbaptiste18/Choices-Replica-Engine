init python:
    def get_zoom_by_body_type(mc):
        global devon_female;

        if mc == "Devon" and 'devon_female' in globals():
            if devon_female == True:
                return 0.7
            else:
                return 0.69

    def get_xoffset_by_body_type(mc):
        global devon_female;

        if mc == "Devon" and 'devon_female' in globals():
            if devon_female == True:
                return 10
            else:
                return 5

    def get_yoffset_by_body_type(mc):
        global devon_female;

        if mc == "Devon" and 'devon_female' in globals():
            if devon_female == True:
                return -15
            else:
                return 10
