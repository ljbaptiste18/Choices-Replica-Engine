transform x_flip():
    xzoom -1

transform inleft():
    offscreenleft
    zoom 0.35
    alpha 0.4
    pos (0.0, 0.75)
    linear 0.25 zoom 1.0 pos (1.0, 1.0) alpha 1.0

transform flipleft():
    offscreenleft
    xzoom -1.0
    pause 0.15
    zoom 0.35
    alpha 0.4
    pos (0.0, 0.75)
    linear 0.25 zoom 1.0 pos (1.0, 1.0) alpha 1.0

transform outleft():
    zoom 1.0
    alpha 1.0
    pause 0.1
    linear 0.25 zoom 0.4 pos (0.0, 0.75) alpha 0.4
    offscreenleft
    alpha 0

transform inright():
    offscreenright
    zoom 0.35
    alpha 0.4
    pos (0.8, 0.75)
    linear 0.25 zoom 1.0 pos (0.0, 1.0) alpha 1.0

transform inright_fast():
    offscreenright
    pause 0.05
    zoom 0.4
    alpha 0.4
    pos (0.8, 0.75)
    linear 0.25 zoom 1.0 pos (0.0, 1.0) alpha 1.0

transform flipright():
    offscreenright
    xzoom -1.0
    pause 0.15
    alpha .4
    zoom 0.4
    anchor (0.0, 0.5)
    pos (1.0, 0.5)
    ease 0.3 zoom 1.0 align (0.6, 1.0) alpha 1.0

transform outright():
    zoom 1.0
    alpha 1.0
    pause 0.1
    linear 0.25 zoom 0.4 pos (0.8, 0.75) alpha 0.4
    offscreenright
    alpha 0

transform flicker_overlay:
    alpha 0.6
    block:
        linear 0.05 alpha 0.2
        pause 0.1
        linear 0.05 alpha 0.6
        pause 0.08
        linear 0.05 alpha 0.3
        pause 0.4
        linear 0.1 alpha 0.6
        pause 0.6
        linear 0.05 alpha 0.1
        pause 0.05
        linear 0.05 alpha 0.6
        pause 0.05
        linear 0.05 alpha 0.2
        pause 0.3
        linear 0.15 alpha 0.6
        pause 0.9
        repeat

init -1:
    transform right_transition_static(old_value=Solid("#00000000"), new_value=Solid("#00000000")):
        old_value
        zoom 1.0 align (0.6, 1.0) alpha 1.0
        new_value
        zoom 1.0 align (0.6, 1.0) alpha 1.0

    transform right_transition_out(old_value=Solid("#00000000"), new_value=Solid("#00000000")):
        old_value
        ease 0.35 zoom 0.6 align (1.5, 0.6) alpha 0.6
        offscreenright
        new_value
        offscreenright
        pause 0.1
        zoom 0.4
        alpha 0.6
        anchor (0.0, 0.5)
        pos (1.0, 0.5)
        ease 0.18 zoom 1.0 align (0.6, 1.0) alpha 1.0

    transform left_transition_out(old_value=Solid("#00000000"), new_value=Solid("#00000000")):
        old_value
        ease 0.35 zoom 0.6 align (-1.5, 0.6) alpha 0.6
        offscreenleft
        new_value
        offscreenleft
        pause 0.1
        zoom 0.4
        alpha 0.6
        anchor (0.0, 0.5)
        pos (0.5, 0.5)
        ease 0.18 zoom 1.0 align (0.1, 1.0) alpha 1.0

transform fulldissolve():
    alpha 0.2
    zoom 1.0
    anchor (1.0, 1.0)
    pos (768, 1360)
    ease .4 alpha 1.0

#hide textbox screen
transform stretch:
    on show:
        alpha 0
        pause 0.3
        alpha 0.3
        yzoom 0.0
        ease 0.3 alpha 1.0 yzoom 1.0
    on hide:
        alpha 1.0
        yzoom 1.0
        ease 0.3 alpha 0.3 yzoom 0.0

transform box_left:
    ease 0.35 xpos -100 alpha 0

transform box_right:
    ease 0.35 xpos 850 alpha 0

transform stretch_ending:
    on show:
        alpha 0
        pause 0.0
        alpha 0.3
        yzoom 0.0
        yanchor 0.5
        ease 0.15 alpha 1.0 yzoom 1.0
    on hide:
        alpha 1.0
        yzoom 1.0
        ease 0.15 alpha 0.3 yzoom 0.0

