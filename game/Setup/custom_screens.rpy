init python:
    config.layers.append("topmenu_layer")
    config.overlay_screens.append("settingsUI_phone")

    def _show_top_menu_once():
        if not renpy.get_screen("top_menu_phone"):
            renpy.show_screen("top_menu_phone")

screen settingsUI_phone():
    zorder 1000000
    layer "overlay"
    if renpy.variant("touch"):
        modal True
        button:
            area (0, 0, 768, 320)
            action Function(_show_top_menu_once)

screen settingsUI():
    if not renpy.variant("touch"):
        modal True
        mousearea:
            area (0, 0, 768, 320)
            hovered Show("top_menu_pc")
            unhovered Hide("top_menu_pc")

screen top_menu_pc():
    zorder 1000001
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 15
        yoffset 35
        idle "gui/ff_idle.png" at roll_in_left
        hover "gui/ff_hover.png"
        action Skip() alternate Skip(fast=True, confirm=True)

    imagebutton at roll_in_right:
        xalign 1.0
        yalign 0.0
        xoffset -15
        yoffset 35
        idle "gui/settings_idle.png"
        hover "gui/settings_hover.png"
        action ShowMenu("show_screens_fade")

    #imagebutton at roll_in_right: closet button is hidden bc it's set for rowan and i don't feel like changing it
    #    xalign 1.0
    #    yalign 0.0
    #    xoffset -15
    #    yoffset 155
    #    idle "gui/closet_button_idle.png"
    #    hover "gui/closet_button_hover.png"
    #    action [
    #        SetVariable("closet",True),
    #        ShowMenu("show_screens_fade")
    #    ]
    #    keysym "c"
    #    alternate_keysym "c"

screen top_menu_phone():
    zorder 1000001
    layer "topmenu_layer"
    timer 3.0 action Hide("top_menu_phone")

    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 15
        yoffset 35
        idle "gui/ff_idle.png" at roll_in_left
        hover "gui/ff_hover.png"
        action Skip() alternate Skip(fast=True, confirm=True)

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -15
        yoffset 35
        idle "gui/settings_idle.png" at roll_in_right
        hover "gui/settings_hover.png"
        action [
            Hide("top_menu_phone"),
            ShowMenu("show_screens_fade")
        ]

    if setup_complete and (not flashback and rowan_outfit != "robe" and rowan_outfit != "Matthias" and rowan_outfit != "Lincoln" and playing_as == capsRowan) or rowan_outfit_on == "beach":
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -15
            yoffset 155
            idle "gui/closet_button_idle.png" at roll_in_right
            hover "gui/closet_button_hover.png"
            action [
                Hide("top_menu_phone"),
                SetVariable("closet", True),
                ShowMenu("show_screens_fade")
            ]
            keysym "c"
            alternate_keysym "c"

transform roll_in_left:
    on show:
        alpha 0.0
        offscreenleft
        zoom 0.85
        xpos -100 yalign 0
        ease 0.3 xalign 0.0 yalign 0 alpha 0.95

    on hide:
        ease 0.3 xpos -150 yalign 0 alpha 0.0

transform roll_in_right:
    on show:
        alpha 0.0
        offscreenright
        zoom 0.85
        xpos 800 yalign 0
        ease 0.3 xalign 1.0 yalign 0 alpha 0.95

    on hide:
        ease 0.3 xpos 900 yalign 0 alpha 0.0

screen show_screens_fade():
    modal True
    zorder 1000000
    add "#000000" at screen_dissolve
    timer 0.5 action [
        If(closet, ShowMenu("closet")),
        If(not closet, ShowMenu("save")),
        Hide("show_screens_fade")
    ]

screen hide_screens_fade():
    modal True
    zorder 1000000
    add "#000000" at screen_dissolve
    timer 0.5 action (Hide("hide_screens_fade"), Return())

