# Scylla

Discord Server : 

>**Scylla** is a Discord bot under development for programmers, hackers and developers.

Most of the times we developers/programmers/hackers hang out in Discord server discussing about our projects. So I wanted to create a bot which would make our lives easier. Well the only problem is exams are few days away and I gotta study. But recently I came across Hacktoberfest so I thought it would be cool opportunity to make this happen with the help of all of you crazy open source guys. It will also be a great first open source project for newbies. So I decided to make it open source. Enough Talk, We got work to do.

I'll be sharing Bot invite link soon. Sadly my Heroku Dynos ran out :( So will update the link to bot invite and server soon.
Also don't mind If this project is not really well documented, I'll try to improve it as much as I can ASAP. If you'd like to improve the documentation please open a PR too :)

If you are new to Discord bot development I'll suggest watching [Discord Rewrite Tutorial by Lucas](https://youtu.be/nW8c7vT6Hl4)

The bot has 4 different **cogs** which are *admin*, *programming*, *general* and *pentesting* and a *main* Python file.

- Admin Cog will have commands only admin can use. e.g. Deleting given number of last messages, Getting Member list by Role, etc.

- General Cog will have general commands for fun. Like 8ball, Ping, Currency converter, etc. 

- Pentesting Cog will have commands built for hackers. Example : URL Encoding, Caeser and ROT13 Cipher, Exiftool, etc.

- Programming Cog will have some basing Programming commands like Hex, Decimal Converter, Linux command man pages, Assembly Command to OP Code converter, Regex stuff etc.

- Finally Developer Cog will have stuff like HTML Table Code Generator, React Docs URL Returner, etc.

- Main Python File will only be used to add load, unload cogs and prefix changing commands.

If you would like to suggest a new command or any kind of suggestion please open a new issue :)

The commands that are implemented in different Cogs and People who implemented them are :

## Contributions

|   Cog/File  |   Command  | Description                                                                                                                                     |               Developer               |    Date    |
|:-----------:|:----------:|-------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------:|:----------:|
|    Admin    |    clear   | Deletes last given number of message as argument.                                                                                               | [p014ri5](https://github.com/p014ri5) | 27-09-2020 |
|   General   |    ping    | Returns Latency of Bot in seconds, with uptime.                                                                                                 | [p014ri5](https://github.com/p014ri5) | 27-09-2020 |
|   General   | 8ball/ball | Return one of the 20 responses, while takes question as argument.                                                                               | [p014ri5](https://github.com/p014ri5) | 27-09-2020 |
| Programming |   convert  | Sub commands : dec, hex, oct Return conversion among decimal, hexadecimal and octal. Also returns UTF-8 Character for the corresponding Number. | [p014ri5](https://github.com/p014ri5) | 27-09-2020 |

If you would like to contribute to it, Please read [CONTRIBUTING.md](https://github.com/p014ri5/scylla/blob/master/CONTRIBUTING.md)


