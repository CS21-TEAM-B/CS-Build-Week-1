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


# Link rooms together in cavern/cave
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

#linking rooms in the garden and garden path
r_outside.connectRooms(r_gardenpath, "s")
r_gardenpath.connectRooms(r_overlook, "n")

r_gardenpath.connectRooms(r_garden, "w")
r_garden.connectRooms(r_gardenpath, "e")

r_garden.connectRooms(r_pumpkinpatch, "n")
r_pumpkinpatch.connectRooms(r_garden, "s")

r_garden.connectRooms(r_tomatopatch, "s")
r_tomatopatch.connectRooms(r_garden, "n")

r_garden.connectRooms(r_cornfield, "w")
r_cornfield.connectRooms(r_garden, "e")

r_cornfield.connectRooms(r_cornpath, "n")
r_cornpath.connectRooms(r_cornfield, "s")

#linking rooms in the crop field (cornpath)
r_cornpath.connectRooms(r_cropcircle, "n")
r_cropcircle.connectRooms(r_cornpath, "s")

r_cropcircle.connectRooms(r_cropsquare, "e")
r_cropsquare.connectRooms(r_cropcircle, "w")

r_cropcircle.connectRooms(r_croptriangle, "w")
r_croptriangle.connectRooms(r_cropcircle, "e")

r_cropcircle.connectRooms(r_spaceship, "n")
##cant go back^^ must find escape pod


### Linking rooms in spaceship
r_spaceship.connectRooms(r_spacewestcorridor, "w")
r_spacewestcorridor.connectRooms(r_spaceship, "e")

r_spacewestcorridor.connectRooms(r_spaceprison, "n")
r_spaceprison.connectRooms(r_spacewestcorridor, "s")

r_spaceship.connectRooms(r_spacenorthcorridor, "n")
r_spacenorthcorridor.connectRooms(r_spaceship, "s")

r_spacenorthcorridor.connectRooms(r_cockpit, "n")
r_cockpit.connectRooms(r_spacenorthcorridor, "s")



r_spaceship.connectRooms(r_spaceeastcorridor, "e")
r_spaceeastcorridor.connectRooms(r_spaceship, "w")

r_spaceship.connectRooms(r_controlroom, "n")
r_controlroom.connectRooms(r_spaceeastcorridor, "s")

r_spaceeastcorridor.connectRooms(r_spacedining, "s")
r_spacedining.connectRooms(r_spaceeastcorridor, "n")


r_controlroom.connectRooms(r_spacelibrary, "n")
r_spacelibrary.connectRooms(r_controlroom, "s")


r_controlroom.connectRooms(r_escapepod, "e")
r_escapepod.connectRooms(r_controlroom, "w")


r_controlroom.connectRooms(r_captainchamber, "w")
r_captainchamber.connectRooms(r_controlroom, "e")

r_escapepod.connectRooms(r_outside, "s")

#linking rooms east of garden to church
r_gardenpath.connectRooms(r_church, "e")
r_church.connectRooms(r_gardenpath, "w")


r_church.connectRooms(r_sanctuary, "n")
r_sanctuary.connectRooms(r_church, "s")


r_church.connectRooms(r_churchkitchen, "e")
r_churchkitchen.connectRooms(r_church, "w")


r_church.connectRooms(r_churchgreetinghall, "s")
r_churchgreetinghall.connectRooms(r_church, "n")


##linking from the garden path to the main path
r_gardenpath.connectRooms(r_mainpath, "s")
r_mainpath.connectRooms(r_gardenpath, "n")


#linking main path south towards cottage
r_mainpath.connectRooms(r_cottage, "s")
r_cottage.connectRooms(r_mainpath, "n")


r_cottage.connectRooms(r_cottagekitchen, "e")
r_cottagekitchen.connectRooms(r_cottage, "w")

r_cottage.connectRooms(r_scottagecorridor, "s")
r_scottagecorridor.connectRooms(r_cottage, "n")

r_scottagecorridor.connectRooms(r_upstairscottage, "e")
r_upstairscottage.connectRooms(r_scottagecorridor, "w")

r_scottagecorridor.connectRooms(r_downstairscottage, "w")
r_downstairscottage.connectRooms(r_scottagecorridor, "e")

r_scottagecorridor.connectRooms(r_cottageroom, "s")
r_cottageroom.connectRooms(r_scottagecorridor, "n")

r_cottageroom.connectRooms(r_cottagecloset, "e")
r_cottagecloset.connectRooms(r_cottageroom, "w")


r_cottage.connectRooms(r_cottagedining, "w")
r_cottagedining.connectRooms(r_cottage, "e")

r_cottagedining.connectRooms(r_downcottagebath, "s")
r_downcottagebath.connectRooms(r_cottagedining, "n")

r_downstairscottage.connectRooms(r_cottageroom2, "w")
r_cottageroom2.connectRooms(r_downstairscottage, "e")

r_downstairscottage.connectRooms(r_bombshelter, "s")
r_bombshelter.connectRooms(r_downstairscottage, "n")

r_upstairscottage.connectRooms(r_upstairscottagehall, "n")
r_upstairscottagehall.connectRooms(r_upstairscottage, "s")

r_upstairscottagehall.connectRooms(r_upstairscottagebedroom, "w")
r_upstairscottagebedroom.connectRooms(r_upstairscottagehall, "e")

r_upstairscottagebedroom.connectRooms(r_cottagecloset2, "n")
r_cottagecloset2.connectRooms(r_upstairscottagebedroom, "s")

r_upstairscottagehall.connectRooms(r_upstairscottagebath, "e")
r_upstairscottagebath.connectRooms(r_upstairscottagehall, "w")


#linking main path east towards private road and mansion





players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

