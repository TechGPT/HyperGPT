"""
Follow on TG: @UnrealCoder
Coded By @BiswaX
"""
from curl_cffi import requests
import random
import re


class HyperGPT2:

        def __init__(self, history: dict = {}):

                self.codedBy = "@BiswaX"
                self.history = history
                self.chat_history_limit = 30

                # set default instruction
                self.instruct = "You are HyperGPT, a large language model trained by OpenAI.\nRespond using Markdown."

                # set api config
                self.url = "https://gptchatly.com"
                self.models = {
                    "gpt-3": {
                        "id": "fetch-response"
                    },
                    "gpt-4": {
                        "id": "fetch-gpt4-response"
                    }
                }

        def random_ua(self):
                android_versions = ["Android 10", "Android 11", "Android 12"]
                ios_versions = ["iOS 14", "iOS 15"]
                windows_versions = ["Windows 10", "Windows 11"]
                mac_versions = [
                    "Macintosh; Intel Mac OS X 10_15",
                    "Macintosh; Intel Mac OS X 10_16"
                ]

                android_ua = f"Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 90)}.0.4430.210 Mobile Safari/537.36"
                ios_ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(ios_versions)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(12, 14)}.0 Mobile/15E148 Safari/604.1"
                windows_ua = f"Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 90)}.0.4430.210 Safari/537.36"
                mac_ua = f"Mozilla/5.0 ({random.choice(mac_versions)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80, 90)}.0.4430.210 Safari/537.36"

                ua_list = [android_ua, ios_ua, windows_ua, mac_ua]
                return random.choice(ua_list)

        def llama2(self, prompt: str):
                try:
                        url = "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1"
                        headers = {
                            "content-Type":
                            "application/json",
                            "User-Agent":
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                        }
                        payload = {"prompt": prompt}
                        r = requests.post(url, json=payload, headers=headers)
                        if not r.status_code == 200:
                                return None, f"Error: Llama Model status code: {r.status_code}"
                        return r.json().get("completion", "No data..."), None
                except Exception as e:
                        return None, str(e)

        def _sse_event(self, data: str):
                # use this function when stream is true
                match = re.search(r'"content":"(.+?)"', data)
                data = match.group(1) if match else None
                return data

        def generate_response(self,
                              prompt: str = "hello",
                              instruct: str = None,
                              session_id: str = None,
                              model: str = "gpt-3",
                              history_limit: int = 30) -> tuple:
                try:
                        chat_history_limit: int = history_limit if history_limit else self.chat_history_limit
                        ses_id = session_id if session_id else "HyperxxxxxxSession"
                        url = "https://api.deepai.org/make_me_a_pizza"
                        messages: list[dict] = [{
                            "role":
                            "system",
                            "content":
                            self.instruct if not instruct else instruct
                        }, {
                            "role": "user",
                            "content": prompt
                        }]
                        if ses_id in self.history:
                                messages = []
                                messages.extend(self.history[ses_id] +
                                                [{
                                                    "role": "user",
                                                    "content": prompt
                                                }])
                                self.history[ses_id] = messages

                        if not self.models.get(model, None):
                                raise Exception(f"No Model found: {model}")
                        model_id: str = self.models[model]['id']
                        headers: dict[str, str] = {
                            "User-Agent": self.random_ua(),
                            "Accept": "*/*",
                            "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Referer": f"{self.url}/",
                            "Content-Type": "application/json",
                            "Origin": self.url,
                            "Connection": "keep-alive",
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-origin",
                            "Pragma": "no-cache",
                            "Cache-Control": "no-cache",
                            "TE": "trailers",
                        }
                        url = "/".join([self.url, model_id])
                        data = {"past_conversations": messages}

                        resp = requests.post(url,
                                             json=data,
                                             headers=headers,
                                             impersonate="chrome110")
                        bres = resp.json().get("chatGPTResponse", None)
                        if not bres:
                                return (
                                    None,
                                    f"No Valid Response Returned: {resp.text}")

                        if ses_id not in self.history:
                                self.history[ses_id] = messages

                        if len(self.history[ses_id]) >= chat_history_limit:
                                self.history[ses_id] = messages[:3]
                        self.history[ses_id].append({
                            'role': 'assistant',
                            'content': bres
                        })

                        return (bres, None)
                except Exception as e:
                        print(e)
                        return (None, str(e))


# Usage is Here


def hyper_is_listening():
        bot = HyperGPT2()
        intro = f"""\n\nHYPER GPT v2\n\nModels: GPT-3/4\nCreator: {bot.codedBy}\n\nlet's chat...\n\n"""
        print(intro)
        while 1:
                

                # set custom instruction if you want
                custom_instruction = None
                model_type = "gpt-3"
                chat_history_limit = 50
                prompt = input("\nYou: ")
                
                response, error = bot.generate_response(
                    prompt,
                    custom_instruction,
                    model=model_type,
                    history_limit=chat_history_limit)
                # print()
                if error:
                        print(f"HyperGPT: {error}")
                        return
                else:
                        print(f"\nHyperGPT: {response}")
                        continue


if __name__ == "__main__":

        # listen...
        hyper_is_listening()
