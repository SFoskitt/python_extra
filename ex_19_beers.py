# "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.

# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.

# Your task here is write a Python program capable of generating all the verses of the song.


def beers_on_the_wall():
    beers = 99
    
    while beers != 0:

        if beers != 1:
            print beers, ' bottles of beer on the wall, ', beers, ' bottles of beer'
        else:
            print 'One bottle of beer on the wall, one bottle of beer' 

        print 'Take one down, pass it around, ',
        beers -= 1
        if beers != 0:
            print beers , ' on the wall'

        if beers == 0:
            print 'No more bottles of beer on the wall'

beers_on_the_wall()