# 基本情報
import os
import requests
from dotenv import load_dotenv

load_dotenv()

ig_user_id = os.environ.get("instagram_business_account")
access_token = os.environ.get("access-token")

base_url = "https://graph.facebook.com"
# 基本情報///


def main():
    # タグ付けされたメディアデータをGET(get)
    get_url = (
        f"{base_url}/v14.0/{ig_user_id}/tags"
        f"?fields=media_url&access_token={access_token}"
    )

    response_get = requests.get(get_url)  # メディアデータを取得
    get_json = response_get.json()  # json形式に変換
    image_url = get_json["data"][0]["media_url"].replace("&", "%26") # 必要なイメージURL
    # タグ付けされたメディアデータをGET///

    # コンテナを作成(create)
    create_url = (
        f"{base_url}/v14.0/{ig_user_id}/media"
        f"?image_url={image_url}&access_token={access_token}"
    )

    response_create = requests.post(create_url)  # コンテナ作成
    create_json = response_create.json()  # json形式に変換
    creation_id = create_json["id"]  # idだけ抽出
    # コンテナを作成///

    # コンテナを公開(post)
    post_url = (
        f"{base_url}/v14.0/{ig_user_id}/media_publish"
        f"?creation_id={creation_id}&access_token={access_token}"
    )

    response_post = requests.post(post_url)  # コンテナ公開
    post_id = response_post.json()
    # コンテナを公開///

    print(post_id)


if __name__ == "__main__":
    main()
