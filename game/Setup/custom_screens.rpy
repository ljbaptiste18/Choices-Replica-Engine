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
    linear 0.4 alpha 0.5  # Fades in to 50% darkness

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

screen StatsUI():
    zorder 1000001
    add "gui/overlay/confirm.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Dominant Personality" size 35
                text "Blood/Shadow" size 35
                text "[Rowan] Nerve" size 35
                text "Amalia Relationship" size 35
                text "Amalia Romance" size 35
                text "Amalia Nerve" size 35
                text "Abel Relationship" size 35
                text "Abel Romance" size 35
                text "Abel Nerve" size 35
                text "Lincoln Relationship" size 35
                text "Lincoln Romance" size 35
                text "Lincoln Nerve" size 35
                text "Jocelyn Relationship" size 35
                text "Jocelyn Romance" size 35
                text "Jocelyn Nerve" size 35
                text "Connor Nerve" size 35
                text "Matthias Romance" size 35

            vbox:
                spacing 10
                text "[personality.dominant_trait!c]" size 35
                text "[human_leaning]/[power_leaning]" size 35
                text "[rowan_nerve]" size 35
                text "[amalia_relationship]" size 35

                if r_li == "Amalia":
                    text "[amalia_romance] (LI)" size 35
                else:
                    text "[amalia_romance]" size 35

                text "[amalia_nerve]" size 35
                text "[abel_relationship]" size 35

                if r_li == "Abel":
                    text "[abel_romance] (LI)" size 35
                else:
                    text "[abel_romance]" size 35

                text "[abel_nerve]" size 35
                text "[lincoln_relationship]" size 35

                if r_li == "Lincoln":
                    text "[lincoln_romance] (LI)" size 35
                else:
                    text "[lincoln_romance]" size 35

                text "[lincoln_nerve]" size 35
                text "[jocelyn_relationship]" size 35

                if r_li == "Jocelyn":
                    text "[jocelyn_romance] (LI)" size 35
                else:
                    text "[jocelyn_romance]" size 35

                text "[jocelyn_nerve]" size 35
                text "[connor_nerve]" size 35

                if matthias_confession_accepted and join_matthias:
                    text "[matthias_romance] (LI)" size 35
                elif matthias_confession_accepted:
                    text "[matthias_romance] (accepted)" size 35
                elif matthias_rejected:
                    text "[matthias_romance] (rejected)" size 35
                else:
                    text "[matthias_romance]" size 35

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "gui/return_%s.png"
        action Return()

screen ILITWStatsUI():
    zorder 1000001
    add "gui/overlay/confirm.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 20

            vbox:
                spacing 10

                text "IT LIVES IN THE WOODS" size 35
                text "[Devon] [Hunter]" size 35
                text "Noah" size 35
                text "Noah romance" size 35
                text "Andy" size 35
                text "Ava" size 35
                text "Lucas" size 35
                text "Stacy" size 35
                text "Dan" size 35
                text "Dan romance" size 35
                text "Lily" size 35

            vbox:
                spacing 10
                text "" size 35

                if hm == Devon:
                    text "human" size 35
                    text "ghost" size 35
                else:
                    text "ghost" size 35
                    text "human" size 35

                text "[noah_romance]" size 35

                if d_li == "Andy":
                    text "[Andy] (LI)" size 35
                else:
                    text "[Andy]" size 35

                if d_li == "Ava":
                    text "[Ava] (LI)" size 35
                else:
                    text "[Ava]" size 35

                if d_li == "Lucas":
                    text "[Lucas] (LI)" size 35
                else:
                    text "[Lucas]" size 35

                if d_li == "Stacy":
                    text "[Stacy] (LI)" size 35
                else:
                    text "[Stacy]" size 35

                text "[Dan]" size 35
                text "[dan_romance]" size 35
                text "[Lily]" size 35

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "gui/return_%s.png"
        action Return()

