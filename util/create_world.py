#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

# rooms outside cave

r_outside = Room(title='Outside Cave Entrance',
                 description=' You are outside.  North of you, the cave mount beckons. To the south you see a nice garden path'
                 )

r_foyer = Room(title='Foyer',
               description="""Dim light filters in from the south. Dusty
passages run north and east."""
               )

r_overlook = Room(title='Grand Overlook',
                  description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. To the east you see an entrance and the smell of gold permeates the air""")

r_narrow = Room(title='Narrow Passage',
                description="""The narrow passage bends here from west
to north. The smell of gold permeates the air."""
                )

r_treasure = Room(title='Treasure Chamber',
                  description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. You may go south, west, or east."""
                  )

# rooms inside cave foyer

r_etunnel = Room(title='East Tunnel',
                 description="""You've entered the east cave tunnel. You notice another tunnel going
south. You also notice the tunnel continues east"""
                 )

r_stunnel = Room(title='South Tunnel',
                 description="""You've entered south tunnel. Nothing to exciting here. You can
continue south or go back from where you came"""
                 )

r_stunnel2 = Room(title='South Tunnel 2',
                  description="""You've gone further in the south tunnel. You can still continue south"""
                  )

r_stunnel3 = Room(title='South Tunnel 3',
                  description="""You've gone as far as you can go. Looks like a dead end. Better go back."""
                  )

r_etunnel2 = Room(title='East Tunnel 2',
                  description="""You've continues east. There is another tunnel going south again, or it continues east"""
                  )

r_etunnel3 = Room(title='East Tunnel 3',
                  description="""You've gone as far as you can go. There is another tunnel going north, or it goes back west"""
                  )

r_stunnel4 = Room(title='South Tunnel 4',
                  description="""You've gone south. The tunnel continues in the same direction"""
                  )

r_stunnel5 = Room(title='South Tunnel 5',
                  description="""You have reached deeper in the tunnel. You think you hear something ahead. You can continue south to investigate, or go back"""
                  )

r_stunnel6 = Room(title='South Tunnel 6',
                  description="""It was just the rocks settling in the cave. Another dead end. You better go back"""
                  )

r_etunnel = Room(title='East Tunnel 3',
                 description="""You have gone as far as you can go in the east tunnel. You notice
a tunnel goes north. You can go this way or go back """
                 )

r_ntunnel = Room(title='North Tunnel',
                 description="""You notice a passage to your west.""")

r_wpassage = Room(title='West Passage',
                  description="""You notice a stairwell to the south, and a chamber entrance 
continuing west."""
                  )

r_cavernstairs = Room(title='Cavern Stairs',
                      description="""These stairs spiral downward. As you take them cobwebs start to thicken, until you enter a lower cavern. You can either enter 
the cavern by continuing south, or go back up the stairs"""
                      )

r_lowercavern = Room(title='Lower Cavern',
                     description="""You are in a lower cavern. You look around but it is pitch black.
You better get out of here! **slithering noise heard near feet"""
                     )

r_cavernchamber = Room(title='Cavern Chamber',
                       description="""You have entered the cavern chamber. To you notice a chamber hall to the north, west, and south."""
                       )

r_nchamberhall = Room(title='North Chamber Hall',
                      description="""Walking along the north chamber hall you notice a
door to the east. Shall you enter or go back?"""
                      )

r_chamberroom = Room(title='Chamber Room',
                     description="""You enter a chamber room. It is dark. It looks
lived in. Where did they go? Nothing to find here.  There are no other exits, you must go back."""
                     )

r_wchamberhall = Room(title='West Chamber Hall',
                      description="""You browse the west chamber hall and notice
a door to the south. You think you heard something inside."""
                      )

r_chamberroom2 = Room(title='Chamber Room Two',
                      description="""You enter and everything starts moving around.
It appears the room is haunted.  You better leave"""
                      )

r_schamberhall = Room(title='South Chamber Hall',
                      description="""You stroll down the south chamber hall
and notice an outline in the cave wall. It's a secret passage! Do you dare enter by continuing south?"""
                      )

r_secretchamber = Room(title='Secret Chamber',
                       description="""You've stumbled across a secret chamber! 
You also find a chest with gold inside. Is this the missing treasure from the treasure room?  Before
you have a chance to grab the treasure, another noise startles you.  This place must be haunted too! Or maybe
the treasure is protected by a curse! You better not risk it.""")

###garden path and garden

r_gardenpath = Room(title='Garden Path',
                    description="""Walking along the garden path you notice a garden to the west and a church
to the east.  You can also go north back to the cave.  While looking south you see the garden path merges with
the main path""")

r_garden = Room(title='Garden',
                description="""You have entered the garden, but where is the gardener? To the north you see a pumpkin patch,
to the south you see a tomato patch, and you hear something coming from the cornfield to the west"""
                )

