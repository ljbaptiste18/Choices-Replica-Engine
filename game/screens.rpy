################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/right.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/left.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style screen_overlay is default

style screen_overlay:
    mouse "transparent"

default is_fullscreen = False

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

label bg(bg, transition=fade):
    $ old_tag = store.last_shown_tag
    $ old_side = store.last_shown_side
    if store.last_shown_tag:
        if old_side == "left":
            $ hl(old_tag)
        else:
            $ hr(old_tag)
        pause 0.15
    scene expression bg
    with transition
    $ store.last_shown_tag = None
    $ store.last_shown_side = None
    $ store.last_shown_expression = None
    $ store.last_named_speaker = None
    $ store.who_old = "NEW"
    return

init python: #reset who on new scene
    def _reset_who_old_on_scene(layer):
        store.who_old = "NEW"
        store.last_shown_tag = None
        store.last_shown_side = None
        store.last_shown_expression = None

    config.scene_callbacks.append(_reset_who_old_on_scene)

    def anim(transform): #skip textbox transitions
        if renpy.is_skipping() or renpy.roll_forward_info() is not None:
            return None
        return transform

screen say(who, what):
    style_prefix "say"
    default show_text = False

    $ speaker_id = "narrator" if who is None else ("center_voice" if who == center_voice else who)
    $ speaker_changed = (speaker_id != who_old)
    $ dialogue_size_old = store.dialogue_size
    $ box_anim_old = store.box_anim  # snapshot before recalculating
    $ previous_hide_duration = store.hide_pause + store.hide_ease_bounce + store.hide_ease
    $ store.hide_pause = 0.1

    on "replace" action [
        SetVariable("who_old", speaker_id),
        SetVariable("dialogue_old", dialogue_current),
        SetVariable("store.dialogue_size_old", dialogue_size),
        SetVariable("store.narrator_size_old", narrator_size)
    ]
    on "hide" action [
        SetVariable("who_old", speaker_id),
        SetVariable("dialogue_old", dialogue_current),
        SetVariable("dialogue_size_old", dialogue_size),
        SetVariable("store.narrator_size_old", narrator_size)
    ]

    # change who_old on dismiss
    if renpy.get_screen("choice"):
        key "dismiss" action SetVariable("who_old", who)
        key "dismiss" action SetVariable("who_old", speaker_id)
    else:
        key "dismiss" action [ SetVariable("who_old", who), Return() ]
        key "dismiss" action [ SetVariable("who_old", speaker_id), Return() ]

    #for timeout labels
    $ show_timeout_tag = (timeout_label is not None or timeout_short_label is not None) and renpy.get_screen("choice")

    if who is None or who == center_voice:
        $ dialogue_current = dialogue_old

        $ clean = renpy.filter_text_tags(what, allow=['b','i','u','font','size'])
        $ test_text = Text(clean, style="say_dialogue")
        $ text_width, text_height = renpy.render(test_text, 600, 1360, 0, 0).get_size()
        $ estimated_lines = int(text_height / 43)

        $ narrator_size_old_snap = store.narrator_size_old

        if estimated_lines <= 2:
            $ narrator_size = "ns"
        elif estimated_lines <= 3:
            $ narrator_size = "nm"
        elif estimated_lines <= 5:
            $ narrator_size = "nl"
        else:
            $ narrator_size = "nxl"

        $ size_order = ["ns", "nm", "nl", "nxl"]
        $ old_rank = size_order.index(narrator_size_old_snap) if narrator_size_old_snap in size_order else -1
        $ new_rank = size_order.index(narrator_size)
        $ box_anim = "in" if speaker_changed else ("grow" if new_rank > old_rank else ("shrink" if new_rank < old_rank else "same"))

        $ store.side_pause = 0.12
        $ store.prev_h_ease = store.hide_ease  # reads OLD hide_ease here
        $ prev_hide_ease = store.hide_ease

        $ store.hide_ease_bounce = 0.05
        if narrator_size == "ns":
            $ store.in_ease = 0.12
            $ store.hide_ease = 0.12
        elif narrator_size == "nm":
            $ store.in_ease = 0.12
            $ store.hide_ease = 0.12
        elif narrator_size == "nl":
            $ store.in_ease = 0.17
            $ store.hide_ease = 0.12
        else:
            $ store.in_ease = 0.24
            $ store.hide_ease = 0.24

        if box_anim == "in":
            $ store._nar_trans_list = [textbox_in(i_pause=0.05, i_ease=store.in_ease), textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans_list = [nar_tag_in(i_pause=0.05, i_ease=store.in_ease), nametag_out(h_ease=store.hide_ease)]
        elif box_anim == "grow":
            $ store._nar_trans_list = [textbox_grow(i_ease=store.in_ease), textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans_list = [nametag_out(h_ease=store.hide_ease)]
        elif box_anim == "shrink":
            $ store._nar_trans_list = [textbox_shrink, textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans_list = [nametag_out(h_ease=store.hide_ease)]
        else:
            $ store._nar_trans_list = [textbox_same, textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans_list = [nametag_out(h_ease=store.hide_ease)]


        if who is None: # narrator nametag
            window at store._nametag_trans_list:
                pos(0,0.348)
                if show_timeout_tag:
                    background "gui/textbox/narrator_timeout.png"
                else:
                    background "gui/textbox/narrator_tag.png"

        else: # center_voice nametag
            window at store._nametag_trans_list:
                pos(0,0.348)
                background "gui/textbox/middle tag.png"

            text who id "who" at store._nametag_trans_list:
                color "#292928"
                outlines [(1, "#E5DBD9", 0, 0)]
                ypos 530
                xalign 0.5

        # SHARED window + text for both narrator and center_voice
        window at store._nar_trans_list:
            if narrator_size == "ns":
                background "gui/textbox/ns.png"
            elif narrator_size == "nm":
                background "gui/textbox/nm.png"
            elif narrator_size == "nl":
                background "gui/textbox/nl.png"
            else:
                background "gui/textbox/nxl.png"

            id "textbox_[narrator_size]_[box_anim]_[speaker_changed]"
            style "narrator_window"

        if speaker_changed:
            if show_text:
                text what id "what" slow_cps 170 ypos 565
            else:
                text what id "what" at hidden_text ypos 565
            timer 0.3 action SetScreenVariable("show_text", True)
        else:
            text what id "what" ypos 565

    else:
        $ clean = renpy.filter_text_tags(what, allow=['b','i','u','font','size'])
        $ test_text = Text(clean, style="say_dialogue")
        $ _, text_height = renpy.render(test_text, 530, 1360, 0, 0).get_size()
        $ estimated_lines = int(text_height / 43)

        $ dialogue_size_old_snap = store.dialogue_size_old

        if estimated_lines <= 2:
            $ store.dialogue_size = "small"
        elif estimated_lines == 3:
            $ store.dialogue_size = "medium"
        elif estimated_lines <= 5:
            $ store.dialogue_size = "large"
        else:
            $ store.dialogue_size = "xl"

        $ dialogue_size_order = ["small", "medium", "large", "xl"]
        $ old_dialogue_rank = dialogue_size_order.index(dialogue_size_old_snap) if dialogue_size_old_snap in dialogue_size_order else -1
        $ new_dialogue_rank = dialogue_size_order.index(store.dialogue_size)
        $ box_anim = "in" if speaker_changed else ("grow" if new_dialogue_rank > old_dialogue_rank else ("shrink" if new_dialogue_rank < old_dialogue_rank else "same"))

        $ new_side = "left" if who == playing_as else "right"
        $ old_side = store.last_shown_side
        if speaker_changed and old_side == new_side:
            $ store.side_pause = 0.12
        else:
            $ store.side_pause = 0

        $ store.prev_h_ease = store.hide_ease

        $ store.bounce_zoom = 1.05
        $ store.hide_ease_bounce = 0.05

        if store.dialogue_size == "small":
            $ store.in_ease = .12
            $ store.hide_ease = 0.12
        elif store.dialogue_size == "medium":
            $ store.in_ease = 0.14
            $ store.hide_ease = 0.12
        elif store.dialogue_size == "large":
            $ store.in_ease = 0.18
            $ store.hide_ease = 0.15
        else:
            $ store.in_ease = 0.2
            $ store.hide_ease = 0.15


        $ store.prev_h_ease = store.hide_ease

        if box_anim == "in":
            $ store._trans_list = [textbox_in(i_pause=0.05, i_ease=store.in_ease), textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans = nametag_in(i_pause=0.05 + store.side_pause, i_ease=store.in_ease, h_ease=store.hide_ease)
        elif box_anim == "grow":
            $ store._trans_list = [textbox_grow(i_pause=0.05, i_ease=store.in_ease), textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans = nametag_out(h_ease=store.hide_ease)
        elif box_anim == "shrink":
            $ store._trans_list = [textbox_shrink, textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans = nametag_out(h_ease=store.hide_ease)
        else:
            $ store._trans_list = [textbox_same, textbox_hide(h_ease=store.hide_ease)]
            $ store._nametag_trans = nametag_out(h_ease=store.hide_ease)

        if who == playing_as:
            $ dialogue_current = "left"
        else:
            $ dialogue_current = "right"

        if who == playing_as:
            #nametags
            if who_old == None and old_side == "left":
                $ side_pause = 0.12
            else:
                $ side_pause = 0

            window at store._nametag_trans:
                pos(0,0.55)
                if show_timeout_tag:
                    add "gui/textbox/timeout_tag.png"

                else:
                    background "gui/textbox/Left Tag.png"

            text who id "who" at store._nametag_trans:
                color "#1E2B3E"
                outlines [(1, "#E5DBD9", 0, 0)]
                pos (315, 795)

            #dialogue window
            window at store._trans_list:
                id "left"
                style "left"

                text what id "what" at hidden_text alt "":
                    xmaximum 530
                    xminimum 530
                    ypos -27
                    xpos 100

            # text
            if show_text:
                text what id "what" slow_cps 170 yoffset 870:
                    xmaximum 530
                    xminimum 530
                    ypos -27
                    xpos 100

            if speaker_changed:
                timer 0.27 action SetScreenVariable("show_text", True)
            else:
                timer 0.05 action SetScreenVariable("show_text", True)

        else:
            if who_old == None and old_side == "right":
                $ side_pause = 0.12
            else:
                $ side_pause = 0
            window at store._nametag_trans:
                pos(0.05, 0.555)
                background "gui/textbox/Right Tag.png"

            text who id "who" at store._nametag_trans:
                color "#1E2B3E"
                outlines [(1, "#E5DBD9", 0, 0)]
                ypos 800
                xalign 0.5

            window at store._trans_list:
                id "right"
                style "right"

                text what id "what" at hidden_text alt "":
                    xmaximum 530
                    xminimum 530
                    xpos 175
                    ypos -27

            if show_text:
                text what id "what" slow_cps 170 yoffset 875:
                    xmaximum 530
                    xminimum 530
                    xpos 175
                    ypos -27

            if speaker_changed:
                timer 0.27 action SetScreenVariable("show_text", True)

            else:
                timer 0.05 action SetScreenVariable("show_text", True)

##textbox transitions
transform textbox_in(i_pause=0.0, i_ease=0.2):
    on show:
        alpha 0
        pause i_pause + side_pause
        yzoom 0.0
        alpha 1.0
        ease i_ease yzoom 1.1
        ease 0.1 yzoom 1.0

transform textbox_grow(i_pause=0.0, i_ease=0.2):
    on show:
        alpha 0
        pause i_pause + side_pause
        yzoom 0.0
        alpha 1.0
        ease i_ease yzoom 1

transform textbox_shrink:
    on show:
        alpha 1.0

transform textbox_same:
    on show:
        alpha 1.0

transform textbox_hide(h_ease=0.12):
    on hide:
        pause 0.12
        ease h_ease yzoom 0

transform nametag_out(h_ease=0.12):
    on hide:
        pause h_ease + 0.12
        ease 0.1 alpha 0

transform nar_tag_in(i_pause=0.0, i_ease=0.2):
    on show:
        alpha 0
        pause i_pause + 0.12
        ease 0.1 alpha 1.0

transform nametag_in(i_pause=0.0, i_ease=0.2, h_ease=0.12):
    on show:
        alpha 0
        pause i_pause
        ease 0.1 alpha 1.0
    on hide:
        pause h_ease + 0.12
        ease 0.1 alpha 0

transform hidden_text:
    alpha 0.0

transform shown_text:
    alpha 1.0

transform input_in:
    alpha 0
    pause 0.2
    alpha 0.5
    easein 0.2 alpha 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

init python:
    #textbox functions
    class TwoFrameBoxLeft(renpy.Displayable):
        def __init__(self, width, height, **kwargs):
            super().__init__(**kwargs)
            self.width = width
            self.height = height

            self.left_frame = Frame("gui/textbox/ls_edge.png", left=5, top=5, right=20, bottom=55, tile=False)
            self.right_frame = Frame("gui/textbox/ls_body.png", left=5, top=5, right=20, bottom=10, tile=False)

        def render(self, width, height, st, at):
            if 165 < height < 200:
                height = 247
            left_fixed_width = 73
            shift_x = -33

            min_width = left_fixed_width + shift_x -33
            total_width = max(width, min_width)
            right_width = total_width - left_fixed_width - shift_x

            left_rend = renpy.render(self.left_frame, left_fixed_width, height, st, at)
            right_rend = renpy.render(self.right_frame, right_width, height, st, at)

            rend = renpy.Render(total_width, height)
            rend.blit(left_rend, (shift_x, 0))
            rend.blit(right_rend, (left_fixed_width + shift_x, 0))

            return rend

    class TwoFrameBoxRight(renpy.Displayable):
        def __init__(self, width, height, **kwargs):
            super().__init__(**kwargs)
            self.width = width
            self.height = height

            self.left_frame = Frame("gui/textbox/rs_body.png", left=5, top=5, right=20, bottom=10, tile=False)
            self.right_frame = Frame("gui/textbox/rs_edge.png", left=5, top=5, right=20, bottom=55, tile=False)

        def render(self, width, height, st, at):
            if 165 < height < 200:
                height = 247
            right_fixed_width = 73
            shift_x = 30

            min_width = right_fixed_width + shift_x
            total_width = max(width, min_width)
            left_width = total_width - right_fixed_width - shift_x

            left_rend = renpy.render(self.left_frame, left_width, height, st, at)
            right_rend = renpy.render(self.right_frame, right_fixed_width, height, st, at)

            rend = renpy.Render(total_width, height)
            rend.blit(left_rend, (shift_x, 0))
            rend.blit(right_rend, (left_width + shift_x, 0))  # <- this is the key fix

            return rend

style left:
    xpos .454
    xalign 0.45
    yoffset 875
    yminimum 100
    xminimum 626
    xmaximum 626

    background TwoFrameBoxLeft(627, 100)

style right:
    xalign 0.796
    yoffset 875
    yminimum 100
    xminimum 688
    background TwoFrameBoxRight(690, 100)

#NARRATOR STYLES
style narrator_window:
    yoffset 607

style namebox:
    xalign .44
    xfill False
    yfill False
    xsize gui.namebox_width
    yalign -.107
    ysize gui.namebox_height

    background "gui/namebox.png"

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    ypos gui.dialogue_ypos
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

init python:
    def get_text():
        return str(renpy.get_widget("input","input").content)

screen input(prompt):
    on "hide" action SetVariable("who_old", "NEW")
    style_prefix "input"

    window:
        add "gui/textbox input.png" at nl_in_out:
            ypos 458

        vbox at input_in:
            xalign gui.dialogue_text_xalign
            xpos 135
            xsize gui.dialogue_width
            ypos 575

            text prompt style "input_prompt"
            input id "input" color "#3A3B45" yoffset -11

            imagebutton:
                auto "gui/input_button_%s.png"
                action get_text
                xpos 320
                ypos 25
                at input_button

transform input_button:
    zoom 0.6

screen input(prompt):
    variant "touch"
    style_prefix "input"

    window:
        add "gui/textbox input touch.png" at nl_in_out:
            ypos 458

        vbox at input_in:
            xalign gui.dialogue_text_xalign
            xpos 135
            xsize gui.dialogue_width
            ypos 575

            text prompt style "input_prompt"
            input id "input" color "#3A3B45" yoffset -11

            imagebutton:
                auto "gui/input_button_%s.png"
                action get_text
                xpos 320
                ypos 25
                at input_button

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    ypos 13


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# How long the player has to make a choice in timeout seconds.
init python:
    import math, pygame

    class RadialTimer(renpy.Displayable):
        def __init__(self, duration, image, radius=30, **kwargs):
            super(RadialTimer, self).__init__(**kwargs)
            self.duration = duration
            self.radius = radius
            self.image = image  ## keep as path string

        def render(self, width, height, st, at):
            size = self.radius * 2
            progress = max(0.0, 1.0 - st / self.duration)

            ## Load image directly as a pygame surface
            img_surf = pygame.image.load(renpy.loader.load(self.image))
            img_surf = pygame.transform.scale(img_surf, (size, size))
            img_surf = img_surf.convert_alpha()

            ## Create the pie slice mask
            mask = pygame.Surface((size, size), pygame.SRCALPHA)
            mask.fill((0, 0, 0, 0))

            if progress > 0:
                cx, cy = self.radius, self.radius
                angle = progress * 360
                points = [(cx, cy)]
                steps = max(int(angle), 1)
                for i in range(steps + 1):
                    a = math.radians(90 + (angle * i / steps))
                    points.append((
                        cx + self.radius * math.cos(a),
                        cy - self.radius * math.sin(a)
                    ))
                pygame.draw.polygon(mask, (255, 255, 255, 255), points)

            ## Apply mask
            result = img_surf.copy()
            result.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

            rv = renpy.Render(size, size)
            rv.blit(result, (0, 0))
            renpy.redraw(self, 0)
            return rv

        def visit(self):
            return []

default timeout = 7.0
default timeout_short = 4

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None
default timeout_short_label = None

# A preference that enables or disables timed choices.
default persistent.timed_choices = True

screen choice(items):
    default phase = "idle"
    default chosen_action = None
    default chosen_index = -1
    default show_timer = False
    default timer_stopped = False

    if phase == "pulse":
        timer 0.3 action SetScreenVariable("phase", "shrink")
    if phase == "shrink":
        timer 0.35 action chosen_action
    if timeout_label is not None or timeout_short_label is not None:
        timer 0.2 action SetScreenVariable("show_timer", True)

    on "hide" action SetVariable("who_old", playing_as)
    on "replace" action SetVariable("who_old", playing_as)
    # on "replaced" action SetVariable("who_old", playing_as)

    if middle:
        window:
            xalign 0.0
            xpos 62
            ypos 675
            yanchor 0.0

            style_prefix "choice"
            vbox:
                style "menu"
                spacing 15
                for index, i in enumerate(items):
                    fixed ysize 92:
                        if phase == "shrink" and index != chosen_index:
                            textbutton i.caption at choice_shrink(index):
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif phase == "shrink" and index == chosen_index:
                            textbutton i.caption at choice_selected_exit:
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif phase == "pulse" and index == chosen_index:
                            textbutton i.caption at choice_pulse:
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                            # idle phase, premium button
                            textbutton i.caption at staggered_dissolve(index):
                                action [
                                    SetScreenVariable("chosen_action", i.action),
                                    SetScreenVariable("chosen_index", index),
                                    SetScreenVariable("phase", "pulse"),
                                    SetScreenVariable("timer_stopped", True)
                                ]
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                background "gui/button/choice_idle_premium.png"
                                hover_background "gui/button/choice_hover_premium.png"

                        else:
                            # idle phase, regular button
                            textbutton i.caption at staggered_dissolve(index):
                                action [
                                    SetScreenVariable("chosen_action", i.action),
                                    SetScreenVariable("chosen_index", index),
                                    SetScreenVariable("phase", "pulse"),
                                    SetScreenVariable("timer_stopped", True)
                                ]
                                align (0.42,0.5)
                                text_align (0.05, 0.48)

    else:
        window:
            xalign 0.0
            xpos 20
            ypos 920
            yanchor 0.0

            style_prefix "choice"
            vbox:
                #if premium_choice = True then the first button should be gui/choice_idle_background_premium.png AND gui/choice_hover_background_premium.png, and should be the first option
                style "menu"
                spacing 15
                for index, i in enumerate(items):
                    fixed ysize 92:
                        $ new_caption = i.caption.replace(" (disabled)", "")

                        if " (disabled)" in i.caption:
                            # disabled always stays as-is regardless of phase
                            textbutton "{s}[new_caption]{/s}" at staggered_dissolve(index):
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)

                        elif phase == "shrink" and index != chosen_index:
                            textbutton i.caption at choice_shrink(index):
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif phase == "shrink" and index == chosen_index:
                            textbutton i.caption at choice_selected_exit:
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif phase == "pulse" and index == chosen_index:
                            textbutton i.caption at choice_pulse:
                                action None
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                if (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                                    background "gui/button/choice_idle_premium.png"

                        elif (index == 0 and premium_choice) or (index == 1 and premium_choice2):
                            # idle phase, premium button
                            textbutton i.caption at staggered_dissolve(index):
                                action [
                                    SetScreenVariable("chosen_action", i.action),
                                    SetScreenVariable("chosen_index", index),
                                    SetScreenVariable("phase", "pulse"),
                                    SetScreenVariable("timer_stopped", True)
                                ]
                                align (0.42,0.5)
                                text_align (0.05, 0.48)
                                background "gui/button/choice_idle_premium.png"
                                hover_background "gui/button/choice_hover_premium.png"

                        else:
                            # idle phase, regular button
                            textbutton i.caption at staggered_dissolve(index):
                                action [
                                    SetScreenVariable("chosen_action", i.action),
                                    SetScreenVariable("chosen_index", index),
                                    SetScreenVariable("phase", "pulse"),
                                    SetScreenVariable("timer_stopped", True)
                                ]
                                align (0.42,0.5)
                                text_align (0.05, 0.48)

    if show_timer and not timer_stopped:
        if (timeout_label is not None) and persistent.timed_choices:
            fixed:
                if middle:
                    xpos 629
                    ypos 493
                    xysize (80, 64)
                    add "gui/slider/timeout_empty.png":   ## background circle
                        xalign 0.5
                        yalign 0.5
                        xoffset 10
                        yoffset 15
                    add RadialTimer(duration=timeout, image="gui/slider/timeout_full.png", radius=56) at textbox_in:
                        xoffset -5
                        yoffset -5

                else:
                    xpos 611
                    ypos 770
                    xysize (80, 64)
                    add RadialTimer(duration=timeout, image="gui/slider/timeout_full.png", radius=50) at textbox_in

            timer timeout action Jump(timeout_label)

        elif (timeout_short_label is not None) and persistent.timed_choices:
            fixed:
                if middle:
                    xpos 611
                    ypos 770
                    xysize (80, 64)
                    add "gui/slider/timeout_empty.png":   ## background circle
                        xalign 0.5
                        yalign 0.5
                        xoffset 10
                        yoffset 15
                    add RadialTimer(duration=timeout_short, image="gui/slider/timeout_full.png", radius=56) at textbox_in:
                        xoffset -5
                        yoffset -5

                else:
                    xpos 611
                    ypos 770
                    xysize (80, 64)
                    add RadialTimer(duration=timeout, image="gui/slider/timeout_full.png", radius=50) at textbox_in

            timer timeout_short action Jump(timeout_short_label)

transform staggered_dissolve(index):
    anchor (0.5, 0.5)
    alpha 0.0
    pause 0.2
    pause index * 0.1
    ease 0.35 alpha 1.0

    on replaced:
        pause index * 0.1
        ease 0.2 alpha 0.0
    on hover:
        linear 0.12 zoom 0.98
    on idle:
        linear 0.12 zoom 1.0

transform choice_pulse:
    anchor (0.5, 0.5)
    zoom 1.0
    ease 0.1 zoom 1.05
    ease 0.1 zoom 1.0
    on hide:
        zoom 1.0
        ease 0.2 zoom 0.9 alpha 0.0

transform choice_shrink(index):
    anchor (0.5, 0.5)
    ease 0.12 zoom 0.6 alpha 0.0

transform choice_selected_exit:
    anchor (0.5, 0.5)
    zoom 1.0
    pause 0.1
    linear 0.15 zoom 0.9 alpha 0.0

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.0
    ypos 900
    yanchor 0.0

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    line_spacing -5


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.95
            yalign 0.98
            spacing 30

            #textbutton _("ILITW Stats") action ShowMenu("ILITWStatsUI") text_outlines [(1, "#000000", 0, 0)]
            #textbutton _("ILB Stats") action ShowMenu("ILBStatsUI") text_outlines [(1, "#000000", 0, 0)]
            #textbutton _("ILW Stats") action ShowMenu("StatsUI") text_outlines [(1, "#000000", 0, 0)]
            textbutton _("Back") action Rollback() text_outlines [(1, "#000000", 0, 0)]

        #    textbutton _("History") action ShowMenu('history')
        #    textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #    textbutton _("Auto") action Preference("auto-forward", "toggle")
        #    textbutton _("Save") action ShowMenu('save')
        #    textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    default lastsave = get_newest_slot()

    vbox:
        style_prefix "navigation"

        if not main_menu:
            xpos gui.navigation_xpos
            yalign 0.23
            spacing 30

        if main_menu:
            xalign 0.5
            ypos 645
            spacing 25
            if main_menu and lastsave is not None:
                textbutton _("Continue") action FileLoad(lastsave, slot=True) text_style "mm_button_text"

            textbutton _("NEW GAME") action Start() text_style "mm_button_text"

            textbutton _("LOAD") action ShowMenu("load") text_style "mm_button_text"

            textbutton _("PREFERENCES") action ShowMenu("preferences") text_style "mm_button_text"

            textbutton _("QUIT") action Quit(confirm=not main_menu) text_style "mm_button_text"

            #imagebutton auto "gui/mm_start_%s.png" xpos 285 ypos 603 focus_mask True action Start()
            #imagebutton auto "gui/mm_load_%s.png" xpos 325 ypos 660 focus_mask True action ShowMenu("load")
            #imagebutton auto "gui/mm_pref_%s.png" xpos 275 ypos 700 focus_mask True action ShowMenu("preferences")
            #imagebutton auto "gui/mm_quit_%s.png" xpos 328 ypos 740 focus_mask True action Quit(confirm=not main_menu)

        else:
            ypos 0.33
            spacing 25

            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}RESUME") action ShowMenu("hide_screens_fade")
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}SAVE") action ShowMenu("save")
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}LOAD") action ShowMenu("load")
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}PREFS") action ShowMenu("preferences")
            #if tester_mode:
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}TRAITS") action ShowMenu("traits")
            #if tester_mode:
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}VARIABLES") action ShowMenu("variables")
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}HISTORY") action ShowMenu("history")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}HOME") action MainMenu()
            textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}QUIT") action Quit()

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("HELP") action ShowMenu("help")

        #if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            #textbutton _("QUIT") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style mm_button_text:
    font gui.mm_button_font
    size 50
    color "#AAFFDF"
    hover_color "#00ffc0"
    xalign 0.5

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 168
    yfill True

    ##background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -12
    xmaximum 480
    yalign 1.0
    yoffset -12

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen side_menu(title):
    add "gui/bg.png"

    text title:
        xpos 20
        ypos 20
        size 44
        color "#a40909"
        outlines [(1, "#000000", 0, 0)]
        font "fonts/TTSupermolotNeue-ExtraBold.ttf"

    if main_menu != True:
        fixed:
            use navigation

    transclude

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude


    if main_menu != True:
        use navigation

    #textbutton _("Return"):
        #style "return_button"

        #action Return()

    text title:
        xpos 20
        ypos 20
        size 44
        color "#888888"
        outlines [(1, "#000000", 0, 0)]
        font "fonts/TTSupermolotNeue-ExtraBold.ttf"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 18
    top_padding 72

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 168
    yfill True

