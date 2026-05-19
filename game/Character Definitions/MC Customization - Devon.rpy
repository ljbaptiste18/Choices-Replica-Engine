default devon_race = 1
default devon_race_max = 8
default devon_outfit = 1
default devon_outfit_max = 9
default devon_hair = 1
default devon_hair_max = 10
default devon_female = True
default devon_undies = 1
default devon_undies_max = 2
default devon_pjs = 1
default devon_pjs_max = 2
default devon_heist = 1
default devon_towel = 1
default devon_body_type = "fem"
default devon_outfit_on = "casual"
default capsDevon = "DEVON"
default rf_eye_glow = False

default rf = None
default d_li_state = None

#####################################renpy langauge version:

###Full Sized
image full devon = Flatten(Composite(
    (769, 1360),
        (0, 0), "Create_Character/Devon/Hair/[devon_body_type]/devon_backhair[devon_hair].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race].webp",
        (0, 0), ConditionSwitch(
            "devon_outfit_on == 'casual'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfit[devon_outfit].webp",
            "devon_outfit_on == 'heist'", "Create_character/Devon/Outfits/[devon_body_type]/devon_heist.webp",
            "devon_outfit_on == 'pjs'", "Create_character/Devon/Outfits/[devon_body_type]/devon_pjs.webp",
            "devon_outfit_on == 'fight'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfitfight.webp",
            "devon_outfit_on == 'towel'", "Create_character/Devon/Outfits/[devon_body_type]/devon_towel.webp",
            "devon_outfit_on == 'undies'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
            "devon_outfit_on == 'bare' and persistent.nipples == 'uncensored' and devon_female", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_nipples[devon_race].webp", "True", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
        ),
        (0, 0), ConditionSwitch(
            "persistent.nipples == 'uncensored' and devon_female and devon_outfit_on == 'bare'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_braless.webp",
            "True", Null()
        ),
        (0, 0), "Create_character/Devon/Hair/[devon_body_type]/devon_hair[devon_hair].webp",
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon", "Create_character/Devon/Eye glow/Glow[devon_race].webp",
            "True", Null(),
        )
))
image full devon hap = Flatten(Composite(
    (769, 1360),
        (0, 0), "Create_Character/Devon/Hair/[devon_body_type]/devon_backhair[devon_hair].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race]_happy.webp",
        (0, 0), ConditionSwitch(
            "devon_outfit_on == 'casual'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfit[devon_outfit].webp",
            "devon_outfit_on == 'heist'", "Create_character/Devon/Outfits/[devon_body_type]/devon_heist.webp",
            "devon_outfit_on == 'pjs'", "Create_character/Devon/Outfits/[devon_body_type]/devon_pjs.webp",
            "devon_outfit_on == 'fight'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfitfight.webp",
            "devon_outfit_on == 'towel'", "Create_character/Devon/Outfits/[devon_body_type]/devon_towel.webp",
            "devon_outfit_on == 'undies'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
            "devon_outfit_on == 'bare' and persistent.nipples == 'uncensored' and devon_female", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_nipples[devon_race].webp", "True", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
        ),
        (0, 0), "Create_character/Devon/Hair/[devon_body_type]/devon_hair[devon_hair].webp",
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon", "Create_character/Devon/Eye glow/Glow[devon_race].webp",
            "True", Null(),
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon and devon_female == True", "eye_glow_flicker_devon_fem",
            "rf_eye_glow == True and rf == Devon and devon_female == False", "eye_glow_flicker_devon_masc",
            "True", Null()
        ),
        )
))
image full devon mad = Flatten(Composite(
    (769, 1360),
        (0, 0), "Create_Character/Devon/Hair/[devon_body_type]/devon_backhair[devon_hair].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race].webp",
        (0, 0), "Create_character/Devon/Mood/devon_[devon_race]_angry.webp",
        (0, 0), ConditionSwitch(
            "devon_outfit_on == 'casual'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfit[devon_outfit].webp",
            "devon_outfit_on == 'heist'", "Create_character/Devon/Outfits/[devon_body_type]/devon_heist.webp",
            "devon_outfit_on == 'pjs'", "Create_character/Devon/Outfits/[devon_body_type]/devon_pjs.webp",
            "devon_outfit_on == 'fight'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfitfight.webp",
            "devon_outfit_on == 'towel'", "Create_character/Devon/Outfits/[devon_body_type]/devon_towel.webp",
            "devon_outfit_on == 'undies'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
            "devon_outfit_on == 'bare' and persistent.nipples == 'uncensored' and devon_female", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_nipples[devon_race].webp", "True", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
        ),
        (0, 0), "Create_character/Devon/Hair/[devon_body_type]/devon_hair[devon_hair].webp",
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon", "Create_character/Devon/Eye glow/Glow[devon_race].webp",
            "True", Null(),
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon and devon_female == True", "eye_glow_flicker_devon_fem",
            "rf_eye_glow == True and rf == Devon and devon_female == False", "eye_glow_flicker_devon_masc",
            "True", Null()
        ),
        )
))
image full devon sad = Flatten(Composite(
    (769, 1360),
        (0, 0), "Create_Character/Devon/Hair/[devon_body_type]/devon_backhair[devon_hair].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race].webp",
        (0, 0), "Create_character/Devon/Mood/devon_[devon_race]_sad.webp",
        (0, 0), ConditionSwitch(
            "devon_outfit_on == 'casual'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfit[devon_outfit].webp",
            "devon_outfit_on == 'heist'", "Create_character/Devon/Outfits/[devon_body_type]/devon_heist.webp",
            "devon_outfit_on == 'pjs'", "Create_character/Devon/Outfits/[devon_body_type]/devon_pjs.webp",
            "devon_outfit_on == 'fight'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfitfight.webp",
            "devon_outfit_on == 'towel'", "Create_character/Devon/Outfits/[devon_body_type]/devon_towel.webp",
            "devon_outfit_on == 'undies'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
            "devon_outfit_on == 'bare' and persistent.nipples == 'uncensored' and devon_female", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_nipples[devon_race].webp", "True", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
        ),
        (0, 0), "Create_character/Devon/Hair/[devon_body_type]/devon_hair[devon_hair].webp",
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon", "Create_character/Devon/Eye glow/Glow[devon_race].webp",
            "True", Null(),
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon and devon_female == True", "eye_glow_flicker_devon_fem",
            "rf_eye_glow == True and rf == Devon and devon_female == False", "eye_glow_flicker_devon_masc",
            "True", Null()
        ),
        )
))
image full devon sur = Flatten(Composite(
    (769, 1360),
        (0, 0), "Create_Character/Devon/Hair/[devon_body_type]/devon_backhair[devon_hair].webp",
        (0, 0), "Create_Character/Devon/Mood/devon_[devon_race].webp",
        (0, 0), "Create_character/Devon/Mood/devon_[devon_race]_shocked.webp",
        (0, 0), ConditionSwitch(
            "devon_outfit_on == 'casual'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfit[devon_outfit].webp",
            "devon_outfit_on == 'heist'", "Create_character/Devon/Outfits/[devon_body_type]/devon_heist.webp",
            "devon_outfit_on == 'pjs'", "Create_character/Devon/Outfits/[devon_body_type]/devon_pjs.webp",
            "devon_outfit_on == 'fight'", "Create_character/Devon/Outfits/[devon_body_type]/devon_outfitfight.webp",
            "devon_outfit_on == 'towel'", "Create_character/Devon/Outfits/[devon_body_type]/devon_towel.webp",
            "devon_outfit_on == 'undies'", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
            "devon_outfit_on == 'bare' and persistent.nipples == 'uncensored' and devon_female", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies_nipples[devon_race].webp", "True", "Create_character/Devon/Outfits/[devon_body_type]/devon_undies.webp",
        ),
        (0, 0), "Create_character/Devon/Hair/[devon_body_type]/devon_hair[devon_hair].webp",
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon", "Create_character/Devon/Eye glow/Glow[devon_race].webp",
            "True", Null(),
        (0, 0), ConditionSwitch(
            "rf_eye_glow == True and rf == Devon and devon_female == True", "eye_glow_flicker_devon_fem",
            "rf_eye_glow == True and rf == Devon and devon_female == False", "eye_glow_flicker_devon_masc",
            "True", Null()
        ),
        )
))

