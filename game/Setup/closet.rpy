default item_name = None

screen show_closet_with_flash():
    modal True
    add "images/backgrounds/closet.webp"
    zorder 1000000
    add "#FCFBFC" at screen_flash
    timer 0.3 action [
        If(not item_selected and item_name != RowanHair, ShowMenu("ChooseMCAsset")),
        If(item_name == RowanHair, ShowMenu("hair_rowan")),
        If(item_selected, ShowMenu("item_selected", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))),
        Hide("show_closet_with_flash")]

screen hide_closet_with_flash():
    modal True
    add "images/backgrounds/closet.webp"
    zorder 1000000
    add "#FCFBFC" at screen_flash
    timer 0.3 action [
        Hide("hide_closet_with_flash"),
        If(item_name == RowanUndies, SetVariable("rowan_undies", AssetStored)),
        If(item_name == RowanOutfit, SetVariable("rowan_outfit", AssetStored)),
        If(item_name == RowanHijab, SetVariable("rowan_hijab", AssetStored)),
        If(item_name == RowanGlasses, SetVariable("rowan_glasses_type", AssetStored)),
        If(item_name == RowanPiercings, SetVariable("rowan_ear_piercing", AssetStored)),
        Function(open_correct_rowan_menu)
    ]

screen closet():
    default screen_page = 1
    default closet_show = True
    zorder 1000000

    modal True

    add "images/backgrounds/closet.webp"
    add "full rowan"

    add "gui/textbox/bottom3menu.png" at (None if PrevScreen else (stretch_show_only if closet_choice_expanded else stretch_hide)):
        yzoom .95
        pos (0.5, 0.94)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text "CUSTOMIZE" xalign 0.5 ypos 890 font gui.name_text_font size 35 color "#FFF" at message_show
        if screen_page == 1:
            if (rowan_outfit_on == "casual" or rowan_outfit_on == "beach") and rowan_outfit != "Fight":
                button at choice_in1:
                    anchor (0.5,0.5)
                    yalign 0.72
                    xpos 0.4
                    frame:
                        background Null()
                        xysize (473, 50)
                        xalign 0.5
                        ypos 10
                        text "Outfits.":
                            size 31
                            ypos 10
                            xpos 30

                    idle_background Transform("gui/small_button_idle.png")
                    hover_background Transform("gui/small_button_hover.png")
                    focus_mask Transform("gui/small_button_idle.png")

                    if rowan_outfit_on == "beach":
                        action [
                            Hide("closet"),
                            SetVariable("item_name", RowanBeach),
                            SetVariable("item_description", RowanBeachDescription),
                            SetVariable("AssetCount", get_rowan_beach_options),
                            SetVariable("AssetSelected", rowan_beach_selected),
                            SetVariable("PrevMCAsset", PrevRowanBeach),
                            SetVariable("NextMCAsset", NextRowanBeach),
                            SetVariable("AssetStored", rowan_beach),
                            ShowMenu("show_closet_with_flash")
                            ]
                    else:
                        action [
                            Hide("closet"),
                            SetVariable("item_name", RowanOutfit),
                            SetVariable("item_description", RowanOutfitDescription),
                            SetVariable("AssetCount", get_rowan_outfit_options),
                            SetVariable("AssetSelected", rowan_outfit_selected),
                            SetVariable("PrevMCAsset", PrevRowanOutfit),
                            SetVariable("NextMCAsset", NextRowanOutfit),
                            SetVariable("AssetStored", rowan_outfit),
                            ShowMenu("show_closet_with_flash")
                            ]

            else:
                button at choice_in1:
                    anchor (0.5,0.5)
                    yalign 0.71
                    xpos 0.4
                    sensitive False
                    action NullAction()
                    frame:
                        background Transform("gui/small_button_gray.png", alpha=0.8)
                        xysize (473, 50)
                        xalign 0.3
                        ypos 10
                        text "Outfits.":
                            size 31
                            ypos 20
                            xpos 30
                            color "#5F5F5F"

            button at choice_in3:
                anchor (0.5,0.5)
                yalign 0.8
                xpos 0.4
                frame:
                    background Null()
                    xysize (473, 50)
                    xalign 0.5
                    ypos 10
                    text "Underwear.":
                        size 31
                        ypos 10
                        xpos 30

                idle_background Transform("gui/small_button_idle.png")
                hover_background Transform("gui/small_button_hover.png")
                focus_mask Transform("gui/small_button_idle.png")
                action [
                    Hide("closet"),
                    SetVariable("item_name", RowanUndies),
                    SetVariable("item_description", RowanUndiesDescription),
                    SetVariable("AssetCount", get_rowan_undies_options),
                    SetVariable("AssetSelected", rowan_undies_selected),
                    SetVariable("PrevMCAsset", PrevRowanUndies),
                    SetVariable("NextMCAsset", NextRowanUndies),
                    SetVariable("AssetStored", rowan_undies),
                    ShowMenu("show_closet_with_flash")
                    ]

            button at choice_in2:
                anchor (0.5,0.5)
                yalign 0.72
                xpos .82
                frame:
                    background Null()
                    xysize (473, 50)
                    xalign 0.5
                    ypos 10
                    text "Hairstyles.":
                        size 31
                        ypos 10
                        xpos 30

                idle_background Transform("gui/small_button_idle.png")
                hover_background Transform("gui/small_button_hover.png")
                focus_mask Transform("gui/small_button_idle.png")
                action [
                    Hide("closet"),
                    SetVariable("PrevScreen", True),
                    SetVariable("AssetStored", rowan_hair),
                    SetVariable("HairTypeStored", hair_type),
                    SetVariable("item_name", RowanHair),
                    ShowMenu("hair_rowan_length")
                ]

            button at choice_in4:
                anchor (0.5,0.5)
                yalign 0.8
                xpos .82
                frame:
                    background Null()
                    xysize (473, 50)
                    xalign 0.5
                    ypos 10
                    text "Accessories.":
                        size 31
                        ypos 10
                        xpos 30

                idle_background Transform("gui/small_button_idle.png")
                hover_background Transform("gui/small_button_hover.png")
                focus_mask Transform("gui/small_button_idle.png")
                action [
                    SetVariable("PrevScreen", True),
                    Hide("closet"),
                    ShowMenu("accessories_rowan_game")
                ]

        else:
            button at choice_in1:
                anchor (0.5,0.5)
                yalign 0.72
                xpos .42
                frame:
                    background Null()
                    xysize (473, 50)
                    xalign 0.5
                    ypos 10
                    if not stubble:
                        text "Add stubble":
                            size 31
                            ypos 10
                            xpos 30
                    else:
                        text "Remove stubble":
                            size 31
                            ypos 10
                            xpos 30

                idle_background Transform("gui/small_button_idle.png")
                hover_background Transform("gui/small_button_hover.png")
                focus_mask Transform("gui/small_button_idle.png")
                action SetVariable("stubble", True if not stubble else False)

            if hijab:
                if rowan_outfit_on != "pjs":
                    button at choice_in2:
                        anchor (0.5,0.5)
                        yalign 0.72
                        xpos 0.82
                        frame:
                            background Null()
                            xysize (473, 50)
                            xalign 0.5
                            ypos 10
                            text "Hijab.":
                                size 31
                                ypos 10
                                xpos 30


                        idle_background Transform("gui/small_button_idle.png")
                        hover_background Transform("gui/small_button_hover.png")
                        focus_mask Transform("gui/small_button_idle.png")
                        action [
                            Hide("closet"),
                            SetVariable("item_name", RowanHijab),
                            SetVariable("item_description", RowanHijabDescription),
                            SetVariable("AssetCount", get_rowan_hijab_options),
                            SetVariable("AssetSelected", rowan_hijab_selected),
                            SetVariable("PrevMCAsset", PrevRowanHijab),
                            SetVariable("NextMCAsset", NextRowanHijab),
                            SetVariable("AssetStored", rowan_hijab),
                            ShowMenu("show_closet_with_flash")
                            ]
                else:
                    button at choice_in2:
                        anchor (0.5,0.5)
                        yalign 0.712
                        xpos 0.82
                        sensitive False
                        action NullAction()
                        frame:
                            background Transform("gui/small_button_gray.png", alpha=0.8)
                            xysize (473, 50)
                            xalign 0.3
                            ypos 10
                            text "Hijab.":
                                size 31
                                ypos 20
                                xpos 30
                                color "#5F5F5F"

        button at choice_in5:
            anchor (0.5,0.5)
            yalign 0.88
            xpos .4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "{color=#FFFFFF}Return to \ngame.":
                    size 29
                    ypos -5
                    xpos 60
                    line_spacing -10
                add "gui/arrow_back.png":
                    ypos -15
                    xpos 15

            idle_background Transform("gui/closet_return_idle.png")
            hover_background Transform("gui/closet_return_hover.png")
            focus_mask Transform("gui/closet_return_idle.png")
            action [
                SetVariable("closet", False),
                Show("hide_screens_fade")
            ]
            keysym "K_ESCAPE"

        button at choice_in6:
            anchor (0.5,0.5)
            yalign 0.88
            xpos .82
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10

                if screen_page == 1:
                    text "{color=#FFFFFF}More 1/2":
                        size 31
                        ypos 10
                        xpos 30
                else:
                    text "{color=#FFFFFF}Previous 2/2":
                        size 31
                        ypos 10
                        xpos 30

                add "gui/arrow_next.png":
                    ypos -15
                    xpos 245

            idle_background Transform("gui/closet_return_idle.png")
            hover_background Transform("gui/closet_return_hover.png")
            focus_mask Transform("gui/closet_return_idle.png")
            action SetScreenVariable("screen_page", 1 if screen_page == 2 else 2)

        imagebutton at message_show:
            xalign 0.895
            yalign 0.68
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action [
                SetVariable("closet_choice_expanded", False),
                SetVariable("PrevScreen", False)
            ]

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen hair_rowan_length():
    default move = truecenter
    default show_textbox = True
    $ hair_return = False

    zorder 1000000
    modal True

    add "images/backgrounds/closet.webp"
    add "full rowan no hijab" at move

    add "gui/textbox/bottom3menu.png" at (None if PrevScreen else stretch_show_only if closet_choice_expanded else stretch_hide):
        yzoom .95
        pos (0.5, 0.94)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text "What length do you want?" at message_show:
            font "Fonts/Sofia Pro Medium.ttf"
            color '#FFFFFF'
            kerning 1.5
            size 33
            xalign 0.5
            ypos 890

        button at choice_in1:
            anchor (0.5,0.5)
            yalign 0.72
            xpos 0.4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Short.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [
                SetVariable("hair_type", "short"),
                If(hair_type != "short", SetVariable("rowan_hair", 0)),
                Hide("hair_rowan_length"),
                ShowMenu("show_closet_with_flash")
            ]

        button at choice_in3:
            anchor (0.5,0.5)
            yalign 0.8
            xpos 0.4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Long.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [
                SetVariable("hair_type", "long"),
                If(hair_type != "long", SetVariable("rowan_hair", 0)),
                Hide("hair_rowan_length"),
                ShowMenu("show_closet_with_flash")
            ]

        button at choice_in2:
            anchor (0.5,0.5)
            yalign 0.72
            xpos .82
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Medium.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [
                SetVariable("hair_type", "medium"),
                If(hair_type != "medium", SetVariable("rowan_hair", 0)),
                Hide("hair_rowan_length"),
                ShowMenu("show_closet_with_flash")
            ]

        button at choice_in5:
            anchor (0.5,0.5)
            yalign 0.88
            xpos .4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "{color=#FFFFFF}Return.":
                    size 31
                    ypos 10
                    xpos 60

                add "gui/arrow_back.png":
                    ypos -15
                    xpos 15

            idle_background Transform("gui/closet_return_idle.png")
            hover_background Transform("gui/closet_return_hover.png")
            focus_mask Transform("gui/closet_return_idle.png")
            action [
                SetVariable("rowan_hair", AssetStored),
                SetVariable("hair_type", HairTypeStored),
                SetVariable("PrevScreen", True),
                Hide("hair_rowan_length"),
                ShowMenu("closet")
            ]
            alternate Return()


        imagebutton at message_show:
            xalign 0.895
            yalign 0.68
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action [
                SetVariable("closet_choice_expanded", False),
                SetVariable("PrevScreen", False)
            ]
    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen accessories_rowan_game():
    default move = truecenter
    default show_textbox = True
    default move_direction = None

    zorder 1000000
    modal True

    if closet:
        add "images/backgrounds/closet.webp"
        add "full rowan no hijab" at move
        add "gui/textbox/bottom3menu.png" at (None if PrevScreen else stretch_show if closet_choice_expanded else stretch_hide):
            yzoom .95
            pos (0.5, 0.94)
            anchor (0.5, 1.0)
    else:
        add "full rowan no hijab" at move
        add "gui/textbox/bottom3menu.png" at (stretch_show if closet_choice_expanded else stretch_hide):
            yzoom .95
            pos (0.5, 0.94)
            anchor (0.5, 1.0)

    if closet_choice_expanded:
        text "ACCESSORIES MENU" xalign 0.5 ypos 890 font gui.name_text_font size 35 color "#FFF" at message_show

        button at choice_in1:
            anchor (0.5,0.5)
            yalign 0.72
            xpos 0.4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Glasses.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [
                Hide("accessories_rowan_game"),
                SetVariable("item_name", RowanGlasses),
                SetVariable("item_description", RowanGlassesDescription),
                SetVariable("AssetCount", get_rowan_glasses_options),
                SetVariable("AssetSelected", rowan_glasses_selected),
                SetVariable("PrevMCAsset", PrevRowanGlasses),
                SetVariable("NextMCAsset", NextRowanGlasses),
                SetVariable("AssetStored", rowan_glasses_type),
                If(closet, ShowMenu("show_closet_with_flash")),
                If(not closet, Jump("accessories_helper_asset"))
            ]

        button at choice_in3:
            anchor (0.5,0.5)
            yalign 0.8
            xpos 0.4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Lobe piercings.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [
                Hide("accessories_rowan_game"),
                SetVariable("item_name", RowanPiercings),
                SetVariable("item_description", RowanPiercingsDescription),
                SetVariable("AssetCount", get_rowan_piercings_options),
                SetVariable("AssetSelected", rowan_piercings_selected),
                SetVariable("PrevMCAsset", PrevRowanPiercings),
                SetVariable("NextMCAsset", NextRowanPiercings),
                SetVariable("AssetStored", rowan_ear_piercing),
                If(closet, ShowMenu("show_closet_with_flash")),
                If(not closet, Jump("accessories_helper_asset"))
            ]

        button at choice_in2:
            anchor (0.5,0.5)
            yalign 0.72
            xpos .82
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "Other piercings.":
                    size 31
                    ypos 10
                    xpos 30

            idle_background Transform("gui/small_button_idle.png")
            hover_background Transform("gui/small_button_hover.png")
            focus_mask Transform("gui/small_button_idle.png")
            action [Hide("accessories_rowan_game"), Show("body_piercings")]

        button at choice_in5:
            anchor (0.5,0.5)
            yalign 0.88
            xpos .4
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "{color=#FFFFFF}Return.":
                    size 31
                    ypos 10
                    xpos 60

                add "gui/arrow_back.png":
                    ypos -15
                    xpos 15

            idle_background Transform("gui/closet_return_idle.png")
            hover_background Transform("gui/closet_return_hover.png")
            focus_mask Transform("gui/closet_return_idle.png")
            action [
                Hide("accessories_rowan_game"),
                If(closet, Show("closet"), SetVariable("PrevScreen", True)),
                If(not closet, Jump("extra_customization"))
            ]

        imagebutton at (message_show if show_textbox else message_hide):
            xalign 0.895
            yalign 0.68
            idle "Dressup_Screen/arrow down.png"
            hover "Dressup_Screen/arrow down_hover.png"
            action [
                SetVariable("closet_choice_expanded", False),
                SetVariable("PrevScreen", False)
            ]

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.965
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

