import os
import requests
from dotenv import load_dotenv

load_dotenv()

# proxycurl_api_key = os.getenv('PROXYCURL_API_KEY')
# print(proxycurl_api_key)


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from linkedin profiles,
    Manually scrape the information from the LinkedIn profile
    """
    # api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    # header_dic = {'Authorization': f'Bearer {proxycurl_api_key}'}

    # params = {
    #     'url': linkedin_profile_url
    # }

    # response = requests.get(api_endpoint,
    #                     params=params,
    #                     headers=header_dic)

    response = requests.get(linkedin_profile_url)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pi_url")

    return data
