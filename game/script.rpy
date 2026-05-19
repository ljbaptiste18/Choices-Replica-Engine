# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

label start:

    # Show a background. File path is "images/background/[file_name]." Make sure backgrounds have the prefix "bg" so that background panning will work properly. Called with a scene statement. You can use "at"

    $ playing_as = capsDevon
    scene bg lecture hall with dissolve
    play music "audio/lovehacks.mp3"
    show screen settingsUI

    luis_hap "Well hello my friends! This is a little tutorial on how to use this replica Choices engine."
    devon_hap "I'm here as well! We'll be your tutorial guides."
    luis_no "First, we'll talk about backgrounds. If you look in the code, you'll see we've called a lecture hall."
    luis_no "The file path is 'images/background/(file_name).' They are called with a 'scene' statement, example, 'scene bg lecture hall'."
    devon_no "Make sure backgrounds have the prefix 'bg' so that background panning will work properly. You can use 'at' to set the location on the screen."
    devon_no "There's right, mid_right, center, mid_left, and left. If you don't state a position, it'll default to center."
    devon_sur "And avoid using 'left' for small bgs, as it'll pan off the screen."
    luis_hap "Don't forget that case sensitivity matters a lot! You can use the 'with ease' transtion to have it slide across the bg. If you want a longer transition, you can use 'longer_ease'."
    devon_no "Ren'Py comes with transitions and transforms. Transitions are default transitions the game comes with, and transforms are custom animations you can make yourself."
    luis_no "All the sprite transitions, textbox transitions, etc are custom transforms. You don't have to worry about them because they were premade, but you can tweak them if you like."

    devon_sur "There's so much to talk about..."
    devon_hap "So let's make a menu. What would you like to see?"
    $ hide_sprite()

    $ regular = False
    $ middle = True
    $ variables_done = False
    $ choice_menu_done = False
    $ cc_done = False
    $ image_defined_done = False
    $ jumps_done = False

