# about
a simple and versatile heading-based documentation generator.

this was created to generate documentation for our <a href='https://github.com/microwaveabletoaster/dunces-and-dungeons'>game</a>.


#usage
put the code that you want to document in the root directory, then run run.py. the code will be chewed up and spit out into the output.js file. once you have done this, pop open index.html and your pretty documentation will be there.

#commenting
docraiser does its thing using html headings. to comment your code for docraiser you need to first put the level of heading you want, then the name of the heading- all enclosed by a special delimeter (which is * by default. it can be changed by editing it on the first line of main.coffee). for example:

``` # * 1 this is my first heading * ```

leaving out the index will add some normal text to the currently active header.

#oh god, it's ugly
yep, docraiser ships without any sort of styling, because i couldn't be bothered. all you have to do is build styles for the h1-h6 and a elements. it probably won't be that hard.

#todo
- add some sort of magic sidebar to help with navigation
- add some styles
- add a 'watch' mode to run.py