r_pumpkinpatch = Room(title='Pumpkin Patch',
                      description="""You stroll the pumpkin patch. You notice a 8 foot
pumpking with a ribbon on it. It must have won at the county fair. There are no other paths."""
                      )

r_tomatopatch = Room(title='Tomato Patch',
                     description="""You walk along the tomato patch and pick a few
to eat. They are delicious!  Nothing else to see here, no other paths"""
                     )

r_cornfield = Room(title='Cornfield',
                   description="""You enter the cornfield. The stalks surround you and make you
feel small. That noise you heard gets louder and sounds like it's coming from the north. Do you investigate or go back?"""
                   )

r_cornpath = Room(title='Corn Path',
                  description="""It appears as if some corn stalks have fallen over and
have made a makeshift path. Do you want to continue north? The sound is getting louder"""
                  )

r_cropcircle = Room(title='Crop Circle',
                    description="""You suddenly are no longer surrounded by corn stalks. 
You are not standing in a massive crop circle. What could have caused this? That noise you heard seems to be coming from
the north.  You also see a bright light coming from that direction. Do you dare move forward? You also notice other crop 
signs to your east and west. If you are scared, you may flee south from where you came.""")

r_cropsquare = Room(title='Crop Square',
                    description="""You have entered a crop square. Perfectly square and symetrical. What is
causing this? There are no other ways out."""
                    )

r_croptriangle = Room(title='Crop Triange',
                      description="""A perfect triangle formed out of corn.  Is this aliens? The
illuminati? There are no other exits."""
                      )

r_spaceship = Room(title='Spaceship',
                   description="""As you move towards the light, you all of a sudden feel yourself being levitated up
towards the sky! It was a UFO. You're being beamed up! Oh no!  The ship is oddly quiet. Where is everyone? 
Now that you are in the ship, you must find a way out!
You notice corridors to your north, west, and east.""")

r_spacewestcorridor = Room(title='West Corridor',
                           description="""Entering the west corridor you notice a door to the north"""
                           )

r_spacenorthcorridor = Room(title='North Corridor',
                           description="""Entering the north corridor you notice a door to the north"""
                           )

r_cockpit = Room(title='Cockpit',
                           description="""You are in the cockpit. Where are all the aliens?"""
                           )

r_spaceprison = Room(title='Prison Entrance',
                     description="""You see what appears to be a holding cell for humans, but you can't see inside.
You hear people yelling for help.  You can't open the door, and you don't want to be one of them. You must find a way out!"""
                     )

r_spaceeastcorridor = Room(title='East Corridor',
                           description="""You walk along the east corridor and see a hall going north, and another room south"""
                           )

r_spacedining = Room(title='Dining Room',
                     description="""It appears to be the dining room for aliens.  You
see a menu on the wall with pictures of humans.... oh no, they eat us! You must leave!"""
                     )

r_controlroom = Room(title='Control Room',
                     description="""You're now in the control room! What a sight!  But no time
to gaze, you need to find a way out.  You notice a door to you north, west, and east."""
                     )

r_captainchamber = Room(title="Capatain's Chamber",
                        description="""You seemed to have entered the captain's chamber,
but he is nowhere to be found.  No other exits"""
                        )

r_spacelibrary = Room(title='Library',
                      description="""You've entered what appears to be a library. You browse
the books and it seems they've been studying us for a long time.  You think you hear a noise, better leave!"""
                      )

r_escapepod = Room(title='Escape Pod',
                   description="""You enter a tiny box.  You can't read the language on the wall,
but the diagrams show that what you're in seems to be an escape pod! You can launch the pod by going south."""
                   )

r_church = Room(title='Church',
                description="""You arrive at the church, but it appears to be empty... Strange, given
that it's a Sunday. Maybe check the sanctuary to the north? There is also a kitchen to the east, and the church greeting hall to the
south""")

r_sanctuary = Room(title='Sanctuary',
                   description="""The Sanctuary is empty as well.  Where is the Pastor, all the congregants?
Better go back."""
                   )

r_churchkitchen = Room(title='Church Kitchen',
                       description="""Clean as a whistle. The church staff really takes
'cleanliness is next to Godliness' seriously.  Not a speck of dust to be seen.... nor a single person.  Better go back and check somewhere else"""
                       )

r_churchgreetinghall = Room(title='Church Greeting Hall',
                       description="""A nice spacious greeting hall. No other exits."""
                       )                      

r_mainpath = Room(title='Main Path',
                  description="""The garden path has ended and you are now on the main path! To the eat you see 
a private road that leads the mansion of Mark Lexington III.  Perhaps he invited all the townspeople over for a gathering?
But then again, why didn't you get an invite?  The south leads to the Old Man Jenkin's Cottage.  """)

r_cottage = Room(title='Cottage',
                 description="""You arrive at Old Man Jenkin's cottage. It's silent as well. The door is unlocked..
(strange, as Jenkins has always been the paranoid type), you enter.  To the east is the kitchen, and to the west is the dining room.
To the south you see a narrow hall.""")