transform stretch_show:
    xpos 0.5
    alpha 0
    alpha 0.3
    yzoom 0.0
    ease 0.2 alpha 1.0 yzoom 1.0
    on hide:
        alpha 1.0
        yzoom 1.0
        pause 0.1
        ease 0.25 alpha 0.3 yzoom 0.0

transform stretch_show_only:
    xpos 0.5
    alpha 0
    alpha 0.3
    yzoom 0.0
    ease 0.2 alpha 1.0 yzoom 1.0

transform stretch_hide:
    alpha 1.0
    yzoom 1.0
    ease 0.2 alpha 0.3 yzoom 0.0

transform choice_in1:
    alpha 0.0
    pause 0.2
    anchor (0.5, 0.5)
    xpos 0.4
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.98
    on idle:
        linear 0.05 zoom 1.0

transform choice_in2:
    alpha 0.0
    pause 0.25
    anchor (0.5, 0.5)
    xpos 0.82
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        pause 0.05
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.98
    on idle:
        linear 0.05 zoom 1.0

transform choice_in3:
    alpha 0.0
    pause 0.3
    anchor (0.5, 0.5)
    xpos 0.4
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        pause 0.1
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.99
    on idle:
        linear 0.05 zoom 1.0

transform choice_in4:
    alpha 0.0
    pause 0.35
    anchor (0.5, 0.5)
    xpos 0.82
    zoom 0.0
    ease 0.3 alpha 1.0 zoom 1.0
    on hide:
        pause 0.15
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.99
    on idle:
        linear 0.05 zoom 1.0

transform choice_in5:
    alpha 0.0
    pause 0.4
    anchor (0.5, 0.5)
    xpos 0.4
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        pause 0.2
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.99
    on idle:
        linear 0.05 zoom 1.0

transform choice_in6:
    alpha 0.0
    pause 0.45
    anchor (0.5, 0.5)
    xpos 0.82
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        pause 0.25
        ease 0.2 zoom 1.1 zoom 0 alpha 0
    on hover:
        linear 0.05 zoom 0.99
    on idle:
        linear 0.05 zoom 1.0

transform choice_hide:
    alpha 1
    ease .2 alpha 0

transform choice_in:
    alpha 0
    pause 0.45
    anchor (0.5, 0.5)
    xpos 0.4
    zoom 0.0
    ease 0.3 alpha 1.0 zoom 1.0
    on hide:
        alpha 1
        ease .2 alpha 0
    on hover:
        linear 0.12 zoom 0.98
    on idle:
        linear 0.12 zoom 1.0

transform choice_in_animation:
    alpha 0.0
    anchor (0.5, 0.5)
    xpos 0.4
    zoom 0.0
    ease 0.2 alpha 1.0 zoom 1.0
    on hide:
        alpha 1
        ease .2 alpha 0
    on hover:
        linear 0.12 zoom 0.98
    on idle:
        linear 0.12 zoom 1.0

transform message_show:
    alpha 0
    pause 0.1
    ease 0.2 alpha 1
    on hide:
        alpha 1
        ease .1 alpha 0

transform message_show_delayed:
    alpha 0
    pause 0.5
    ease 0.2 alpha 1
    on hide:
        alpha 1
        ease .1 alpha 0

transform message_hide:
    alpha 1
    ease .1 alpha 0

transform image_dissolve:
    truecenter
    on show:
        alpha 0
        pause 0.3
        ease 0.3 alpha 1
    on hide:
        alpha 1
        ease .2 alpha 0

transform image_dissolve_hide:
    truecenter
    on hide:
        alpha 1
        ease .5 alpha 0

transform screen_dissolve:
    alpha 0
    linear 0.5 alpha 1

transform screen_flash:
    alpha 0
    linear 0.3 alpha 1

transform item_dissolve():
    alpha 0
    ease 0.3 alpha 1.0
    on hide:
        ease 0.2 zoom 0.9 alpha 0.0

transform delayed_dissolve():
    alpha 1.0
    pause 1
    alpha 0

transform b_up():
    alpha 0.0
    pause 0.2
    yoffset 50
    ease .3 alpha 1.0 yoffset -12

transform b_hide():
    ease .2 alpha 0.0

transform b_down():
    alpha 0.0
    yoffset 180
    yzoom 0.01
    pause 0.2
    alpha 1.0
    parallel:
        linear 0.2 yoffset -12
    parallel:
        linear 0.2 yzoom 1.0
    linear 0.1 yoffset 0

