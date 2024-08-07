from processor import Processor
import os
import json
import dotenv
from discord import Intents, Client, Message
import asyncio

dotenv.load_dotenv()
# RPC_URI = os.environ.get("RPC_URI")
# processor = Processor(RPC_URI)
# total_reserve_dict = processor.get_total_reserves()


# def get_variance_1h(variance_percentage_threshold):
#     alert_dict = {}
#     with open("src/reserve_data.json", "r") as f:
#         old_total_reserve_dict = json.load(f)
        
#         for pool_name, reserve_pair in old_total_reserve_dict.items():
#             old_total_reserve = sum(reserve_pair)
#             new_total_reserve = sum(
#                 total_reserve_dict[pool_name]
#             )    

#             variance_percentage = (new_total_reserve - old_total_reserve) / old_total_reserve * 100

#             if variance_percentage >= variance_percentage_threshold:
#                 alert_dict[pool_name] = variance_percentage

#     return alert_dict

# def write_data_to_json():
#     with open("src/reserve_data.json", "w") as f:
#         json.dump(total_reserve_dict, f, indent=6)


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
print(DISCORD_TOKEN)
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def send_alert():
    channel = client.get_channel(1063008961764278325)
    await channel.send("Hello")
asyncio.run(
    client.run(DISCORD_TOKEN)
)