r_cottagekitchen = Room(title='Cottage Kitchen',
                        description="""Nothing too exciting here.  You see tin foil plastered all over
the kitchen, with sketches of UFOs... Jenkins really is paranoid. You always knew he was, but thought it was more about government
conspiracy than aliens.  Nothing else to see in here.""")

r_scottagecorridor = Room(title='Cottage Corridor',
                          description="""The narrow hall seems to lead to another part of the cottage.
The east leads upstairs, and west leads downstairs, and in front of you to the south is a door."""
                          )

r_cottageroom = Room(title='Cottage Room',
                     description="""A nice homey cottage room.  Seems strange
compared to the rest of the cottage. To the east is a door. The closet perhaps?"""
                     )

r_cottagecloset = Room(title='Cottage Closet',
                       description="""Yep. Just a small closet. Nothing in here."""
                       )

r_downstairscottage = Room(title='Basement',
                           description="""Downstairs is small, but there does appear to be
other rooms, to the west and south there are doors."""
                           )

r_cottageroom2 = Room(title='Spare Room',
                      description="""Appears to be guest room. There is a bed in the corner. No windows though. No other
exits"""
                      )

r_bombshelter = Room(title='Bomb Shelter',
                     description="""You enter what appears to be the first portion of a
bomb shelter.  Jenkins isn't messing around, he really is paranoid.  The actual bomb shelter is in front of you, but it is locked.
You peek through the small eye hole on the door and see steps going down. Maybe Jenkins went down there? Better not
investigate... even if you did get in, he'd probably shoot you for trespassing... Come to think of it, you better leave.""")

r_cottagedining = Room(title='Cottage Dining',
                       description="""Nice cozy dining room. To the south you see a door."""
                       )

r_downcottagebath = Room(title='Bathroom',
                     description="""Small bathroom.  It does have a nice clawfoot bathtub... don't see those around
too often anymore."""
                     )

r_upstairscottage = Room(title='Upstairs Cottage',
                         description="""You have arrived upstairs. The upstairs continues north."""
                         )

r_upstairscottagehall = Room(title='Upstairs Hall',
                             description="""In the hallway you see a door to the east and west."""
                             )

r_upstairscottagebedroom = Room(title='Cottage Master Room',
                                description="""Nice cottage room. Must be the mater room. There is a buck and an elk
hanging on the well, with a nice fireplace in the corner. A door is to the north."""
                                )

r_cottagecloset2 = Room(title='Master Closet',
                        description="""Closet is completely empty.  You also see a gun
case that has been emptied.  It seems Jenkins took all his belongings and guns and fled. Where did he go?"""
                        )

r_upstairscottagebath = Room(title='Upstairs Bath',
                             description="""Nice bathroom for a cottage.  You see a clawfoot bathtub
and a shower in the corner.  You also see a homemade eyewash station.  """
                             )

r_mansionentrance = Room(title='Mansion Entrance',
                         description="""The private road has led you to the Lexington's mansion. You are standing
at the entrance.  You thought maybe all the townspeople were invited here, but it is still quiet... shall you enter?  You may enter by going
east.""")

r_mansionhall = Room(title='Mansion Hall',
                     description="""You are standing in the main mansion hall.  What a sight!
There is a beautiful chandelier made of gold, diamond and crystal hanging above your head. To the east is a large
staircase heading upstairs made of pure oak.  To the south is the dining hall, and to the north is the entertainment hall.""")

r_livingroom = Room(title='Entertainment Hall',
                    description="""Seems to be the living room (or the 'entertainment hall') as Lexington
likes to call it.  To the west is a door, and the east leads towards the billiard room."""
                    )

r_mansionbath = Room(title='Mansion Bath',
                     description="""What a beautiful bathroom. You've never seen anything
like it. It's just a bathroom though, why all the grandour? You see a toilet made of pure gold, a shower lined in gold,
as well as the sink.  The tiles on the floor are heated. What a sight!""")

r_billiardroom = Room(title='Billiard Room',
                      description="""Nice cozy billiard room.  The walls are a dark oak wtih a fireplace in the corner.
Shall you rack up and play a few rounds?  You notice a door to the north that leads to another part of the mansion."""
                      )

r_northeasthall = Room(title='Northeast Hall',
                       description="""You've entered the northeast part of the house. What's over here anyway?
You see doors on both sides of the hall heading north.  Shall you continue north down the hall towards the other rooms
or inspect the rooms beside you?  The doors are to your east and west.""")

r_barpub = Room(title='Bar/Pub',
                description="""Lexington has his own bar. Of course he does.  You browse and find your
favorite liquor.  Shall you make yourself a drink?  You don't mind if you do.  You mix yourself a Tom Collins... better get to inspecting 
the rest of the mansion.""")

