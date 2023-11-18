from enum import Enum
import random

random.seed(0)

class Typ(Enum):
  MILITIA = 1
  ARCHER = 2
  FOOTSOLDIER = 3
  CAVALRY = 4
  LONGBOW_ARCHER = 5
  KNIGHT = 6
  CROSSBOWMAN = 7
  CUIRASSIER = 8
  CANNONEER = 9
  ORCLING = 10
  ORC_HUNTER = 11
  ORC_RAIDER = 12
  WARG_RIDER = 13
  ELITE_ORC_HUNTER = 14
  ORC_VETERAN = 15
  ELITE_ORC_SNIPER = 16
  ORC_VANGUARD = 17
  ORC_DEMOLISHER = 18
  BULA = 19
  AGUK = 20
  MAZOGA = 21
  DURGASH = 22



class militia:
  typ, hp, dam = Typ.MILITIA, 15, 5
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier, cost =  0.8, 1, 1

class archer:
  typ, hp, dam = Typ.ARCHER, 10, 20
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, False, False
  crit, tier, cost = 0.8, 1, 4

class footsoldier:
  typ, hp, dam = Typ.FOOTSOLDIER, 40, 15
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier, cost = 0.8, 1, 8

class cavalry:
  typ, hp, dam = Typ.CAVALRY, 5, 5
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, True, False, True, False, False
  crit, tier, cost = 0.8, 2, 16

class longbow_archer:
  typ, hp, dam = Typ.LONGBOW_ARCHER, 10, 15
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, True, False
  crit, tier, cost = 0.8, 2, 32

class knight:
  typ, hp, dam = Typ.KNIGHT, 90, 20
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier, cost = 0.8, 3, 64

class crossbowman:
  typ, hp, dam = Typ.CROSSBOWMAN, 15, 90
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, False, False
  crit, tier, cost = 0.8, 3, 64

class cuirassier:
  typ, hp, dam = Typ.CUIRASSIER, 120, 10
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, True, False, False
  crit, tier, cost = 0.8, 4, 128

class cannoneer:
  typ, hp, dam = Typ.CANNONEER, 60, 80
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, True, True, False, False, True
  crit, tier, cost = 0.8, 4, 128



class orcling:
  typ, hp, dam = Typ.ORCLING, 15, 5
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier =  0.6, 1

class orc_hunter:
  typ, hp, dam = Typ.ORC_HUNTER, 10, 20
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, False, False
  crit, tier =  0.6, 1

class orc_raider:
  typ, hp, dam = Typ.ORC_RAIDER, 40, 15
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier =  0.6, 1

class warg_rider:
  typ, hp, dam = Typ.WARG_RIDER, 5, 5
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, True, False, True, False, False
  crit, tier =  0.6, 2

class elite_orc_hunter:
  typ, hp, dam = Typ.ELITE_ORC_HUNTER, 10, 15
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, True, False
  crit, tier =  0.6, 2

class orc_veteran:
  typ, hp, dam = Typ.ORC_VETERAN, 90, 20
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, False, False, False
  crit, tier =  0.6, 3

class elite_orc_sniper:
  typ, hp, dam = Typ.ELITE_ORC_SNIPER, 15, 90
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, False, False, False, False, False
  crit, tier =  0.6, 3

class orc_vanguard:
  typ, hp, dam = Typ.ORC_VANGUARD, 120, 10
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, False, True, False, False
  crit, tier =  0.6, 4

class orc_demolisher:
  typ, hp, dam = Typ.ORC_DEMOLISHER, 60, 80
  ranged, flanking, trample, first_strike, double_strike, last_strike = True, True, True, False, False, True
  crit, tier =  0.6, 4



class bula:
  typ, hp, dam = Typ.BULA, 5_000, 150
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, True, False, False, True
  crit, tier =  0.5, 100

class aguk:
  typ, hp, dam = Typ.AGUK, 11_000, 300
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, True, False, False, True
  crit, tier =  0.5, 150

class mazoga:
  typ, hp, dam = Typ.MAZOGA, 120_000, 100
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, True, False, False, True
  crit, tier =  0.5, 200

class durgash:
  typ, hp, dam = Typ.DURGASH, 40_000, 500
  ranged, flanking, trample, first_strike, double_strike, last_strike = False, False, True, False, False, True
  crit, tier =  0.5, 300



def cost(team):
  return sum(i.cost for i in team)

def duration(team):
  tier_sum = sum(i.tier for i in team)
  duration = (2*tier_sum)**1.4
  return min(8*60*60,duration)

def deal_damage(team, dam, trample = False, flanking = False):
  if flanking:
    raise ValueError
  elif trample:
    raise ValueError
  else:
    tmp = [i for i in team if i.hp > 0]
    if len(tmp) > 0:
      tmp[0].hp -= dam

def phase(paragons, orcs, paragons_active, orcs_active):
  for i in paragons_active:
    dam = i.dam
    if random.random() < i.crit:
      dam *= 2
    deal_damage(orcs, dam)
  for i in orcs_active:
    dam = i.dam
    if random.random() < i.crit:
      dam *= 2
    deal_damage(paragons, dam)
  paragons = [i for i in paragons if i.hp > 0]
  orcs = [i for i in orcs if i.hp > 0]
  return paragons, orcs

