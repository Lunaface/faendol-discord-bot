import re
import urllib.parse
bracketsRegex = re.compile(r'\[\[(.*?)\]\]')

async def handle_message(message):
    linked_pages = re.findall(bracketsRegex, message.content)
    if len(linked_pages) == 0:
        return
    
    for linked_page in linked_pages:
        # todo: page existance verification
        await message.reply(f'https://faendol.com/{urllib.parse.quote(linked_page)}')