r_arcaderoom = Room(title='Arcade Room',
                    description="""Lexington has an arcade room? He never struck you
as the type to play video games.  Maybe they are for his guests... but then again the town doesn't have many children. 
Maybe they are for his nephews?  Does Lexington have nephews?""")

r_northeasthall2 = Room(title='Northeast Hall Two',
                        description="""The second second section of the hall... do you continue or inspect the rooms
to west and east?"""
                        )

r_trampolineroom = Room(title='Trampoline Room',
                        description="""Wow! You've always heard about these but never
thought they actually existed!  A room made entirely out of trampoline.  You take off your shoes and bounce
around for a while.... whew! You are exhausted... you forgot what you were doing for a moment... better get back
to investigating.""")

r_indoorpool = Room(title='Indoor Pool',
                    description="""Of coure he has a pool, why wouldn't he!  You see a beautiful
waterfall that pours into the pool, as well as a HUGE waterslide!  Ah man, if only you brought your swimming clothes!"""
                    )

r_northeasthall3 = Room(title='Northeast Hall Three',
                        description="""You've reached the end of the hall. You can go back or inspect the rooms
to the east or west."""
                        )

r_mansionlibrary = Room(title='Mansion Library',
                        description="""The biggest library you've ever seen! How does anyone collect this
many books! What's the point? Books are meant to be read and it's impossible to read all of these!  It reminds you of that library scene
out of Beauty and the Beast.... so many books!""")

r_securityroom = Room(title='Security Room',
                      description="""Surprisingly the security room is unlocked. You see multiple
minitors surrounding the perimeter of the mansion.  The live footage seems to be all you have access to.  Evetything else seems to be 
encrypted or password protected.""")

r_mansiondining = Room(title='Dining Hall',
                       description="""A beautiful dining hall with a long table for entertaining lots
of guests. To the east is the kitchen, and another part of the house is to the south.  It appears to be a stairway going downstairs."""
                       )

r_mansionkitchen = Room(title='Mansion Kitchen',
                        description="""Huge commercial size kitchen!  You've never been much of a cook so this
doesn't excite you."""
                        )

r_mansionkitchen = Room(title='Mansion Kitchen',
                        description="""Huge commercial size kitchen!  You've never been much of a cook so this
doesn't excite you."""
                        )

r_downstairsmansion = Room(title='Downstairs Mansion',
                           description="""Downstairs you see a door to your the east and west, as well as the 
hall continuing south."""
                           )

r_downstairsmansionbed = Room(title='Guest Room',
                              description="""A guest bedroom. It has a bed and it's own fireplace. Nice."""
                              )

r_downstairsmansionbed2 = Room(title='Guest Room Two',
                               description="""A guest bedroom. It has a mini fridge with sodas and shots."""
                               )

r_downstairshall = Room(title='Downstairs Hall',
                        description="""To the east you see a broad entrance with the words 'Bowling Alley' in neon lights
hanging above it! To the west you see the same thing, only the lights say 'Movie Theater"""
                        )

r_bowlingalley = Room(title='Bowling Alley',
                      description="""A nice 5 line bowling alley!  You grab a ball and roll the ball down the alley....Strike!"""
                      )

r_movietheater = Room(title='Movie Theater',
                      description="""As you enter the theater you take a seat in one of the many reclined seats.  'How do I start a movie?', you ask yourself....Suddenly the screen turns
on and a voice comes through the speakers.... 'Good evening sir, did I hear you wanted to start a movie?'.  Voice activated movie theater! Wow!
You don't have time to sit and watch a flick, you say 'No thank you'... the screen shuts off. You better get moving.""")

r_mansionupstairs = Room(title='Upstairs',
                         description="""You've arrived upstairs.  Shall you continue north
to see more of the mansion, or go back downstairs?"""
                         )

r_upstairshall = Room(title='Upstairs Hall',
                      description="""The hall continues north with rooms on both sides. Shall you inspect the rooms
to the east or west?"""
                      )

r_upstairshall2 = Room(title='Upstairs Hall 2',
                      description="""The hall continues north with rooms on both sides. Shall you inspect the rooms
to the east or west?"""
                      )  

r_upstairshall3 = Room(title='Upstairs Hall 3',
                      description="""The hall continues north with rooms on both sides. Shall you inspect the rooms
to the east or west?"""
                      )                                           

r_upstairsguestbed = Room(title='Upstairs Guest Bed',
                          description="""Beautiful guest room... but you're starting to get sick of guest rooms. You've seen one
you've seen them all."""
                          )

r_upstairsguestbed2 = Room(title='Upstairs Guest Bed Two',
                           description="""Another guest room... there is a door to the north and south"""
                           )

r_upstairsguestbed3 = Room(title='Upstairs Guest Bed Three',
                           description="""Another guest room..."""
                           )

r_upstairsguestbath2 = Room(title='Upstairs Guest Bath Two',
                            description="""Beautiful guest bath, layed with gold. Lexington goes all out, even for guests."""
                            )

