from datetime import datetime
import discord


embed_ping = discord.Embed(
    title="What masterpiece shall we play today ?",
    description='> The Discord app was successfully integrated, enabling seamless interaction within the platform. All core features, including slash commands, event handling, and user permissions, are now fully operational and responsive inside Discord servers.\n\n_"A wrong note is just...a happy little accident."_',
    colour=0x00B0F4,
    timestamp=datetime.now(),
)

embed_ping.set_author(
    name="Sona Buvelle",
    url="https://github.com/AmbitiousFlow",
    icon_url="https://cdn.discordapp.com/attachments/1383187634129731755/1383189049661067304/L-QJcaAQ_400x400.jpg?ex=684de2af&is=684c912f&hm=072114886ea5d4d883fb5beccf813ae4095bd9e440092b967629e9f4d0b7698c&",
)

embed_ping.set_image(
    url="https://cdn.discordapp.com/attachments/1383187634129731755/1383189049254346842/22dcd432b093464565f87e4776f0669b.jpg?ex=684de2af&is=684c912f&hm=217dedc39b9a61d7a60e02b75b551ab25a25c8b7a601f11d3456440ff0818619&"
)