# Vu-Bot
Simple bot. Another version on python since Deno discord library can't kep the connection alive for more than 3 hours. This bot is now deployed on EC2 AWS server running as a service worker.

## Commands
| Command | Arguments | Description |
|---------|---------------|---------|
| $generate | your prompt | Generate an image base on your prompt
| $quote | - | Send a random quote to discord

## How to run
1. Place your bot token in .env file 

2. Run the command
```sh
deno run --allow-read --allow-env --allow-net --watch mods.js
```
## Overview
<img src="https://firebasestorage.googleapis.com/v0/b/chatapp-be9bd.appspot.com/o/Screenshot%202022-12-07%20210802.png?alt=media&token=63ec062e-3496-4a55-9c12-e0367990d43b">
<img src="https://firebasestorage.googleapis.com/v0/b/chatapp-be9bd.appspot.com/o/bot2.png?alt=media&token=a54f69c8-3a83-4170-af71-72ee404da682"/>