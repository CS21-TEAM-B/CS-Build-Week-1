from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()
#rooms outside cave
r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons. To the south you see a nice garden path")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. To the east you see an entrance and the smell of gold permeates the air""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. You may go south, west, or east.""")

#rooms inside cave foyer

r_etunnel= Room(title="East Tunnel", description="""You've entered the east cave tunnel. You notice another tunnel going
south. You also notice the tunnel continues east""")

r_stunnel= Room(title="South Tunnel", description="""You've entered south tunnel. Nothing to exciting here. You can
continue south or go back from where you came""")

r_stunnel2= Room(title="South Tunnel 2", description="""You've gone further in the south tunnel. You can still continue south""")

r_stunnel3= Room(title="South Tunnel 3", description="""You've gone as far as you can go. Looks like a dead end. Better go back.""")

r_etunnel2= Room(title="East Tunnel 2", description="""You've continues east. There is another tunnel going south again, or it continues east""")

r_stunnel4= Room(title="South Tunnel 4", description="""You've gone south. The tunnel continues in the same direction""")

r_stunnel5= Room(title="South Tunnel 5", description="""You have reached deeper in the tunnel. You think you hear something ahead. You can continue south to investigate, or go back""")

r_stunnel6= Room(title="South Tunnel 6", description="""It was just the rocks settling in the cave. Another dead end. You better go back""")

r_etunnel= Room(title="East Tunnel 3", description="""You have gone as far as you can go in the east tunnel. You notice
a tunnel goes north. You can go this way or go back """)

r_ntunnel= Room(title="North Tunnel", description="""You notice a passage to your west.""")

r_wpassage= Room(title="West Passage", description="""You notice a stairwell to the south, and a chamber entrance 
continuing west.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_etunnel.save()
r_etunnel2.save()
r_etunnel3.save()
r_stunnel.save()
r_stunnel2.save()
r_stunnel3.save()
r_stunnel4.save()
r_stunnel5.save()
r_stunnel6.save()
r_ntunnel.save()
r_wpassage.save()

#add these above
r_lowercavern.save()
r_cavernstairs.save()


# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_overlook, "w")
r_overlook.connectRooms(r_treasure, "e")

r_treasure.connectRooms(r_etunnel, "e")
r_etunnel.connectRooms(r_treasure, "w")

r_etunnel.connectRooms(r_stunnel, "s")
r_stunnel.connectRooms(r_etunnel, "n")

r_stunnel.connectRooms(r_stunnel2, "s")
r_stunnel2.connectRooms(r_stunnel, "n")

r_stunnel2.connectRooms(r_stunnel3, "s")
r_stunnel3.connectRooms(r_stunnel2, "n")

r_etunnel.connectRooms(r_etunnel2, "e")
r_etunnel2.connectRooms(r_etunnel, "w")

#
r_etunnel2.connectRooms(r_stunnel4, "s")
r_stunnel4.connectRooms(r_etunnel2, "n")

r_stunnel4.connectRooms(r_stunnel5, "s")
r_stunnel5.connectRooms(r_stunnel4, "n")

r_stunnel5.connectRooms(r_stunnel6, "s")
r_stunnel6.connectRooms(r_stunnel5, "n")

r_etunnel2.connectRooms(r_etunnel3, "e")
r_etunnel3.connectRooms(r_etunnel2, "w")

r_etunnel3.connectRooms(r_ntunnel, "n")
r_ntunnel.connectRooms(r_etunnel3, "s")

r_ntunnel.connectRooms(r_wpassage, "w")
r_wpassage.connectRooms(r_npassage, "e")

r_wpassage.connectRooms(r_cavernstairs, "s")
r_cavernstairs.connectRooms(r_wpassage, "n")

r_cavernstairs.connectRooms(r_lowercavern, "s")
r_lowercavern.connectRooms(r_cavernstairs, "n")

r_wpassage.connectRooms(r_cavernchamber, "w")
r_cavernchamber.connectRooms(r_wpassage, "e")

r_cavernchamber.connectRooms(r_nchamberhall, "n")
r_nchamberhall.connectRooms(r_cavernchamber, "s")

r_cavernchamber.connectRooms(r_wchamberhall, "w")
r_wchamberhall.connectRooms(r_cavernchamber, "e")

r_cavernchamber.connectRooms(r_schamberhall, "s")
r_schamberhall.connectRooms(r_cavernchamber, "n")

r_wchamberhall.connectRooms(r_secretchamber, "s")
r_secretchamber.connectRooms(r_wchamberhall, "n")

r_nchamberhall.connectRooms(r_chamberroom, "e")
r_chamberroom.connectRooms(r_nchamberhall, "w")

r_schamberhall.connectRooms(r_chamberroom2, "s")
r_chamberroom2.connectRooms(r_schamberhall, "n")



players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

