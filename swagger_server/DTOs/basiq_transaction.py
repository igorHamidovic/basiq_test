from dataclasses import dataclass
import pandas as pd
from decimal import Decimal
from pandas import DataFrame


@dataclass
class SubClass:
    title: str
    code: str


@dataclass
class Links:
    self: str
    account: str
    institution: str
    connection: str


@dataclass
class BasiqTransaction:
    type: str
    id: str
    status: str
    description: str
    amount: str
    account: str
    balance: str
    direction: str
    institution: str
    connection: str
    enrich: str
    transactionDate: str
    postDate: str
    subClass: SubClass
    links: Links

    @staticmethod
    def from_disc(response_item: dict):
        del response_item['class']
        return BasiqTransaction(**response_item)

    @staticmethod
    def to_dataframe(transactions_from_basiq_api) -> DataFrame:
        transactions = list(map(lambda x: {
            "category": x.subClass['code'] if x.subClass else None,
            "amount": Decimal(x.amount)
        }, transactions_from_basiq_api))
        return pd.DataFrame(transactions)
