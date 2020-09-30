

import discord
from discord.ext import commands

import time
import random
import youtube_dl

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



class General(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.initial_time = time.monotonic() # initialize time for calculating uptime
	 

	@commands.command()
	async def ping(self, ctx):
		current_ping = round(self.bot.latency, 2)
		current_uptime = round(time.monotonic() - self.initial_time, 2)
		embed = discord.Embed(title="Scylla", description="Ping Details", color=0xc41c1c)
		embed.set_thumbnail(url="https://github.com/p014ri5/scylla/raw/master/assets/profile.png")
		embed.add_field(name="🏓 Ping ", value=str(current_ping)+"s", inline=False)
		embed.add_field(name="👍 Uptime", value=str(current_uptime)+"s", inline=False)
		await ctx.send(embed=embed)

	@commands.command(aliases=['8ball'])
	async def ball(self, ctx, *, question):
		responses = [
			"It is certain.",
			"It is decidedly so.",
			"Without a doubt.",
			"Yes – definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."
		]
		await ctx.send(f"{random.choice(responses)}")

	@client.command(pass_context = True)
	async def play(ctx, url):
		try:
			channel = ctx.author.voice.channel
			await channel.connect()
		except Exception:
			ctx.send("```Join a voice channel first!```")
		try:
			async with ctx.typing():
				player = await YTDLSource.from_url(url)
				ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

			await ctx.send('```Now playing: {}```'.format(player.title))
		except Exception:
			ctx.send("```Error! Try doing $join first?```")

	@client.command(pass_context=True)
	async def leave(ctx):
		try:
			server = ctx.message.guild.voice_client
			await server.disconnect()
		except Exception:
			await ctx.send("```Not in a voice channel! Use $join!```")

def setup(bot):
	bot.add_cog(General(bot))