def fight(paragons, orcs):

  i_round = 0
  
  while True:
    if log_level > 0:
      print("Round:", i_round)
      
    for phase0 in [1,2,3]:
      if phase0 == 1:
        paragons_active = [i for i in paragons if i.first_strike or i.double_strike]
        orcs_active     = [i for i in orcs     if i.first_strike or i.double_strike]
      elif phase0 == 2:
        paragons_active = [i for i in paragons if not i.first_strike and not i.double_strike and not i.last_strike]
        orcs_active     = [i for i in orcs     if not i.first_strike and not i.double_strike and not i.last_strike]
      elif phase0 == 3:
        paragons_active = [i for i in paragons if i.last_strike or i.double_strike]
        orcs_active     = [i for i in orcs     if i.last_strike or i.double_strike]
      if len(paragons_active) > 0 or len(orcs_active) > 0:       
        if log_level > 1:
          print("Phase:", phase0) 
        paragons, orcs = phase(paragons, orcs, paragons_active, orcs_active)
        if len(orcs) == 0:
          return 1, paragons, orcs
        elif len(paragons) == 0:
          return 0, paragons, orcs
        if log_level > 0:
          print("Remaining orcs:",len(orcs),"Remaining paragons:",len(paragons))
      
    # Increment round counter
    i_round += 1

def create_paragons(militia0, archer0, footsoldier0, cavalry0, longbow_archer0, knight0, crossbowman0, cuirassier0, cannoneer0):
  return \
    [militia()        for i in range(militia0       )] +\
    [archer()         for i in range(archer0        )] +\
    [footsoldier()    for i in range(footsoldier0   )] +\
    [cavalry()        for i in range(cavalry0       )] +\
    [longbow_archer() for i in range(longbow_archer0)] +\
    [knight()         for i in range(knight0        )] +\
    [crossbowman()    for i in range(crossbowman0   )] +\
    [cuirassier()     for i in range(cuirassier0    )] +\
    [cannoneer()      for i in range(cannoneer0     )]

def create_orcs(orcling0, orc_hunter0, orc_raider0, warg_rider0, elite_orc_hunter0, orc_veteran0, elite_orc_sniper0, orc_vanguard0, orc_demolisher0, bula0, aguk0, mazoga0, durgash0):
  return \
    [orcling()          for i in range(orcling0          )] +\
    [orc_hunter()       for i in range(orc_hunter0       )] +\
    [orc_raider()       for i in range(orc_raider0       )] +\
    [warg_rider()       for i in range(warg_rider0       )] +\
    [elite_orc_hunter() for i in range(elite_orc_hunter0 )] +\
    [orc_veteran()      for i in range(orc_veteran0      )] +\
    [elite_orc_sniper() for i in range(elite_orc_sniper0 )] +\
    [orc_vanguard()     for i in range(orc_vanguard0     )] +\
    [orc_demolisher()   for i in range(orc_demolisher0   )] +\
    [bula()             for i in range(bula0             )] +\
    [aguk()             for i in range(aguk0             )] +\
    [mazoga()           for i in range(mazoga0           )] +\
    [durgash()          for i in range(durgash0          )]


militia0        = 0
archer0         = 0
footsoldier0    = 0
cavalry0        = 0
longbow_archer0 = 0
knight0         = 0
crossbowman0    = 0
cuirassier0     = 0
cannoneer0      = 0

orcling0          = 0
orc_hunter0       = 0
orc_raider0       = 0
warg_rider0       = 0
elite_orc_hunter0 = 0
orc_veteran0      = 0
elite_orc_sniper0 = 0
orc_vanguard0     = 0
orc_demolisher0   = 0

bula0 = 0
aguk0 = 0
mazoga0 = 0
durgash0 = 0

example = 0
if example == 0:
  cavalry0 = 21
  orcling0          = 20
  reps = 10
  fights = 1000
  log_level = 0
elif example == 1:
  cavalry0 = 21
  orcling0 = 20
  reps = 1
  fights = 1
  log_level = 2


paragons = create_paragons(militia0, archer0, footsoldier0, cavalry0, longbow_archer0, knight0, crossbowman0, cuirassier0, cannoneer0)
orcs     = create_orcs(orcling0, orc_hunter0, orc_raider0, warg_rider0, elite_orc_hunter0, orc_veteran0, elite_orc_sniper0, orc_vanguard0, orc_demolisher0, bula0, aguk0, mazoga0, durgash0)
print("This team costs",cost(paragons),"gold.")
print("This fights takes",duration(paragons+orcs),"seconds.")



for j in range(reps):
  wins = 0
  n_paragons = 0
  n_orcs = 0

  for i_fight in range(fights):
    if log_level > 0:
      print("Fight:", i_fight)
    
    paragons = create_paragons(militia0, archer0, footsoldier0, cavalry0, longbow_archer0, knight0, crossbowman0, cuirassier0, cannoneer0)
    orcs     = create_orcs(orcling0, orc_hunter0, orc_raider0, warg_rider0, elite_orc_hunter0, orc_veteran0, elite_orc_sniper0, orc_vanguard0, orc_demolisher0, bula0, aguk0, mazoga0, durgash0)
    win, paragons, orcs = fight(paragons, orcs)
    wins += win
    n_paragons += len(paragons)
    n_orcs += len(orcs)
  print(wins / fights, n_paragons / fights, n_orcs / fights)