r_upstairsguestcloset2 = Room(title='Upstairs Guest Closet Two',
                              description="""Nice, spacious walk in closet. Empty though."""
                              )

r_upstairsguestbed = Room(title='Upstairs Guest Bed',
                          description="""Beautiful guest room... but you're starting to get sick of guest rooms. You've seen one
you've seen them all."""
                          )


r_storagecloset = Room(title='Storage Closet',
                       description="""Storage closet. Seems to be packed with canned food, survival items, blankets, towels,
pretty much everything."""
                       )

r_sauna = Room(title='Sauna',
               description="""Ooo... a sauna! Better not though.""")

r_upstairshall3 = Room(title='Upstairs Hall Three',
                       description="""Continue north or inspect rooms?"""
                       )

r_upstairsguestbed4 = Room(title='Upstairs Guest Room Four',
                           description="""Nice and cozy guest room. There are doors to the north and south. 
Probably a closet and a bath."""
                           )

r_upstairsguestbath = Room(title='Upstairs Guest Bath Four',
                           description="""Beautiful guest bath layed in gold"""
                           )

r_upstairsguestcloset = Room(title='Upstairs Guest Closet Four',
                             description="""Big walk in closet. Nice."""
                             )

r_upstairshall4 = Room(title='Upstairs Hall Four',
                       description="""You have reached the end of the hall. There are no doors to the east or west.
There is, however, a door in front of you facing north."""
                       )

r_mastersuite = Room(title='Master Suite',
                     description="""The master suite! This entire room is bigger than your own house!
There is a mini bar in the corner, a fireplace on the opposite side, and a double king sized bed. The master bath is to the west, with a 
walk in closet to the east.""")

r_masterbath = Room(title='Master Bath',
                    description="""Biggest bathroom in the mansion.  Words cannot describe what you see. Gold and diamonds everywhere."""
                    )

r_mastercloset = Room(title='Master Closet',
                      description="""Who needs a closet this big? This room is big enough to live in."""
                      )

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
r_lowercavern.save()
r_cavernstairs.save()
r_cavernchamber.save()
r_nchamberhall.save()
r_wchamberhall.save()
r_schamberhall.save()
r_secretchamber.save()
r_chamberroom.save()
r_chamberroom2.save()
r_gardenpath.save()
r_garden.save()
r_pumpkinpatch.save()
r_tomatopatch.save()
r_cornfield.save()
r_cornpath.save()
r_cropcircle.save()
r_cropsquare.save()
r_croptriangle.save()
r_spaceship.save()
r_spacewestcorridor.save()
r_spaceprison.save()
r_spacenorthcorridor.save()
r_cockpit.save()
r_spaceeastcorridor.save()
r_spacedining.save()
r_spacelibrary.save()
r_controlroom.save()
r_captainchamber.save()
r_escapepod.save()
r_church.save()
r_sanctuary.save()
r_churchkitchen.save()
r_churchgreetinghall.save()
r_mainpath.save()
r_cottage.save()
r_cottagekitchen.save()
r_scottagecorridor.save()
r_upstairscottage.save()
r_downstairscottage.save()
r_cottageroom.save()
r_cottagecloset.save()
r_cottagedining.save()
r_downcottagebath.save()
r_cottageroom2.save()
r_bombshelter.save()
r_upstairscottage.save()
r_cottagecloset2.save()
r_upstairscottagehall.save()
r_upstairscottagebath.save()
r_upstairscottagebedroom.save()
r_mansionentrance.save()
r_mansionhall.save()
r_livingroom.save()
r_mansiondining.save()
r_mansionkitchen.save()
r_downstairsmansion.save()
r_downstairsmansionbed.save()
r_downstairsmansionbed2.save()
r_downstairshall.save()
r_bowlingalley.save()
r_movietheater.save()
r_mansionbath.save()
r_billiardroom.save()
r_northeasthall.save()
r_barpub.save()
r_arcaderoom.save()
r_northeasthall2.save()
r_trampolineroom.save()
r_northeasthall3.save()
r_indoorpool.save()
r_mansionlibrary.save()
r_securityroom.save()
r_mansionupstairs.save()
r_upstairshall.save()
r_upstairshall2.save()
r_upstairshall3.save()
r_upstairsguestbed.save()
r_upstairsguestbed2.save()
r_upstairsguestbath2.save()
r_upstairsguestcloset2.save()
r_sauna.save()
r_storagecloset.save()
r_upstairsguestbed3.save()
r_upstairsguestbed4.save()
r_upstairsguestbath.save()
r_upstairsguestcloset.save()
r_mastersuite.save()
r_masterbath.save()
r_mastercloset.save()

# Link rooms together in cavern/cave

r_outside.connectRooms(r_foyer, 'n')
r_foyer.connectRooms(r_outside, 's')

r_foyer.connectRooms(r_overlook, 'n')
r_overlook.connectRooms(r_foyer, 's')

