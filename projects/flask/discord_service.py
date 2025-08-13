#  this is the Discord configuration file


import requests as R

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1404827548927397898/O3hv5lUmeMZVdBXMx91lrWNesPRcy_sxZ6djh5nhF7DY82Eg7gPgRiM38pGe3Dcu1TjB"


def send_to_discord(msg: str) -> None:
    response_post = R.post(DISCORD_WEBHOOK_URL, json={"content": msg})
    response_post.raise_for_status()
