
import os
import json

# variables
prefix = os.environ.get("PREFIX")
embedColor = os.environ.get("EMBED_COLOR")
icon = os.environ.get("ICON")

allowedChannels = json.loads(os.environ['BOT_INTERACTION_CHANNEL_ID'])

wallet_ERC20 = "soon"
wallet_akash = "soon"
