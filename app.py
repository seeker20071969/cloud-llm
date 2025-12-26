import chainlit as cl
from openai import OpenAI

#client = OpenAI()

@cl.on_message
async def main(message: cl.Message):

    '''
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content},
        ],
    )

    reply = response.choices[0].message.content
    '''

    await cl.Message(content=message.content).send()