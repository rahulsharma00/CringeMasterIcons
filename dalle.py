import os

from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.utilities.dalle_image_generator import DallEAPIWrapper

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt to generate an image based on the following description: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)

image_url = DallEAPIWrapper().run(chain.run("Crying emoji"))

print(image_url)