label accessories_helper_asset:
    $renpy.pause(0.2)
    call screen ChooseMCAsset

label accessories_helper_menu:
    $renpy.pause(0.2)
    call screen accessories_rowan_game


screen item_selected(sparkles, sparkle_image="images/sparkle.png"):
    on "hide" action SetVariable("who_old", "NEW")
    zorder 1000000
    modal True

    if closet or item_name == RowanFormal:
        add "images/backgrounds/closet.webp"
        #add "#888888"

    for xpos_start, ypos_start, x_offset, y_offset, duration, scale in [
        (384, 400, 320, -290, 1.3, 0.8),
        (250, 400, -120, -280, 1.4, 0.9),
        (410, 395, 280, -310, 1.3, 1),
        (350, 405, 300, -270, 1.2, 0.7),
        (180, 410, -120, -250, 1.2, 1.1),
        (500, 408, 200, -260, 1.3, 0.9),

        (475, 435, 220, -80, 1.1, 1.2),
        (298, 433, -220, -60, 1.4, 0.9),
        (398, 450, 160, -30, 1.0, 1),
        (310, 450, -130, -20, 1.5, 0.7),

        (204, 415, -180, -230, 1.3, 1),
        (330, 412, -260, -240, 1.2, 0.9),
        (429, 433, 80, -210, 1.2, 1.1),
        (189, 430, -80, -200, 1.1, 0.7),

        (432, 402, 0, -300, 1.4, 1.3),
        (308, 412, -260, -10, 1.2, 1.0),
        (294, 450, -260, 0, 1.3, 1.2),
        (398, 435, 220, 10, 1.4, 1.1),
        (293, 450, -190, 20, 1.2, 0.9),
        (401, 450, 150, 30, 1.3, 1.1),
    ]:
        add "images/sparkle.png" at sparkle_burst(xpos_start, ypos_start, x_offset, y_offset, duration, scale)

    for x_off, y_off, dur, delay, zoom in sparkles:
        add sparkle_image at sparkle_explosion_burst(
            x_offset=x_off,
            y_offset=y_off,
            duration=dur,
            delay=delay,
            zoom=zoom
        )

    if PrevScreen == "mcquoid_pjs":
        if ch13_borrowed_pjs == "none":
            add "full rowan" at image_dissolve_hide
            timer 0.1 action [Hide("item_selected"), Return()]
        else:
            add "full rowan hap" at image_dissolve_hide

    else:
        if item_name == RowanBodyType or item_name == RowanClosetTat or PrevMCAsset == PrevRowanTattoo or item_name == RowanUndies:
            add "full rowan undies hap"

        elif item_name == RowanHijab or item_name == RowanFormal or item_name == RowanGlasses or item_name == RowanOutfit:
            add "full rowan hap"

        else:
            add "full rowan no hijab hap"

    if not setup_complete:
        add "item chosen" at image_dissolve
        if item_name == RowanGlasses or item_name == RowanPiercings:
            timer 2.0 action [Hide("item_selected"), Jump("accessories_helper_menu")] repeat False
        else:
            timer 2.0 action [Hide("item_selected", transition=dissolve)] repeat False

    elif not closet:
        timer 2.0 action [
            Hide("item_selected"),
            If(PrevScreen == "bottom", Jump(JumpStore)),
            If(PrevScreen != "bottom", Return()),
            SetVariable("PrevScreen", None),
        ]

    else:
        add "item chosen" at image_dissolve
        timer 2.0 action [
            SetVariable("item_selected", False),
            SetVariable("PrevScreen", None),
            Hide("item_selected", dissolve),
            Show("closet")
        ] repeat False

