"""
Main Server engine
"""
# Import Libraries
from web3 import Web3, HTTPProvider
from flask import Flask
from flask_restful import Resource, Api, reqparse


class GetTrustScore(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument("receiver", type=str)
        parser.add_argument("sender", type=str)
        args = parser.parse_args()
        sender = args["sender"]
        receiver = args["receiver"]

        try:
            print(f"Checking trust from {sender} to {receiver}")
            return {}
        except Exception as e:
            print(e)


class Server():
    """
    Class binding components together
    """

    def __init__(self):
        """
        Initialize the various components and bind them together
        """
        self.contract = Web3(HTTPProvider('https://ropsten.infura.io')).eth.contract(
            address='0x059745F23cc4D942BC1C890E7589f7d3A8a3406d',
            abi="[{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"address\"},{\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"reverseLookup\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"receiver\",\"type\":\"address\"},{\"name\":\"sender\",\"type\":\"address\"}],\"name\":\"isTrustedLink\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"address\"},{\"name\":\"\",\"type\":\"address\"}],\"name\":\"trustLinks\",\"outputs\":[{\"name\":\"trusted\",\"type\":\"bool\"},{\"name\":\"updated\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"receiver\",\"type\":\"address\"},{\"name\":\"trusted\",\"type\":\"bool\"}],\"name\":\"addTrustLink\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"
        )

        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(GetTrustScore, "/")

    def start(self):
        """
        Start the server
        """
        self.app.run(debug=True)

        return self

    def hasDirectTrustLink(self, receiver, sender):
        """
        Check if there is a direct trust link between a sender and a receiver
        Returns the answer: True/False, and the block number since the relationship was established
        """
        res = self.contract.functions.trustLinks(receiver, sender).call()
        return res[0], res[1]


server = Server()
server.start()
print(server.hasDirectTrustLink())