transform arrow:
    on show:
        alpha 0
        pause .3
        alpha 0.3
        yoffset 50
        zoom 0.5
        ease 0.2 zoom 1.2 alpha 1 yoffset 0
        ease 0.1 zoom 1
    on hide:
        alpha 01
        yoffset 0
        zoom 1
        ease 0.2 zoom 0 alpha 0 yoffset 50

transform arrow_show:
    alpha 0
    alpha 0.3
    yoffset 50
    zoom 0.5
    ease 0.2 zoom 1.2 alpha 1 yoffset 0
    ease 0.1 zoom 1
    on hide:
        alpha 01
        yoffset 0
        zoom 1
        ease 0.2 zoom 0 alpha 0 yoffset 50

transform arrow_hide:
    alpha 01
    yoffset 0
    zoom 1
    ease 0.2 zoom 0 alpha 0 yoffset 50

transform autosave_wobble:
    rotate 0 yoffset 0
    ease 0.25 rotate 12 yoffset 3
    ease 0.5 rotate -12 yoffset 3
    ease 0.25 rotate 0 yoffset 0
    repeat

transform sparkle_burst(xpos_start, ypos_start, x_offset, y_offset, duration, scale):
    xpos xpos_start
    ypos ypos_start
    zoom scale
    alpha 1.0

    parallel:
        easeout duration xpos xpos_start + x_offset ypos ypos_start + y_offset
    parallel:
        pause duration * 0.7
        easeout duration * 0.3 alpha 0.0

##alpha mask

image alpha_mask = Composite((768, 1360),
    (0, 0), Transform("images/bubbles/mask.png"),
    # (0, -100), Transform("images/bubbles/Reaction Bubble Neutral MC.png"),
    # (0, 0), Transform("images/bubbles/Reaction Bubble Neutral MC.png")
)
image alpha_mask_flip = Composite((768, 1360),
    (0, 0), Transform("images/bubbles/mask.png", xzoom=-1),
    # (0, -100), Transform("images/bubbles/Reaction Bubble Neutral MC.png"),
    # (0, 0), Transform("images/bubbles/Reaction Bubble Neutral MC.png")
)
image alpha_mask_corner = Composite((768, 1360),
    (0, 0), Transform("images/bubbles/corner_mask.png"),
    # (0, -100), Transform("images/bubbles/Reaction Bubble Neutral MC.png"),
    # (0, 0), Transform("images/bubbles/Reaction Bubble Neutral MC.png")
)


define dis = Dissolve(0.1)
define longer_ease = MoveTransition(1.5, enter=offscreenright, enter_time_warp=_warper.ease)
define longdissolve = Dissolve(1.2)
define move = MoveTransition(1.0)
define wipedown = CropMove(0.5, mode="custom", startcrop=(0.25, 0.0, 0.5, 1.0), endcrop=(0.0, 0.0, 1.0, 1.0), topnew=False)
image title_cutscene = Movie(play="images/Video/Title-animation.ogv")
image noahmc_cg = Movie(play="images/Video/noahmc.ogv")
image abel_cg = Movie(play="images/Video/abel_cg.ogv")
image matthias_cg = Movie(play="images/Video/matthias_cg.ogv")

label show_title(duration=8.25):
    $ _skipping = False
    $ renpy.stop_skipping()
    show title_cutscene
    $ renpy.pause(3,hard=True)
    $ renpy.pause(5.25)
    hide title_cutscene
    $ _skipping = True
    return

init python:
    class StarField(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            # A list of (sprite, starting-x, speed).
            self.stars = [ ]

            # Note: We store the displayable in a variable here.
            # That's important - it means that all of the stars at
            # a given speed have the same displayable. We render that
            # displayable once, and cache the result.

            d = Transform(ColorBlend2("images/particle.png", "#FFF000", 0.75), zoom=10, alpha=0.25)
            for i in range(0, 10):
                self.add(d, 80)

            d = Transform(ColorBlend2("images/particle.png", "#00FF00", 0.75), zoom=7, alpha=0.25)
            for i in range(0, 5):
                self.add(d, 80)

            d = Transform(ColorBlend2("images/particle.png", "#FF0000", 0.75), zoom=7, alpha=0.25)
            for i in range(0, 5):
                self.add(d, 80)

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 840)
            s.x = renpy.random.randint(0, 600)

            self.stars.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.stars:
                s.y = (start + speed * st) % 840 - 20

            return 0