label tutorial_questions_loop:
    menu:
        "I want to learn about..."
        "Variables." if not variables_done:
            $ variables_done = True
            "Variables time! I'm typing this to show that if you don't specify a speaker, you will have narration. The textboxes all automate to the correct size."
            "If they're too long they might overflow, so just don't make them too long."

            devon_no "Variables are stored using this symbol: $"
            luis_no "They can be True/False, numbers, or strings."
            luis_no "If you look at this tutorial, you'll see that I'm using a True/False toggle to show if a menu choice should be included. Once you complete an option, it's marked off as done and will not be shown on the loop."
            devon_no "Variables can be used with if/elif/else statements. Use indentation to have simple control of variants before merging back to the main branch."
            if choice_menu_done:
                devon_no "We completed the choices menu option, for example!"
            else:
                devon_no "For example, we didn't complete the choices menu option, so you're getting this dialogue that says we didn't."

            luis_no "When using string variables, put them in brackets. For example, if we'd customized Devon's name, we'd put it in brackets like this, [Devon]."
            devon_no "Let's do a thought experiment. Change my name to Taylor!"

            $ Devon = "Taylor"

            devon_hap "Now my name is [Devon]!"
            luis_no "The variables system is simple and powerful. You can find more about it in Ren'Py's documentation."

        "Choice menus." if not choice_menu_done:
            $ choice_menu_done = True

            devon_no "We have two types of choice menus. Middle (like we're using now), and regular. If using middle, set middle to True and regular to False, and vice versa."

            $ middle = False
            $ regular = True

            $ auto_sprite_transition("DEVON","hap")
            menu:
                devon_hap "New menu!"
                "Choice one.":
                    devon_no "This is cool."
                    luis_hap "Yes it is."
                "Choice two.":
                    devon_no "This is cooler."
                    luis_hap "Yes it is."

            luis_no "And we merge here."
            devon_no "Menus are called using 'menu:' The first line is just the dialogue text before the choices. The choices are followed by a colon, then the next line is indented and includes the variant."
            devon_no "When you return to the same level of indentation as the menu call, it merges back together."
            luis_no "You can set different variables in menus, also go to different scenes entirely using 'jumps,' which are talked about in the jumps/labels section."

            $ regular = False
            $ middle = True

        "Character creation." if not cc_done:
            $ cc_done = True
            devon_hap "Oh, character creation is pretty crazy."
            devon_no "To access the code, open up 'Choose MC Asset.rpy' in the MC Customization Code. It may look a bit daunting, but the most important part is calling the screen, and assigning variables."
            devon_hap "Open the code to see what variables we set before calling the screen! Also, you can swap my gender using varialbes!"
            devon_sad "Also, you need to hide me. The coder could only get automated sprites to work so much."
            devon_no "You need to manually hide sprites before screens or scene changes, using $ hide_sprite()"

            $ hide_sprite()

            menu:
                "[Devon] is a..."

                "Girl.":
                    $ devon_female = True
                    $ devon_she = "she"
                    $ devon_her = "her"
                    $ devon_her_pos = "her"
                    $ devon_hers = "hers"
                    $ devon_herself = "herself"
                    $ devon_girlfriend = "girlfriend"
                    $ devon_girl = "girl"
                    $ devon_daughter = "daughter"
                    $ devon_sister = "sister"
                    $ devon_body = "fem"
                    $ devon_race = 1
                    $ devon_outfit = 1
                    $ devon_hair = 1
                    $ devon_undies = 1
                    $ devon_pjs = 1
                    $ devon_heist = 1
                    $ devon_body_type = "fem"

                "Guy.":
                    $ devon_female = False
                    $ devon_she = "he"
                    $ devon_her = "him"
                    $ devon_her_pos = "his"
                    $ devon_hers = "his"
                    $ devon_herself = "himself"
                    $ devon_girlfriend = "boyfriend"
                    $ devon_girl = "guy"
                    $ devon_daughter = "son"
                    $ devon_sister = "brother"
                    $ devon_body = "masc"
                    $ devon_race = 5
                    $ devon_outfit = 1
                    $ devon_hair = 6
                    $ devon_undies = 2
                    $ devon_pjs = 2
                    $ devon_heist = 2
                    $ devon_body_type = "masc"

            $ PrevMCAsset = PrevDevonRace
            $ NextMCAsset = NextDevonRace
            $ item_name = RaceDevon
            $ item_description = ArrowsMessage
            $ AssetCount = get_devon_race
            $ AssetSelected = devon_race_selected

            call screen ChooseMCAsset with dissolve

            show full devon hap:
                pos(0, 0)
                zoom 1.0
            show item chosen with dissolve
            pause 1.0
            hide item chosen with dissolve
            hide full devon hap with dissolve

            luis_no "You use this same screen for all the MC assets. Just change the variable from 'DevonRace' to 'DevonHair' or whatever asset it is that you're changing."
            $ hide_sprite()

            $ PrevMCAsset = PrevDevonHair
            $ NextMCAsset = NextDevonHair
            $ item_name = DevonHair
            $ item_description = DevonHairDescription
            $ AssetCount = get_devon_hair_options
            $ AssetSelected = devon_hair_selected

            call screen ChooseMCAsset with dissolve

            show full devon hap:
                pos(0, 0)
                zoom 1.0

            show item chosen with dissolve
            pause 1.0
            hide item chosen with dissolve
            hide full devon hap with dissolve

            "See how that worked?"
            "Also, we can swap out variables to call different file paths. Devon being 'fem' or 'masc' calls a separate folder for the clothing."

            luis_no "The next things you need to understand are found in Closet Functions.rpy and Customization Names.rpy"
            luis_no "Closet Functions is where you define how many options you have to get the tabs at the bottom using a 'get_hair_options' and 'get_hair_selected'."
            luis_no "It also tells you what the options are by defining Prev and Next menu variables. I won't go too into it, but know that's where you find those options."
            devon_no "Customization Names is where you will give the assets a name and a description."

        "Defining characters." if not image_defined_done:
            $ image_defined_done = True

            luis_no "The easiest way to do this is to just look at what we did. [Devon]'s is more complicated than mine, because of the variables."
            devon_no "Basically, you make a composite full image of all the separate layers of a sprite. Body, expression, hair, outfit, and any other additions."
            devon_hap "For example, cool glowing eyes layers or blood layers!"
            luis_no "Once you have the full size image, you can resize it to the bubble using a resize transform combined with an alpha mask."
            luis_hap "Don't forget to create separate images for all the expressions! We use no for neutral, sad, mad, hap for happy, and sur for surprised."
            devon_no "Once you have your image set up, you have to go to 'setup/Character Defaults' to define an image that can get an autocallback in character definitions."
            luis_no "Capitalized name is the callback name. Lowercase name is the image name we just defined. Right/left tells us which side of the screen we're on."

            $ playing_as = None

            devon_hap "Mine is automated so that if playing_as is not set to capsDevon (the variable), then I'll switch sides. Neat!"
            $ playing_as = capsDevon
            luis_hap "Yes, very cool."
            luis_no "The final step is to define our speaker names. It is automated so that you just need to type our name + expression (connected by an underscore) to call our images."
            luis_sur "We used to call every image manually! Those days were terrible!"
            devon_no "Go back to character definitions/(character name), where you defined the first image. There, you'll define five speaker names, one for each expression."
            luis_no "Just follow the example to figure it out."

        "Labels and jumps.":
            $ jumps_done = True
            devon_no "Labels are scene names that you can jump to. Just make sure the jump is the same name as the label and it'll go there."
            luis_no "You can see this in action with the tutorial_questions_loop. After asking a question, it'll jump back to the beginning of the choice menu, unless you've already asked every question."

    if variables_done and choice_menu_done and cc_done and image_defined_done and jumps_done:
        "Yay, no more questions!"
    else:
        $ hide_sprite()
        jump tutorial_questions_loop

    devon_no "Now, we'll just call a handful of screens so that you can see how they work. I won't tell you how to do it,but you can look in the code to see."
    $ hide_sprite()

    call screen item_display("food_oyster","Type the title here","Type the button text here.") #first is the image name

    call screen item_display_choice("food_waffles","Type the title here","Choice one here.","item_display_choice1","Choice two here.","item_display_choice2")
    # This ends the game.

