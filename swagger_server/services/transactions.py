from swagger_server.repositories.BasiqApiRepo import BasiqApiRepo
from swagger_server.DTOs.basiq_transaction import BasiqTransaction
from swagger_server.models.transaction_analyses import TransactionAnalyses


class Transactions:
    def calculate_average_spending(self, category=None):
        transactions = self._load_data_from_api(category)
        transactions = BasiqTransaction.to_dataframe(transactions)
        mean_transactions = transactions.groupby('category').mean().to_dict()['amount']
        return [TransactionAnalyses(category=k, average_spending=v) for k, v in mean_transactions.items()]

    @classmethod
    def _load_data_from_api(cls, category):
        api_repo = BasiqApiRepo()
        transactions = []
        next_id = None
        while True:
            basiq_transactions, next_id = api_repo.get_transactions(next_id)
            if category:
                if isinstance(category, str):
                    category = [category]
                basiq_transactions = list(filter(lambda x: x.subClass.code in category, basiq_transactions))
            transactions.extend(basiq_transactions)
            if not next_id:
                break
        return transactions
