# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:06:06 2018

@author: Sherry
"""

#Mock Maze Code

start = 'room1'
end = 'room114'
currentRoom = 'room1'

roomlist = dict(
room1 = { 
	"desc": "Room 1",
	"directions": {"North": 2}
	},
	
room2 = { 
	"desc": "Room 2",
	"directions": {"North": 3, "South": 1}
	},

room3 = { 
	"desc": "Room 3",
	"directions": {"West": 4,"East": 5, "South": 2}
	},	

room4 = { 
	"desc": "Room 4",
	"directions": {"East": 3}
	},	
	
room5 = { 
	"desc": "Room 5",
	"directions": {"North": 6, "West": 3}
	},

room6 = { 
	"desc": "Room 6",
	"directions": {"North": 7, "South": 5}
	},
	
room7 = { 
	"desc": "Room 7",
	"directions": {"West": 72, "South": 6, "East": 8}
	},
		
room8 = { 
	"desc": "Room 8",
	"directions": {"West": 7, "East": 9}
	},
		
room9 = { 
	"desc": "Room 9",
	"directions": {"North": 10, "West": 8, "South": 13 }
	},
		
room10 = { 
	"desc": "Room 10",
	"directions": {"North": 11, "South": 9}
	},
		
room11 = { 
	"desc": "Room 11",
	"directions": {"East": 12, "South": 10}
	},
		
room12 = { 
	"desc": "Room 12",
	"directions": {"West": 11}
	},
		
room13 = { 
	"desc": "Room 13",
	"directions": {"North": 9, "South": 14}
	},
		
room14 = { 
	"desc": "Room 14",
	"directions": {"North": 13, "East": 15}
	},
		
room15 = { 
	"desc": "Room 15",
	"directions": {"West": 14, "South": 16}
	},
		
room16 = { 
	"desc": "Room 16",
	"directions": {"North": 15, "South": 17}
	},
		
room17 = { 
	"desc": "Room 17",
	"directions": {"North": 16, "South": 18}
	},
		
room18 = { 
	"desc": "Room 18",
	"directions": {"North": 17, "West": 19}
	},
	
room19 = { 
	"desc": "Room 19",
	"directions": {"East": 18, "South": 20}
	},
		
room20 = {
	"desc": "Room 20",
	"directions": {"North": 19, "South": 21}
	},
	
room21 = { 
	"desc": "Room 21",
	"directions": {"North": 20, "South": 22 }
	},
	
room22 = {
	"desc": "Room 22",
	"directions": {"North": 21, "South": 23}
	},
		
room23 = {
	"desc": "Room 23",
	"directions": {"North": 22, "West": 24}
	},
	
room24 = {
	"desc": "Room 24",
	"directions": {"West": 25, "East": 23}
	},
		
room25 = {
	"desc": "Room 25",
	"directions": {"North": 27, "South": 26, "East": 23}
	},
	
room26 = {
	"desc": "Room 26",
	"directions": {"North": 25}
	},
	
room27 = {
	"desc": "Room 27",
	"directions": {"west": 27, "South": 26}
	},
	
room28 = {
	"desc": "Room 28",
	"directions": {"West": 30, "East": 27}
	},
	
room29 = {
	"desc": "Room 29",
	"directions": {"West": 34, "South": 30}
	},
	
room30 = {
	"desc": "Room 30",
	"directions": {"North": 29, "South": 31}
	},
	
room31 = {
	"desc": "Room 31",
	"directions": {"North": 30, "South": 32}
	},
		
room32 = {
	"desc": "Room 32",
	"directions": {"North": 31, "West": 33}
	},
	
room33 = {
	"desc": "Room 33",
	"directions": {"East": 32}
	},
	
room34 = {
	"desc": "Room 34",
	"directions": {"West": 35, "East": 29}
	},
	
room35 = {
	"desc": "Room 35",
	"directions": {"North": 39, "South": 36, "East": 34}
	},
	
room36 = {
	"desc": "Room 36",
	"directions": {"North":35, "South":37}
	},
	
room37 = {
	"desc": "Room 37",
	"directions": {"North": 36, "West": 38}
	},
	
room38 = {
	"desc": "Room 38",
	"directions": {"West": 89, "East": 37}
	},
	
room39 = {
	"desc": "Room 39",
	"directions": {"North":40, "South":35}
	},
	
room40 = {
	"desc": "Room 40",
	"directions": {"North":41, "South":39}
	},
	
room41 = {
	"desc": "Room 41",
	"directions": {"North":42, "South":40}
	},
	
room42 = {
	"desc": "Room 42",
	"directions": {"South":41, "West":43}
	},
	
room43 = {
	"desc": "Room 43",
	"directions": {"West":44, "East":42}
	},
	
room44 = {
	"desc": "Room 44",
	"directions": {"South":45, "East":43}
	},
	
room45 = {
	"desc": "Room 45",
	"directions": {"North":44, "West":46}
	},
	
room46 = {
	"desc": "Room 46",
	"directions": {"South":47, "East":45}
	},
	
room47 = {
	"desc": "Room 47",
	"directions": {"North":46, "West":48}
	},
	
room48 = {
	"desc": "Room 48",
	"directions": {"West":49, "East":47}
	},
	
room49 = {
	"desc": "Room 49",
	"directions": {"North":50, "West":75, "East":48}
	},
	
room50 = {
	"desc": "Room 50",
	"directions": {"North":51, "South":49}
	},
	
room51 = {
	"desc": "Room 51",
	"directions": {"North":52, "South":50}
	},
	
room52 = {
	"desc": "Room 52",
	"directions": {"West":53, "East":57}
	},
	
room53 = {
	"desc": "Room 53",
	"directions": {"West":54, "East":52}
	},
	
room54 = {
	"desc": "Room 54",
	"directions": {"South":55, "East":53}
	},
	
room55 = {
	"desc": "Room 55",
	"directions": {"North":54, "West":56}
	},
	
room56 = {
	"desc": "Room 56",
	"directions": {"East":55}
	},
	
room57 = {
	"desc": "Room 57",
	"directions": {"North":59, "West":52, "East":58}
	},
	
room58 = {
	"desc": "Room 58",
	"directions": {"West":57}
	},
	
room59 = {
	"desc": "Room 59",
	"directions": {"North":60, "South":57}
	},
	
room60 = {
	"desc": "Room 60",
	"directions": {"North":61, "South":59}
	},
	
room61 = {
	"desc": "Room 61",
	"directions": {"North":62, "South":60}
	},
	
room62 = {
	"desc": "Room 62",
	"directions": {"South":61, "West":63}
	},
	
room63 = {
	"desc": "Room 63",
	"directions": {"East":62}
	},
	
room64 = {
	"desc": "Room 64",
	"directions": {"West":60, "East":65}
	},
	
room65 = {
	"desc": "Room 65",
	"directions": {"West":64, "East":66}
	},
	
room66 = {
	"desc": "Room 66",
	"directions": {"West":65, "East":67}
	},
	
room67 = {
	"desc": "Room 67",
	"directions": {"North":68, "South":73, "West":66}
	},
	
room68 = {
	"desc": "Room 68",
	"directions": {"South":67, "East":69}
	},
	
room69 = {
	"desc": "Room 69",
	"directions": {"West":68, "East":70}
	},
	
room70 = {
	"desc": "Room 70",
	"directions": {"West":69, "East":71}
	},
	
room71 = {
	"desc": "Room 71",
	"directions": {"South":72, "West":70}
	},
	
room72 = {
	"desc": "Room 72",
	"directions": {"North":71, "East":7}
	},
	
room73 = {
	"desc": "Room 73",
	"directions": {"North":67, "East":74}
	},
	
room74 = {
	"desc": "Room 74",
	"directions": {"West":73}
	},
	
room75 = {
	"desc": "Room 75",
	"directions": {"West":76, "East":49}
	},
	
room76 = {
	"desc": "Room 76",
	"directions": {"West":77, "East":75}
	},
	
room77 = {
	"desc": "Room 77",
	"directions": {"South":78, "East":76}
	},
	
room78 = {
	"desc": "Room 78",
	"directions": {"North":77, "South":79}
	},
	
room79 = {
	"desc": "Room 79",
	"directions": {"North":78, "East":80}
	},
	
room80 = {
	"desc": "Room 80",
	"directions": {"South":94, "West":79, "East":81}
	},
	
room81 = {
	"desc": "Room 81",
	"directions": {"West":80, "East":82}
	},
	
room82 = {
	"desc": "Room 82",
	"directions": {"South":83, "West":81}
	},
	
room83 = {
	"desc": "Room 83",
	"directions": {"North":82, "East":84}
	},
	
room84 = {
	"desc": "Room 84",
	"directions": {"West":83, "East":85}
	},
	
room85 = {
	"desc": "Room 85",
	"directions": {"North":86, "West":84}
	},
	
room86 = {
	"desc": "Room 86",
	"directions": {"South":85, "East":87}
	},
	
room87 = {
	"desc": "Room 87",
	"directions": {"South":88, "West":86}
	},
	
room88 = {
	"desc": "Room 88",
	"directions": {"North":87, "South":89}
	},
	
room89 = {
	"desc": "Room 89",
	"directions": {"North":88, "South":90, "East":38}
	},
	
room90 = {
	"desc": "Room 90",
	"directions": {"North":89, "South":91}
	},
	
room91 = {
	"desc": "Room 91",
	"directions": {"North":90, "West":92}
	},
	
room92 = {
	"desc": "Room 92",
	"directions": {"West":93, "East":91}
	},
	
room93 = {
	"desc": "Room 93",
	"directions": {"South":100,"East":92}
	},
	
room94 = {
	"desc": "Room 94",
	"directions": {"North":80, "South":95}
	},
	
room95 = {
	"desc": "Room 95",
	"directions": {"North":94, "South":96}
	},
	
room96 = {
	"desc": "Room 96",
	"directions": {"North":95, "East":97}
	},
	
room97 = {
	"desc": "Room 97",
	"directions": {"South":98, "West":96}
	},
	
room98 = {
	"desc": "Room 98",
	"directions": {"North":97, "South":99}
	},
	
room99 = {
	"desc": "Room 99",
	"directions": {"North":98}
	},
	
room100 = {
	"desc": "Room 100",
	"directions": {"North":93, "South":101}
	},
	
room101 = {
	"desc": "Room 101",
	"directions": {"North":100, "South":102}
	},
	
room102 = {
	"desc": "Room 102",
	"directions": {"North":101, "West":113, "East":103}
	},
	
room103 = {
	"desc": "Room 103",
	"directions": {"West":102, "East":104}
	},
	
room104 = {
	"desc": "Room 104",
	"directions": {"North":105, "West":103}
	},
	
room105 = {
	"desc": "Room 105",
	"directions": {"South":104, "East":106}
	},
	
room106 = {
	"desc": "Room 106",
	"directions": {"West":105, "East":107}
	},
	
room107 = {
	"desc": "Room 107",
	"directions": {"North":108, "West":106}
	},
	
room108 = {
	"desc": "Room 108",
	"directions": {"South":107, "East":109}
	},
	
room109 = {
	"desc": "Room 109",
	"directions": {"West":108, "East":110}
	},
	
room110 = {
	"desc": "Room 110",
	"directions": {"West":109, "East":111}
	},
	
room111 = {
	"desc": "Room 111",
	"directions": {"South":112, "West":110}
	},
	
room112 = {
	"desc": "Room 112",
	"directions": {"South":111}
	},
	
room113 = {
	"desc": "Room 113",
	"directions": {"South":114, "East":102}
	},
	
room114 = {
	"desc": "Room 114",
	"directions": {"North":113, "South":"Out"}
	}
)


def main_run(currentRoom):
    print ("Welcome to the Dungeon Maze #1.  Can you find your way out??")
  #  while currentRoom != 'room114':
    print("You are in {}".format(roomlist[currentRoom]["desc"]))
    l = len(roomlist[currentRoom]["directions"])
    if l == 1:
        print("There is one exit to the {}".format(roomlist[currentRoom]["desc"]))
    elif l > 1:
        print ("There are {} exits from this room".format(l))
        for key in roomlist[currentRoom]["desc"]:
            print(key)
    d = ""
    while d not in roomlist[currentRoom]["desc"]:
        d = input ("Type the direction you want to go: ")
    if d in roomlist[currentRoom]["desc"]:
            currentRoom = roomlist[currentRoom]["desc"][d]

        


main_run(currentRoom)