style game_menu_content_frame:
    left_margin 24
    right_margin 12
    top_margin 6

style game_menu_viewport:
    xsize 552

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 6

style game_menu_label:
    xpos 30
    ysize 72

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -18


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        vbox:
            xsize 480
            xoffset 50
            yoffset 100
            label "{font=fonts/sofia pro black condensed.ttf}{size=35}{color=#878c91}[config.name!t]"
            text _("Version [config.version!t]\n"):
                color "#888888"
                size 30

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n":
                    color "#888888"
                    size 30

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
                color "#888888"
                size 30


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

python early:
    class PageBarValue(BarValue):
        def __init__(self, current, total, visible):
            self.current = current
            self.total = total
            self.visible = visible

        def get_value(self):
            return float(self.current - 1)

        def get_range(self):
            return float(max(1, self.total - self.visible))

        def get_page(self):
            return float(self.visible)  # fixed thumb — always represents 9 pages

        def set_value(self, value):
            renpy.run(FilePage(int(round(value)) + 1))
            renpy.restart_interaction()

screen save():
    zorder 1000001

    tag menu

    use file_slots(_("SAVE"))

screen load():
    zorder 1000001

    tag menu

    use file_slots(_("LOAD"))

    if main_menu:
        textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}RETURN") action Return():
            ypos 0.075
            xpos 0.025

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use side_menu(title):
        fixed:
            xpos 50
            ypos 120
            xsize 718
            ysize 1240

            ## This ensures the input will get the enter event before any of the buttons do.
            order_reverse True

            ## The grid of file slots.
            vbox:
                style_prefix "slot"
                xoffset -20
                xalign 1.0
                ypos 60
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action If("save" in title.lower(), true=Show("give_save_name", slotIndex = slot), false=FileLoad(slot))

                        xsize 500
                        ysize 150

                        has hbox
                        spacing 20

                        add FileScreenshot(slot) xsize 70 ysize 120

                        vbox:
                            spacing 10
                            xsize 300

                            text FileSaveName(slot).strip("[]{}"):
                                style "slot_time_text"
                                xalign 0.0

                            text "[FileTime(slot, format=_('%b %d, %H:%M'), empty=_('empty slot'))]  •  [format_playtime(FileJson(slot, '_game_runtime', 0))]":
                                style "slot_name_text"
                                xalign 0.0
                                size 20

                        if FileLoadable(slot):
                            imagebutton:
                                idle "gui/icon_delete.png"
                                action FileDelete(slot)
                                xalign 1.0
                                yalign 0.5

                        key "save_delete" action FileDelete(slot)

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                yalign 1.0
                yoffset -125
                xoffset -20

                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    default page_name_value
                    length 20
                    value page_name_value

            ## Buttons to access other pages.
            $ saves = len(renpy.list_saved_games(fast=True))
            $ savePages = int((len(renpy.list_saved_games(fast=True)) / (gui.file_slot_rows))) + 1

            hbox:
                xalign 0.5
                yalign 1.0
                yoffset -55
                xoffset -25
                spacing 35

                imagebutton:
                    yoffset 5
                    xoffset 5
                    idle "gui/button/left_arrow.png"
                    hover "gui/button/left_arrow_hover.png"
                    action FilePagePrevious(quick=False)

                $ current_page = persistent._file_page if isinstance(persistent._file_page, int) else 1
                $ button_stride = 65  # approximate width per page button + spacing, tune if needed
                $ scroll_to = max(0, (current_page - 1) * button_stride - 270)  # 270 = half of viewport xsize 600
                $ page_adj = ui.adjustment(value=scroll_to, range=savePages * button_stride)

                viewport id "pagination":
                    xsize 600
                    ysize 44
                    draggable True
                    xadjustment page_adj

                    hbox:
                        style_prefix "page"
                        spacing 35

                        if savePages < 10:
                            for page in range(1, 10):
                                textbutton "{font=fonts/Sofia Pro Black Condensed.ttf}[page]" action FilePage(page)
                        else:
                            for page in range(1, savePages + 1):
                                textbutton "{font=fonts/Sofia Pro Black Condensed.ttf}{size=42}[page]" action FilePage(page)

                imagebutton:
                    yoffset 5
                    xoffset -5
                    idle "gui/button/right_arrow.png"
                    hover "gui/button/right_arrow_hover.png"
                    action FilePageNext(quick=False)

            bar:
                xalign 0.5
                xoffset -25
                xsize 590
                ysize 10
                ypos 0.975
                value XScrollValue("pagination")
                # unscrollable "hide"

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button:
    background "gui/button/slot_idle_background.png"