screen bottom_choices_two(im, title, choice_mes1, jump1, choice_mes2):
    image im at image_dissolve
    default OnShow = True
    on "hide" action SetVariable("who_old", "NEW")

    add "gui/textbox/bottom2menu.png" at (stretch if OnShow else (stretch_show if closet_choice_expanded else stretch_hide)):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text title at (message_show_delayed if OnShow else message_show):
            font "Fonts/Sofia Pro Medium.ttf"
            color '#FFFFFF'
            kerning 1.5
            if len(title) <= 35:
                size 38
                xalign 0.5
                yalign 0.72
            else:
                size 38
                xsize 550
                xalign 0.45
                yalign 0.735
                line_spacing -10

        imagebutton at (message_show_delayed if OnShow else message_show):
            anchor (0.5,0.5)
            xalign 0.895
            yalign 0.72
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action (SetVariable("closet_choice_expanded", False), SetScreenVariable("OnShow", False))

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.765
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes1:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    if len(choice_mes1) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.2
                    yalign 0.5
                    line_spacing -5
                    xpos 50

            if premium_choice:
                idle_background Transform("gui/button/choice_idle_premium.png")
                hover_background Transform("gui/button/choice_hover_premium.png")
                focus_mask Transform("gui/button/choice_idle_premium.png")
                action [
                    SetVariable("current_LI", im),
                    SetVariable("JumpStore", jump1),
                    SetVariable("PrevScreen","bottom"),
                    Hide("bottom_choices_two"),
                    If(sparkles, Show("LI_sparkles", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))),
                    If(not sparkles, Jump(jump1))]
            else:
                idle_background Transform("gui/button/choice_idle_background.png")
                hover_background Transform("gui/button/choice_hover_background.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [
                    Hide("bottom_choices_two"),
                    Jump(jump1)
                ]

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.85
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes2:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    if len(choice_mes2) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.2
                    yalign 0.5
                    line_spacing -5
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Hide("bottom_choices_two",), Return()

    else:
        imagebutton at b_down:
            anchor (0.5,0.5)
            xalign 0.895
            yalign 0.965
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen bottom_choices_two_jumps(im, title, choice_mes1, jump1, choice_mes2,jump2):
    image im at image_dissolve
    default OnShow = True
    on "hide" action SetVariable("who_old", "NEW")

    add "gui/textbox/bottom2menu.png" at (stretch if OnShow else (stretch_show if closet_choice_expanded else stretch_hide)):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text title at (message_show_delayed if OnShow else message_show):
            font "Fonts/Sofia Pro Medium.ttf"
            color '#FFFFFF'
            kerning 1.5
            size 33
            xalign 0.5
            yalign 0.71

        imagebutton at (message_show_delayed if OnShow else message_show):
            xalign 0.895
            yalign 0.72
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action (SetVariable("closet_choice_expanded", False), SetScreenVariable("OnShow", False))

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.760
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes1:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    if len(choice_mes1) > 45:
                        yanchor 0.2
                        size 30
                    else:
                        yanchor 0.0
                        size 31
                    ypos 10
                    xpos 50

            if premium_choice:
                idle_background Transform("gui/button/choice_idle_premium.png")
                hover_background Transform("gui/button/choice_hover_premium.png")
                focus_mask Transform("gui/button/choice_idle_premium.png")
                action [
                    SetVariable("current_LI", im),
                    SetVariable("JumpStore", jump1),
                    SetVariable("PrevScreen","bottom"),
                    Hide("bottom_choices_two_jumps"),
                    If(sparkles, Show("LI_sparkles", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))),
                    If(not sparkles, Jump(jump1))]
            else:
                idle_background Transform("gui/button/choice_idle_background.png")
                hover_background Transform("gui/button/choice_hover_background.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [
                    Hide("bottom_choices_two_jumps"),
                    Jump(jump1)
                ]

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.855
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes2:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    if len(choice_mes2) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.0
                    size 31
                    ypos 10
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Hide("bottom_choices_two_jumps"), Jump(jump2)

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.965
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen bottom_choices_three(im, title, choice_mes1, jump1, choice_mes2, jump2, choice_mes3, jump3):
    image im at image_dissolve
    default OnShow = True
    on "hide" action SetVariable("who_old", "NEW")

    add "gui/textbox/bottom3menu.png" at (stretch if OnShow else (stretch_show if closet_choice_expanded else stretch_hide)):
        pos (0.5, 0.99)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text title at (message_show_delayed if OnShow else message_show):
            font "Fonts/Sofia Pro Medium.ttf"
            color '#FFFFFF'
            kerning 1.5
            size 33
            xalign 0.5
            yalign 0.71

        imagebutton at (message_show_delayed if OnShow else message_show):
            xalign 0.895
            yalign 0.72
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action (SetVariable("closet_choice_expanded", False), SetScreenVariable("OnShow", False))

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.750
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes1:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    if len(choice_mes1) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.0
                    size 31
                    ypos 10
                    xpos 50

            if premium_choice:
                idle_background Transform("gui/button/choice_idle_premium.png")
                hover_background Transform("gui/button/choice_hover_premium.png")
                focus_mask Transform("gui/button/choice_idle_premium.png")
                action [
                    SetVariable("current_LI", im),
                    SetVariable("JumpStore", jump1),
                    SetVariable("PrevScreen","bottom"),
                    Hide("bottom_choices_three"),
                    If(sparkles, Show("LI_sparkles", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))),
                    If(not sparkles, Jump(jump1))
                ]
            else:
                idle_background Transform("gui/button/choice_idle_background.png")
                hover_background Transform("gui/button/choice_hover_background.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [
                    Hide("bottom_choices_three"),
                    Jump(jump1)
                ]

        button at (choice_in if OnShow else choice_in_animation):
            anchor (0.5,0.5)
            yalign 0.835
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes2:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    if len(choice_mes2) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.0
                    size 31
                    ypos 10
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action [
                Hide("bottom_choices_three"),
                Jump(jump2)
            ]

        button at choice_in:
            anchor (0.5,0.5)
            yalign 0.92
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text choice_mes3:
                    xsize 600
                    font "Fonts/Sofia Pro Medium.ttf"
                    if len(choice_mes3) > 45:
                        yanchor 0.3
                    else:
                        yanchor 0.0
                    size 31
                    ypos 10
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Hide("bottom_choices_three"), Jump(jump3)

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.965
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen items_choice(im1, im2, im3, im4, title, im1_message, im2_message, im3_message, im4_message):
    on "hide" action SetVariable("who_old", "NEW")

    add "gui/overlay/confirm.png" at item_dissolve
    if selected_index != -1:
        fixed:
            at truecenter
            add Solid("#000"):
                alpha 0.25
            xysize (config.screen_width, config.screen_height)

    default selected_index = -1
    default items = [
        (im1, im1_message),
        (im2, im2_message),
        (im3, im3_message),
        (im4, im4_message)
    ]

    $ visible_items = [item for item in items if item[0] is not None]
    $ item_count = len(visible_items)

    $ positions_by_count = {
        2: [(0.3, 0.4), (0.75, 0.55)],
        3: [(0.3, 0.32), (0.48, 0.6), (0.75, 0.4)],
        4: [(0.28, 0.38), (0.48, 0.59), (0.58, 0.24), (0.78, 0.45)],
    }

    $ positions = positions_by_count.get(item_count, [])

    for i, (image_path, message) in enumerate(visible_items):

        $ pos = positions[i]
        $ xpos = pos[0]
        $ ypos = pos[1]

        # Draw the base button for all items
        button at item_in:
            xpos xpos
            ypos ypos
            background None
            focus_mask True
            action [
                SetVariable("item_choice_variable", image_path),
                SetVariable("choice_mes", message),
                SetScreenVariable("selected_index", i),
                Function(renpy.restart_interaction)
            ]

            if selected_index == i:
                # Selected button visuals (full color, with click_bounce)
                add "images/Items/item_bubble.webp" at click_bounce:
                    anchor (0.5, 0.5)
                    align (0.5, 0.5)
                    if item_count == 4:
                        zoom .55
                    else:
                        zoom .65

                if not npc_selection:
                    add image_path at click_bounce:
                        anchor (0.5, 0.5)
                        align (0.5, 0.5)
                        xoffset -25
                        yoffset -25
                        if item_count == 4:
                            zoom .55
                        elif item_count == 3:
                            zoom .6
                        else:
                            zoom .65

                else:
                    add image_path at click_bounce:
                        anchor (0.5, 0.5)
                        align (0.5, 0.5)
                        xzoom -1
                        if item_count == 4:
                            xoffset 78
                            yoffset -11
                            zoom .55
                        else:
                            xoffset 90
                            yoffset -15
                            zoom .65

            else:
                if not npc_selection:
                    add "images/Items/item_bubble.webp" at hexagon_in:
                        if selected_index != -1 and selected_index != i:
                            matrixcolor BrightnessMatrix(-0.05)*TintMatrix('#888888')
                        anchor (0.5, 0.5)
                        align (0.5, 0.5)
                        if item_count == 4:
                            zoom .55
                        else:
                            zoom .65

                    add image_path at choice_item_display:
                        if selected_index != -1 and selected_index != i:
                            matrixcolor BrightnessMatrix(-0.05)*TintMatrix('#888888')
                        anchor (0.5, 0.5)
                        align (0.5, 0.5)
                        xoffset -25
                        yoffset -25
                        if item_count == 4:
                            zoom .55
                        elif item_count == 3:
                            zoom .6
                        else:
                            zoom .65

                else:
                    add image_path at choice_item_display:
                        if selected_index != -1 and selected_index != i:
                            matrixcolor BrightnessMatrix(-0.05)*TintMatrix('#888888')
                        anchor (0.5, 0.5)
                        align (0.5, 0.5)
                        xoffset 80
                        yoffset -15
                        xzoom -1
                        if item_count == 4:
                            zoom .55
                        else:
                            zoom .65

    text title at item_dissolve:
        font "Fonts/TTSupermolotNeue-ExtraBold.ttf"
        color '#FFFFFF'
        kerning 1.5
        size 45
        xalign 0.5
        yalign 0.8

    showif choice_mes != "none":
        button at button_bounce:
            anchor (0.5,0.5)
            yalign 0.845
            xalign 0.4
            frame:
                background Null()
                xysize (500, 50)
                ypos 10
                text choice_mes:
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    if len(choice_mes) > 25:
                        align (0.8, 0.5)
                        yoffset 15
                    else:
                        align (0.3, 0.5)
                        yoffset 15

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Return() keysym "K_RETURN"

