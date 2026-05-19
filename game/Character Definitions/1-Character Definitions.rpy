init:
## narrator - callback=narrator_sprite_callback should be aggregated to any center_voice speaker
    $ narrator = Character(None, callback=narrator_sprite_callback)
## texts
    $ example_text = Character('Example', kind=nvl, advance=False, color="#E5DBD9", what_color="#E5DBD9", who_size=28, what_size=33, what_xpos=45, who_xpos=45, what_slow_cps=0)
    $ date = Character('date', kind=nvl, advance=False, color="#E5DBD9", what_color="#E5DBD9", who_size=28, what_size=33, what_xpos=45, who_xpos=45, what_slow_cps=0)

##center voices (example)
    $ tutorial = Character("TUTORIAL", color="#292928", what_color="#9E0101", who_outlines=[ (1, "#E5DBD9") ], callback=narrator_sprite_callback)
    $ v = Character("VOICE", color="#292928", what_color="#111E6C", who_outlines=[ (1, "#E5DBD9") ], callback=narrator_sprite_callback)
    $ crowd = Character("CROWD", color="#292928", what_color="#111E6C", who_outlines=[ (1, "#E5DBD9") ], callback=narrator_sprite_callback)

    $ center_luis = Character("LUIS", what_color="#111E6C", callback=narrator_sprite_callback)