#sparkles
    import math
    import random

    def generate_sparkles(count=100, min_distance=250, max_distance=780, base_delay=0.0):
        sparkles = []
        for _ in range(count):
            angle_deg = random.uniform(0, 360)
            angle_rad = math.radians(angle_deg)
            distance = random.uniform(min_distance, max_distance)

            x_offset = math.cos(angle_rad) * distance / 768
            y_offset = math.sin(angle_rad) * distance / 1360

            delay = base_delay + random.uniform(0.0, 0.1)
            zoom = random.uniform(0.2, 0.6)

            sparkles.append((x_offset, y_offset, 1.2, delay, zoom))
        return sparkles

    def generate_sparkle_waves(wave_count=3, wave_delay=0.1):
        all_sparkles = []
        for i in range(wave_count):
            delay_offset = i * wave_delay
            all_sparkles.extend(generate_sparkles(base_delay=delay_offset))
        return all_sparkles

transform sparkle_explosion_burst(x_offset=0.0, y_offset=0.0, duration=1.0, delay=0.0, zoom=1.0):
    alpha 0.0
    pos (0.5, 0.5)
    zoom zoom
    anchor (0.5, 0.5)
    rotate 0

    on show:
        parallel:
            pause delay
            linear 0.2 alpha 0.6
            pause duration - 0.4
            linear 0.2 alpha 0.0
        parallel:
            pause delay
            linear duration pos (0.5 + x_offset, 0.5 + y_offset)
        parallel:
            pause delay
            linear duration rotate 45

transform my_tr(t=0):
    xpos 1.2 xanchor 0.0
    t*0.5
    linear 1.0 xalign 0.5

transform fromRight:
    subpixel True
    alpha 0.0 xalign 1.0 xanchor 0.0
    parallel:
        easein 1.0 alpha 1.0
    parallel:
        easein 1.0 xalign 0.5
    on hide:
        alpha 1 zoom 1 xanchor 0.5 yanchor 0.5
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0

transform toOffscreenLeft():
    subpixel True
    truecenter
    ease 0.5 offscreenleft

transform toOffscreenRight():
    subpixel True
    truecenter
    ease 0.5 offscreenright

transform fromOffscreenLeft():
    subpixel True
    offscreenleft
    ease 0.5 truecenter

transform fromOffscreenRight():
    subpixel True
    offscreenright
    ease 0.5 truecenter

transform move_left(fn=None, fn2=None):
    toOffscreenLeft
    function renpy.partial(tfn, callback=fn)
    fromOffscreenRight
    function renpy.partial(tfn, callback=fn2)

transform move_right(fn=None, fn2=None):
    toOffscreenRight
    function renpy.partial(tfn, callback=fn)
    fromOffscreenLeft
    function renpy.partial(tfn, callback=fn2)

transform cave_rumbling:
    subpixel True
    center
    choice:
        linear 0.2 xoffset 5
        linear 0.2 xoffset -5
    repeat

transform forward_spin:
        subpixel True
        zoom 2
        rotate 0 xanchor 0.4 yanchor 0.3
        ease 10.0 rotate 180
        ease 10.0 rotate -180
        ease 20 rotate 360
        repeat

init -2:
    style nvl_dialogue:
        line_spacing 0
    style say_dialogue:
        line_spacing -2

define flash = Fade(0.2, 0.1, 0.2, color='#fff')

transform toss:
    xalign 0.0 yalign 0.0 zoom 1
    easeout 0.2 zoom 50 xalign 1.0 yalign 1.0
    offscreenright

init:
    image bg rain light:
        "images/rain/rain1.webp"
        0.2
        "images/rain/rain3.webp"
        0.2
        repeat

    image bg rain:
        "images/rain/rain1.webp"
        0.2
        "images/rain/rain3.webp"
        0.2
        "images/rain/rain2.webp"
        0.2
        repeat

init python:
    def tfn(tr, st, at, callback=None):
        fn = callback

        if callable(fn):
            fn()
            renpy.restart_interaction()

    def ColorBlend(d, color="#00FFFF"):
        return Transform(d, matrixcolor=BrightnessMatrix(0.25)*TintMatrix(color))

    def ColorBlend2(d, color="#FFF", alpha=.25):
        return AlphaBlend(Transform(d, alpha = alpha), d, Solid(color, xysize=(config.screen_width, config.screen_height)), alpha=True)

    def Desaturate(d):
        return Transform(d, matrixcolor=SaturationMatrix(0.0))

    def Saturate(d, level=1.5):
        return Transform(d, matrixcolor=SaturationMatrix(level))
