import json

from units.vehicles import Vehicles
from units.soldier import Soldier
from units.squad import Squad
from units.army import Army


def data_armies(clock):
    with open('data/armies.json') as json_file:
        json_data = json.load(json_file)
    armies = []
    for army in range(len(json_data['armies'])):
        units = []
        squads = []
        for squad in range(len(json_data['armies'][army]['squads'])):
            for unit in json_data['armies'][army]['squads'][squad]['units']:
                if unit['unit_type'] == 'soldier':
                    units.append(Soldier(unit['health'], unit['name'], clock))
                elif unit['unit_type'] == 'vehicle':
                    units.append(Vehicles(unit['health'], unit['name'], [
                        Soldier(operator['health'], operator['name'], clock)
                        for operator in unit['operators']
                    ], clock))
            squads.append(Squad(json_data['armies'][army]['squads'][squad]['name'], units))
        armies.append(Army(json_data['armies'][army]['name'], squads, json_data['armies'][army]['strategy']))
    return armies
