screen ChooseMCAsset():
    default move = truecenter
    default show_textbox = True
    default move_direction = None

    zorder 1000000
    modal True

    add "full devon" at move

    $ total = len(AssetCount())
    $ spacing = 0.04
    $ start = 0.5 - ((total - 1) * spacing / 2.0)

    for i, option in enumerate(AssetCount()):
        $ xpos = start + i * spacing

        add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

        if (AssetSelected() == option):
            add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

    add "gui/textbox/bottom2menu.png" at (stretch_show if closet_choice_expanded and show_textbox else (stretch_hide if not closet_choice_expanded else (box_left if move_direction == "left" else box_right))):
        anchor (0.5, 1.0)
        pos (0.5, 0.93)

    if closet_choice_expanded:

        text "[item_name()!u]" xalign 0.5 ypos 945 font gui.name_text_font size 35 color "#FFF" at (message_show if show_textbox else message_hide)
        text "[item_description()]" xpos 90 yalign .79 size 33 color "#FFF" at (message_show if show_textbox else message_hide)

        button at (choice_in_animation if show_textbox else (box_left if move_direction == "left" else box_right)):
            anchor (0.5,0.5)
            yalign 0.850
            xpos 0.5
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Choose this look!":
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Return() keysym "K_RETURN"

        imagebutton at (message_show if show_textbox else message_hide):
            xalign 0.895
            yalign 0.72
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action (SetVariable("closet_choice_expanded", False))

        imagebutton at (arrow_show if show_textbox else arrow_hide):
            xoffset 20
            xalign 0.0
            yalign 0.5
            idle "Dressup_Screen/arrow left.png"
            hover "Dressup_Screen/arrow left_hover.png"
            action [
                SetScreenVariable("show_textbox", False),
                SetScreenVariable("move_direction", "right"),
                SetScreenVariable("move", move_right(PrevMCAsset, SetScreenVariable("move", truecenter)))
            ]
            keysym "K_LEFT"

        imagebutton at (arrow_show if show_textbox else arrow_hide):
            xoffset -20
            xalign 1.0
            yalign 0.5
            idle "Dressup_Screen/arrow right.png"
            hover "Dressup_Screen/arrow right_hover.png"
            action [
                SetScreenVariable("show_textbox", False),
                SetScreenVariable("move_direction", "left"),
                SetScreenVariable("move", move_left(NextMCAsset, SetScreenVariable("move", truecenter)))
            ]
            keysym "K_RIGHT"

        if not show_textbox:
            timer 1.0 action SetScreenVariable("show_textbox", True)

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))