r_foyer.connectRooms(r_narrow, 'e')
r_narrow.connectRooms(r_foyer, 'w')

r_narrow.connectRooms(r_treasure, 'n')
r_treasure.connectRooms(r_narrow, 's')

r_treasure.connectRooms(r_overlook, 'w')
r_overlook.connectRooms(r_treasure, 'e')

r_treasure.connectRooms(r_etunnel, 'e')
r_etunnel.connectRooms(r_treasure, 'w')

r_etunnel.connectRooms(r_stunnel, 's')
r_stunnel.connectRooms(r_etunnel, 'n')

r_stunnel.connectRooms(r_stunnel2, 's')
r_stunnel2.connectRooms(r_stunnel, 'n')

r_stunnel2.connectRooms(r_stunnel3, 's')
r_stunnel3.connectRooms(r_stunnel2, 'n')

r_etunnel.connectRooms(r_etunnel2, 'e')
r_etunnel2.connectRooms(r_etunnel, 'w')

r_etunnel2.connectRooms(r_stunnel4, 's')
r_stunnel4.connectRooms(r_etunnel2, 'n')

r_stunnel4.connectRooms(r_stunnel5, 's')
r_stunnel5.connectRooms(r_stunnel4, 'n')

r_stunnel5.connectRooms(r_stunnel6, 's')
r_stunnel6.connectRooms(r_stunnel5, 'n')

r_etunnel2.connectRooms(r_etunnel3, 'e')
r_etunnel3.connectRooms(r_etunnel2, 'w')

r_etunnel3.connectRooms(r_ntunnel, 'n')
r_ntunnel.connectRooms(r_etunnel3, 's')

r_ntunnel.connectRooms(r_wpassage, 'w')
r_wpassage.connectRooms(r_ntunnel, 'e')

r_wpassage.connectRooms(r_cavernstairs, 's')
r_cavernstairs.connectRooms(r_wpassage, 'n')

r_cavernstairs.connectRooms(r_lowercavern, 's')
r_lowercavern.connectRooms(r_cavernstairs, 'n')

r_wpassage.connectRooms(r_cavernchamber, 'w')
r_cavernchamber.connectRooms(r_wpassage, 'e')

r_cavernchamber.connectRooms(r_nchamberhall, 'n')
r_nchamberhall.connectRooms(r_cavernchamber, 's')

r_cavernchamber.connectRooms(r_wchamberhall, 'w')
r_wchamberhall.connectRooms(r_cavernchamber, 'e')

r_cavernchamber.connectRooms(r_schamberhall, 's')
r_schamberhall.connectRooms(r_cavernchamber, 'n')

r_wchamberhall.connectRooms(r_secretchamber, 's')
r_secretchamber.connectRooms(r_wchamberhall, 'n')

r_nchamberhall.connectRooms(r_chamberroom, 'e')
r_chamberroom.connectRooms(r_nchamberhall, 'w')

r_schamberhall.connectRooms(r_chamberroom2, 's')
r_chamberroom2.connectRooms(r_schamberhall, 'n')

# linking rooms in the garden and garden path

r_outside.connectRooms(r_gardenpath, 's')
r_gardenpath.connectRooms(r_outside, 'n')

r_gardenpath.connectRooms(r_garden, 'w')
r_garden.connectRooms(r_gardenpath, 'e')

r_garden.connectRooms(r_pumpkinpatch, 'n')
r_pumpkinpatch.connectRooms(r_garden, 's')

r_garden.connectRooms(r_tomatopatch, 's')
r_tomatopatch.connectRooms(r_garden, 'n')

r_garden.connectRooms(r_cornfield, 'w')
r_cornfield.connectRooms(r_garden, 'e')

r_cornfield.connectRooms(r_cornpath, 'n')
r_cornpath.connectRooms(r_cornfield, 's')

# linking rooms in the crop field (cornpath)

r_cornpath.connectRooms(r_cropcircle, 'n')
r_cropcircle.connectRooms(r_cornpath, 's')

r_cropcircle.connectRooms(r_cropsquare, 'e')
r_cropsquare.connectRooms(r_cropcircle, 'w')

r_cropcircle.connectRooms(r_croptriangle, 'w')
r_croptriangle.connectRooms(r_cropcircle, 'e')

r_cropcircle.connectRooms(r_spaceship, 'n')

##cant go back^^ must find escape pod

### Linking rooms in spaceship

r_spaceship.connectRooms(r_spacewestcorridor, 'w')
r_spacewestcorridor.connectRooms(r_spaceship, 'e')

r_spacewestcorridor.connectRooms(r_spaceprison, 'n')
r_spaceprison.connectRooms(r_spacewestcorridor, 's')

r_spaceship.connectRooms(r_spacenorthcorridor, 'n')
r_spacenorthcorridor.connectRooms(r_spaceship, 's')

