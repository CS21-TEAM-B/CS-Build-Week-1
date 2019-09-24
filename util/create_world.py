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

r_stunnel4= Room(title="SouthTunnel 4", description="""You've gone south. The tunnel continues in the same direction""")

r_stunnel5= Room(title="SouthTunnel 5", description="""You have reached deeper in the tunnel. You think you hear something ahead. You can continue south to investigate, or go back""")

r_stunnel6= Room(title="SouthTunnel 6", description="""It was just the rocks settling in the cave. Another dead end. You better go back""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_etunnel.save()
r_etunnel2.save()

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



players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

