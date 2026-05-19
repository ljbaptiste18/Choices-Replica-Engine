init:
    $renpy.music.register_channel("sfx", mixer="sfx", loop=True)

init python:
    def play_sound_n_times(sound_file, n, duration):
        for _ in range(n):
            renpy.sound.play(sound_file)
            renpy.pause(duration, hard=True)
