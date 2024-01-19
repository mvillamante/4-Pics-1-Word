import winsound
import os

CLICK_SOUND = os.getcwd() + "\\assets\\sound\\click.wav"
WIN_SOUND = os.getcwd() + "\\assets\\sound\\correct.wav"
INC_SOUND = os.getcwd() + "\\assets\\sound\\incorrect.wav"

def dbtn_snd():
    """This is the function that plays the click sound effect of all the buttons in the game."""
    winsound.PlaySound(CLICK_SOUND, winsound.SND_ASYNC)

def win_snd():
    """This is the function that plays the correct sound effect, if the answer of the user is correct."""
    winsound.PlaySound(WIN_SOUND, winsound.SND_ALIAS)

def inc_snd():
    """This is the function that plays the incorrect sound effect, if the answer of the user is incorrect."""
    winsound.PlaySound(INC_SOUND, winsound.SND_ASYNC)