style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 30
    ypadding 2

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style save_button:
    properties gui.button_properties("save_button")

style save_button_text:
    properties gui.button_text_properties("save_button")

init python:
    def file_name_has_forbidden_symbols(filename):
        return any(symbols in filename for symbols in ["[", "]", "{", "}"])

    def assign_save_name(name):
        global current_chapter, Rowan, save_name;

        if name == "":
            save_name = Rowan + " - Ch " + `current_chapter`

    def autosave_name():
        return "Autosave"

    config.autosave_callback = autosave_name

screen give_save_name(slotIndex):
    on 'show' action Function(assign_save_name, save_name, _update_screens=True)

    zorder 1000002
    modal True
    #style_prefix "confirm"
    #add "gui/overlay/confirm.png"

    hbox at stretch_ending:
        xalign 0.5
        yalign 0.43
        fixed:
            xsize 380
            ysize 60
            add "gui/save input.png":
                align (0.5, 0.4)
                yzoom 0.8
            input:
                style "save_input"
                value VariableInputValue("save_name")
                exclude "[]${}"
                length 36
                pixel_width 450
                color "#000"
                xoffset -38
                yoffset 40
                size 29

            text "ENTER SAVE NAME" xoffset -50 yoffset -45 size 33 color "#9a0000" font "Fonts/Sofia Pro Semi Bold Az.otf"
            #text "Enter save name" xoffset -46 yoffset 5 size 28 xsize 450 at ending_dissolve

            imagebutton:
                auto "gui/input_button_%s.png"
                xpos 270
                ypos 130
                at input_button
                action [Hide("give_save_name"), FileSave(slotIndex, confirm=False), ShowMenu('save'), With(None), SetVariable("save_name", "")]

            imagebutton:
                auto "gui/input_cancel_%s.png"
                xpos 130
                ypos 130
                at input_button
                action [Hide("give_save_name"), ShowMenu('save'), With(None), SetVariable("save_name", "")]

    key 'K_RETURN' action [Function(renpy.transition, None), Hide("give_save_name"), FileAction(slotIndex, confirm=False), Show("file_slots", title="Save"), SetVariable("save_name", "")]


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    zorder 1000000

    tag menu

    use game_menu(_("{color=#a40909}{font=fonts/TTSupermolotNeue-ExtraBold.ttf}{size=45}PREFERENCES"), scroll="viewport"):
        vbox:
            xpos 50
            ypos 100

            vbox:
                spacing 25
                if config.has_music:
                    label _("{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}MUSIC VOLUME")
                    if renpy.variant("pc"):
                        bar value Preference("music volume") xmaximum 480
                    else:
                        bar value Preference("music volume") xmaximum 400

                    label _("{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}SFX VOLUME")
                    if renpy.variant("pc"):
                        bar value Preference("sfx volume") xmaximum 480
                    else:
                        bar value Preference("sfx volume") xmaximum 400

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

            null height 15

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                hbox:
                    xfill True
                    frame:
                        xsize 300
                        background None
                        padding (0, 0)

                        text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}DISPLAY{/size}{/font} \n{size=29}Show full screen."

                    frame:
                        xsize 100
                        background None
                        padding (0, 0)
                        imagebutton at Transform(zoom=0.75):
                            if is_fullscreen:
                                idle "gui/button/button_off.png"
                            else:
                                idle "gui/button/button_on.png"

                            action [Preference("display", "toggle"), Function(update_display_mode)]
                            yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}NUDITY{/size}{/font} \n{size=29}Show topless sprites."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if persistent.nipples == "censored":
                            idle "gui/button/button_off.png"
                        else:
                            idle "gui/button/button_on.png"

                        action ToggleVariable("persistent.nipples", "censored", "uncensored")
                        yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}SKIP UNSEEN{/size}{/font} \n{size=28}Skip all text."
                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if preferences.skip_unseen:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"
                        action Preference("skip", "toggle")
                        yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}SKIP AFTER CHOICE{/size}{/font} \n{size=28}Resume skip after \nchoice."
                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if preferences.skip_after_choices:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action Preference("after choices", "toggle")
                        yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}BACKGROUND PAN{/size}{/font} \n{size=28}Show panning."
                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if panning_on:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("panning_on", True, False)
                        yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}AUTOHIDE UI{/size}{/font} \n{size=28}Hide settings icons."
                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if settings_autohide:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("settings_autohide", True, False)
                        yoffset 10

            null height 35

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#878c91}{font=fonts/Sofia Pro Black Condensed.ttf}{size=35}SELF-VOICING{/size}{/font} \n{size=28}Enable spoken text."
                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if _preferences.self_voicing:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"
                        action ToggleField(_preferences, "self_voicing")
                        yoffset 10

    if main_menu:
        textbutton _("{font=fonts/TTSupermolotNeue-ExtraBold.ttf}RETURN") action Return():
            ypos 0.075
            xpos 0.025

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 135

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    xsize 400

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    xpos 10

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    xsize 400

