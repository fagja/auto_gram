import os
import requests

from dotenv import load_dotenv


base_url = "https://graph.facebook.com"

# .envを環境変数として読み込む
# .envが存在しない場合でもエラーにはならない
load_dotenv()

ig_user_id = os.environ.get("instagram_business_account")
token = os.environ.get("access-token")

tags_basic = f"{base_url}/v14.0/{ig_user_id}/tags?fields=id,username&access_token=token"

# print(os.environ['SECRET'])  # 存在しなかった場合はKeyError
# print(os.environ.get('SECRET'))  # 存在しなかった場合はNone

response = requests.get(tags_basic)
mention_id = response.json()
print(mention_id)


# print(os.environ.get("instagram_business_account"))
