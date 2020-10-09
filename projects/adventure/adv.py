from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST----------------------------------------------------------------------------------------------------------------------------
visited_rooms = set()

myDict = {}
for i in range(0, 500):
    myDict[i] = set()
    myDict[i] = world.rooms[i].get_exits()

player.current_room.id = world.starting_room.id
# visited_rooms.add(player.current_room)
stack = []
last_intersect = {'room_id': 0, 'neighbors': []}
go_back = {'n': 's', 's': 'n', 'w':'e', 'e':'w'}
'''
step one
'''
def travel(direction):
    player.travel(direction)
#--------------------------------------------------------------------------------------------------------------------------------------------
# while rooms != 10:
#     next_room = myDict[player.current_room.id][0]
#     if player.current_room.
#     if player.current_room.id not in visited_rooms:
#         '''
#         If not in visted:
#         add to visited
#         add to room counter
#         remove first direction unless its the direction you came from (traversel[-1])
#         if next room is visted remove path 
#         if clear
#         move into that room and add direction to traversal

#         if visited: remove path, 
#         '''
#         print(player.current_room)
#         print(myDict[player.current_room.id])


#         if player.current_room.id not in visited_rooms :
#             #add to visted and increase counter
#             visited_rooms.add(player.current_room.id)
#             rooms += 1
#             #remove path unless origin
#             print(len(myDict[player.current_room.id]),'len')
#             if len(myDict[player.current_room.id]) > 0 and len(traversal_path)> 0:
#                 print(traversal_path[-1],'trvers')
#                 print(go_back[traversal_path[-1]], 'gobck')
#                 print(next_room, 'nxt')

#                 while player.current_room.get_room_in_direction(next_room).id in visited_rooms and next_room != go_back[traversal_path[-1]]:
#                     print(go_back[traversal_path[-1]], 'gobck')
#                     print(next_room)
#                     print(player.current_room.id)
#                     print(myDict[player.current_room.id])
#                     next_room = myDict[player.current_room.id].pop(0)
#                     print(player.current_room.get_room_in_direction(next_room).id in visited_rooms, '......')
#         print(next_room)
#     player.travel(next_room)
#     traversal_path.append(next_room)

#     # # print(player.current_room.s_to.name,'s',player.current_room.s_to.id)
#     # # print(player.current_room.n_to.name,'n')
#     # # print(player.current_room.e_to.name,'e')
#     # # print(player.current_room.w_to.name,'w')
#     # # print(player.current_room.id, '...')
#     # # player.travel('e')
#     # # rooms += 1
#     # print(player.current_room,'cuurent room')

#     # #keeps track of last known intersection
#     # if len(player.current_room.get_exits()) > 1:
#     #     last_intersect['room_id'] = player.current_room.id
#     #     go_back = []
        

#     # print(last_intersect,'2')

#     # # prints directions
#     # if player.current_room.get_exits()[0] == 'n':
#     #     print('Next room: ', player.current_room.n_to.id)
#     # if player.current_room.get_exits()[0] == 'e':
#     #     print('Next room: ', player.current_room.e_to.id)
#     # if player.current_room.get_exits()[0] == 's':
#     #     print('Next room: ', player.current_room.s_to.id)
#     # if player.current_room.get_exits()[0] == 'w':
#     #     print('Next room: ', player.current_room.w_to.id)

#     # #moves one room
#     # print(traversal_path,'4')

#     # visited_rooms.add(player.current_room.id)
#     # if myDict[player.current_room.id][0]:
#     #     traversal_path.append(player.current_room.get_exits()[0])
#     #     myDict[player.current_room.id].pop(0))



#     # print(myDict[player.current_room.id])
#     # player.travel(player.current_room.get_exits()[0])


#     # visited = set()
#     # stacks = Stack()
#     # stacks.push(starting_vertex)

#     # #dft
#     # while stack.size() > 0:
#     #     current = stacks.pop()
        
#     #     if current not in visited:
#     #         visited.add(current)
#     #         print(current)

#     #     for neighbors in self.vertices[current]:
#     #         if neighbors not in visited:
#     #             stacks.push(neighbors)
#     rooms += 1

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
