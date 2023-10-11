# Follow on https://t.me/unrealcoder

import requests
import secrets
import re


class GodGPT:
    def __init__(self) -> None:
        self.api_url = "https://gptgod.site/api/session/free/gpt3p5"

    def generate_id(self, hex_id:int = 16, zfill:int = 32):
        return {"id": secrets.token_hex(hex_id).zfill(zfill)}

    def generate_text(self, prompt: str):

        payload = {
            **self.generate_id(),
            "content": prompt
        }

        response = requests.get(self.api_url, params=payload)
        convo = []
        for data in response.iter_lines(chunk_size=None):
            msg = re.findall(r'data:\s*"(.*)"', data.decode())
            if msg:
                convo.append(msg[0])
        return "".join(convo)


bot = GodGPT()
print(bot.generate_text("how are you"))