screen LI_sparkles(sparkles, sparkle_image="images/sparkle.png"):
    zorder 1000000
    modal True
    on "hide" action SetVariable("who_old", "NEW")

    if current_LI != "Rowan" and current_LI != "None":
        for xpos_start, ypos_start, x_offset, y_offset, duration, scale in [
            (384, 400, 320, -290, 1.3, 0.8),
            (250, 400, -120, -280, 1.4, 0.9),
            (410, 395, 280, -310, 1.3, 1),
            (350, 405, 300, -270, 1.2, 0.7),
            (180, 410, -120, -250, 1.2, 1.1),
            (500, 408, 200, -260, 1.3, 0.9),

            (475, 435, 220, -80, 1.1, 1.2),
            (298, 433, -220, -60, 1.4, 0.9),
            (398, 450, 160, -30, 1.0, 1),
            (310, 450, -130, -20, 1.5, 0.7),

            (204, 415, -180, -230, 1.3, 1),
            (330, 412, -260, -240, 1.2, 0.9),
            (429, 433, 80, -210, 1.2, 1.1),
            (189, 430, -80, -200, 1.1, 0.7),

            (432, 402, 0, -300, 1.4, 1.3),
            (308, 412, -260, -10, 1.2, 1.0),
            (294, 450, -260, 0, 1.3, 1.2),
            (398, 435, 220, 10, 1.4, 1.1),
            (293, 450, -190, 20, 1.2, 0.9),
            (401, 450, 150, 30, 1.3, 1.1),
        ]:
            add "images/sparkle.png" at sparkle_burst(xpos_start, ypos_start, x_offset, y_offset, duration, scale)

    for x_off, y_off, dur, delay, zoom in sparkles:
        add sparkle_image at sparkle_explosion_burst(
            x_offset=x_off,
            y_offset=y_off,
            duration=dur,
            delay=delay,
            zoom=zoom
        )

    if PrevScreen == "bottom":
        add "[current_LI!l] hap" at image_dissolve_hide
    else:
        add "full [current_LI!l] hap" at image_dissolve_hide

    timer 1.5 action [
        Hide("LI_sparkles"),
        If(PrevScreen == "bottom", Jump(JumpStore)),
        If(PrevScreen != "bottom", Return()),
        SetVariable("PrevScreen", None),
    ]

