from prompts import *
import os
from openai import OpenAI
from anthropic import Anthropic


API_KEY = os.getenv("LLM_API_TOKEN")
MAX_TOKENS = 2000


class GPT:
    def __init__(self, temperature=0.1):
        self.llm = os.getenv("LLM")
        self.temperature = temperature
        self.client = self._init_client()

    def _init_client(self):
        if "claude" in self.llm.lower():
            self.client = Anthropic(
                api_key=API_KEY
            )
        else:
            self.client = OpenAI(
                api_key=API_KEY
            )
        return self.client

    def get_response(self, system_prompt, prompt):
        messages = [{"role": "user", "content": prompt}]
        if "gpt" in self.llm:
            messages = self.generate_system_prompt(system_prompt) + messages
            return self._get_openai_response(messages)
        elif "claude" in self.llm:
            return self._get_anthropic_response(system_prompt, messages)
        else:
            raise ValueError(f"Unsupported service type: {self.llm}")

    def generate_system_prompt(self, system_prompt):
        return [{"role": "system", "content": system_prompt}]

    def _get_openai_response(self, messages):
        response = self.client.chat.completions.create(
            model=self.llm,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=self.temperature,
        )
        return response.choices[0].message.content

    def _get_anthropic_response(self, system_prompt, messages):
        response = self.client.messages.create(
            model=self.llm,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            temperature=self.temperature,
            messages=messages
        )
        return response.content[0].text


def process_text(features_list, description):
    gpt_engine = GPT()
    system_prompt = build_system_prompt(features_list)
    main_prompt = build_main_prompt(description)
    print(0.03*(len(system_prompt) + len(main_prompt))/(4000))
    return gpt_engine.get_response(system_prompt, main_prompt)
    