transform button_bounce:
    alpha 0.5
    anchor (0.5, 0.5)
    zoom 0.6
    ease 0.2 alpha 1.0 zoom 1.0
    on hover:
        linear 0.05 zoom 0.98
    on idle:
        linear 0.05 zoom 1.0

transform screen_shade_in:
    alpha 0.0
    linear 0.4 alpha 0.5

transform click_bounce:
    ease 0.08 zoom .9
    ease 0.08 zoom 1.15

screen item_display(im, title, choice_mes):
    add "gui/overlay/confirm.png" at item_dissolve
    on "hide" action SetVariable("who_old", "NEW")
    default phase = "idle"
    if phase == "pulse":
        timer 0.3 action Return()

    add "images/items/item_bubble.webp" at hexagon_in:
        pos (0.55,0.47)

    image im at item_in:
        pos (0.5,0.45)

    text title.upper() at item_dissolve:
        font "Fonts/TTSupermolotNeue-ExtraBold.ttf"
        color '#FFFFFF'
        kerning 1.5
        size 45
        xalign 0.5
        yalign 0.78

    button at (choice_item_display if phase == "idle" else choice_pulse):
        anchor (0.5,0.5)
        yalign 0.845
        xalign 0.42
        frame:
            background Null()
            xysize (500, 50)
            ypos 10
            text choice_mes:
                font "Fonts/Sofia Pro Medium.ttf"
                size 31
                ypos 10
                if len(choice_mes) > 15:
                    xalign 0.75
                else:
                    xalign 0.68

        idle_background Transform("gui/button/choice_idle_background.png")
        hover_background Transform("gui/button/choice_hover_background.png")
        focus_mask Transform("gui/button/choice_idle_background.png")
        action SetScreenVariable("phase", "pulse")