screen mcquoid_pjs():
    default move = truecenter
    default show_textbox = True

    zorder 1000000
    modal True

    add "full rowan" at move

    add "gui/textbox/bottom2menu.png" at (stretch_show if closet_choice_expanded and show_textbox else (stretch_hide if not closet_choice_expanded else (box_left if move_direction == "left" else box_right))):
        pos (0.5, 0.93)
        anchor (0.5, 1.0)

    if closet_choice_expanded:
        text "[RowanOutfit()!u]" xalign 0.5 ypos 945 font gui.name_text_font size 35 color "#FFF" at (message_show if show_textbox else message_hide)
        text "[RowanOutfitDescription()]" xpos 90 yalign .79 size 33 color "#FFF" at (message_show if show_textbox else message_hide)

        $ total = len(pj_options)
        $ spacing = 0.04
        $ start = 0.5 - ((total - 1) * spacing / 2.0)

        for i, option in enumerate(pj_options):
            $ xpos = start + i * spacing

            add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

            if (ch13_borrowed_pjs == "none" and option == "None") or (ch13_borrowed_pjs == option):
                add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

        button at (choice_in_animation if show_textbox else (box_left if move_direction == "left" else box_right)):
            anchor (0.5,0.5)
            yalign 0.850
            xalign 0.22
            frame:
                background Null()
                xysize (473, 50)
                xalign 0.5
                ypos 10
                text "[ch13_borrowed_pjs_message].":
                    font "Fonts/Sofia Pro Medium.ttf"
                    size 31
                    ypos 10
                    xpos 50

            idle_background Transform("gui/button/choice_idle_background.png")
            hover_background Transform("gui/button/choice_hover_background.png")
            focus_mask Transform("gui/button/choice_idle_background.png")
            action SetVariable("PrevScreen", "mcquoid_pjs"), Hide("mcquoid_pjs"), Show("item_selected", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))

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
                SetScreenVariable("move", move_right(PrevRowanPJs, SetScreenVariable("move", truecenter)))
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
                SetScreenVariable("move", move_left(NextRowanPJs, SetScreenVariable("move", truecenter)))
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

