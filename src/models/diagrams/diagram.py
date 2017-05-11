import uuid
import src.models.users.errors as UserErrors
import src.models.users.constants as UserConstants

from src.common.database import Database
from src.common.utils import Utils


class Transaction(object):
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        # self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Transaction {}>".format(self.email)


    def json(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "message": self.message
        }

