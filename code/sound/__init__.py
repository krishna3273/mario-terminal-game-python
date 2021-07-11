import os, sys
from subprocess import Popen

def play(sound_path):
        Popen(["aplay","-q",sound_path])
        

SOUND_PATHS = {
    'breakblock':os.path.abspath('sound/smb_breakblock.wav'),
    'coin':os.path.abspath('sound/smb_coin.wav'),
    'gameover':os.path.abspath('sound/smb_gameover.wav'),
    'jump-small':os.path.abspath('sound/smb_jump-small.wav'),
    'jump-super':os.path.abspath('sound/smb_jump-super.wav'),
    'mariodie':os.path.abspath('sound/smb_mariodie.wav'),
    'powerup':os.path.abspath('sound/smb_powerup.wav'),
    'powerup-appears':os.path.abspath('sound/smb_powerup-appears.wav'),
    'stage':os.path.abspath('sound/smb_stage_clear.wav'),
    'bump' : os.path.abspath('sound/smb_bump.wav')
}

'''if __name__ == "__main__":
    for i,v in SOUND_PATHS.items():
        song = v
        play(song)'''