r_spacenorthcorridor.connectRooms(r_cockpit, 'n')
r_cockpit.connectRooms(r_spacenorthcorridor, 's')

r_spaceship.connectRooms(r_spaceeastcorridor, 'e')
r_spaceeastcorridor.connectRooms(r_spaceship, 'w')

r_spaceship.connectRooms(r_controlroom, 'n')
r_controlroom.connectRooms(r_spaceeastcorridor, 's')

r_spaceeastcorridor.connectRooms(r_spacedining, 's')
r_spacedining.connectRooms(r_spaceeastcorridor, 'n')

r_controlroom.connectRooms(r_spacelibrary, 'n')
r_spacelibrary.connectRooms(r_controlroom, 's')

r_controlroom.connectRooms(r_escapepod, 'e')
r_escapepod.connectRooms(r_controlroom, 'w')

r_controlroom.connectRooms(r_captainchamber, 'w')
r_captainchamber.connectRooms(r_controlroom, 'e')

r_escapepod.connectRooms(r_outside, 's')

# linking rooms east of garden to church

r_gardenpath.connectRooms(r_church, 'e')
r_church.connectRooms(r_gardenpath, 'w')

r_church.connectRooms(r_sanctuary, 'n')
r_sanctuary.connectRooms(r_church, 's')

r_church.connectRooms(r_churchkitchen, 'e')
r_churchkitchen.connectRooms(r_church, 'w')

r_church.connectRooms(r_churchgreetinghall, 's')
r_churchgreetinghall.connectRooms(r_church, 'n')

##linking from the garden path to the main path

r_gardenpath.connectRooms(r_mainpath, 's')
r_mainpath.connectRooms(r_gardenpath, 'n')

# linking main path south towards cottage

r_mainpath.connectRooms(r_cottage, 's')
r_cottage.connectRooms(r_mainpath, 'n')

r_cottage.connectRooms(r_cottagekitchen, 'e')
r_cottagekitchen.connectRooms(r_cottage, 'w')

r_cottage.connectRooms(r_scottagecorridor, 's')
r_scottagecorridor.connectRooms(r_cottage, 'n')

r_scottagecorridor.connectRooms(r_upstairscottage, 'e')
r_upstairscottage.connectRooms(r_scottagecorridor, 'w')

r_scottagecorridor.connectRooms(r_downstairscottage, 'w')
r_downstairscottage.connectRooms(r_scottagecorridor, 'e')

r_scottagecorridor.connectRooms(r_cottageroom, 's')
r_cottageroom.connectRooms(r_scottagecorridor, 'n')

r_cottageroom.connectRooms(r_cottagecloset, 'e')
r_cottagecloset.connectRooms(r_cottageroom, 'w')

r_cottage.connectRooms(r_cottagedining, 'w')
r_cottagedining.connectRooms(r_cottage, 'e')

r_cottagedining.connectRooms(r_downcottagebath, 's')
r_downcottagebath.connectRooms(r_cottagedining, 'n')

r_downstairscottage.connectRooms(r_cottageroom2, 'w')
r_cottageroom2.connectRooms(r_downstairscottage, 'e')

r_downstairscottage.connectRooms(r_bombshelter, 's')
r_bombshelter.connectRooms(r_downstairscottage, 'n')

r_upstairscottage.connectRooms(r_upstairscottagehall, 'n')
r_upstairscottagehall.connectRooms(r_upstairscottage, 's')

r_upstairscottagehall.connectRooms(r_upstairscottagebedroom, 'w')
r_upstairscottagebedroom.connectRooms(r_upstairscottagehall, 'e')

r_upstairscottagebedroom.connectRooms(r_cottagecloset2, 'n')
r_cottagecloset2.connectRooms(r_upstairscottagebedroom, 's')

r_upstairscottagehall.connectRooms(r_upstairscottagebath, 'e')
r_upstairscottagebath.connectRooms(r_upstairscottagehall, 'w')

# linking main path east towards private road and mansion
# mansion main floor

r_mainpath.connectRooms(r_mansionentrance, 'e')
r_mansionentrance.connectRooms(r_mainpath, 'w')

r_mansionentrance.connectRooms(r_mansionhall, 'e')
r_mansionhall.connectRooms(r_mansionentrance, 'w')

r_mansionhall.connectRooms(r_livingroom, 'n')
r_livingroom.connectRooms(r_mansionhall, 's')

r_mansionhall.connectRooms(r_mansiondining, 's')
r_mansiondining.connectRooms(r_mansionhall, 'n')

r_mansiondining.connectRooms(r_mansionkitchen, 'e')
r_mansionkitchen.connectRooms(r_mansiondining, 'w')

# downstairs mansion

r_mansiondining.connectRooms(r_downstairsmansion, 's')
r_downstairsmansion.connectRooms(r_mansiondining, 'n')

r_downstairsmansion.connectRooms(r_downstairsmansionbed, 'w')
r_downstairsmansionbed.connectRooms(r_downstairsmansion, 'e')

