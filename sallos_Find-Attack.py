# Target Closest, Attack and Humanoid only options by Prioriety
#   aka sallos target find
# by MatsaMilla & contributions by Trick Tickler
# Last Update: 3/15/21 - added agro gray for player check
from System.Collections.Generic import List
from System import Byte
import sys

# true to attack, false will only set as last target
attack = True

# true for humanoid only, false excludes humaniods
humanoid = False

# true to also target red targets. (I keep false to not auto target bosses)
redTargets = True

# true to send target message to party
sendMessage = False

# true to display target overhead & over mobile
displayTarget = False

# range at which target will aquire
targetRange = 12

# filter
def find(notoriety, humanoid):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = targetRange
    fil.IsHuman = humanoid
    fil.IsGhost = False
    fil.Friend = False
    fil.Notorieties = List[Byte](bytes(notoriety))
    list = Mobiles.ApplyFilter(fil)

    return list

# Possible Selections:
# 1 blue, 2 green, 3 grey, 4 grey(agro), 5 orange, 6 red, 7 invul
# Random, Nearest,Farthest, Weakest, Strongest, Next

# if your toon is blue, green, or gray or militia
if (Player.Notoriety == 1 or Player.Notoriety == 2 or Player.Notoriety == 3 or Player.Notoriety == 4):
    greyMobile = Mobiles.Select(find([3,4],humanoid),'Nearest',)
    orangeMobile = Mobiles.Select(find([5],humanoid),'Nearest')
    if redTargets:
        redMobile = Mobiles.Select(find([6],humanoid),'Nearest')
    else:
        redMobile = None
    if orangeMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
        if displayTarget:
            Player.HeadMessage(47, "Target: " + orangeMobile.Name)
            Mobiles.Message(orangeMobile, 15, "*Target*")
    elif redMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)
        if displayTarget:
            Player.HeadMessage(33, "Target: " + redMobile.Name)
            Mobiles.Message(redMobile, 15, "*Target*")
    elif greyMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)
        if displayTarget:
            Player.HeadMessage(902, "Target: " + greyMobile.Name)
            Mobiles.Message(greyMobile, 15, "*Target*")
    else:
        Misc.SendMessage('No Targets', 33)

# if your toon is red
elif Player.Notoriety == 6:
    blueMobile = Mobiles.Select(find([1],humanoid),'Nearest')
    greyMobile = Mobiles.Select(find([3,4],humanoid),'Nearest')
    orangeMobile = Mobiles.Select(find([5],humanoid),'Nearest')
    if redTargets:
        redMobile = Mobiles.Select(find([6],humanoid),'Nearest')
    else:
        redMobile = None
    if blueMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + blueMobile.Name)
        Target.SetLast(blueMobile)
        if attack:
            Player.Attack(blueMobile)
        if displayTarget:
            Player.HeadMessage(1266, "Target: " + blueMobile.Name)
            Mobiles.Message(blueMobile, 15, "*Target*")
    elif greyMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)
        if displayTarget:
            Player.HeadMessage(902, "Target: " + greyMobile.Name)
            Mobiles.Message(greyMobile, 15, "*Target*")
    elif orangeMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
        if displayTarget:
            Player.HeadMessage(47, "Target: " + orangeMobile.Name)
            Mobiles.Message(orangeMobile, 15, "*Target*")
    elif redMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)
        if displayTarget:
            Player.HeadMessage(33, "Target: " + redMobile.Name)
            Mobiles.Message(redMobile, 15, "*Target*")
    else:
        Misc.SendMessage('No Targets', 33)