transform choice_item_display:
    alpha 0.5
    anchor (0.5, 0.5)
    zoom 0.6
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        alpha 1
        ease .2 alpha 0

    on hover:
        linear 0.05 zoom 0.98
    on idle:
        linear 0.05 zoom 1.0

transform hexagon_in:
    on show:
        anchor (0.5, 0.5)
        zoom 0.9
        ease 0.2 zoom 1.0
    on hide:
        alpha 1
        ease .2 alpha 0

transform item_in:
    on show:
        anchor (0.5, 0.5)
        zoom 0.9
        ease 0.2 zoom 1.0
    on hide:
        alpha 1
        ease .2 alpha 0

screen item_display_choice(im, title, choice_mes1, jump1, choice_mes2, jump2):
    on "hide" action SetVariable("who_old", "NEW")

    add "gui/overlay/confirm.png" at item_dissolve

    add "images/items/item_bubble.webp" at hexagon_in:
        pos (0.55,0.47)

    image im at item_in:
        pos (0.5,0.45)

    text title at item_dissolve:
        font "Fonts/TTSupermolotNeue-ExtraBold.ttf"
        color '#FFFFFF'
        kerning 1.5
        size 45
        xalign 0.5
        yalign 0.72

    button at item_dissolve:
        anchor (0.5,0.5)
        yalign 0.78
        xalign 0.22
        frame:
            background Null()
            xysize (500, 50)
            xalign 0.5
            ypos 10
            text choice_mes1:
                font "Fonts/Sofia Pro Medium.ttf"
                size 31
                ypos 10
                if len(choice_mes1) > 15:
                    xalign 0.75
                else:
                    xalign 0.68

        idle_background Transform("gui/button/choice_idle_background.png")
        hover_background Transform("gui/button/choice_hover_background.png")
        focus_mask Transform("gui/button/choice_idle_background.png")
        action Hide("bottom_choices_three"), Jump(jump1)

    button at item_dissolve:
        anchor (0.5,0.5)
        yalign 0.865
        xalign 0.22
        frame:
            background Null()
            xysize (500, 50)
            xalign 0.5
            ypos 10
            text choice_mes2:
                font "Fonts/Sofia Pro Medium.ttf"
                size 31
                ypos 10
                if len(choice_mes2) > 15:
                    xalign 0.75
                else:
                    xalign 0.68

        idle_background Transform("gui/button/choice_idle_background.png")
        hover_background Transform("gui/button/choice_hover_background.png")
        focus_mask Transform("gui/button/choice_idle_background.png")
        action Hide("bottom_choices_three"), Jump(jump2)