screen ILBStatsUI():
    zorder 1000001
    add "gui/overlay/confirm.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 20

            vbox:
                spacing 10

                text "IT LIVES BENEATH" size 35
                text "[Harper] Vance" size 35
                text "Grandpa" size 35
                text "Tom" size 35
                text "Imogen" size 35
                text "Danni" size 35
                text "Parker" size 35

            vbox:
                spacing 10
                text "" size 35
                text "[harper_status]" size 35
                text "[Grandpa]" size 35

                if h_li == "Tom":
                    text "[Tom] (LI)" size 35
                else:
                    text "[Tom]" size 35

                if h_li == "Imogen":
                    text "[Imogen] (LI)" size 35
                else:
                    text "[Imogen]" size 35

                if h_li == "Danni":
                    text "[Danni] (LI)" size 35
                else:
                    text "[Danni]" size 35

                if h_li == "Parker":
                    text "[Parker] (LI)" size 35
                else:
                    text "[Parker]" size 35

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "gui/return_%s.png"
        action Return()

screen traits():
    zorder 1000000

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("{color=#a40909}{font=fonts/TTSupermolotNeue-ExtraBold.ttf}{size=45}TRAITS")):

        vbox:
            xpos 50
            ypos 100

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Musician."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_musician:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_musician", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Artist."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_artist:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_artist", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Computer whiz."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_computer:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_computer", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Handy."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_handy:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_handy", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Athlete."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_athlete:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_athlete", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Fiction lover."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_fiction:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_fiction", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Scientist."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_scientist:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_scientist", True, False)
                        yoffset 25

            null height 40

            hbox:
                xfill True
                frame:
                    xsize 300
                    background None
                    padding (0, 0)

                    text "{color=#888888}Activist."

                frame:
                    xsize 100
                    background None
                    padding (0, 0)
                    imagebutton at Transform(zoom=0.75):
                        if trait_activist:
                            idle "gui/button/button_on.png"
                        else:
                            idle "gui/button/button_off.png"

                        action ToggleVariable("trait_activist", True, False)
                        yoffset 25

            null height 40

