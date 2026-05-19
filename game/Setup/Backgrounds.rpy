transform mid_right:
    xalign 0.75
    yalign 1.0

transform mid_left:
    xalign 0.25
    yalign 1.0

transform left:
    xalign 0.05
    yalign 1.0

transform right:
    xalign 0.95
    yalign 1.0


image art = ColorBlend(Desaturate("images/icons/art.png"), "#2106ba")
image music = ColorBlend(Desaturate("images/icons/music.png"), "#79069c")
image computer = ColorBlend(Desaturate("images/icons/computer.png"), "#d65d00")
image handy = ColorBlend(Desaturate("images/icons/handy.png"), "#d60400")
image megaphone = ColorBlend(Desaturate("images/icons/megaphone.png"), "#a6028d")
image sports = ColorBlend(Desaturate("images/icons/sports.png"), "#cfb000")
image book = ColorBlend(Desaturate("images/icons/book.png"), "#02a695")
image science = ColorBlend(Desaturate("images/icons/science.png"), "#1e782e")

##texting boxes
image jocelyn_label = ColorBlend(Desaturate("gui/texting/name_left_label.png"), "#7512b3")
image jocelyn_label_rounded = ColorBlend(Desaturate("gui/texting/name_left_label_round.png"), color="#7512b3")
image jocelyn_text_box = Saturate(ColorBlend(Desaturate("gui/texting/text_bar.png"), color="#7512b3"), level=1.5)
image jocelyn_speech = Saturate(ColorBlend(Desaturate("gui/texting/speech_left.png"), color="#7512b3"), level=1.5)

image abel_label = ColorBlend(Desaturate("gui/texting/name_left_label.png"), color="#fff200")
image abel_label_rounded = ColorBlend(Desaturate("gui/texting/name_left_label_round.png"), color="#fff200")
image abel_text_box = Saturate(ColorBlend(Desaturate("gui/texting/text_bar.png"), color="#fff200"), level=2.5)
image abel_speech = Saturate(ColorBlend(Desaturate("gui/texting/speech_left.png"), color="#fff200"), level=2.5)

image lincoln_label = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label.png"), color="#447bfc"), level=1.5)
image lincoln_label_rounded = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label_round.png"), color="#447bfc"), level=1.5)
image lincoln_text_box = Saturate(ColorBlend(Desaturate("gui/texting/text_bar.png"), color="#447bfc"), level=2.5)
image lincoln_speech = Saturate(ColorBlend(Desaturate("gui/texting/speech_left.png"), color="#447bfc"), level=2.5)

image connor_label = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label.png"), color="#c25004"), level=1.5)
image connor_label_rounded = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label_round.png"), color="#c25004"), level=1.5)
image connor_text_box = Saturate(ColorBlend(Desaturate("gui/texting/text_bar.png"), color="#c25004"), level=2.5)
image connor_speech = Saturate(ColorBlend(Desaturate("gui/texting/speech_left.png"), color="#c25004"), level=2.5)

image amalia_label = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label.png"), color="#fc6262"), level=1.5)
image amalia_label_rounded = Saturate(ColorBlend(Desaturate("gui/texting/name_left_label_round.png"), color="#fc6262"), level=1.5)
image amalia_text_box = Saturate(ColorBlend(Desaturate("gui/texting/text_bar.png"), color="#fc6262"), level=2.5)
image amalia_speech = Saturate(ColorBlend(Desaturate("gui/texting/speech_left.png"), color="#fc6262"), level=2.5)

###A
init:
    image red = Solid("#880808")  # Or Solid((255, 0, 0, 255))

