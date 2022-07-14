from dhooks import Embed, Webhook




embed = Embed(
    color=0x6436CB
)

# test https://discord.com/api/webhooks/974346899521937549/p4XwuCyJv541UM_jfHOWPyDf2hyY2AeoynBKpdSVFg5vkCTOEc1x2w92A9XX0gaLd5FW
webhook = "https://discord.com/api/webhooks/983775338574262342/QfX4iSmMGLDjHo7izOXzVheUcqSFLtH03oQtnIX0-mSWTfz2Ch-ln4yahZwAdCVhldRZ"


value = """
- Auto-scheduling 
- Scam & honeypot detector 
- Metaplex fee bypass 
- Custom wallets, tasks and delay 
"""
embed.add_field(name="**Candy Machine v2 minting** :candy:", value=value, inline=False)

value = """
- Transaction speeding and cancelation 
- Gas manager 
- Custom wallets, tasks and delay 
"""
embed.add_field(name="**Ethereum contract minting** <:Ethereum:918873522053455934>", value=value, inline=False)

value = """
- Auto-scheduling
- Anti-bot bypass
- Proxy support 
- Custom wallets, tasks and delay 
"""
embed.add_field(name="**MagicEden launchpad minting** <:ME_Logo_Gradient:925606536468906015>", value=value, inline=False)

value = """
- Auto-scheduling
- Custom wallets, tasks and delay 
"""
embed.add_field(name="**LaunchMyNFT minting** <:mmm:783824151835443200>", value=value, inline=False)

value = """
- Auto-scheduling
- Custom wallets, tasks and delay 
"""
embed.add_field(name="**MonkeLabs minting** :monkey_face:", value=value, inline=False)

value = """
- Blockchain based 
- Filtered sniping (max and min price, floor %)
- Add ranks
- Add attributes 
- Auto-lister (sniped price %, floor price %, highest trait %)
- In-time floor monitor
- Multiple collections
"""
embed.add_field(name="**MagicEden & CoralCube sniper** :dart:", value=value, inline=False)

value = """
- Blockchain based
"""
embed.add_field(name="**FamousFox sniper** <:angyfox:911451631093178378>", value=value, inline=False)

value = """
- By price 
- By attributes 
- In-time floor monitor
"""
embed.add_field(name="**OpenSea sniper** <:OpenSeaLogo:862443378461638697>", value=value, inline=False)

value = """
- Mass listing 
- Mass delisting 
- Funds transfer 
- NFT transfer
- NFT burner
"""
embed.add_field(name="**Solana wallets manager** :briefcase:", value=value, inline=False)

value = """
- Candy Machine ID scraper 
- ME new listings monitor
- ME collection data scraper
- LaunchMyNFT new candys
"""
embed.add_field(name="**Discord monitors and tools** :gear:", value=value, inline=False)

value = """
- WL spots
- WL early infos 
- Investment calls, short and long term 
- Profitable daily and degen plays 
"""
embed.add_field(name="**Alpha group opportunites** :sparkles:", value=value, inline=False)

value = """
- Currently on beta testing for holders
"""
embed.add_field(name="**Custom RPC node** :zap:", value=value, inline=False)

value = """
- Windows only
"""
embed.add_field(name="**Platform** :computer:", value=value, inline=False)

magiceden = "https://magiceden.io/marketplace/txneura"
opensea = "https://opensea.io/collection/neura"
twitter = "https://twitter.com/txNeura"

links = f"[MagicEden]({magiceden}) [OpenSea]({opensea}) [Twitter]({twitter})"

embed.add_field(name="‎", value=links)
embed.set_image(url="https://cdn.discordapp.com/attachments/974346875538898974/983789981686448158/banner.png")

Webhook(webhook).send(embed=embed)