# ganymede

Cupbearer to ~zod. A bot for acknowledging dotposts.

Note that this software is currently under development, and I am not responsible for any loss of confidentiality, availability, or integrity of data resulting from use of this software.

## Features

* acknowledge dotposts (any single-character message) in a subscribed chat by responding to a dotposting user with the user's mention and a message
* rudimentary file-based logging for tracking issues & debugging
* configurable settings:
  * log filename
  * welcome message
  * dotpost acknowledgement message
  * ship log-in settings

## Requirements

* [Quinnat](https://github.com/midsum-salrux/quinnat)

## Setup

Install Quinnat via `pip`.

Copy `example.ini` to `default.ini`, and modify it as appropriate to meet your needs.

Add your bot to the chats you want it to acknowledge posts in.

Start the bot:

`python3 main.py`