image bg a apartment day = im.FactorScale("images/backgrounds/bg a apartment day.webp", 1.8)
image bg a apartment night = im.FactorScale("images/backgrounds/bg a apartment night.webp", 1.8)
image bg ambulance = im.FactorScale("images/backgrounds/bg ambulance.webp", 1.4)
image bg archives = im.FactorScale("images/backgrounds/bg archives.webp", 1.4)
image bg armory = im.FactorScale("images/backgrounds/bg armory.webp", 1.4)
image bg alleyway = im.FactorScale("images/backgrounds/bg alleyway.webp", 1.4)
image bg apartment bathroom = im.FactorScale("images/backgrounds/bg apartment bathroom.webp", 1.4)
image bg apartment bedroom = im.FactorScale("images/backgrounds/bg apartment bedroom.webp", 1.4)
image bg apartment devon = im.FactorScale("images/backgrounds/bg apartment devon.webp", 1.4)
image bg apartment andy = im.FactorScale("images/backgrounds/bg apartment andy.webp", 1.4)
image bg apartment exterior day = im.FactorScale("images/backgrounds/bg apartment exterior day.webp", 1.4)
image bg apartment exterior night = im.FactorScale("images/backgrounds/bg apartment exterior night.webp", 1.4)
image bg apartment kitchen = im.FactorScale("images/backgrounds/bg apartment kitchen.webp", 1.4)
image bg apartment lia = im.FactorScale("images/backgrounds/bg apartment lia.webp", 1.4)
image bg apartment lucas day = im.FactorScale("images/backgrounds/bg apartment lucas day.webp", 1.35)
image bg apartment joss = im.FactorScale("images/backgrounds/bg apartment joss.webp", 1.4)
image bg apartment hallway = im.FactorScale("images/backgrounds/bg apartment hallway.webp", 1.4)
image bg apartment rowan = im.FactorScale("images/backgrounds/bg apartment rowan.webp", 0.7)
image bg apartment bedroom rowan = im.FactorScale("images/backgrounds/bg apartment bedroom rowan.webp", 1.4)
image bg axe range = im.FactorScale("images/backgrounds/bg gym interior.webp", 1.4)

###B
image bg baby linky room = im.FactorScale("images/backgrounds/bg baby linky room.webp", 1.13)
image bg ballroom blood = im.FactorScale("images/backgrounds/bg ballroom blood.webp", 1.13)
image bg bar fancy = im.FactorScale("images/backgrounds/bg bar fancy.webp", 0.7)
image bg bar = im.FactorScale("images/backgrounds/bg bar.webp", 1.4)
image bg bathroom lia = im.FactorScale("images/backgrounds/bg bathroom lia.webp", 1.4)
image bg bathtub = im.FactorScale("images/backgrounds/bg bathtub.webp", 1.5)
image bg basement = im.FactorScale("images/backgrounds/bg bgz_romance_int_cabin_basement_creepy_neutral-v01.webp", 1.4)
image bg bedroom abel = im.FactorScale("images/backgrounds/bg a bedroom.webp", 1)
image bg bedroom lia = im.FactorScale("images/backgrounds/bg bedroom lia.webp", 1.35)
image bg bedroom amalia night = im.FactorScale("images/backgrounds/bg bg_romance_int_dorm_bedroom_night-v01.webp", 1.4)
image bg bedroom connor = im.FactorScale("images/backgrounds/bg bedroom connor.webp", 1.4)
image bg bedroom devon day = im.FactorScale("images/backgrounds/bg bedroom devon.webp", 1.4)
image bg bedroom devon night = im.FactorScale("images/backgrounds/bg devon bedroom.webp", 1.4)
image bg bedroom lincoln teen = im.FactorScale("images/backgrounds/bg bedroom lincoln teen.webp", 1.13)
image bg bedroom matthias = im.FactorScale("images/backgrounds/bg bedroom matthias.webp", 1.4)
image bg stacy bedroom = im.FactorScale("images/backgrounds/bg stacy bedroom.webp", 1.4)
image bg black = Solid("#000000", xysize=(1000, 1360))


