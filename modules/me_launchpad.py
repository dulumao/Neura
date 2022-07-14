from requests import Response
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Commitment
from solana.blockhash import Blockhash
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.publickey import PublicKey
from spl.token.instructions import get_associated_token_address
from base58 import b58decode, b58encode
from solana.rpc.core import UnconfirmedTxError
from requests.structures import CaseInsensitiveDict
from anchorpy import Program, Wallet, Provider
from solana.rpc.async_api import AsyncClient
import requests

from utils.bypass import create_tls_payload

TOKEN_PROGRAM_ID = 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'
METADATA_PROGRAM_ID = 'metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s'
SYSTEM_PROGRAM_ID = '11111111111111111111111111111111'
SYSTEM_RENT_PROGRAM = 'SysvarRent111111111111111111111111111111111'
SYSTEM_SLOT_HASHES = "SysvarS1otHashes111111111111111111111111111"
ASSOCIATED_TOKEN_ID = "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
WRAPPED_SOL = "So11111111111111111111111111111111111111112"

ME_PROGRAM = "CMZYPASGWeTz7RNGHaRJfCq2XQ5pYK6nDvVQxzkH51zb"

OPTS = TxOpts(skip_preflight=True, skip_confirmation=False, preflight_commitment=Commitment("confirmed"))
MINT_LEN = 82

class MagicEdenLaunchpad():
    
    def __init__(self, privkey: str, cmid: str, rpc: str, candy_machine_meta: Program):

        self.config_addres = candy_machine_meta.config
        self.wallet_auth = candy_machine_meta.wallet_authority
        self.order_info = candy_machine_meta.order_info
        self.notary = candy_machine_meta.notary
        
        self.cmid = cmid
        
        self.client = Client(rpc)
        self.async_client = AsyncClient(rpc)
        
        self.payer = Keypair.from_secret_key(b58decode(privkey))
        
    def _get_blockhash(self):
        
        res = self.client.get_recent_blockhash(Commitment('finalized'))
    
        return Blockhash(res['result']['value']['blockhash'])

    def get_transaction_hash(self, blockhash: Blockhash) -> Response:
                    
        headers = {
            'Host': 'wk-notary-prod.magiceden.io',
            'accept': '*/*',
            'access-control-request-method': 'POST',
            'access-control-request-headers': 'content-type',
            'origin': 'https://magiceden.io',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-fetch-dest': 'empty',
            'referer': 'https://magiceden.io/',
            'accept-language': 'es-ES,es;q=0.9',
        }
                    
        #session.options('https://wk-notary-prod.magiceden.io/mintix')
            
        headers = {
            'Host': 'wk-notary-prod.magiceden.io',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            'sec-ch-ua-platform': '"macOS"',
            'origin': 'https://magiceden.io',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://magiceden.io/',
            'accept-language': 'es-ES,es;q=0.9',
        }
                
        payload = {
            'params': {
                'walletLimitInfoBump': self.WALLET_LIMIT_ADDRESS[1],
                'inOrder': False,
                'blockhash': str(blockhash),
                'needsNotary': True,
            },
            'accounts': {
                'config': str(self.config_addres),
                'candyMachine': str(self.cmid),
                'launchStagesInfo': str(self.LAUNCH_STAGES_ADDRESS[0]),
                'candyMachineWalletAuthority': str(self.wallet_auth),
                'mintReceiver': str(self.payer.public_key),
                'payer': str(self.payer.public_key),
                'payTo': str(self.pay_to_ata),
                'payFrom': str(self.payer.public_key),
                'mint': str(self.mint_account.public_key),
                'tokenAta': str(self.associated_token_account),
                'metadata': str(self.METADATA_PROGRAM_ADDRESS[0]),
                'masterEdition': str(self.EDITION_PROGRAM_ADDRESS[0]),
                'walletLimitInfo': str(self.WALLET_LIMIT_ADDRESS[0]),
                'tokenMetadataProgram': METADATA_PROGRAM_ID,
                'tokenProgram': TOKEN_PROGRAM_ID,
                'systemProgram': SYSTEM_PROGRAM_ID,
                'rent': SYSTEM_RENT_PROGRAM,
                'orderInfo': str(self.order_info),
                'slotHashes': SYSTEM_SLOT_HASHES,
                'notary': str(self.notary),
                'associatedTokenProgram': ASSOCIATED_TOKEN_ID,
            },
        }
        
        payload = create_tls_payload(
            url="https://wk-notary-prod.magiceden.io/mintix",
            method="POST",
            headers=headers,
            params=payload
        )
                
        return requests.post('http://127.0.0.1:3000', json=payload).json()
            
        
    def find_transaction_accounts(self):        
        
        self.mint_account = Keypair.generate()

        self.associated_token_account = get_associated_token_address(self.payer.public_key, self.mint_account.public_key)
        self.pay_to_ata = get_associated_token_address(self.wallet_auth, PublicKey(WRAPPED_SOL))
        
        self.METADATA_PROGRAM_ADDRESS = PublicKey.find_program_address(
            
            seeds=[
                'metadata'.encode('utf-8'),
                bytes(PublicKey(METADATA_PROGRAM_ID)),
                bytes(self.mint_account.public_key)
            ],

            program_id= PublicKey(METADATA_PROGRAM_ID)
        )


        self.EDITION_PROGRAM_ADDRESS = PublicKey.find_program_address(
            
            seeds=[
                'metadata'.encode('utf-8'),
                bytes(PublicKey(METADATA_PROGRAM_ID)),
                bytes(self.mint_account.public_key),
                'edition'.encode('utf-8')
            ],
            
            program_id= PublicKey(METADATA_PROGRAM_ID)
        )


        self.WALLET_LIMIT_ADDRESS = PublicKey.find_program_address(
            seeds=[
                'wallet_limit'.encode('utf-8'),
                bytes(PublicKey(self.cmid)),
                bytes(self.payer.public_key)
            ],

            program_id= PublicKey(ME_PROGRAM)
        )


        self.LAUNCH_STAGES_ADDRESS = PublicKey.find_program_address(
            seeds=[
                'candy_machine'.encode('utf-8'),
                'launch_stages'.encode('utf-8'),
                bytes(PublicKey(self.cmid)),
            ],
            program_id=PublicKey(ME_PROGRAM)
        )


    def send_transaction(self, tx_data: str):

        try:
            
            tx = Transaction.deserialize(b58decode(tx_data)) 

            wallet = Wallet(self.payer)
            
            tx = wallet.sign_all_transactions([tx])[0]
            
            tx.sign_partial(*[self.mint_account])

            serialized = tx.serialize()

            tx_hash = self.client.send_raw_transaction(serialized, OPTS)["result"]

            return tx_hash
        
        except UnconfirmedTxError:
            
            return None
        
        except:
            
            return False
        
if __name__ == "__main__":

    MagicEdenLaunchpad()