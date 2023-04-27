import time
import asyncio
import webbrowser


class User:
    def __init__(self, name: str, avatar_url: str):
        self.name = name
        self.avatar_url = avatar_url


async def fetch_user(user_id: int) -> User:
    users_db = {
        1: {
            'name': 'soymilk',
            'avatar_url': 'https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif'
        },
        2: {
            'name': 'somebody',
            'avatar_url': 'https://media.tenor.com/bHAgDpHZgfAAAAAd/now-youre-just-somebody-that-i-used-to-know-wouter-de-backer.gif'
        },

    }

    # simulate the time it takes to fetch user from a db
    await asyncio.sleep(1)
    data = users_db[user_id]
    print(f'user {data["name"]} is fetched successfully.')
    return User(data['name'], data['avatar_url'])


async def fetch_avatar(user_id: int) -> str:
    # in order to get the url for the avatar of the user
    # we must first fetch the user
    user = await fetch_user(user_id)

    # simulate the time it takes to download the image or whatever
    # However, here we are just returning the url of the image
    await asyncio.sleep(1)
    return user.avatar_url


async def main():
    avatar_urls = await asyncio.gather(
        fetch_avatar(1),
        fetch_avatar(2)
    )
    for url in avatar_urls:
        webbrowser.open(url)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'It took {end - start:.4f}s.')
