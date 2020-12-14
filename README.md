CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Starting the Bot
  * Starting the Bot with Drush
  * Starting the Bot with bot_start.php
 * Using the Bot
 * IRC Message Hooks
 * Other IRC Hooks
 * Design Decisions


INTRODUCTION
------------

This is a small (but timecostly) school project that was quite fun. It does not do really much.
You can give it a url (should give out a json) and it will log the atribute you provide.



INSTALLATION
------------

A made it a pip3 package so you can install it with 

pip3 install restlogger

It is a packaged CLI package so it does not need a python3 infront of it when executed.

Otherwise it can be cloned directly from git and there is a install.sh script that probably should be executed before running restlogger.

The Arguments that can be given are:


The program can be stopped by pressing Ctrl+c (control+c on Mac)



USING THE BOT
-------------

Read the licence.




DESIGN DECISIONS
----------------

There are odd things in this program, mainly because I do not know it better and some of the imported models I used for the first time.
