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

def is_first_strike(i):
  return i.typ in [Typ.CAVALRY,Typ.CUIRASSIER]

def is_ranged(i):
  return i.typ in [Typ.ARCHER, Typ.LONG_BOWARCHER, Typ.CROSSBOWMAN, Typ.CANNONEER]

def is_flanking(i):
  return i.typ in [Typ.CAVALRY,Typ.CANNONEER]

def is_double_strike(i):
  return i.typ in [Typ.LONGBOW_ARCHER]

def is_trample(i):
  return i.typ in [Typ.CANNONEER]

def is_last_strike(i):
  return i.typ in [Typ.CANNONEER]

def crit(i):
  if i.typ.value < 10:
    return .8
  elif i.typ.value < 19:
    return .6
  else:
    return .5

class militia:
  typ = Typ.MILITIA
  hp = 15
  dam = 5
  tier = 1
  cost = 1

class archer:
  typ = Typ.ARCHER
  hp = 10
  dam = 20
  tier = 1
  cost = 4

class footsoldier:
  typ = Typ.FOOTSOLDIER
  hp = 40
  dam = 15
  tier = 1
  cost = 8

class orcling:
  typ = Typ.ORCLING
  hp = 15
  dam = 5
  order = 1
  ranged = False

class orchunter:
  typ = Typ.ORC_HUNTER
  hp = 10
  dam = 20
  order = 1
  ranged = True

class orcraider:
  typ = Typ.ORC_RAIDER
  hp = 40
  dam = 15
  order = 2
  ranged = False

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
    #print("\nRound:", i_round)

    for i in paragons:
      dam = i.dam
      if random.random() < crit(i):
        dam *= 2
      orcs = deal_damage(orcs, dam)
    for i in orcs:
      dam = i.dam
      if random.random() < crit(i):
        dam *= 2
      paragons = deal_damage(paragons, dam)
    paragons = [i for i in paragons if i.hp > 0]
    orcs = [i for i in orcs if i.hp > 0]
    if len(orcs) == 0:
      return 1, paragons, orcs
    elif len(paragons) == 0:
      return 0, paragons, orcs

    # Increment round counter
    i_round += 1

def create_paragons(militia0,archer0,footsoldier0):
  return [militia() for i in range(militia0)] + [footsoldier() for i in range(footsoldier0)] + [archer() for i in range(archer0)]

def create_orcs(orcling0,orchunter0,orcraider0):
  return [orcling() for i in range(orcling0)] + [orcraider() for i in range(orcraider0)] + [orchunter() for i in range(orchunter0)]

for j in range(10):
  nfights = 1000
  wins = 0
  n_paragons = 0
  n_orcs = 0
  for i_fight in range(nfights):
    #print("\nFight:",i_fight)
    paragons = create_paragons(26,10,0)
    orcs = create_orcs(42,0,0)
    win, paragons, orcs = fight(paragons, orcs)
    wins += win
    n_paragons += len(paragons)
    n_orcs += len(orcs)
  print(wins / nfights,n_paragons / nfights, n_orcs / nfights)
