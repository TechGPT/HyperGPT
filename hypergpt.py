"""
~ Coded By @BiswaX
~ Follow me on Github: @techgpt
"""
import requests

class HyperAttr:

        def __init__(self, json_dict) -> None:
                self.__dict__ = json_dict
                for key, value in json_dict.items():
                        if isinstance(value, dict):
                                setattr(self, key, HyperAttr(value))

        def __getattr__(self, attr):
                if attr in self.__dict__:
                        return self.__dict__[attr]
                else:
                        return None


class HyperGPT:

        def __init__(self, base_api: str = None):
                self.base_api = base_api
                self.commonErr = [
                        "Please provide a promote for {}",
                        "It looks like invalid model provided: {}",
                        "Getting error from server code: {}",
                        "An error occured: {}"
                ]
                self.session = requests.session()
                self.chat_models = ["gpt", "llama", "bard"]
                self.img_models = ["art", "photography", "3d"]

        def _response(self, _jsonObj: bool = True, **response):
                # create hyper json object
                return HyperAttr(response) if _jsonObj else response

        def chatbot(self, prompt: str = None, model: str = None):
                #create a chatbot instant
                if not model or model not in self.chat_models:
                        return self._response(
                                error=self.commonErr[1].format(model))
                if not prompt:
                        return self._response(
                                error=self.commonErr[0].format(model))
                url = self.base_api.format("chat")

                params = dict(model=model, prompt=prompt)
                r = self.session.get(url, params=params)
                _res, _code = HyperAttr(r.json()), r.status_code
                if not _code == 200:
                        return self._response(
                                error=self.commonErr[2].format(_code))
                if _res.error:
                        return self._response(
                                error=self.commonErr[3].format(_res.error))

                return self._response(response=_res.data)

        def generate_image(self, prompt: str, model: str = None):
                try:
                        if not model or model not in self.img_models:
                                return self._response(
                                        error=self.commonErr[1].format(model))
                        if not prompt:
                                return self._response(
                                        error=self.commonErr[0].format(model))
                        url = self.base_api.format("image")
                        params = dict(prompt=prompt, model=model)
                        r = self.session.get(url, params=params)
                        _res, _code = HyperAttr(r.json()), r.status_code
                        if not _code == 200:
                                return self._response(
                                        error=self.commonErr[2].format(_code))
                        if _res.error:
                                return self._response(error=self.commonErr[3].
                                                      format(_res.error))

                        return self._response(result=_res.result)
                except Exception as e:
                        print(e)
                        return self._response(
                                error=self.commonErr[3].format(e))


hyper = HyperGPT()
hyper.base_api = "https://api.biswax.dev/{}"

prompt = "what is your name?"

# chatgpt response
print("ChatGPT Response: ")
chatgpt = hyper.chatbot(prompt, model="gpt")
print(chatgpt.response)

# facebook's llama response
print("\nLLAMA Response: ")
llama = hyper.chatbot(prompt, model="llama")
print(llama.response)

# Generate Image
print("\nGenerate Image: ")
imageai = hyper.generate_image("elon musk", model="3d")
print("Image is ready: ", imageai.result)