init -1:
    transform resize_dev:
        zoom get_zoom_by_body_type("Devon")
        xoffset get_xoffset_by_body_type("Devon")
        yoffset get_yoffset_by_body_type("Devon")
        xalign 0.0
        yalign 0.5
        xzoom -1.0

layeredimage devon:
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
                Composite((768, 1360),(255, 315), At(Flatten("full devon"), resize_dev),),
                "alpha_mask_flip"
            )
        attribute hap:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon hap"), resize_dev),),
                "alpha_mask_flip"
            )
        attribute sad:
            AlphaMask(
                Composite((768, 1360),(255, 315), At(Flatten("full devon sad"), resize_dev),),
                "alpha_mask_flip"
            )
        attribute mad:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon mad"), resize_dev),),
                "alpha_mask_flip"
            )
        attribute sur:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon sur"), resize_dev),),
                "alpha_mask_flip"
            )

layeredimage devon_pjs:
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
                Composite((768, 1360),(255, 315), At(Flatten("full devon pjs"), resize_dev)),
                "alpha_mask_flip"
            )
        attribute hap:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon pjs hap"), resize_dev)),
                "alpha_mask_flip"
            )
        attribute sad:
            AlphaMask(
                Composite((768, 1360),(255, 315), At(Flatten("full devon pjs sad"), resize_dev)),
                "alpha_mask_flip"
            )
        attribute mad:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon pjs mad"), resize_dev)),
                "alpha_mask_flip"
            )
        attribute sur:
            AlphaMask(
                Composite((768, 1360), (255, 315), At(Flatten("full devon pjs sur"), resize_dev)),
                "alpha_mask_flip"
            )

image devflip no  = Transform("devon no",  xzoom=-1)
image devflip hap = Transform("devon hap", xzoom=-1)
image devflip sad = Transform("devon sad", xzoom=-1)
image devflip mad = Transform("devon mad", xzoom=-1)
image devflip sur = Transform("devon sur", xzoom=-1)
