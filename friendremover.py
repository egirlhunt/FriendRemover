import discord
import asyncio

class SelfBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print(f'You have {len(self.user.friends)} friends.')
        print('Starting friend removal process...\n')

        for friend in self.user.friends:
            username = f"{friend.name}#{friend.discriminator}"
            print(f"Remove {username} as a friend? (y/n)")
            
            # Wait for user input
            response = await asyncio.get_event_loop().run_in_executor(None, input, "> ")
            
            if response.lower() == 'y':
                try:
                    await friend.remove_friend()
                    print(f"✅ Removed {username}\n")
                except Exception as e:
                    print(f"❌ Error removing {username}: {e}\n")
            else:
                print(f"⏭️  Skipped {username}\n")
        
        print("Done processing all friends. Script ending.")
        await self.close()

# Get token from user
token = input("Enter your Discord user token: ")

# Run the client
client = SelfBot()
client.run(token, bot=False)
