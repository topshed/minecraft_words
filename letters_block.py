import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import subprocess
import copy

mc = minecraft.Minecraft.create()               
mc.saveCheckpoint()

var_input = raw_input('Enter word to be built: ')
var_blck_input = raw_input('Enter type of block: ')
var_blck_input = var_blck_input.upper()
find_centre = len(var_input) *2

player_pos = mc.player.getPos()
print 'player starts at'  + str(player_pos)
start_pos = copy.copy(player_pos)
#mc.player.setPos(player_pos.x, player_pos.y, player_pos.z)
mc.camera.setPos(player_pos.x +find_centre, player_pos.y, player_pos.z + 15)

def build_A(pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, getattr(block,var_blck_input))

def build_B(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y +1,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, getattr(block,var_blck_input))

def build_C(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))

def build_D(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +2,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))

def build_E(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y ,pos.z, getattr(block,var_blck_input))

def build_F(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y +2,pos.z, getattr(block,var_blck_input))

def build_G(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+1 ,pos.z, getattr(block,var_blck_input))

def build_H(pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y +2,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))

def build_I(pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+1 , pos.y+1 , pos.z, pos.x+1,pos.y +3,pos.z, getattr(block,var_blck_input))

def build_J(pos):
	mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y +4,pos.z, getattr(block,var_blck_input))
	mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y +3,pos.z, getattr(block,var_blck_input))

def build_K(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, getattr(block,var_blck_input))


def build_L(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))


def build_M(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+3,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+4 , pos.y , pos.z, pos.x+4,pos.y+3,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+4,pos.y+4 ,pos.z, getattr(block,var_blck_input))

def build_N(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y +3,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+3,pos.z, getattr(block,var_blck_input))

def build_O(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y+4 ,pos.z, getattr(block,var_blck_input))

def build_P(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+2,pos.y+2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+3 ,pos.z, getattr(block,var_blck_input))

def build_Q(pos):
        mc.setBlocks(pos.x , pos.y+2 , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+1,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+4 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+3 , pos.y , pos.z, pos.x+2,pos.y ,pos.z, getattr(block,var_blck_input))

def build_R(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x,pos.y+2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+3,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1 ,pos.z, getattr(block,var_blck_input))

def build_S(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+2,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+2 , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))

def build_T(pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y+3,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))          

def build_U(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))          

def build_V(pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))          

def build_W(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+4,pos.y,pos.z, getattr(block,var_blck_input))          
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+1 , pos.z, pos.x+2,pos.y+4,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+4 , pos.y+1 , pos.z, pos.x+4,pos.y+4 ,pos.z, getattr(block,var_blck_input))

def build_X(pos):
        mc.setBlock(pos.x+1 , pos.y+2 , pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x,pos.y+1 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y , pos.z, pos.x+2,pos.y+1 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+3 , pos.z, pos.x,pos.y+4 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, getattr(block,var_blck_input))

def build_Y(pos):
        mc.setBlocks(pos.x+1 , pos.y , pos.z, pos.x+1,pos.y+3 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+3 , pos.z, pos.x+2,pos.y+4 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+3 , pos.z, pos.x,pos.y+4 ,pos.z, getattr(block,var_blck_input))

def build_Z(pos):
        mc.setBlocks(pos.x , pos.y , pos.z, pos.x+2,pos.y ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+1 , pos.z, pos.x,pos.y+2 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+1 , pos.y+2 , pos.z, pos.x+1,pos.y+2 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x+2 , pos.y+2 , pos.z, pos.x+2,pos.y+4 ,pos.z, getattr(block,var_blck_input))
        mc.setBlocks(pos.x , pos.y+4 , pos.z, pos.x+1,pos.y+4 ,pos.z, getattr(block,var_blck_input))

for letter in var_input:
        if letter == 'A' or letter == 'a':
                build_A(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'B' or letter == 'b':
                build_B(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'C' or letter == 'c':
                build_C(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'D' or letter == 'd':
                build_D(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'E' or letter == 'e':
                build_E(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'F' or letter == 'f':
                build_F(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'G' or letter == 'g':
                build_G(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'H' or letter == 'h':
                build_H(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'I' or letter == 'i':
                build_I(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'J' or letter == 'j':
                build_J(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'K' or letter == 'k':
                build_K(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'L' or letter == 'l':
                build_L(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'M' or letter == 'm':
                build_M(player_pos)
                player_pos.x = player_pos.x+6
        elif letter == 'N' or letter == 'n':
                build_N(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'O' or letter == 'o':
                build_O(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'P' or letter == 'p':
                build_P(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'Q' or letter == 'q':
                build_Q(player_pos)
                player_pos.x = player_pos.x+5
        elif letter == 'R' or letter == 'r':
                build_R(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'S' or letter == 's':
                build_S(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'T' or letter == 't':
                build_T(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'U' or letter == 'u':
                build_U(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'V' or letter == 'v':
                build_V(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'W' or letter == 'w':
                build_W(player_pos)
                player_pos.x = player_pos.x+6
        elif letter == 'X' or letter == 'x':
                build_X(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == 'Y' or letter == 'y':
                build_Y(player_pos)
                player_pos.x = player_pos.x+6
        elif letter == 'Z' or letter == 'z':
                build_Z(player_pos)
                player_pos.x = player_pos.x+4
        elif letter == ' ': 
                player_pos.x = player_pos.x+4
	else:
		print "sorry that word uses letters we don't know how to build"

time.sleep(5)
print 'moving player back'
mc.player.setPos(start_pos)
time.sleep(1)
end_pos = mc.player.getPos()
print 'player endss at'  + str(end_pos)

print 'start: ' + str(start_pos)
print 'player: ' + str(player_pos)
print 'end: ' + str(end_pos)
#subprocess.call('/home/pi/raspi2png-master/raspi2png -p /tmp/test2.png',shell=True)
#time.sleep(6)
#mc.restoreCheckpoint()
