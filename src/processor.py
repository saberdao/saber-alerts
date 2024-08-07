from solana.rpc.api import Client
from api import SABER_POOLS_DATA
from solders.pubkey import Pubkey


class Processor:
    def __init__(self, RPC_URI):
        self.client = Client(RPC_URI)
        self.reserve_pair_dict = {}
        for pool_data in SABER_POOLS_DATA:
            if pool_data["isVerified"]:
                self.reserve_pair_dict[pool_data["name"]] = pool_data["addresses"]["reserves"]

    def get_total_reserves(self):
        total_reserve_dict = {}
        for pool_name, reserve_pair in self.reserve_pair_dict.items():
            balance_a = self.client.get_token_account_balance(
                Pubkey.from_string(reserve_pair[0])
            ).value.ui_amount

            balance_b = self.client.get_token_account_balance(
                Pubkey.from_string(reserve_pair[1])
            ).value.ui_amount

            total_reserve_dict[pool_name] = [balance_a, balance_b]
         
        return total_reserve_dict
