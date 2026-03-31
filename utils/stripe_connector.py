from stripe import StripeClient
import os
from dotenv import load_dotenv

load_dotenv()

class StripeConnector():
    def __init__(self):

        self.client = StripeClient(os.getenv("STRIPE_SECRET_KEY"))


    def list_accounts(self, configurations:list=None, limit=10):
        """
        Returns a list of accounts associated with our application
        
        https://docs.stripe.com/api/v2/core/accounts/list

        args: 
            limit (int): The upper limit of the amount of accounts we are requesting.
            configurations (list): A filter for only accounts with the configurations specified. 
                                   (The "applied_configurations" item in the account object.)

        returns:
            accounts (list): A list of accounts associated with our application.
        """

        accounts = self.client.v2.core.accounts.list({
            "limit": limit,
            "applied_configurations": configurations,
        })

        return accounts
    
    def create_account(self, new_account:dict):
        """
        Creates an Account object used to represent a company, individual, or other
        entity that a user interacts with.

        https://docs.stripe.com/api/v2/core/accounts/create

        args: 
            new_account (dict): A dictionary object containing the parameters for an account object.

        returns:
            new_account (dict): A dictionary containing the new account info.
        """

        account = self.client.v2.core.accounts.create(new_account)
        return account
    
    def close_account(self, id:str, configurations:list=None):
        """
        Closes an account associated with our application

        https://docs.stripe.com/api/v2/core/accounts/close

        args: 
            id (str): The Id of the account to be closed.
            configurations (dict): A filter for only accounts with the configurations specified. 
                                   (The "applied_configurations" item in the account object.)

        returns:
            closed_account (account): Account object of the account to be closed.
        """

        closed_account = self.client.v2.core.accounts.close(
            id,
            {"applied_configurations": configurations},
        )

        return closed_account
    
    def get_account(self, id:str, include:list = None):
        """
        Retrieves an account associated with our application

        https://docs.stripe.com/api/v2/core/accounts/retrieve

        args: 
            id (str): The Id of the account to be closed.
            include (dict): Additional fields to include in the response.

        returns:
            closed_account (account): Account object of the account to be closed.
        """

        account = self.client.v2.core.accounts.retrieve(
            id,
            {"include": include}
        )

        return account
    
stripey = StripeConnector()

new_account = {
  "contact_email": "furever@example.com",
  "display_name": "Furever",
  "identity": {
    "country": "us",
    "entity_type": "company",
    "business_details": {"registered_name": "Furever"},
  },
  "configuration": {
    "customer": {"capabilities": {"automatic_indirect_tax": {"requested": True}}},
    "merchant": {"capabilities": {"card_payments": {"requested": True}}},
  },
  "defaults": {
    "responsibilities": {"fees_collector": "stripe", "losses_collector": "stripe"},
  },
  "dashboard": "full",
  "include": [
    "configuration.merchant",
    "configuration.customer",
    "identity",
    "defaults",
  ],
}

print(stripey.get_account(id="acct_1TH8UtJZDFeKm36S", include=["identity"]))

#print(stripey.list_accounts())
# closed_account = stripey.close_account(
#     'acct_1TH84vJZDFODGlLE', 
#     {"applied_configurations": [
#         "customer",
#         "merchant"
#     ]})

# print(closed_account)