screen closet_beach_game():
    default move = truecenter
    default show_textbox = True

    zorder 1000000
    modal True

    add "images/backgrounds/closet.webp"
    add "full rowan" at move

    $ total = len(get_rowan_beach_options())
    $ spacing = 0.04
    $ start = 0.5 - ((total - 1) * spacing / 2.0)

    for i, option in enumerate(get_rowan_beach_options()):
        $ xpos = start + i * spacing

        add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

        if (rowan_beach == option):
            add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

    if closet_choice_expanded:
        add "gui/textbox/bottom2menu.png" at stretch_show:
            pos (0.5, 0.93)
            anchor (0.5, 1.0)
        text "[RowanBeach()!u]" xalign 0.5 ypos 945 font gui.name_text_font size 35 color "#FFF" at (message_show if show_textbox else message_hide)
        text "[RowanBeachDescription()]" xpos 90 yalign .79 size 33 color "#FFF" at (message_show if show_textbox else message_hide)

        button at choice_in:
            anchor (0.5,0.5)
            yalign 0.850
            xalign 0.22
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
            action [Hide("closet_beach_game"), ShowMenu("item_selected", sparkles=generate_sparkle_waves(wave_count=2, wave_delay=0.1))]

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
            action SetScreenVariable("move", move_right(PrevRowanBeach, SetScreenVariable("move", truecenter)))
            keysym "K_LEFT"

        imagebutton at (arrow_show if show_textbox else arrow_hide):
            xoffset -20
            xalign 1.0
            yalign 0.5
            idle "Dressup_Screen/arrow right.png"
            hover "Dressup_Screen/arrow right_hover.png"
            action SetScreenVariable("move", move_left(NextRowanBeach, SetScreenVariable("move", truecenter)))
            keysym "K_RIGHT"

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))

