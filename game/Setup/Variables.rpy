###personality points
init python:
    current_dlc_save_index = 0

    def toggle_fullscreen():
        if renpy.config.window == "window":
            renpy.config.window = "fullscreen"
        else:
            renpy.config.window = "window"

        renpy.restart_interaction()

#closet / animation controls
default closet_choice_expanded = True
default setup_complete = False
default playing_from_beginning = True
default closet = False
default dlc_customization = False
default PrevScreen = False
default item_selected = False
default hair_return = False
default AssetStored = None
default HairTypeStored = None
default sparkles = True
default JumpStore = None
default current_LI = None
default premium_choice = False
default premium_choice2 = False
default dialogue_size = "small"
default dialogue_size_old = "small"
default choose_LI_text = "I'll spend time with..."
default rowan_available = True

#other defaults
default selected_index = -1
default textbox_old = "nm"
default narrator_size = "nm"
default narrator_size_old = "nm"
default textbox_current = "nm"
default dialogue_old = "left"
default dialogue_current = "left"
default bottom_pad = 0
default in_pause = 0.15
default in_ease = 0.15
default bounce_in_ease = 0.15
default hide_ease = 0.15
default hide_ease_bounce = 0.15
default hide_pause = 0.1
default shrink_pause = 0.15
default last_hide_duration = 0.17
default bounce_zoom = 1.05
default side_pause = 0
default textbox_trans = None
default _show_trans = None
default _hide_trans = None
default _trans_list = None
default box_anim = "in"
default nvl_mode = None
default cleared = False
default center_voice = None
default who = None
default who_old = None
default current_chapter = 1
default npc_selection = False
default panning_on = True

#saving and other technical defaults
default loaded_from_chapter_end = False

###Devon Pronouns
default Devon = "Devon"
default Hunter = "Hunter"
default devon_she = "she"
default devon_her = "her"
default devon_her_pos = "her"
default devon_hers = "hers"
default devon_herself = "herself"
default devon_girlfriend = "girlfriend"
default devon_girl = "girl"
default devon_daughter = "daughter"
default devon_beautiful = "beautiful"
default devon_sister = "sister"
