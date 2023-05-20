import os
import json

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. two interesting facts about them

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", request_timeout=120)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    url = "https://gist.githubusercontent.com/noircir/52de0d7488dfe1af0e50b20077aaa6da/raw/83d8dceeded1ca8d8f84073b1c0d6e25c17abea6/harrison.json"

    linkedin_data = scrape_linkedin_profile(url)

    print(chain.run(information=linkedin_data))

    # json_str = json.dumps(linkedin_data, indent=4)
    # print(json_str)
