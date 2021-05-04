#!/usr/bin/env python3

from os import system

class Title:

    def __init__( self, text ):
        self.text = text

#    def __str__( self):
#        return self.text
    
    def outColor( self ):
        for i in self.text:
            if( i == "-" ):
                print( f"\033[30m{i}", sep = "", end = "" )
            elif( i == "=" ):
                print( f"\033[34m{i}", sep = "", end = "" )

            else:
             print( f"\033[35m{i}", sep = "", end = "" )
    
    def modTitle( self ):
        self.text = self.text.upper()
        self.text = self.text.split()
        self.text.insert( 0, "-" )
        self.text.insert( 1, "=" )
        self.text.append( "=" )
        self.text.append( "-" )
        return self.text
    
    def outColor( self, splitText ):
        
        extrem_1 = 0
        extrem_2 = 1
        k = 0
        max_range = len(splitText) - 1
        
        for i in splitText:
            #coloring extrem letters 1
            if( i == splitText[extrem_1] or\
                i == splitText[max_range - extrem_1]\
               ):
                print( f"\033[30m{i} ", end = "" )
                k += 1
            #coloring extrem letters 2
            elif( i == splitText[extrem_2] or\
                  i == splitText[max_range - extrem_2]\
                ):
                print( f"\033[34m{i} ", end = "" )
                k += 1
            
            #coloring two first words of text
            elif( i == splitText[k] or i == splitText[k + 1] ):
                print( f"\033[35m{i} ", end = "" )
            
            #coloring rest
            else:
                print( f"\033[34m{i} ", end = "" )
        print()


###### create ######

title = Title( "Programming in Python 3" )
mod = title.modTitle()

#### VIEW ############

system( "clear" )
print()
title.outColor(mod)

##
