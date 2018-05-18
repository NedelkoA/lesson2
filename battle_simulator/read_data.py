import json

from units.vehicles import Vehicles
from units.soldier import Soldier
from units.squad import Squad
from units.army import Army


def data_armies():
    with open('data/armies.json') as f:
        d = json.load(f)
    armies = []
    for army in range(len(d['armies'])):
        units = []
        squads = []
        for squad in range(len(d['armies'][army]['squads'])):
            for i in d['armies'][army]['squads'][squad]['units']:
                if i['unit_type'] == 'soldier':
                    units.append(Soldier(i['health'], i['name']))
                elif i['unit_type'] == 'vehicle':
                    units.append(Vehicles(i['health'], i['name'], [
                        Soldier(j['health'], j['name'])
                        for j in i['operators']
                    ]))
        squads.append(Squad(d['armies'][army]['squads'][army]['name'], units))
        armies.append(Army(d['armies'][army]['name'], squads))
    return armies
