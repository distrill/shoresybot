from random import sample
import sys
import os
import traceback
import praw


client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
username = os.environ.get('BOTUSERNAME')
password = os.environ.get('PASSWORD')
sub = os.environ.get('SUB')
dev = os.environ.get('DEV')

prompts = [
    'fuck you shoresy',
    'fuck you shorsey',
]

def genreddit():
    if client_id is None:
        raise Exception('CLIENT_ID is required env var')
    if client_secret is None:
        raise Exception('CLIENT_SECRET is required env var')
    if username is None:
        raise Exception('USERNAME is required env var')
    if password is None:
        raise Exception('PASSWORD is required env var')
    if sub is None:
        raise Exception('SUB is required env var')
    if dev is None:
        raise Exception('DEV is required env var')

    return praw.Reddit(
        user_agent=f'shoresy_bot (by /u/{dev})',
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
    )


responses = [
    lambda x: f'Fuck you {x}, Fight me see what happens.',
    lambda x: f"Here's what happens: I hit you, you hit the pavement, ambulance hits 60",
    lambda x: f"Here's what happens: I hit you, you hit the pavement and I fuck your mom again.",
    lambda x: f"Your mom just liked my Instagram post from two years ago in Puerto Vallarta. Tell her I'll put my swimming trunks on for her anytime she likes.",
    lambda x: f"{x} I made an opsies, can you tell your mom to pick up Jonesys mom on the way over to my place I double booked them by mistake you fuckin loser",
    lambda x: f"Shoulda heard your mom last night {x}, she sounded like a window closing on a Tonkinese cats tail like, mmmrrrooowwwwwowowwww",
    lambda x: f"Shoulda heard your mom last night {x}, she sounded like my great aunt when I pop in for a surprise visit like, ooooooooooohhhhhhhhhhhhh",
    lambda x: f"Fuck you {x}, your mom keeps tryin' to slip a finger in my bum but I keep telling her that I only let jonsey's mom do that ya fuckin loser",
    lambda x: f"Fuck you {x}, I made your mom cum so hard that they made a canadian heritage moment out of it and Don Mckellar played my dick",
    lambda x: f"Fuck you {x}, your mom shot cum straight across the room and killed my siamese fighting fish, threw off the PH levels in my aquarium.",
    lambda x: f"Fuck you {x}, your mum loves butt play like I love haagen dazs; let's get some fuckin' ice cream.",
    lambda x: f"Fuck you {x}, tell your mom I drained the bank account she set up for me. Top it up so I can get some fucking KFC.",
]

def main():
    reddit = genreddit()
    subreddit = reddit.subreddit(sub)
    print(f'listening on {sub}')
    for c in subreddit.stream.comments(skip_existing=True):
        try:
            comment = reddit.comment(f'{c}')
            body = comment.body.lower()
            author = comment.author

            # ignore if comment is from me
            if author == username:
                continue

            for p in prompts:
                if p in body:
                    print(f'chirping: {author}')
                    chirp = sample(responses, 1)[0](author)
                    comment.reply(chirp)
        except Exception as e:
            print("ERR:", e)

if __name__ == "__main__":
    main()
