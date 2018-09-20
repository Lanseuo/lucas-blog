import requests
import twitter
from onesignal import OneSignal, SegmentNotification

import config


twitter_client = twitter.Api(config.twitter_consumer,
                             config.twitter_consumer_secret,
                             config.twitter_token,
                             config.twitter_token_secret)

onesignal_client = OneSignal(config.onesignal_app_id, config.onesignal_rest_api_key)


def post_to_twitter(post):
    twitter_client.PostUpdate(
        f"Neuer Artikel auf meinem Blog: {post['title']} https://blog.lucas-hild.de/{post['permalink']}")
    print("\nTweeted about post")


def send_web_notification(post):
    notification = SegmentNotification(
        contents={
            "en": f"Neuer Artikel: {post['title']}"
        },
        included_segments=[SegmentNotification.ALL],
        url=f"https://blog.lucas-hild.de/{post['permalink']}"
    )

    result = onesignal_client.send(notification)
    print(f"Sent OneSignal Notification to {result['recipients']} Recipients")


def main():
    r = requests.get("https://blog.lucas-hild.de/api/posts")
    posts = r.json()[:3]

    for (index, post) in enumerate(posts):
        print(f"({index}) {post['title']}")

    index_of_post = input("Index of post: ")
    post = posts[int(index_of_post)]

    post_to_twitter(post)
    send_web_notification(post)


main()
