import asyncio


async def start_strongman(name, power):
    ball = 5
    delay = 1 / power
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(ball):
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {ball_number + 1} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = list()
    participants = {'Pasha': 3, 'Denis': 4, 'Apollon': 5}
    for user in participants:
        tasks.append(asyncio.create_task(start_strongman(user, participants[user])))
    for task in tasks:
        await task


asyncio.run(start_tournament())