screen variables():
    zorder 1000000

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("{color=#a40909}{font=fonts/TTSupermolotNeue-ExtraBold.ttf}{size=45}VARIABLES"), scroll=("viewport")):

        vbox:
            xpos 50
            xsize 450
            spacing 15

            text "Who is Redfield?":
                color "#FFF"

            hbox:
                xsize 300

                textbutton "Noah.":
                    action [
                        SetVariable("rf","Noah"),
                        SetVariable("rf_ln","Marshall"),
                        SetVariable("rf_she","he"),
                        SetVariable("rf_her_pos","his"),
                        SetVariable("rf_her","him"),
                        SetVariable("rf_hers","his"),
                        SetVariable("rf_herself","himself"),
                        SetVariable("hm",Devon),
                        SetVariable("hm_ln",Hunter),
                        SetVariable("hm_she",devon_she),
                        SetVariable("hm_her_pos",devon_her_pos),
                        SetVariable("hm_her",devon_her),
                        SetVariable("hm_hers",devon_hers),
                        SetVariable("hm_herself",devon_herself)
                    ]
                    selected rf == "Noah"

                textbutton "[Devon].":
                    action [
                        SetVariable("rf",Devon),
                        SetVariable("rf_ln",Hunter),
                        SetVariable("rf_she",devon_she),
                        SetVariable("rf_her_pos",devon_her_pos),
                        SetVariable("rf_her",devon_her),
                        SetVariable("rf_hers",devon_hers),
                        SetVariable("rf_herself",devon_herself),
                        SetVariable("hm","Noah"),
                        SetVariable("hm_ln","Marshall"),
                        SetVariable("hm_she","he"),
                        SetVariable("hm_her_pos","his"),
                        SetVariable("hm_her","him"),
                        SetVariable("hm_hers","his"),
                        SetVariable("hm_herself","himself")
                    ]
                    selected rf == Devon

            text "Who lived in ILITW?":
                color "#FFF"

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "Andy"
                    textbutton "[Andy!c]":
                        action [
                            If(
                                Andy == "alive",
                                [
                                    SetVariable("Andy","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Andy","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                        ]

                vbox:
                    spacing 5
                    text "Ava"
                    textbutton "[Ava!c]":
                        action [
                            If(
                                Ava == "alive",
                                [
                                    SetVariable("Ava","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Ava","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                                ToggleVariable("witch","Sunny","Ava"),
                                ToggleVariable("witch_she","they","she"),
                                ToggleVariable("witch_she_was","they were","she was"),
                                ToggleVariable("witch_shes","they've","she's"),
                                ToggleVariable("witch_her_pos","their","her"),
                                ToggleVariable("witch_her","them","her"),
                                ToggleVariable("witch_hers","theirs","hers"),
                                ToggleVariable("witch_herself","herself","themself")
                            ]

                vbox:
                    spacing 5
                    text "Dan"
                    textbutton "[Dan!c]":
                        action [
                            If(
                                Dan == "alive",
                                [
                                    SetVariable("Dan","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Dan","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                        ]

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "Lily"
                    textbutton "[Lily!c]":
                        action [
                            If(
                                Lily == "alive",
                                [
                                    SetVariable("Lily","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Lily","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                        ]

                vbox:
                    spacing 5
                    text "Lucas"
                    textbutton "[Lucas!c]":
                        action [
                            If(
                                Lucas == "alive",
                                [
                                    SetVariable("Lucas","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Lucas","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                        ]

                vbox:
                    spacing 5
                    text "Stacy"
                    textbutton "[Stacy!c]":
                        action [
                            If(
                                Stacy == "alive",
                                [
                                    SetVariable("Stacy","dead"),
                                    SetVariable("ilitw_dead", ilitw_dead + 1),
                                    SetVariable("ilitw_alive", ilitw_alive - 1)
                                ],
                                [
                                    SetVariable("Stacy","alive"),
                                    SetVariable("ilitw_dead", ilitw_dead - 1),
                                    SetVariable("ilitw_alive", ilitw_alive + 1)
                                ]
                            ),
                        ]

            text "Who is [Devon]'s LI?":
                color "#FFF"

            grid 3 2:
                xsize 300

                textbutton "Andy.":
                    action [
                        SetVariable("d_li","Andy"),
                        SetVariable("d_li_ln", "Kang"),
                        SetVariable("d_li_she", "he"),
                        SetVariable("d_li_her_pos","his"),
                        SetVariable("d_li_her","him"),
                        SetVariable("d_li_hers","his"),
                        SetVariable("d_li_herself","himself"),
                        SetVariable("d_li_girl","boy"),
                        SetVariable("d_li_girlfriend","boyfriend"),
                        SetVariable("d_li_state","alive" if Andy == "alive" else "dead")
                    ]

                    selected d_li == "Andy"
                textbutton "Ava.":
                    action [
                        SetVariable("d_li","Ava"),
                        SetVariable("d_li_ln", "Cunningham"),
                        SetVariable("d_li_she", "she"),
                        SetVariable("d_li_her_pos","her"),
                        SetVariable("d_li_her","her"),
                        SetVariable("d_li_hers","hers"),
                        SetVariable("d_li_herself","herself"),
                        SetVariable("d_li_girl","girl"),
                        SetVariable("d_li_girlfriend","girlfriend"),
                        SetVariable("d_li_state","alive" if Stacy == "alive" else "dead")
                    ]
                    selected d_li == "Ava"

                textbutton "Connor.":
                    action [
                        SetVariable("d_li","Connor"),
                        SetVariable("d_li_ln", "Green"),
                        SetVariable("d_li_she", "he"),
                        SetVariable("d_li_her_pos","his"),
                        SetVariable("d_li_her","him"),
                        SetVariable("d_li_hers","his"),
                        SetVariable("d_li_herself","himself"),
                        SetVariable("d_li_girl","boy"),
                        SetVariable("d_li_girlfriend","boyfriend"),
                        SetVariable("d_li_state","Connor")
                    ]
                    selected d_li == "Connor"

                textbutton "Lucas.":
                    action [
                        SetVariable("d_li","Lucas"),
                        SetVariable("d_li_ln", "Thomas"),
                        SetVariable("d_li_she", "he"),
                        SetVariable("d_li_her_pos","his"),
                        SetVariable("d_li_her","him"),
                        SetVariable("d_li_hers","his"),
                        SetVariable("d_li_herself","himself"),
                        SetVariable("d_li_girl","boy"),
                        SetVariable("d_li_girlfriend","boyfriend"),
                        SetVariable("d_li_state","alive" if Lucas == "alive" else "dead")
                    ]
                    selected d_li == "Lucas"

                textbutton "Stacy.":
                    action [
                        SetVariable("d_li","Stacy"),
                        SetVariable("d_li_ln", "Green"),
                        SetVariable("d_li_she", "she"),
                        SetVariable("d_li_her_pos","her"),
                        SetVariable("d_li_her","her"),
                        SetVariable("d_li_hers","hers"),
                        SetVariable("d_li_herself","herself"),
                        SetVariable("d_li_girl","girl"),
                        SetVariable("d_li_girlfriend","girlfriend"),
                        SetVariable("d_li_state","alive" if Stacy == "alive" else "dead")
                    ]
                    selected d_li == "Stacy"

                textbutton "None." action SetVariable("d_li","none")

            text "Who lived in ILB?":
                color "#FFF"

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "[Harper]"
                    textbutton "[harper_status!c]" action ToggleVariable("harper_status","dead","alive")
                vbox:
                    spacing 5
                    text "Danni"
                    textbutton "[Danni!c]":
                        action [
                            ToggleVariable("Danni","dead","alive"),
                            If(Tom == "dead", SetVariable("Tom","alive"),
                            If(Imogen == "dead", SetVariable("Imogen","alive"),
                            If(Parker == "dead", SetVariable("Parker","alive")))),
                        ]

                vbox:
                    spacing 5
                    text "Imogen"
                    textbutton "[Imogen!c]":
                        action [
                            ToggleVariable("Imogen","dead","alive"),
                            If(Tom == "dead", SetVariable("Tom","alive"),
                            If(Danni == "dead", SetVariable("Danni","alive"),
                            If(Parker == "dead", SetVariable("Parker","alive")))),
                        ]

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "Parker"
                    textbutton "[Parker!c]":
                        action [
                            If(
                                Parker == "alive",
                                [
                                    SetVariable("Parker", "dead"),

                                    If(Tom == "dead", SetVariable("Tom","alive")),
                                    If(Danni == "dead", SetVariable("Danni","alive")),
                                    If(Imogen == "dead", SetVariable("Imogen","alive")),
                                ],
                                If(
                                    Parker == "dead",
                                    SetVariable("Parker", "runaway"),
                                    SetVariable("Parker", "alive")
                                )
                            )
                        ]

                vbox:
                    spacing 5
                    text "Tom"
                    textbutton "[Tom!c]":
                        action [
                            ToggleVariable("Tom","dead","alive"),
                            If(Imogen == "dead", SetVariable("Imogen","alive"),
                            If(Danni == "dead", SetVariable("Danni","alive"),
                            If(Parker == "dead", SetVariable("Parker","alive")))),
                        ]

            text "Who is [Harper]'s LI?":
                color "#FFF"

            grid 3 2:
                xsize 300
                spacing 10

                textbutton "Danni.":
                    action [
                        SetVariable("h_li","Danni"),
                        SetVariable("h_li_ln", "Asturias"),
                        SetVariable("h_li_she", "she"),
                        SetVariable("h_li_her_pos","her"),
                        SetVariable("h_li_her","her"),
                        SetVariable("h_li_hers","hers"),
                        SetVariable("h_li_herself","herself"),
                        SetVariable("h_li_girl","girl"),
                        SetVariable("h_li_girlfriend","girlfriend"),
                        SetVariable("h_li_state","alive" if Danni == "alive" else "dead")
                    ]
                    selected h_li == "Danni"

                textbutton "Imogen.":
                    action [
                        SetVariable("h_li","Imogen"),
                        SetVariable("h_li_ln", "Wescott"),
                        SetVariable("h_li_she", "she"),
                        SetVariable("h_li_her_pos","her"),
                        SetVariable("h_li_her","her"),
                        SetVariable("h_li_hers","hers"),
                        SetVariable("h_li_herself","herself"),
                        SetVariable("h_li_girl","girl"),
                        SetVariable("h_li_girlfriend","girlfriend"),
                        SetVariable("h_li_state","alive" if Imogen == "alive" else "dead")
                    ]
                    selected h_li == "Imogen"

                textbutton "Parker.":
                    action [
                        SetVariable("h_li","Parker"),
                        SetVariable("h_li_ln", "Shaw"),
                        SetVariable("h_li_she", "he"),
                        SetVariable("h_li_her_pos","his"),
                        SetVariable("h_li_her","him"),
                        SetVariable("h_li_hers","his"),
                        SetVariable("h_li_herself","himself"),
                        SetVariable("h_li_girl","boy"),
                        SetVariable("h_li_girlfriend","boyfriend"),
                        SetVariable("h_li_state","alive" if Parker == "alive" else "dead")
                    ]
                    selected h_li == "Parker"

                textbutton "Tom.":
                    action [
                        SetVariable("h_li","Tom"),
                        SetVariable("h_li_ln", "Sato"),
                        SetVariable("h_li_she", "he"),
                        SetVariable("h_li_her_pos","his"),
                        SetVariable("h_li_her","him"),
                        SetVariable("h_li_hers","his"),
                        SetVariable("h_li_herself","himself"),
                        SetVariable("h_li_girl","boy"),
                        SetVariable("h_li_girlfriend","boyfriend"),
                        SetVariable("h_li_state","alive" if Tom == "alive" else "dead")
                    ]
                    selected h_li == "Tom"

                textbutton "None." action SetVariable("h_li","none")

            text "What collectibles do you have?":
                color "#FFF"

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "Gauntlet"
                    textbutton "[connor_collectible!c]" action ToggleVariable("connor_collectible","True","False")
                vbox:
                    spacing 5
                    text "Whip"
                    textbutton "[jocelyn_collectible!c]" action ToggleVariable("jocelyn_collectible","True","False")
                vbox:
                    spacing 5
                    text "Watch"
                    textbutton "[lincoln_collectible!c]" action ToggleVariable("lincoln_collectible","True","False")

            hbox:
                spacing 25
                vbox:
                    spacing 5
                    text "Moss"
                    textbutton "[rowan_collectible!c]" action ToggleVariable("rowan_collectible","True","False")

                vbox:
                    spacing 5
                    text "Shield"
                    textbutton "[abel_collectible!c]" action ToggleVariable("abel_collectible","True","False")

            text "Shadow points: [power_leaning]"
            bar value FieldValue(store, "power_leaning", 25) xmaximum 400

            text "Blood points: [human_leaning]"
            bar value FieldValue(store, "human_leaning", 25) xmaximum 400

            text "Genuine Points: [personality.genuine]"
            bar value FieldValue(store, "personality.genuine", 60) xmaximum 400

            text "Sarcastic Points: [personality.sarcastic]"
            bar value FieldValue(store, "personality.sarcastic", 60) xmaximum 400

            text "Aggressive Points: [personality.aggressive]"
            bar value FieldValue(store, "personality.aggressive", 60) xmaximum 400

            text "Abel Relationship: [abel_relationship]"
            bar value FieldValue(store, "abel_relationship", 100) xmaximum 400

            text "Abel Nerve: [abel_nerve]"
            bar value FieldValue(store, "abel_nerve", 100) xmaximum 400

            text "Amalia Relationship: [amalia_relationship]"
            bar value FieldValue(store, "amalia_relationship", 100) xmaximum 400

            text "Amalia Nerve: [amalia_nerve]"
            bar value FieldValue(store, "amalia_nerve", 100) xmaximum 400

            text "Jocelyn Relationship: [jocelyn_relationship]"
            bar value FieldValue(store, "jocelyn_relationship", 100) xmaximum 400

            text "Jocelyn Nerve: [jocelyn_nerve]"
            bar value FieldValue(store, "jocelyn_nerve", 100) xmaximum 400

            text "Lincoln Relationship: [lincoln_relationship]"
            bar value FieldValue(store, "lincoln_relationship", 100) xmaximum 400

            text "Lincoln Nerve: [lincoln_nerve]"
            bar value FieldValue(store, "lincoln_nerve", 100) xmaximum 400

            text "Connor Nerve: [connor_nerve]"
            bar value FieldValue(store, "connor_nerve", 100) xmaximum 400

            text "Rowan Nerve: [rowan_nerve]"
            bar value FieldValue(store, "rowan_nerve", 100) xmaximum 400

            null height 5
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

# for ch 12

screen direction_arrow(direction):
    if direction == "left":
        text _("Left!") at direction_arrow_transform_text:
            size 30 color "#ffffff"
        add "images/Nerve Icons/point loss.png" at direction_arrow_transform_rotate
    elif direction == "right":
        text _("Right!") at direction_arrow_transform_text:
            size 30 color "#ffffff"
        add "images/Nerve Icons/point gain.png" at direction_arrow_transform_rotate
    elif direction == "forward":
        text _("Forward!") at direction_arrow_transform_text:
            size 30 color "#ffffff"
        add "images/Nerve Icons/point gain.png" at direction_arrow_transform
    else:
        text _("Backward!") at direction_arrow_transform_text:
            size 30 color "#ffffff"
        add "images/Nerve Icons/point loss.png" at direction_arrow_transform

transform direction_arrow_transform:
    alpha 0
    pause 0.5
    zoom .8
    xalign 0.62
    xanchor (0.5)
    yanchor (0.5)
    ypos 400
    ease 0.25 zoom 1.5 alpha .8
    ease .25 zoom 1 alpha 1
    easeout 2.0 ypos -100 alpha .3

    on hide:
        alpha 0

transform direction_arrow_transform_rotate:
    alpha 0
    rotate 90
    pause 0.5
    zoom .8
    xalign 0.62
    xanchor (0.5)
    yanchor (0.5)
    ypos 400
    ease 0.25 zoom 1.5 alpha .8
    ease .25 zoom 1 alpha 1
    easeout 2.0 ypos -100 alpha .3

    on hide:
        alpha 0

transform direction_arrow_transform_text:
    alpha 0
    pause 0.5
    zoom .9
    xanchor -550
    ypos 380
    ease 0.25 zoom 1.2 alpha .8
    ease .25 zoom 1 alpha 1
    easeout 2.0 ypos -100 alpha .3

    on hide:
        alpha 0

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

screen LI_ILITW():
    default move = truecenter
    default show_textbox = True
    default move_direction = None
    zorder 1000000
    modal True

    add "full [current_LI!l]" at move

    add "gui/textbox/bottom2menu.png" at (stretch_show_only if closet_choice_expanded and show_textbox else (stretch_hide if not closet_choice_expanded else (box_left if move_direction == "left" else box_right))):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)
        yzoom 0.8

    if closet_choice_expanded:
        text "I loved..." xalign 0.5 ypos 1005 size 35 color "#FFF" at (message_show if show_textbox else message_hide)

        $ total = len(get_devon_LI())
        $ spacing = 0.04
        $ start = 0.5 - ((total - 1) * spacing / 2.0)

        for i, option in enumerate(get_devon_LI()):
            $ xpos = start + i * spacing

            add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

            if (current_LI == option):
                add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

        button at (choice_in_animation if show_textbox else (box_left if move_direction == "left" else box_right)):
            anchor (0.5,0.5)
            yalign 0.830
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "[li_message]":
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    line_spacing -5
                    xpos 0.12
                    if len(li_message) > 40:
                        yanchor 0.25
                    else:
                        yanchor 0.0

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Return() keysym "K_RETURN"

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
                SetScreenVariable("move", move_right(PrevILITW_LI, SetScreenVariable("move", truecenter)))
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
                SetScreenVariable("move", move_left(NextILITW_LI, SetScreenVariable("move", truecenter)))
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

screen LI_ILB():
    default move = truecenter
    default show_textbox = True
    default move_direction = None

    zorder 1000000
    modal True

    add "full [current_LI!l]" at move

    add "gui/textbox/bottom2menu.png" at (stretch_show_only if closet_choice_expanded and show_textbox else (stretch_hide if not closet_choice_expanded else (box_left if move_direction == "left" else box_right))):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)
        yzoom 0.8

    if closet_choice_expanded:
        text "I loved..." xalign 0.5 ypos 1005 size 35 color "#FFF" at (message_show if show_textbox else message_hide)

        $ total = len(get_harper_LI())
        $ spacing = 0.04
        $ start = 0.5 - ((total - 1) * spacing / 2.0)

        for i, option in enumerate(get_harper_LI()):
            $ xpos = start + i * spacing

            add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

            if (current_LI == option):
                add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

        button at (choice_in_animation if show_textbox else (box_left if move_direction == "left" else box_right)):
            anchor (0.5,0.5)
            yalign 0.830
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "[li_message]":
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    line_spacing -5
                    xpos 0.12
                    if len(li_message) > 40:
                        yanchor 0.25
                    else:
                        yanchor 0.0

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action Return() keysym "K_RETURN"

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
                SetScreenVariable("move", move_right(PrevILB_LI, SetScreenVariable("move", truecenter)))
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
                SetScreenVariable("move", move_left(NextILB_LI, SetScreenVariable("move", truecenter)))
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

screen timing_bar_game(target_start=0.4, target_end=0.6, speed=0.02):

    add "gui/overlay/confirm.png" at item_dissolve

    add "images/items/item_bubble.webp" at hexagon_in:
        pos (0.55,0.47)

    image "images/items/stop_button.png" at item_in:
        pos (0.5,0.45)

    text "STOP IN THE YELLOW" at item_dissolve:
        font "Fonts/TTSupermolotNeue-ExtraBold.ttf"
        color '#FFFFFF'
        kerning 1.5
        size 45
        xalign 0.5
        yalign 0.73

    ##timer bar
    default pos = 0.0
    default direction = 1

    # move the marker
    timer 0.016 repeat True action SetScreenVariable("pos", pos + direction * speed)

    if pos >= 1.0:
        $ direction = -1
    elif pos <= 0.0:
        $ direction = 1

    # The container
    fixed:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 40

        # Base black background
        add Solid("#888888") xpos 0 ypos 380 xsize 600 ysize 40
        # Yellow target zone
        add Solid("#ffaa00") xpos int(600 * target_start) ypos 380 xsize int(600 * (target_end - target_start)) ysize 40
        # White moving bar
        add Solid("#ffffff") xpos int(600 * pos) - 4 ypos 380 xsize 8 ysize 40

    button at choice_item_display:
        anchor (0.5,0.5)
        yalign 0.845
        xalign 0.41
        frame:
            background Null()
            xysize (500, 50)
            ypos 10
            text "Push the button!":
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

        action [
            SetVariable("timing_stop", (pos >= target_start and pos <= target_end)),
            Return()
        ]

#screen autosave_indicator():
#    zorder 9999
#    timer 1.5 action [Function(renpy.transition, Dissolve(0.3)), Hide("autosave_indicator")]
#    frame:
#        xalign 1.0
#        yalign 1.0
#        xoffset -20
#        yoffset -20
#        background None
#        hbox:
#            spacing 8
#            add At("gui/save_icon.png", autosave_wobble):
#                anchor (0.5, 0.5)
#                pos (1.4, 0.2)
#                zoom 0.8
#            text "Saving...":
#                color "#FFFF"
#                pos (1, .5)
#                size 20

init python:  # saves
    import time

    # --- Force autosave and wait until confirmed written ---
    def force_autosave_sync(timeout=2.0, interval=0.1):
        autosave_name()
        renpy.force_autosave()
        deadline = time.time() + timeout
        while time.time() < deadline:
            slot = renpy.newest_slot(r"auto-\d+")
            if slot and renpy.slot_mtime(slot):
                break
            renpy.pause(interval, hard=True)

    # --- Periodic autosave: saves every N interactions ---
    _interaction_count = 0  # <---- define it here
    _AUTOSAVE_EVERY = 2  # save every 2 interactions

    # Screens or situations to exclude from autosave
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
        # add other custom screens here
    }

    _autosave_initialized = False  # skip autosave on first interaction after start

    def _periodic_autosave():
        global _interaction_count, _autosave_initialized

        # Skip first interaction after game start
        if not _autosave_initialized:
            _autosave_initialized = True
            return

        # Only autosave in gameplay context (not menu, screen, or rollback)
        if renpy.context()._main_menu:
            return
        current = renpy.current_screen()
        if current in AUTOSAVE_EXCLUDED_SCREENS:
            return
        # Increment and save if threshold reached
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
        xsize 768   ## match your game's resolution
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

##collectibles screen
image collectibles screen = Flatten(Composite(
    (768, 1360),
        (0, 0), "images/collectibles/collectible_screen.png",
        (0, 0), ConditionSwitch(
            "lore_doc_1", "images/collectibles/lore_doc_1.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_2", "images/collectibles/lore_doc_2.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_3", "images/collectibles/lore_doc_3.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_4", "images/collectibles/lore_doc_4.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_5", "images/collectibles/lore_doc_5.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_6", "images/collectibles/lore_doc_6.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_7", "images/collectibles/lore_doc_7.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_8", "images/collectibles/lore_doc_8.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lore_doc_9", "images/collectibles/lore_doc_9.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "abel_collectible", "images/collectibles/abel_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "connor_collectible", "images/collectibles/connor_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "lincoln_collectible", "images/collectibles/lincoln_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "jocelyn_collectible", "images/collectibles/jocelyn_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "amalia_collectible", "images/collectibles/amalia_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "rowan_collectible", "images/collectibles/rowan_collectible_True.png",
            "True", Null()
        ),
        (0, 0), ConditionSwitch(
            "rod_collectible", "images/collectibles/rod_collectible_True.png",
            "True", Null()
        )
))

image joss_cg = Flatten(Composite(
    (769, 1350),
        (0, 0), "images/CGs/joss cg/joss_cg.jpg",
        (0, 0), "images/CGs/joss cg/joss_cg_[jocelyn_collectible].png",
        (0, 0), "images/CGs/joss cg/joss_cg_[matthias_age].png",
))
image matthias blood cg = Flatten(Composite(
    (769, 1350),
        (0, 0), "images/CGs/blood_end_base.jpg",
        (0, 0), "images/CGs/blood_end_[matthias_age].png",
))
image matthias shadow cg:
    contains:
        "images/CGs/matt cg shadow/matt_cg_1.png" with Dissolve(0.5)
        2.0
        "images/CGs/matt cg shadow/matt_cg_2.png" with Dissolve(0.5)
        2.0
        "images/CGs/matt cg shadow/matt_cg_3.png" with Dissolve(0.5)
        2.0
        repeat