#click to continue
screen ctc():
    if nvl_mode != "phone" and nvl_mode != "lore":
        zorder 100
        add "gui/ctc.png" at ctc_appear
        text _("{i}TAP TO CONTINUE{/i}") at ctc_text alt "":
            size 30 font "Fonts/TTSupermolotNeue-ExtraBold.ttf" color "#ffffff"
    else:
        pass

screen ctc_text():
    if nvl_mode != "phone" and nvl_mode != "lore":
        zorder 100
        text _("{i}TAP TO CONTINUE{/i}") at ctc_text:
            size 30 font "Fonts/TTSupermolotNeue-ExtraBold.ttf" color "#ffffff"
    else:
        pass

transform ctc_text():
    alpha 0.0
    xalign .5
    yalign .98
    pause 5.0
    ease 0.35 alpha 0.5

transform ctc_appear():
    alpha 0.0
    xalign .5
    yalign .93
    zoom .45
    pause 5.0
    block:
        ease 0.35 alpha 1.0 zoom .65
        ease 0.35 zoom .45
        ease 0.25 zoom .58
        ease 0.25 zoom .45
        pause 1.5
        repeat
    repeat

transform truecenter:
    anchor (0.5, 1.0)
    align (0.5, 1.0)

screen chooseLI():
    default move = truecenter
    default show_textbox = True
    default move_direction = None
    default dissolving = False

    zorder 10000000
    modal True

    add "full [current_LI!l]" at (image_dissolve_hide if dissolving else move)

    $ total = len(get_available_LIs())
    $ spacing = 0.04
    $ start = 0.5 - ((total - 1) * spacing / 2.0)

    for i, option in enumerate(get_available_LIs()):
        $ xpos = start + i * spacing

        add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

        if (current_LI == option):
            add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

    add "gui/textbox/bottom2menu.png" at (stretch_show_only if closet_choice_expanded and show_textbox else (stretch_hide if not closet_choice_expanded else (box_left if move_direction == "left" else box_right))):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)
        yzoom 0.8

    if closet_choice_expanded:
        text choose_LI_text xalign 0.5 ypos 1015 size 38 color "#FFF" at (message_show if show_textbox else message_hide)

        button at (choice_in_animation if show_textbox else (box_left if move_direction == "left" else box_right)):
            anchor (0.5,0.5)
            yalign 0.830
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "[li_message].":
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    line_spacing -5
                    xpos 0.12
                    if len(li_message) > 40:
                        yanchor 0.25
                    else:
                        yanchor 0.0

            if li_message == mc_message:
                idle_background Transform("gui/button/choice_idle_background.png")
                hover_background Transform("gui/button/choice_hover_background.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [SetVariable("PrevScreen", None), SetScreenVariable("dissolving", True)]

            elif premium_choice:
                idle_background Transform("gui/button/choice_idle_premium.png")
                hover_background Transform("gui/button/choice_hover_premium.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [Hide("chooseLI"), SetVariable("PrevScreen", "chooseLI"), Show("LI_sparkles", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))]

            else:
                idle_background Transform("gui/button/choice_idle_background.png")
                hover_background Transform("gui/button/choice_hover_background.png")
                focus_mask Transform("gui/button/choice_idle_background.png")
                action [SetVariable("PrevScreen", None), SetScreenVariable("dissolving", True)]

        imagebutton at (message_show if show_textbox else message_hide):
            xalign 0.895
            yalign 0.77
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
                SetScreenVariable("move", move_right(PrevLI, SetScreenVariable("move", truecenter)))
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
                SetScreenVariable("move", move_left(NextLI, SetScreenVariable("move", truecenter)))
            ]
            keysym "K_RIGHT"

        if not show_textbox:
            timer 1.0 action SetScreenVariable("show_textbox", True)

        if dissolving:
            timer 0.15 action Return()

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))


