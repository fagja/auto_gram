# 基本情報
import os
import requests
from dotenv import load_dotenv

load_dotenv()

ig_user_id = os.environ.get("instagram_business_account")
access_token = os.environ.get("access-token")

base_url = "https://graph.facebook.com"
# 基本情報///
fields = 'name,username,biography,follows_count,followers_count,media_count'

followers_url = f"{base_url}/v14.0/{ig_user_id}?fields=business_discovery.username(hiraizumi_ds){{{fields}}}&access_token={access_token}"
response_followers = requests.get(followers_url)
followers_json = response_followers.json()

print(followers_json)