r_downstairsmansion.connectRooms(r_downstairsmansionbed2, 'e')
r_downstairsmansionbed2.connectRooms(r_downstairsmansion, 'w')

r_downstairsmansion.connectRooms(r_downstairshall, 's')
r_downstairshall.connectRooms(r_downstairsmansion, 'n')

r_downstairshall.connectRooms(r_bowlingalley, 'e')
r_bowlingalley.connectRooms(r_downstairshall, 'w')

r_downstairshall.connectRooms(r_movietheater, 'w')
r_movietheater.connectRooms(r_downstairshall, 'e')

##mansion main floor

r_livingroom.connectRooms(r_mansionbath, 'w')
r_mansionbath.connectRooms(r_livingroom, 'e')

r_livingroom.connectRooms(r_billiardroom, 'e')
r_billiardroom.connectRooms(r_livingroom, 'w')

r_billiardroom.connectRooms(r_northeasthall, 'n')
r_northeasthall.connectRooms(r_billiardroom, 's')

r_northeasthall.connectRooms(r_barpub, 'w')
r_barpub.connectRooms(r_northeasthall, 'e')

r_northeasthall.connectRooms(r_arcaderoom, 'e')
r_arcaderoom.connectRooms(r_northeasthall, 'w')

r_northeasthall.connectRooms(r_northeasthall2, 'n')
r_northeasthall2.connectRooms(r_northeasthall, 's')

r_northeasthall2.connectRooms(r_trampolineroom, 'w')
r_trampolineroom.connectRooms(r_northeasthall2, 'e')

r_northeasthall2.connectRooms(r_indoorpool, 'e')
r_indoorpool.connectRooms(r_northeasthall2, 'w')

r_northeasthall2.connectRooms(r_northeasthall3, 'n')
r_northeasthall3.connectRooms(r_northeasthall2, 's')

r_northeasthall3.connectRooms(r_mansionlibrary, 'w')
r_mansionlibrary.connectRooms(r_northeasthall3, 'e')

r_northeasthall3.connectRooms(r_securityroom, 'e')
r_securityroom.connectRooms(r_northeasthall3, 'w')

##mansion upstairs

r_mansionhall.connectRooms(r_mansionupstairs, 'e')
r_mansionupstairs.connectRooms(r_mansionhall, 'w')

r_mansionupstairs.connectRooms(r_upstairshall, 'n')
r_upstairshall.connectRooms(r_mansionupstairs, 's')

r_upstairshall.connectRooms(r_upstairsguestbed, 'w')
r_upstairsguestbed.connectRooms(r_upstairshall, 'e')

r_upstairshall.connectRooms(r_upstairsguestbed2, 'e')
r_upstairsguestbed2.connectRooms(r_upstairshall, 'w')

r_upstairsguestbed2.connectRooms(r_upstairsguestbath2, 'n')
r_upstairsguestbath2.connectRooms(r_upstairsguestbed2, 's')

r_upstairsguestbed2.connectRooms(r_upstairsguestcloset2, 's')
r_upstairsguestcloset2.connectRooms(r_upstairsguestbed2, 'n')

r_upstairshall.connectRooms(r_upstairshall2, 'n')
r_upstairshall2.connectRooms(r_upstairshall, 's')

r_upstairshall2.connectRooms(r_sauna, 'w')
r_sauna.connectRooms(r_upstairshall2, 'e')

r_upstairshall2.connectRooms(r_storagecloset, 'e')
r_storagecloset.connectRooms(r_upstairshall2, 'w')

r_upstairshall2.connectRooms(r_upstairshall3, 'n')
r_upstairshall3.connectRooms(r_upstairshall2, 's')

r_upstairshall3.connectRooms(r_upstairsguestbed3, 'w')
r_upstairsguestbed3.connectRooms(r_upstairshall3, 'e')

r_upstairshall3.connectRooms(r_upstairsguestbed4, 'e')
r_upstairsguestbed4.connectRooms(r_upstairshall3, 'w')

r_upstairsguestbed4.connectRooms(r_upstairsguestbath, 'n')
r_upstairsguestbath.connectRooms(r_upstairsguestbed4, 's')

r_upstairsguestbed4.connectRooms(r_upstairsguestcloset, 's')
r_upstairsguestcloset.connectRooms(r_upstairsguestbed4, 'n')

r_upstairshall3.connectRooms(r_upstairshall4, 'n')
r_upstairshall4.connectRooms(r_upstairshall3, 's')

r_upstairshall4.connectRooms(r_mastersuite, 'n')
r_mastersuite.connectRooms(r_upstairshall4, 's')

r_mastersuite.connectRooms(r_masterbath, 'w')
r_masterbath.connectRooms(r_mastersuite, 'e')

r_mastersuite.connectRooms(r_mastercloset, 'e')
r_mastercloset.connectRooms(r_mastersuite, 'w')

players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()
