# state.py
import reflex as rx
import asyncio
import os

import openai

openai.API_KEY = os.environ["OPENAI_API_KEY"]


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    # def answer(self):
    #     # Our chatbot has some brains now!
    #     session = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "user", "content": self.question}],
    #         stop=None,
    #         temperature=0.7,
    #         stream=True,
    #     )

    #     # Add to the answer as the chatbot responds.
    #     answer = ""
    #     self.chat_history.append((self.question, answer))
    #     for item in session:
    #         if hasattr(item.choices[0].delta, "content"):
    #             answer += item.choices[0].delta.content
    #             self.chat_history[-1] = (self.question, answer)
    #             yield

    # def answer(self):
    #     # Our chatbot is not very smart right now...
    #     answer = "I don't know!"
    #     self.chat_history.append((self.question, answer))

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))
        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.1)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (self.question, answer[:i])
            yield
