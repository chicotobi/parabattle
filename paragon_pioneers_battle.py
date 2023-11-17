from enum import Enum
import random

random.seed(0)

log_level = 1

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
    for i in team:
      if i.hp > 0:
        i.hp -= dam
        return team
    return team


def fight(paragons, orcs):

  i_round = 0

  while True:
    if log_level > 0:
      print("\nRound:", i_round)

    for i in paragons:
      dam = i.dam
      if random.random() < i.crit:
        dam *= 2
      orcs = deal_damage(orcs, dam)
    for i in orcs:
      dam = i.dam
      if random.random() < i.crit:
        dam *= 2
      paragons = deal_damage(paragons, dam)
    paragons = [i for i in paragons if i.hp > 0]
    orcs = [i for i in orcs if i.hp > 0]
    if len(orcs) == 0:
      return 1, paragons, orcs
    elif len(paragons) == 0:
      return 0, paragons, orcs
    if log_level > 0:
      print(len(orcs),len(paragons))

    # Increment round counter
    i_round += 1

def create_paragons(militia0,archer0,footsoldier0):
  return [militia() for i in range(militia0)] + [footsoldier() for i in range(footsoldier0)] + [archer() for i in range(archer0)]

def create_orcs(orcling0,orc_hunter0,orc_raider0):
  return [orcling() for i in range(orcling0)] + [orc_raider() for i in range(orc_raider0)] + [orc_hunter() for i in range(orc_hunter0)]


paragons = create_paragons(26,10,0)
orcs = create_orcs(42,0,0)
print("This team costs",cost(paragons),"gold.")
print("This fights takes",duration(paragons+orcs),"seconds.")

for j in range(10):
  nfights = 1000
  wins = 0
  n_paragons = 0
  n_orcs = 0

  for i_fight in range(nfights):
    paragons = create_paragons(40,0,0)
    orcs = create_orcs(42,0,0)
    win, paragons, orcs = fight(paragons, orcs)
    wins += win
    n_paragons += len(paragons)
    n_orcs += len(orcs)
  print(wins / nfights,n_paragons / nfights, n_orcs / nfights)
