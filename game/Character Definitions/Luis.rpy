###Luis Textbox
init:
    $ luis = Character("LUIS")
    $ left_luis = Character("LUIS")
    $ luis_text = Character('Luis', kind=nvl, color="#E5DBD9", what_color="#E5DBD9", who_size=28, what_size=33, what_xpos=45, who_xpos=45)

    $ luis_no = Character("LUIS", callback=make_char_callback("LUIS"))
    $ luis_sad = Character("LUIS", callback=make_char_callback("LUIS","sad"))
    $ luis_hap = Character("LUIS", callback=make_char_callback("LUIS","hap"))
    $ luis_mad = Character("LUIS", callback=make_char_callback("LUIS","mad"))
    $ luis_sur = Character("LUIS", callback=make_char_callback("LUIS","sur"))

###luis - create the composite image, then use layered image to autoresize based on hexagon image mask. This can be used for all characters. If you want to flip the hexagon (for example left side mc) you can either use xzoom -1 in the image transform

default luis_outfit = "casual"

image full luis = Transform(
    Flatten(Composite(
        (768, 1360),
            (0, 0), "images/luis/luis_base.webp",
            (0, 0), ConditionSwitch(
                "luis_outfit == 'casual'", "images/luis/outfit.webp",
            ),
            (0, 0), "images/luis/luis_neutral.webp",
            (0, 0), "images/luis/luis_hair.webp",
    )),
    yalign=1.0
)

image full luis sad = Transform(
    Flatten(Composite(
        (768, 1360),
            (0, 0), "images/luis/luis_base.webp",
            (0, 0), ConditionSwitch(
                "luis_outfit == 'casual'", "images/luis/outfit.webp",
            ),
            (0, 0), "images/luis/luis_sad.webp",
            (0, 0), "images/luis/luis_hair.webp",
    )),
    yalign=1.0
)

image full luis hap = Transform(
    Flatten(Composite(
        (768, 1360),
            (0, 0), "images/luis/luis_base.webp",
            (0, 0), ConditionSwitch(
                "luis_outfit == 'casual'", "images/luis/outfit.webp",
            ),
            (0, 0), "images/luis/luis_happy.webp",
            (0, 0), "images/luis/luis_hair.webp",
    )),
    yalign=1.0
)
image full luis mad = Transform(
    Flatten(Composite(
        (768, 1360),
            (0, 0), "images/luis/luis_base.webp",
            (0, 0), ConditionSwitch(
                "luis_outfit == 'casual'", "images/luis/outfit.webp",
            ),
            (0, 0), "images/luis/luis_mad.webp",
            (0, 0), "images/luis/luis_hair.webp",
    )),
    yalign=1.0
)
image full luis sur = Transform(
    Flatten(Composite(
        (768, 1360),
            (0, 0), "images/luis/luis_base.webp",
            (0, 0), ConditionSwitch(
                "luis_outfit == 'casual'", "images/luis/outfit.webp",
            ),
            (0, 0), "images/luis/luis_shocked.webp",
            (0, 0), "images/luis/luis_hair.webp",
    )),
    yalign=1.0
)

init -1:
    transform resize_luis:
        zoom 0.7
        xalign 0.0
        yalign 0.43
        xzoom -1.0 #this flips him, since his sprite faces the wrong way

layeredimage luis:
    group bubble auto:
        attribute no default:
            "images/Bubbles/Reaction Bubble Neutral right.png"
        attribute hap:
            "images/Bubbles/Reaction Bubble Happy right.png"
        attribute sad:
            "images/Bubbles/Reaction Bubble Sad right.png"
        attribute mad:
            "images/Bubbles/Reaction Bubble Angry right.png"
        attribute sur:
            "images/Bubbles/Reaction Bubble Surprised right.png"

    group mood auto:
        attribute no default:
            AlphaMask(
                Composite((768, 1360),(210, 300), At(Flatten("full luis"), resize_luis),),
                "alpha_mask_flip"
            )
        attribute hap:
            AlphaMask(
                Composite((768, 1360), (210, 300), At(Flatten("full luis hap"), resize_luis),),
                "alpha_mask_flip"
            )
        attribute sad:
            AlphaMask(
                Composite((768, 1360),(210, 300), At(Flatten("full luis sad"), resize_luis),),
                "alpha_mask_flip"
            )
        attribute mad:
            AlphaMask(
                Composite((768, 1360), (210, 300), At(Flatten("full luis mad"), resize_luis),),
                "alpha_mask_flip"
            )
        attribute sur:
            AlphaMask(
                Composite((768, 1360), (210, 300), At(Flatten("full luis sur"), resize_luis),),
                "alpha_mask_flip"
            )
