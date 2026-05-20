### Transition shortcuts
init -1 python:

    import renpy.exports as renpy_

    def delayed_hide(name, delay=0.4):
        def _hide():
            renpy_.hide(name)
        renpy_.timeout(delay)
        renpy_.queue_event((_hide,))

    def sl(name):
        """
        FOR PC
        shows name inleft
        """

        if panning_on and dialogue_old == "right":
            if who_old == None:
                renpy.pause(.15)
            renpy.show("bg", at_list=[pan_bg_right])
            renpy.pause(.05)
            store.dust_xoffset = -50
            renpy.pause(.05)

        else:
            if narrator_size_old == "nxl":
                renpy.pause(store.hide_ease + 0.12)
            else:
                renpy.pause(store.hide_ease)

        if renpy.config.skipping or renpy.in_rollback():
            renpy.show(name)
            return

        if textbox_old == "nxl":
            renpy.pause(.12)
        renpy.show(name, at_list = [inleft])

    def sr(name):
        """
        FOR NPC
        shows name inright
        """
        if panning_on and dialogue_old == "left":
            if who_old == None:
                renpy.pause(.1)
            renpy.show("bg", at_list=[pan_bg_left])
            renpy.pause(.05)
            store.dust_xoffset = 50
            renpy.pause(.05)

        else:
            if narrator_size_old == "nxl":
                renpy.pause(store.hide_ease + 0.12)
            else:
                renpy.pause(store.hide_ease)

        if renpy.config.skipping or renpy.in_rollback():
            renpy.show(name)
            return

        if textbox_old == "nxl":
            renpy.pause(.12)
        renpy.show(name, at_list = [inright])

    def hl(name):
        """
        FOR PC
        hides name outleft
        and adds 0.3s pause
        """
        if renpy.config.skipping or renpy.in_rollback():
            renpy.hide(name)
            return

        renpy.show(name, at_list = [outleft])
        def _hide():
            import time
            time.sleep(0.43)
            renpy.hide(name)
            renpy.restart_interaction()
        renpy.invoke_in_thread(_hide)

    def hr(name):
        """
        FOR NPC
        hides name outright
        and adds 0.3s pause
        """
        if renpy.config.skipping or renpy.in_rollback():
            renpy.hide(name)
            return

        renpy.show(name, at_list = [outright])
        def _hide():
            import time
            time.sleep(0.43)
            renpy.hide(name)
            renpy.restart_interaction()
        renpy.invoke_in_thread(_hide)

    def lr(name1, name2):
        """
        FOR PC-NPC
        hides name1 outleft and
        shows name2 inright
        """
        if renpy.config.skipping or renpy.in_rollback():
            if panning_on:
                renpy.show("bg", at_list=[pan_bg_left])
                renpy.pause(.15)
            renpy.hide(name1)
            renpy.show(name2)
            return

        renpy.show(name1, at_list = [outleft])

        ##bg pan
        if panning_on:
            renpy.show("bg", at_list=[pan_bg_left])
            renpy.pause(.15)
            store.dust_xoffset = 50
            renpy.pause(.05)

        ##sr
        renpy.show(name2, at_list = [inright])
        def _hide():
            import time
            time.sleep(0.2)
            renpy.hide(name1)
            renpy.restart_interaction()

    def rl(name1, name2):
        """
        FOR NPC-PC
        hides name1 outright and
        shows name2 inleft
        """
        if renpy.config.skipping or renpy.in_rollback():
            if panning_on:
                renpy.show("bg", at_list=[pan_bg_right])
                renpy.pause(.15)
            renpy.hide(name1)
            renpy.show(name2)
            return

        renpy.show(name1, at_list = [outright])

        #bg pan
        if panning_on:
            renpy.show("bg", at_list=[pan_bg_right])
            renpy.pause(.15)
            store.dust_xoffset = -50
            renpy.pause(.05)

        #sl
        renpy.show(name2, at_list = [inleft])
        def _hide():
            import time
            time.sleep(0.2)
            renpy.hide(name1)
            renpy.restart_interaction()

    def rr(name1, name2):
        """
        FOR NPC-NPC
        hides name1 outright and
        shows name2 inright
        """
        if renpy.config.skipping or renpy.in_rollback():
            renpy.hide(name1)
            renpy.show(name2)
            return

        renpy.show(name1, zorder=0)
        renpy.show(name2, at_list = [inright_fast], zorder=1)
        renpy.with_statement(Dissolve(0.2))
        hr(name1)

    def fr(name):
        """
        FOR RIGHT-SIDE MC
        flips character to the right side
        and shows it inright
        """
        if renpy.config.skipping or renpy.in_rollback():
            return

        renpy.show(name, at_list = [flipright])
        renpy.with_statement(Dissolve(0.2))

    def fl(name):
        """
        FOR LEFT-SIDE NON-MC PC
        flips character to the left side
        and shows it inleft
        """
        if dialogue_old == "right":
            if who_old == None:
                renpy.pause(.2)
            renpy.show("bg", at_list=[pan_bg_right])
            renpy.pause(.05)

        if renpy.config.skipping or renpy.in_rollback():
            return

        if textbox_old == "nxl":
            renpy.pause(.12)

        renpy.show(name, at_list = [flipleft])
        renpy.with_statement(Dissolve(0.2))

    def rfl(name1, name2):
        """
        FOR NPC and NON-MC PC
        hides name1 outright and
        shows name2 flipleft
        """
        if renpy.config.skipping or renpy.in_rollback():
            if panning_on:
                renpy.show("bg", at_list=[pan_bg_left])
                renpy.pause(.15)
            renpy.hide(name1)
            renpy.show(name2)
            return

        hr(name1)
        fl(name2)

    def rfr(name1, name2):
        """
        FOR NON-MC PC and NON-PC MC
        hides name1 outright and
        shows name2 flipright
        """
        renpy.show(name1, zorder=0)
        renpy.show(name2, at_list = [flipright], zorder=1)
        renpy.with_statement(Dissolve(0.2))
        hr(name1)

    def lfr(name1, name2):
        """
        FOR NON-MC PC and NON-PC MC
        hides name1 outright and
        shows name2 flipright
        """
        hl(name1)
        fr(name2)

    def sf(name):
        renpy.show(name, at_list = [fulldissolve])
        renpy.with_statement(Dissolve(0.5))

    def resolve_side(who_name, default_side):
        """
        Returns the side a character should appear on right now.
        Characters whose name matches playing_as are always on the left.
        """
        playing_as = renpy.store.playing_as  # or whatever your store variable is
        if playing_as and who_name == playing_as:
            return "left"
        return default_side

    def auto_sprite_transition(new_who, expression="no"):
        old_who = renpy.store.last_named_speaker
        old_tag = renpy.store.last_shown_tag
        old_side = renpy.store.last_shown_side

        new_info = get_character_defaults().get(new_who) if new_who else None
        new_side = resolve_side(new_who, new_info[1]) if new_info else None

        new_tag = new_info[0].split()[0] if new_info else None   # e.g. "lincoln"
        new_img = "{} {}".format(new_tag, expression) if new_tag else None  # e.g. "lincoln sad"

        new_visible = (new_tag == renpy.store.last_shown_tag)

        # Same character — just dissolve to new expression if it changed
        if old_who == new_who:
            if new_tag and expression != renpy.store.last_shown_expression:
                renpy.show(new_img)
                #renpy.with_statement(Dissolve(0.1))
                renpy.store.last_shown_expression = expression
            renpy.store.last_named_speaker = new_who
            return

        # Different character — same transition logic as before, but using new_img
        if old_tag and new_info and not new_visible:
            if old_side == "left" and new_side == "right":
                lr(old_tag, new_img)
            elif old_side == "right" and new_side == "left":
                rl(old_tag, new_img)
            elif old_side == "right" and new_side == "right":
                rr(old_tag, new_img)
            elif old_side == "left" and new_side == "left":
                rr(old_tag, new_img)
            renpy.store.last_shown_tag = new_tag
            renpy.store.last_shown_side = new_side
            renpy.store.last_shown_expression = expression

        elif not old_tag and new_info and not new_visible:
            if new_side == "left":
                sl(new_img)
            else:
                sr(new_img)
            renpy.store.last_shown_tag = new_tag
            renpy.store.last_shown_side = new_side
            renpy.store.last_shown_expression = expression

        elif old_tag and not new_info:
            if old_side == "left":
                hl(old_tag)
            else:
                hr(old_tag)
            renpy.store.last_shown_tag = None
            renpy.store.last_shown_side = None
            renpy.store.last_shown_expression = "no"

        renpy.store.last_named_speaker = new_who

    def hide_sprite():
        old_tag = renpy.store.last_shown_tag
        old_side = renpy.store.last_shown_side
        if old_tag:
            if old_side == "left":
                renpy.show(old_tag, at_list=[outleft])
            else:
                renpy.show(old_tag, at_list=[outright])
            renpy.pause(0.15)
            delayed_hide(old_tag, 0.4)
        renpy.store.last_shown_tag = None
        renpy.store.last_shown_side = None
        renpy.store.last_shown_expression = "no"
        renpy.store.last_named_speaker = None

    def make_char_callback(who_name, expression="no"):
        def _cb(event, interact=True, **kwargs):
            if event == "begin" and interact:
                auto_sprite_transition(who_name, expression)
        return _cb

    def narrator_sprite_callback(event, interact=True, **kwargs):
        if event == "begin" and interact:
            auto_sprite_transition(None)

    #for CHARACTER DEFAULTS, you are naming a callback which can be combined with character definitions, as shown BELOW. first column is the character callback, second is the character image, third column is their designated side.

    #$ connor_no = Character("CONNOR", color="#292928", who_outlines=[ (1, "#E5DBD9") ], what_xpos=175, what_ypos=-27, who_xpos=305, who_ypos=805, callback=make_char_callback("CONNOR"))

default last_named_speaker = None
default last_shown_tag = None
default last_shown_side = None
default last_shown_expression = "no"
default dust_xoffset = 0

transform dust_follow:
    on show:
        xoffset 0
    on replace:
        linear 0.3 xoffset dust_xoffset

transform pan_bg_right:
    linear 0.3 xoffset 50

transform pan_bg_left:
    linear 0.3 xoffset -50