###C
image bg cabin day = im.FactorScale("images/backgrounds/bg cabin day.webp", 1.2)
image bg cabin night = im.FactorScale("images/backgrounds/bg cabin night.webp", 1)
image bg cabin night rain = Composite(
    (1280, 1553),
        (0, 0), im.FactorScale("images/backgrounds/bg cabin night.webp", 1),
        (0, 200), "bg rain",
)
image bg cabin bedroom = im.FactorScale("images/backgrounds/bg cabin bedroom.webp", 1.4)
image bg cabin devon = im.FactorScale("images/backgrounds/bg cabin devon.webp", 1.4)
image bg cabin devon night = im.FactorScale("images/backgrounds/bg cabin devon night.webp", 1.4)
image bg cabin interior day = im.FactorScale("images/backgrounds/bg cabin interior day.webp", 1.4)
image bg cabin interior night = im.FactorScale("images/backgrounds/bg cabin interior night.webp", 1.4)
image bg cafe day = im.FactorScale("images/backgrounds/bg cafe day.webp", 1.4)
image bg campus = im.FactorScale("images/backgrounds/bg campus.webp", 1.4)
image bg campus 2 = im.FactorScale("images/backgrounds/bg campus 2.webp", 1.4)
image bg campus night = im.FactorScale("images/backgrounds/bg campus night.webp", 1.4)
image bg campsite day = im.FactorScale("images/backgrounds/bg campsite day.webp", 1.4)
image bg campsite night = im.FactorScale("images/backgrounds/bg campsite night.webp", 1.4)
image bg car town day = im.FactorScale("images/backgrounds/bg car town day.webp", 1.4)
image bg car neighborhood = im.FactorScale("images/backgrounds/bg car neighborhood.webp", 1.4)
image bg car woods day = im.FactorScale("images/backgrounds/bg car woods day.webp", 1.4)
image bg car woods night = im.FactorScale("images/backgrounds/bg car woods night.webp", 1)
image bg carnival booth = im.FactorScale("images/backgrounds/bg bgz_romance_ext_island_coney_day-v01.webp", 1.4)
image bg carnival day = im.FactorScale("images/backgrounds/bg bgz_romance_ext_fairgounds_rural_day-v01.webp", 1.0)
image bg carnival clouded = Composite(
    (1121, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival clouded.webp", 1.4)
)
image bg carnival clouded rain light = Composite(
    (1121, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival clouded.webp", 1.4),
        (0, 0), "bg rain light"
)
image bg carnival clouded rain = Composite(
    (1121, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival clouded.webp", 1.4),
        (0, 0), Tile("bg rain light")
)

image bg carnival evening rain light = Composite(
    (2242, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival evening.webp", 1),
        (0, 0), Tile("bg rain light")
)
image bg carnival evening rain = Composite(
    (2242, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival evening.webp", 1),
        (0, 0), Tile("bg rain")
)
image bg carnival evening car = Composite(
    (2242, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival evening.webp", 1),
        (0, 0), Tile("bg rain"),
        (500, 0), "images/backgrounds/car overlay.webp"
)

image bg carnival dance rain = Composite(
    (1121, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg carnival dance night.webp", 1.2),
        (0, 0), "bg rain"
)

image bg carnival stage rain = Composite(
    (1121, 1360),
        (0, 0), "images/backgrounds/stage_night.webp",
        (0, 0), "bg rain light"
)

image bg carnival dance = im.FactorScale("images/backgrounds/bg carnival dance.webp", 1.13)
image bg cave inside = im.FactorScale("images/backgrounds/bg bgz_romance_int_cave_mysterious_neutral-v01.webp", 1.4)
image bg cemetery = im.FactorScale("images/backgrounds/bg bgz_historical_ext_graveyard_lush_day-v01.webp", 1.0)
image bg cemetery night = im.FactorScale("images/backgrounds/bg cemetery.webp", 1.13)
image bg chamber = im.FactorScale("images/backgrounds/bg chamber.webp", 1.8)
image bg clearing night = Composite(
    (1123, 1360),
        (-180, -340), "images/backgrounds/bg dirt clearing.webp",
        (0, -1), im.FactorScale("images/backgrounds/car overlay.webp", 1.05)
)
image bg classroom = im.FactorScale("images/backgrounds/bg classroom.webp", 1.4)
image bg clearing day = im.FactorScale("images/backgrounds/bg clearing day.webp", 1.4)
image bg closet = im.FactorScale("images/backgrounds/bg closet.webp", 1.4)
image bg college fair = im.FactorScale("images/backgrounds/bg college fair.webp", 1.4)
image bg college park = im.FactorScale("images/backgrounds/bg college park.webp", 1.4)
image bg lake fall night = Composite(
    (1123, 1362),
        (125, 0), "images/backgrounds/bg lake fall night.webp",
        (0, 0), "images/backgrounds/car overlay.webp"
)
###D
image bg dam night = im.FactorScale("images/backgrounds/bg dam night.webp", 1.2)
image bg dark cave = im.FactorScale("images/backgrounds/bg dark cave.webp", 1.4)
image bg diner = im.FactorScale("images/backgrounds/bg diner.webp", 1.8)
image bg beach car = Composite(
    (1123, 1362),
        (-100, -300), "images/backgrounds/beach ep/bg downtown shops.webp",
        (0, 0), "images/backgrounds/car overlay.webp"
)

image bg beach car night = Composite(
    (1123, 1362),
        (0, 0), "images/backgrounds/beach ep/bg downtown shops night.webp",
        (0, 0), "images/backgrounds/car overlay.webp"
)

###E
image bg er = im.FactorScale("images/backgrounds/bg er.webp", 1.4)
image bg estate_greer night = im.FactorScale("images/backgrounds/bg estate_greer night.webp", 1.4)

###F
image bg ferris wheel = im.FactorScale("images/backgrounds/bg Ferris wheel.webp", 1.13)

image bg ferris wheel night = Composite(
    (1121, 1360),
        (0, 0), "images/backgrounds/bg ferris wheel night.webp",
        (0, 0), "bg rain light"
)
image bg flooded house = im.FactorScale("images/backgrounds/bg flooded house.webp", 1.5)
image bg forest night = im.FactorScale("images/backgrounds/bg forest night.webp", 1.0)
image bg forest pond day = im.FactorScale("images/backgrounds/bg forest pond day.webp", 1.4)
image bg forest pond night = im.FactorScale("images/backgrounds/bg forest pond night.webp", 1.4)
image bg forest road night = im.FactorScale("images/backgrounds/bg forest road night.webp", 1.4)
image bg forest road night car = Composite(
    (2242, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg forest road night.webp", 1.4),
        (0, 0), "bg rain",
        (500, 0), "images/backgrounds/car overlay.webp"
)

image bg forest rocky foggy = im.FactorScale("images/backgrounds/bg forest rocky foggy.webp", 1.2)
image bg fountain night = Composite(
    (866, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg fountain night.webp", 1.13),
)

###G
image bg garage = im.FactorScale("images/backgrounds/bg garage.webp", 1.4)
image bg glowing cave = im.FactorScale("images/backgrounds/bg glowing cave.webp", 1.2)
image bg grand balcony night = im.FactorScale("images/backgrounds/bg grand balcony night.webp", 1.4)
image bg grand staircase = im.FactorScale("images/backgrounds/bg grand staircase.webp", 1.4)
image bg gym interior = im.FactorScale("images/backgrounds/bg gym interior.webp", 1.4)

###H
image bg hallway luxurious night = im.FactorScale("images/backgrounds/bg hallway luxurious night.webp", 1.4)
image bg hallway sleek = im.FactorScale("images/backgrounds/bg hallway sleek.webp", 1.4)
image bg hallway lab = im.FactorScale("images/backgrounds/bg hallway lab.webp", 0.7)
image bg hallway mansion = im.FactorScale("images/backgrounds/bg hallway mansion.webp", 0.7)
image bg hallway fancy apartment = im.FactorScale("images/backgrounds/bg hallway fancy apartment.webp", 0.7)
image bg haunted house = im.FactorScale("images/backgrounds/bg haunted house.webp", 1.13)
image bg hedge maze = im.FactorScale("images/backgrounds/bg bgz_romance_ext_maze_hedge_night-v01.webp", 1.4)
image bg hospital waiting room = im.FactorScale("images/backgrounds/bg hospital waiting room.webp", 1.4)
image bg hospital room day = im.FactorScale("images/backgrounds/bg hospital room.webp", 1.4)
image bg hospital room night = im.FactorScale("images/backgrounds/bg hospital room night.webp", 1.4)
image bg hotel pool = im.FactorScale("images/backgrounds/bg hotel pool.webp", 1.4)
image bg hotel night = im.FactorScale("images/backgrounds/bg hotel night.webp", 1.35)

##
image bg ilitw mc house night = im.FactorScale("images/backgrounds/bg ilitw mc house night.webp", 1.8)
image bg ilitw mc house day = im.FactorScale("images/backgrounds/bg ilitw mc house day.webp", 1.8)

##
image bg j bedroom night = im.FactorScale("images/backgrounds/bg j bedroom night.webp", 2.3)
image bg j bedroom 2 = im.FactorScale("images/backgrounds/bg j bedroom 2.webp", 1.35)
image bg joss apartment = im.FactorScale("images/backgrounds/bg joss apartment.webp", 1.4)

##k
image bg kitchen matthias = im.FactorScale("images/backgrounds/bg kitchen matthias.webp", 1.8)
image bg kitchen matthias night = im.FactorScale("images/backgrounds/bg kitchen matthias night.webp", 1.8)

##L
image bg lake1 night = im.FactorScale("images/backgrounds/bg bg_timeline_romance_ext_rising_ghost_lake_night-v01.webp", 1.4)
image bg lake2 night = im.FactorScale("images/backgrounds/bg bgz_romance_ext_lake_estate_night-v01.webp", 0.7)
image bg lakehouse interior = im.FactorScale("images/backgrounds/bg lakehouse interior.webp", 1.4)
image bg lakehouse day = im.FactorScale("images/backgrounds/bg lakehouse day.webp", 1.4)
image bg lakehouse night = im.FactorScale("images/backgrounds/bg lakehouse night.webp", 1.4)
image bg library 2 = im.FactorScale("images/backgrounds/bg library 2.webp", 1.4)
image bg linc apartment = im.FactorScale("images/backgrounds/bg linc apartment.webp", 1.4)
image bg living room lucia = im.FactorScale("images/backgrounds/bg living room.webp", 1.4)
image bg living room mari = im.FactorScale("images/backgrounds/bg living room 2.webp", 1.4)
image bg living room stacy = im.FactorScale("images/backgrounds/bg stacy living.webp", 1.4)
image bg locker room = im.FactorScale("images/backgrounds/bg locker room.webp", 1.4)
image bg lobby = im.FactorScale("images/backgrounds/bg lobby.webp", 0.7)


###M
image bg mansion rowan outside = im.FactorScale("images/backgrounds/bg mansion.webp", 1)
image bg mansion rowan living = im.FactorScale("images/backgrounds/bg mansion rowan living.webp", 1.4)
image bg mansion adrian outside = im.FactorScale("images/backgrounds/bg mansion adrian outside.webp", 1)
image bg mansion adrian hallway = im.FactorScale("images/backgrounds/bg mansion adrian hallway.webp", 1.13)
image bg mansion adrian living = im.FactorScale("images/backgrounds/bg mansion adrian living room.webp", 1)
image bg mansion adrian study = im.FactorScale("images/backgrounds/bg mansion adrian study.webp", 1)
image bg mansion dining room = im.FactorScale("images/backgrounds/bg mansion dining room.webp", 1)
image bg mansion matthias = im.FactorScale("images/backgrounds/bg matthias house.webp", 1.8)
image bg mansion matthias study = im.FactorScale("images/backgrounds/bg study matthias.webp", 1)
image bg mansion outside matthias = im.FactorScale("images/backgrounds/bg mansion outside matthias.webp", 1.4)
image bg mansion outside matthias night = im.FactorScale("images/backgrounds/bg mansion outside matthias night.webp", 1.4)
image bg matthias basement  = im.FactorScale("images/backgrounds/bg matthias basement.webp", 1.13)
image bg mirror house = im.FactorScale("images/backgrounds/bg mirror house.webp", 1.13)
image bg mountain river night = im.FactorScale("images/backgrounds/bg mountain river night.webp", 1.4)

image bg motelnight = im.FactorScale("images/backgrounds/bg motelnight.webp", 1.13)

##N
image bg neighborhood = im.FactorScale("images/backgrounds/bg neighborhood.webp", 1.4)
image bg neighborhood 2 = im.FactorScale("images/backgrounds/bg neighborhood 2.webp", 1.4)

###O
image bg office = im.FactorScale("images/backgrounds/bg office.webp", 1.4)
image bg outer cave night = im.FactorScale("images/backgrounds/bg outer cave night.webp", 1.8)

###P
image bg portal harper creepy = Composite(
    (1123, 1362),
        (0.25, 0.2), im.FactorScale("images/backgrounds/bg harpers creepy house.webp", 0.9),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)
image bg portal harper underwater  = Composite(
    (1123, 1362),
        (0.25, 0.2), im.FactorScale("images/backgrounds/bg underwater ocean.webp", 0.9),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)
image bg parking = im.FactorScale("images/backgrounds/bg parking.webp", 1.4)
image bg police station = im.FactorScale("images/backgrounds/bg police station.webp", 1.4)
image bg portal = im.FactorScale("images/backgrounds/bg portal.webp", 1.4)
image bg portland = im.FactorScale("images/backgrounds/bg portland.webp", 1.4)
image bg portal forest = Composite(
    (1123, 1362),
        (0.25, 0.2), im.FactorScale("images/backgrounds/bg deep forest.webp", 0.9),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)
image bg portal white = Composite(
    (1123, 1362),
        (0.25, 0.2), im.FactorScale("images/backgrounds/bg bg_white.webp", 0.9),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)
image bg portal ruin = Composite(
    (1123, 1362),
        (0,0), im.FactorScale("images/backgrounds/bg temple ruin.webp", 1),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)
image bg portal tomb = Composite(
    (1123, 1362),
        (.15,0), im.FactorScale("images/backgrounds/bg tomb.webp", 0.9),
        (0, 0), "images/backgrounds/bg portal rift.webp"
)

#### R
image bg restaurant = im.FactorScale("images/backgrounds/bg restaurant fancy.webp", 1.0)
image bg ritual night = im.FactorScale("images/backgrounds/bg ritual night.webp", 1.8)
image bg ritual night rain = Composite(
    (1121, 1360),
        (0, 0), im.FactorScale("images/backgrounds/bg ritual night.webp", 1.8),
        (0, 0), "bg rain",
)
image bg cliff night rain = Composite(
    (1121, 1360),
        (0, 0), "images/backgrounds/bg cliff night.jpg",
        (0, 0), "bg rain",
)

image bg rodeo = im.FactorScale("images/backgrounds/bg rodeo.webp", 1.4)
image bg ruins = im.FactorScale("images/backgrounds/bg ruins.webp", 1.4)
image bg rundown building = im.FactorScale("images/backgrounds/bg rundown building.webp", 1)

##U
image bg u of o  = im.FactorScale("images/backgrounds/bg bgz_romance_ext_quad_college_day-v01.webp", 0.7)
image bg u of o night  = im.FactorScale("images/backgrounds/bg bgz_romance_ext_quad_college_night-v01.webp", 0.7)

###S
image bg school exterior = im.FactorScale("images/backgrounds/bg school exterior.webp", 1.4)
image bg school hallway = im.FactorScale("images/backgrounds/bg school hallway.webp", 1.4)
image bg security room = im.FactorScale("images/backgrounds/bg security room.webp", 1.4)
image bg sidewalk = im.FactorScale("images/backgrounds/bg sidewalk.webp", 1.4)
image bg stump = im.FactorScale("images/backgrounds/bg stump.webp", 1.4)

###T
image bg tablets_empty = im.FactorScale("images/tablets puzzle/tablets_shelf.webp", 1)
image bg tent = im.FactorScale("images/backgrounds/bg tent.webp", 1.4)
image bg tattoo parlor = im.FactorScale("images/backgrounds/bg tattoo parlor.webp", 1.4)
image bg tunnel = im.FactorScale("images/backgrounds/bg tunnel.webp", 1.7)

###V
image bg villa day = im.FactorScale("images/backgrounds/bg roman villa day.webp", 1.4)
image bg villa night = im.FactorScale("images/backgrounds/bg roman villa night.webp", 1.4)

###w
image bg warehouse = im.FactorScale("images/backgrounds/bg warehouse.webp", 1.35)
image bg westchester day = im.FactorScale("images/backgrounds/bg westchester_day.webp", 1.5)
image bg westchester night = im.FactorScale("images/backgrounds/bg westchester_night.webp", 1.5)
image bg westchester woods foggy = im.FactorScale("images/backgrounds/bg westchester woods foggy.webp", 1.4)
image bg witch cave day = im.FactorScale("images/backgrounds/bg witch cave day.webp", 1.8)
image bg woman cave = im.FactorScale("images/backgrounds/bg woman cave.webp", 1.4)
image bg white = im.FactorScale("images/backgrounds/bg bg_white.webp", 1.4)

#heart
image bg heart = "images/heart.png"
image bg heartbreak = "images/heartbreak.png"
#ok emoji
image okhand = "images/ok hand.png"
