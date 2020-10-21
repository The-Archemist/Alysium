# -*- coding: utf-8 -*-
"""
Connection screen

This is the text to show the user when they first connect to the game (before
they log in).

To change the login screen in this module, do one of the following:

- Define a function `connection_screen()`, taking no arguments. This will be
  called first and must return the full string to act as the connection screen.
  This can be used to produce more dynamic screens.
- Alternatively, define a string variable in the outermost scope of this module
  with the connection string that should be displayed. If more than one such
  variable is given, Evennia will pick one of them at random.

The commands available to the user when the connection screen is shown
are defined in evennia.default_cmds.UnloggedinCmdSet. The parsing and display
of the screen is done by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|b===================================================================|n

                            |C Alysium

|c    .                  |W.-.    |c.      |C*     |w_   |c.
           |C*          |w/   \\              _/ \\       |C*    |c.
        |w__    |c.   |w.--'\\/\\_ \\            /    \\  |C*   |w___
     |C* |w/  \\_    _/ ^      \\/\\'__       /\\/\\  /\\  __/   \\ |C*
|w      /     \\  /    .'   _/  /  \\  |C*  |w/    \\/  \\/ .`'\\_/\\   |c.
|c  .  |Y/\\/\\   /\\/ :' __  ^/  ^/    `--./.'  ^  `-.\\ _    _:\\ _
|Y    /    \\/   \\  _/  \\-' __/.' ^ _   \\_   .'\\   _/ \\ .  __/ \\
|Y   /\\  .-   `. \\/     \\ / -.   _/ \\ -. `_/   \\ /    `._/  ^  \\
|Y  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
|Y /        `.  / /      `-.   /  .-'   / .   .'   \\    \\  \\  .-  \\
|n

 If you have an existing account, connect to it by typing:
      |wconnect <username> <password>|n
 If you need to create an account, type (without the <>'s):
      |wcreate <username> <password>|n

|b===================================================================|n\n> """.format(
    settings.SERVERNAME, utils.get_evennia_version("short")
)
