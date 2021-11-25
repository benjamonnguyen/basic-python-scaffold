import asyncio

from nextcord.ext import commands, tasks


class TaskLooper(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.test.start()

    @tasks.loop(seconds=5.0)
    async def test(self):
        print(f'Start - {self.test.current_loop}')
        await asyncio.sleep(20.0)
        print(f'End - {self.test.current_loop}')

    @test.before_loop
    async def before(self):
        print('Starting before loop.')
        await self.client.wait_until_ready()


def setup(client):
    client.add_cog(TaskLooper(client))
