
#! python3
import fdefs as f

# keep this Section as it is
f.setup()
f.enterWolt()
f.autoStartMunich() # exeption: for shifts showing up at 10:00 use "f.startAt(10)" instead
f.refresh()
f.moveToLaterDays()
# end of Section

### booking ###

# for booking shifts use "f.bookingMunich( day, slot )" function
# input here the shifts you want - one copy of f.bookingMunich() per shift

# slot numbers are as displayed in the code generator

# day numbers are as follows:
# ( day - [if there is an extra Saturday at the end] - [if there is NO extra Saturday at the end] )
# Monday - 8 - 7
# Tuesday - 7 - 6
# Wenesday - 6 - 5
# Thursday - 5 - 4
# Friday - 4 - 3
# Saturday - 3 - 2
# Sunday - 2 - 1


# example: 

# booking for 7th shift from the top on Tuesday,
# if there is an extra Saturday from next month at the end would be:
f.bookingMunich(7,7)
# and if the extra Saturday isn't there:
f.bookingMunich(6,7)

### end of booking ###

f.pause()
