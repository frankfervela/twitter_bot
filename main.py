import time
import random
import openai
import tweepy
import keys

# OpenAI API Key
openai.api_key = keys.openai_api_key
engine = "gpt-3.5-turbo"
chatgpt_prompt_list = [
    "Compose a tweet that encourages individuals to embrace change and view it as an opportunity for growth and learning.",
    "Craft a tweet that inspires people to persevere and remain optimistic during challenging times, emphasizing resilience and inner strength.",
    "Write a tweet promoting the importance of self-care and balance in life, highlighting the role it plays in maintaining both mental and physical health.",
    "Create a tweet to encourage individuals to chase their dreams fearlessly, emphasizing the importance of ambition and hard work.",
    "Generate a tweet that inspires the pursuit of continuous learning, emphasizing how knowledge can empower and open new opportunities.",
    "Compose a tweet to motivate people to practice gratitude in everyday life, explaining its positive impact on overall happiness.",
    "Craft a tweet to inspire people to maintain financial discipline, highlighting the long-term benefits of saving and investing.",
    "Create a tweet encouraging people to embrace and spread love, stressing how kindness and compassion can make the world a better place.",
    "Write a tweet to motivate people to stay curious and appreciate the wonders of science and technology, emphasizing their role in shaping our future.",
    "Generate a tweet to inspire individuals to believe in themselves and their abilities, emphasizing that self-confidence is key to success."
]

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=keys.consumer_key,
    consumer_secret=keys.consumer_secret,
    access_token=keys.access_token,
    access_token_secret=keys.access_token_secret
)


def create_tweet(tweet):
    response = client.create_tweet(text=tweet)
    print(response)


# Creates a poll with the provided content, duration and poll options
def create_poll(tweet, poll_duration_in_minutes, poll_options):
    response = client.create_tweet(
        text=tweet,
        poll_duration_minutes=poll_duration_in_minutes,
        poll_options=poll_options)

    print(response)


# Retweets a tweet and returns true if the tweet was successfully retweeted
def retweet(tweet_id):
    response = client.retweet(tweet_id=tweet_id)
    return response


# Replies to a tweet
def reply_to_tweet(tweet_id, content):
    response = client.create_tweet(in_reply_to_tweet_id=tweet_id, text=content)
    print(response)


def get_tweet_from_chat_gpt(prompt):
    final_prompt = prompt + 'Use Jordan Peterson style of writing. Keep the tweet under 150 characters'
    response = openai.ChatCompletion.create(model=engine, messages=[{"role": "user", "content": final_prompt}])
    return response.choices[0].message.content.replace("\"", "")


def run_bot(sleep_time_out):
    while True:
        tweet = get_tweet_from_chat_gpt(random.choice(chatgpt_prompt_list))

        create_tweet(tweet)

        # Sleep for 30 minutes
        time.sleep(sleep_time_out)


if __name__ == '__main__':
    run_bot(1800)