init python:  # saves
    import time

    def force_autosave_sync(timeout=2.0, interval=0.1):
        autosave_name()
        renpy.force_autosave()
        deadline = time.time() + timeout
        while time.time() < deadline:
            slot = renpy.newest_slot(r"auto-\d+")
            if slot and renpy.slot_mtime(slot):
                break
            renpy.pause(interval, hard=True)

    _interaction_count = 0  # <---- define it here
    _AUTOSAVE_EVERY = 2  # save every 2 interactions

    AUTOSAVE_EXCLUDED_SCREENS = {
        "main_menu",
        "save",
        "load",
        "history",
        "closet",
        "achievements",
        "gallery",
        "preferences",
        "settings_ui",
        "quick_menu",
        "file_slots"
    }

    _autosave_initialized = False

    def _periodic_autosave():
        global _interaction_count, _autosave_initialized

        if not _autosave_initialized:
            _autosave_initialized = True
            return

        if renpy.context()._main_menu:
            return
        current = renpy.current_screen()
        if current in AUTOSAVE_EXCLUDED_SCREENS:
            return
        _interaction_count += 1
        if _interaction_count >= _AUTOSAVE_EVERY:
            _interaction_count = 0
            autosave_name()
            renpy.force_autosave()

    config.interact_callbacks.append(_periodic_autosave)

    def get_newest_slot():
        manual = renpy.newest_slot(r"\d+")
        autosave = renpy.newest_slot(r"auto-\d+")

        slots = []
        if manual:
            slots.append((manual, renpy.slot_mtime(manual)))
        if autosave:
            slots.append((autosave, renpy.slot_mtime(autosave)))

        slots = [(s, t) for s, t in slots if t is not None]

        if slots:
            return max(slots, key=lambda x: x[1])[0]

        return None

    def format_playtime(seconds):
        if not seconds:
            return ""
        seconds = int(seconds)
        h = seconds // 3600
        m = (seconds % 3600) // 60
        return "{}h {:02d}m".format(h, m)

