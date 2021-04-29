#!/usr/bin/env python3

from os import system

class Title:
    pass

class Author:
    pass


def newTitle( text ):
    title = Title()
    title = text
    return title

def newAuthor( text ):
    author = Author()
    author = text
    return author

title1 = newTitle( "A Very Easy Death" )
title2 = newTitle( "Dauther" )


author2 = newAuthor( "Alexandra Lvovna Tolstaya" )
author1 = newAuthor( "Simone De Beauvoir" )





system( "clear" )
print()
print( f"{title1:20}  {author1}" )
print( f"{title2:20} {author2}" )
