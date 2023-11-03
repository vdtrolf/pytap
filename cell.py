import random
from json import JSONEncoder
import json

from util import *

cellTypes1 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M, SHADES_H, SHADES_H, SHADES_H, SHADES_H)
cellTypes2 = ('      ', f'  {SHADE_L}  {SHADE_L}',f'  {SHADE_L}  {SHADE_L}',f' {SHADE_L}   {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', f' {SHADE_L} {SHADE_L} {SHADE_L}',f' {SHADE_L} {SHADE_L} {SHADE_L}', SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M, SHADES_H, SHADES_H, SHADES_H, SHADES_H)
cellTypes3 = ('      ', f'{SHADE_L}  {SHADE_L}  ',f'{SHADE_L}  {SHADE_L}  ',f'  {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', f'{SHADE_L} {SHADE_L} {SHADE_L} ',f'{SHADE_L} {SHADE_L} {SHADE_L} ', SHADES_L, SHADES_L, SHADES_M, SHADES_M, SHADES_M, SHADES_M, SHADES_H, SHADES_H, SHADES_H, SHADES_H)

cellfg = (239, 239, 239, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
cellbg = (COLOR_WATER, COLOR_ICE1, COLOR_ICE1, COLOR_ICE1, COLOR_ICE1, COLOR_ICE2, COLOR_ICE2,
          COLOR_ICE2, COLOR_ICE3, COLOR_ICE3, COLOR_ICE3, COLOR_ICE4, COLOR_ICE4, COLOR_ICE4, 
          COLOR_GROUND1, COLOR_GROUND2, COLOR_GROUND3)
angles = ('a','b')


class Cell:

    def __init__(self, vpos, hpos, cellType):
        self.key = get_next_key()
        self.vpos = vpos
        self.hpos = hpos
        self.cellType = cellType
        self.angle = angles[random.randint(0,1)]

    def startBuilding(self):
        """Sets the cell attributes related to the begin of a 'building' proces"""
        self.cellType = 3

    def endBuilding(self):
        """Sets the cell attributes related to the end of a 'building' proces"""
        self.cellType = 8

    def get_ascii(self):
        """ returns the ascii image of the cell """
        return [
            cellTypes1[self.cellType], cellTypes2[self.cellType], cellTypes3[self.cellType],
            cellfg[self.cellType], cellfg[self.cellType]
        ]

    def get_bg(self):
        """Returns the left and right characters to be used as background"""
        return [cellTypes1[self.cellType][0:1],cellTypes1[self.cellType][5:4],cellTypes2[self.cellType][0:1],cellTypes2[self.cellType][5:4],cellTypes3[self.cellType][0:1],cellTypes3[self.cellType][5:4]]

    def isGround(self):
        """Returns true if the content of the cell is ground (celltype > 0)"""
        return self.cellType > 0

    def isMount(self):
        """Returns true if the content of the cell is a mountain (celltype > 9)"""
        return self.cellType > 9

    def isSea(self):
        """Returns true if the content of the cell is sea (celltype = 0)"""
        return self.cellType == 0

    def become_older(self, weather,evolution_speed):
        """
        makes the ice smelt or reconstruct according to the weather
        smelting goes faster if the evolution_speed is higher and it's sunny
        smelting goes a bit faster if the evolution_speed is higher and it's raining
        rasing happens when it snows and goes slowwer if the evolution_speed is higher
        """
        if weather == WEATHER_SUN and self.cellType > 0 and self.cellType < 12 and random.randint(
                0, 6 - evolution_speed) == 0:
            self.cellType -= 1
        elif weather == WEATHER_RAIN and self.cellType > 0 and self.cellType < 12 and random.randint(
                0, (6 - evolution_speed) * 2) == 0:
            self.cellType -= 1
        elif weather == WEATHER_SNOW and self.cellType > 0 and self.cellType < 11 and random.randint(
                0, int((2 + evolution_speed)/2)) == 0:
            self.cellType += 1
            
    def get_data(self):
        return {
            'key' : self.key,
            'vpos' : self.vpos,
            'hpos' : self.hpos,
            'cellType' : self.cellType,
            'angle' : self.angle
        }