label item_display_choice1:
    "Here's the first choice!"
    jump post_item_display_choice

label item_display_choice2:
    "Here's the second choice!"

label post_item_display_choice:
    "Now they merge here with the jumps."

    $ choice_mes = "none"

    call screen items_choice("food_oyster", "food_waffles", None, None, "Pick your poison!", "Oysters!", "Waffles!", None, None)

    if choice_mes == "Oysters!":
        "We picked oysters!"
    elif choice_mes == "Waffles!":
        "We picked waffles!"

    call screen bottom_choices_two("full luis hap", "Hey, Luis!", "Here's my first choice.", "tutorial_luis", "This is my second choice!")

label bottom_choices_merge:
    "Bottom menus are good for if you want an option to spend time with an LI or a special scene with a friend."

    devon_hap "Time for the 'Choose LI screen' but it's really just me and Luis. Make sure to set your messages properly! We can also add a premium_choice tag to make the top button gold!"

    $ premium_choice = True
    $ mc_available = True
    $ mc_message = "No one."
    $ luis_available = True
    $ luis_message = "Luis"
    $ li_message = luis_message
    $ current_LI = "Luis"
    $ hide_sprite()

    call screen chooseLI

    if current_LI == "Luis":
        devon_sur "God, Luis, why are you so off-center?"
        luis_sur "It's not my fault!"
        devon_no "Anyway, you use current_LI as the variable to track who was chosen, and from there you can jump or just use indentation to write the variants."
    else:
        devon_hap "You chose me!"
        devon_no "And now, you use current_LI as the variable to track who was chosen, and from there you can jump or just use indentation to write the variants."

    "Feel free to look through everything. This should get you started, but there's a lot more this engine is capable of."
    return

label tutorial_luis:
    luis_sur "This screen requires a jump for the first button, but not the second! The second will just continue."
    devon_no "So I added a label so that I can jump back to where it was."
    jump bottom_choices_merge