transform ending_dissolve:
    alpha 0
    pause 0.1
    ease 0.1 alpha 1.0
    on hover:
        linear 0.05 zoom 0.98
    on idle:
        linear 0.05 zoom 1.0
    on hide:
        ease 0.1 alpha 0

screen ending_confirmation:
    add "gui/textbox/ending textbox.png" at stretch_ending:
        pos (0.5, 0.46)
        anchor (0.5, 1.0)
        yzoom 0.8

    text "CHAPTER [current_chapter] COMPLETE" xalign 0.35 ypos 470 size 33 color "#000" font "Fonts/Sofia Pro Semi Bold Az.otf" at ending_dissolve
    text "Do you want to keep playing?" size 28 xpos 0.2 ypos 530 xsize 450 at ending_dissolve

    button at ending_dissolve:
        anchor (0.5,0.5)
        yalign 0.455
        xalign 0.5
        frame:
            background Null()
            xysize (473, 50)
            xalign 0.5
            ypos 10
            text "Continue on.":
                font "Fonts/Sofia Pro Medium.ttf"
                color "#FFF"
                align (0.1, 0.0)
                size 28
                yoffset 5

        idle_background Transform("gui/button/ending_idle.png")
        hover_background Transform("gui/button/ending_hover.png")
        focus_mask Transform("gui/button/ending_idle.png")
        action Return()

    button at ending_dissolve:
        anchor (0.5,0.5)
        yalign 0.52
        xalign 0.5
        frame:
            background Null()
            xysize (473, 50)
            xalign 0.5
            ypos 10
            text "Save and quit.":
                font "Fonts/Sofia Pro Medium.ttf"
                color "#FFF"
                align (0.1, 0.5)
                yoffset 5
                size 28

        idle_background Transform("gui/button/ending_idle.png")
        hover_background Transform("gui/button/ending_hover.png")
        focus_mask Transform("gui/button/ending_idle.png")
        action MainMenu(confirm=False)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 1000003
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    fixed at stretch_ending:
        xsize 768
        ysize 1360
        ypos 0.5

        add "gui/textbox/ending textbox.png":
            pos (0.5, 0.6)
            anchor (0.5, 1.0)
            yzoom 0.8

        vbox at ending_dissolve:
            xalign 0.5
            ypos 470
            spacing 20
            xsize 450

            text "CONFIRMATION":
                xsize 450
                text_align 0.0
                size 33
                color "#000"
                font "Fonts/Sofia Pro Semi Bold Az.otf"

            text message:
                xsize 450
                text_align 0.0
                size 27
                line_spacing -5

        button at ending_dissolve:
            anchor (0.5,0.5)
            yalign 0.455
            xalign 0.5
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Yes.":
                    font "Fonts/Sofia Pro Medium.ttf"
                    color "#FFF"
                    align (0.05, 0.0)
                    yoffset 11
                    size 28
            idle_background Transform("gui/button/ending_idle.png")
            hover_background Transform("gui/button/ending_hover.png")
            focus_mask Transform("gui/button/ending_idle.png")
            action yes_action

        button at ending_dissolve:
            anchor (0.5,0.5)
            yalign 0.52
            xalign 0.5
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "No.":
                    font "Fonts/Sofia Pro Medium.ttf"
                    color "#FFF"
                    align (0.05, 0.0)
                    yoffset 11
                    size 28
            idle_background Transform("gui/button/ending_idle.png")
            hover_background Transform("gui/button/ending_hover.png")
            focus_mask Transform("gui/button/ending_idle.png")
            action no_action

        key "game_menu" action no_action