style check_button_text:
    properties gui.button_text_properties("check_button")
    xpos 10

style slider_slider:
    xsize 400

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 6

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 270


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    zorder 1000000

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("{color=#a40909}{font=fonts/TTSupermolotNeue-ExtraBold.ttf}{size=45}HISTORY"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        vbox:
            spacing 15
            xsize 480
            xoffset 50

            for h in _history_list:

                if h.who != None and h.who not in ["b", "b3"]:
                    text h.who:
                        font "fonts/sofia pro black condensed.ttf"
                        size 30
                        color "#878c91"
                        xpos 0
                        yoffset 10
                        substitute False

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    color "#888888"
                    size 27
                    xpos 0
                    substitute False

            if not _history_list:
                text _("The dialogue history is empty."):
                    color "#888888"
                    size 27
                    xpos 0


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize None

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 9

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 5

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 150
    right_padding 12

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 1000003

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        background Frame("gui/frame2.png", 40, 10, 40, 0)
        xsize 600
        # bottom_padding 0

        vbox:
            xalign 0.5
            yalign 0.5
            first_spacing 20

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            null height 10

            hbox:
                xalign 0.85
                spacing 100
                textbutton _("No") action no_action
                textbutton _("Yes") action yes_action
            #
            # frame:
            #     background Solid("#550000")
            #     xsize 600
            #     hbox:
            #         xalign 0.85
            #         spacing 100
            #
            #         button:
            #             action no_action
            #             has hbox:
            #                 spacing 5
            #                 order_reverse True
            #                 add "gui/confirm_no.png" xsize 50 ysize 40 yalign 0.51
            #                 text "No" color "#FFFFFF" hover_color "#CC0000" yalign 0.5
            #
            #         button:
            #             action yes_action
            #             has hbox:
            #                 spacing 5
            #                 order_reverse True
            #                 add "gui/confirm_yes.png" xsize 50 ysize 40 yalign 0.51
            #                 text "Yes" color "#FFFFFF" hover_color "#CC0000" yalign 0.5
            #
            #
            #         # textbutton _("No") action no_action:
            #         #     text_color "#FFFFFF"
            #         # textbutton _("Yes") action yes_action:
            #         #     text_color "#FFFFFF"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    text_align 0.5
    # layout "subtitle"
    font gui.text_font
    color "#190000"
    line_spacing 0

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    font gui.interface_text_font


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 4

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen
init python:
    def grant_achievement(name):
        achievement.grant(name)
        achievement.sync()

    def update_display_mode():
        import renpy.display
        global is_fullscreen
        is_fullscreen = renpy.display.interface.fullscreen

screen achievement(achiev_name, achiev_text="", achiev_box="gui/notify.png"):
    on "show" action Function(grant_achievement, achiev_name)

    zorder 100
    vbox at notify_box_appear:
        xsize 500
        spacing 10
        null height 1
        add achiev_box
        text achiev_name:
            xalign (0.5)
            yoffset -175
            size 33
            color "#292928"
            outlines [ (absolute(1), "#E5DBD9", absolute(0), absolute(0)) ]
            font "Fonts/TTSupermolotNeue-ExtraBold.ttf"
        text achiev_text:
            xalign (0.5)
            yoffset -190
            size 30
            color "#E5DBD9"

    timer 3.5 action Hide("achievement")

transform notify_box_appear:
    zoom 1.2
    on show:
        alpha 0
        xalign 0.5
        ypos -100
        linear .3 ypos 70 alpha 1.0
        linear 0.1 ypos 50
    on hide:
        linear .1 ypos 65
        linear .2 ypos -75 alpha 0.0
        linear .3 ypos -100 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

transform fast_fade:
    # Applied to menu buttons.
    on show:
        alpha 0.0
        linear 0.15 alpha 1.0
    on hide:
        pause 1.5
        linear 0.15 alpha 0.0
    on hover:
        linear 0.05 zoom 0.93
    on idle:
        linear 0.05 zoom 1.0

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

transform nvl_slide_in:
    yoffset 70
    easein_cubic 0.35 yoffset 0

transform staggered_dissolve_phone(index):
    transform_anchor (0.5, 0.5)
    xanchor 0.5 xpos 0.5
    yanchor 0.5 ypos 0.5
    alpha 0.0
    zoom 0.5
    pause index * 0.05
    ease 0.35 alpha 1.0 zoom 1.0

    on replaced:
        pause index * 0.1
        ease 0.2 alpha 0.0

transform text_contine:
    on hover:
        ease 0.1 zoom 0.98
    on idle:
        zoom 1.0
        ease 0.1 zoom 1.0

screen nvl(dialogue, items=None):
    on "hide" action SetVariable("who_old", "NEW")
    if nvl_mode == "lore":
        window:
            style "nvl_window_lore"

            has vbox:
                spacing 5

            ## Displays dialogue in either a vpgrid or the vbox.
            use nvl_lore_dialogue(dialogue)
            key "dismiss" action Return()
            if renpy.is_skipping():
                timer 0.05 action Return() repeat False

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
        add SideImage() xalign 0.0 yalign 1.0

    else:
        window:
            background "gui/texting/nvl_bg.png"
            xsize 768

            if items != None and len(items) > 0:
                key "dismiss" action NullAction()
            if not (items != None and len(items) > 0):
                if renpy.is_skipping():
                    timer 0.05 action Return() repeat False
                else:
                    imagebutton at text_contine:
                        xalign 0.5
                        yalign 1.0
                        yoffset 300
                        idle "gui/texting/texting_continue.png"
                        hover "gui/texting/texting_continue.png"
                        action Return() keysym "K_RETURN", "K_SPACE"

            if len(items) > 0:
                ysize 800
            else:
                ysize 1000

            viewport id "vp":
                draggable True
                yinitial 1.0
                yadjustment ui.adjustment(value=99999, range=99999)

                frame:
                    background None
                    if len(items) > 0:
                        yminimum 780
                    else:
                        yminimum 980

                    vbox:
                        yalign 1.0
                        first_spacing 10
                        spacing 10
                        use nvl_dialogue(dialogue)

            if not (renpy.variant("small") or renpy.variant("phone")):
                vbar:
                    xpos 0.99
                    value YScrollValue("vp")
                    unscrollable "hide"

        if items != None and len(items) > 0:
            hbox:
                frame:
                    xfill True
                    yfill True
                    background "gui/overlay/confirm.png"

                    window at nvl_slide_in:
                        xsize 650
                        xalign 0.5
                        ypos 800
                        background Frame("gui/texting/choices_bg.png", left=20, top=20, right=20, bottom=50, bottom_padding=50)
                        bottom_padding 30

                        vbox:
                            spacing 10
                            null height 1
                            add Solid("#ffffff", xsize=600, ysize=2) xalign .5:
                                yoffset 25
                                xoffset 25
                            frame:
                                xalign 0.5
                                xoffset 25
                                yoffset -10
                                xpadding 15
                                ypadding 2
                                background "#444242"  # match your screen background
                                text text_choice:
                                    size 30
                                    color "#FFF"
                            null height -40
                            for index, i in enumerate(items):
                                button at staggered_dissolve_phone(index):
                                    action i.action
                                    xsize 600
                                    ysize 68
                                    xoffset 25
                                    yoffset 25
                                    background Frame("gui/texting/text_bar_right.png")
                                    hover_background Frame("gui/texting/text_bar_hover.png")

                                    text i.caption:
                                        xalign 0.0
                                        xoffset 10
                                        yalign 0.5
                                        size 30
                                        color "#FFF"

                            null height 5

                    window at nvl_slide_in:
                        background Frame("gui/texting/speech_choice.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                        xsize 35
                        ysize 55
                        yalign 1.0
                        xalign 1.0
                        xoffset -21
                        yoffset -475


screen nvl_dialogue(dialogue):
    if nvl_mode == "phone":

        for i in range(len(dialogue)):
            $ d = dialogue[i]

            window at nvl_slide_in:
                id d.window_id

                vbox:
                    xpos 20
                    if d.who != None and d.who == "date":
                        hbox:
                            window:
                                xalign 1.0
                                xoffset 27

                                background Frame("gui/texting/date_box.png", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                xsize 650
                                xpos 660
                                padding (0,0,0,5)

                                text d.what:
                                    id d.what_id
                                    color "#FFF"
                                    yoffset -5

                        null height 25

                    elif d.who != None and d.who.lower().strip() == playing_as.lower().strip():
                        if i == 0 or d.who != dialogue[i-1].who:
                            hbox:
                                xalign 1.0
                                xoffset 27

                                window:
                                    xsize 70
                                    ysize 40
                                    xoffset -22
                                    background Frame("gui/texting/name_right_label_round.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)

                                window:
                                    ysize 40
                                    xoffset -22
                                    padding (20,0,5,0)
                                    background Frame("gui/texting/name_right_label.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)

                                    hbox:
                                        spacing 0
                                        xalign 1.0
                                        if d.who == Rowan:
                                            add "images/Nerve Icons/nerve[r_nerve_icon].png":
                                                zoom .7
                                                yoffset 3
                                        text d.who font "Fonts/Sofia Pro Black Condensed.ttf":
                                            id d.who_id
                                            xoffset -200

                        hbox:
                            window:
                                id "nvl_right"
                                background Frame("gui/texting/text_bar_right.png", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                xsize 650
                                xpos 40
                                padding (0,5,0,15)

                                text d.what:
                                    id d.what_id
                                    color "#FFF"
                                    xoffset -170
                                    yoffset -5
                                    xsize 600
                            if i == 0 or d.who != dialogue[i-1].who:
                                window:
                                    background Frame("gui/texting/speech_right.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    xsize 35
                                    ysize 70
                                    xoffset 40

                    else:
                        if d.who != None and (i == 0 or d.who != dialogue[i-1].who):
                            hbox:
                                xalign 0.0
                                xoffset 40
                                window:
                                    ysize 40
                                    if d.who == "Jocelyn":
                                        background Frame("jocelyn_label", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Abel":
                                        background Frame("abel_label", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Connor":
                                        background Frame("connor_label", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Lincoln":
                                        background Frame("lincoln_label", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Amalia":
                                        background Frame("amalia_label", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    else:
                                        background Frame("gui/texting/name_left_label.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)

                                    padding (5,0,20,0)
                                    hbox:
                                        spacing -5
                                        xalign 0.0
                                        if d.who == "Jocelyn":
                                            add "images/Nerve Icons/nerve[j_nerve_icon].png":
                                                zoom .7
                                                yoffset 2
                                        elif d.who == "Abel":
                                            add "images/Nerve Icons/nerve[ab_nerve_icon].png":
                                                zoom .7
                                                yoffset 2
                                        elif d.who == "Amalia":
                                            add "images/Nerve Icons/nerve[am_nerve_icon].png":
                                                zoom .7
                                                yoffset 2
                                        elif d.who == "Connor":
                                            add "images/Nerve Icons/nerve[c_nerve_icon].png":
                                                zoom .7
                                                yoffset 2
                                        elif d.who == "Lincoln":
                                            add "images/Nerve Icons/nerve[l_nerve_icon].png":
                                                zoom .7
                                                yoffset 2
                                        text d.who font "Fonts/Sofia Pro Black Condensed.ttf":
                                            id d.who_id
                                            xoffset -30
                                            xpos 50

                                window:
                                    xsize 70
                                    ysize 40
                                    if d.who == "Jocelyn":
                                        background Frame("jocelyn_label_rounded", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Abel":
                                        background Frame("abel_label_rounded", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Connor":
                                        background Frame("connor_label_rounded", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Lincoln":
                                        background Frame("lincoln_label_rounded", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Amalia":
                                        background Frame("amalia_label_rounded", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    else:
                                        background Frame("gui/texting/name_left_label_round.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)

                        hbox:
                            xpos 40
                            window:
                                id "nvl_left"
                                if d.who == "Jocelyn":
                                    background Frame("jocelyn_text_box", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                elif d.who == "Abel":
                                    background Frame("abel_text_box", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                elif d.who == "Connor":
                                    background Frame("connor_text_box", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                elif d.who == "Lincoln":
                                    background Frame("lincoln_text_box", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                elif d.who == "Amalia":
                                    background Frame("amalia_text_box", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                else:
                                    background Frame("gui/texting/text_bar.png", left=5, top=5, right=5, bottom=10, bottom_padding=15)
                                xsize 650
                                padding (0,5,0,15)

                                text d.what:
                                    id d.what_id
                                    color "#FFF"
                                    yoffset -5
                                    xoffset -20

                            if i == 0 or d.who != dialogue[i-1].who:
                                window:
                                    xpos -685
                                    if d.who == "Jocelyn":
                                        background Frame("jocelyn_speech", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Abel":
                                        background Frame("abel_speech", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Connor":
                                        background Frame("connor_speech", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Lincoln":
                                        background Frame("lincoln_speech", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    elif d.who == "Amalia":
                                        pass
                                    else:
                                        background Frame("gui/texting/speech_left.png", left=0, top=0, right=0, bottom=0, bottom_padding=0)
                                    xsize 35
                                    ysize 70


screen nvl_lore_dialogue(lore_dialogue):
    if nvl_mode == "lore":

        for d in lore_dialogue:

            window:
                id d.window_id

                fixed:
                    yfit gui.nvl_height is None

                    window:
                        id "nvl_lore"
                        style "nvl_lore"
                        text d.what:
                            id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_lore is say_lore_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_left:
    xfill True
    xanchor gui.nvl_text_xalign
    xpos 0
    yanchor 0
    yoffset 38
    bottom_padding 25
    text_align 0

    background Frame("gui/nvl_left.png", left=5, top=5, right=5, bottom=10, bottom_padding=15)

style nvl_right:
    xfill True
    xanchor gui.nvl_text_xalign
    xpos 0
    yanchor 0
    yoffset 38
    bottom_padding 25
    text_align gui.nvl_text_xalign

    background Frame("gui/nvl_right.png", left=5, top=5, right=5, bottom=10, bottom_padding=15)

style nvl_lore:
    xfill True
    xanchor gui.nvl_text_xalign
    xpos 0
    yanchor 0

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_window_lore:
    xfill True
    yfill True

    background "gui/nvl_lore.png"
    padding gui.nvl_borders.padding


style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor -.1
    yoffset 60
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    yanchor 0
    yoffset 10
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xfill True
    xpadding 20
    ypadding 20
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    xalign 1.0
    color "#E5DBD9"
    hover_underline True
    properties gui.button_text_properties("nvl_button")


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 270

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    #background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    #background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 204

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 240

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/right.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/left.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 360
