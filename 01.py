# 基本情報
import os
import requests
from dotenv import load_dotenv

load_dotenv()

ig_user_id = os.environ.get("instagram_business_account")
access_token = os.environ.get("access-token")

base_url = "https://graph.facebook.com"
# 基本情報///


# タグ付けされたメディアデータをGET(get)
get_url = (
    f"{base_url}/v14.0/{ig_user_id}/tags?fields=like_count&access_token={access_token}"
)

response_get = requests.get(get_url)  # メディアデータを取得

get_json = response_get.json()  # json形式に変換

l = get_json["data"]
max = get_json["data"][0]
for i in get_json["data"]:
    if max["like_count"] < i["like_count"]:
        max = i

print(max)

# n = len(get_json["data"])  # タグ付けされた投稿数
# for i in range(n):
#     likes = get_json["data"][i]["like_count"]  # like数だけ表示
#     # print(likes)
# # タグ付けされたメディアデータをGET///