screen closet_beach():
    default move = truecenter
    default show_textbox = True

    zorder 1000000
    modal True

    add "images/backgrounds/closet.webp"
    add "full rowan" at move

    $ total = len(get_rowan_beach_options())
    $ spacing = 0.04
    $ start = 0.5 - ((total - 1) * spacing / 2.0)

    for i, option in enumerate(get_rowan_beach_options()):
        $ xpos = start + i * spacing

        add "Dressup_Screen/option_not_selected.png" xpos xpos ypos 0.95

        if (rowan_beach == option):
            add "Dressup_Screen/option_selected.png" xpos xpos ypos 0.95

    if closet_choice_expanded:
        add "gui/textbox/bottom2menu.png" at stretch_show:
            pos (0.5, 0.93)
            anchor (0.5, 1.0)
        text "[RowanBeach()!u]" xalign 0.5 ypos 945 font gui.name_text_font size 35 color "#FFF" at (message_show if show_textbox else message_hide)
        text "[RowanBeachDescription()]" xpos 90 yalign .79 size 33 color "#FFF" at (message_show if show_textbox else message_hide)

        button at choice_in:
            anchor (0.5,0.5)
            yalign 0.850
            xalign 0.22
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
            action SetScreenVariable("move", move_right(PrevRowanBeach, SetScreenVariable("move", truecenter)))
            keysym "K_LEFT"

        imagebutton at (arrow_show if show_textbox else arrow_hide):
            xoffset -20
            xalign 1.0
            yalign 0.5
            idle "Dressup_Screen/arrow right.png"
            hover "Dressup_Screen/arrow right_hover.png"
            action SetScreenVariable("move", move_left(NextRowanBeach, SetScreenVariable("move", truecenter)))
            keysym "K_RIGHT"

    else:
        imagebutton at b_down:
            xalign 0.895
            yalign 0.98
            idle "Dressup_Screen/arrow up.png"
            hover "Dressup_Screen/arrow up_hover.png"
            action (SetVariable("closet_choice_expanded", True))
