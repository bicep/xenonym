
import utils as utils
import constants as constants
from LogDestination import LogDestination
from MockBlockchain import MockBlockchain

class BlockchainDestination(LogDestination):
    def __init__(self):
        self.blockchain = None
        self.outfile = None
        self._is_opened = False

    def init(self, options):
        self.blockchain = MockBlockchain()

        self.outfile = open("/tmp/blockchain.txt", "a")
        self.outfile.write("initialized with {}\n".format(options))
        self.outfile.flush()

        return True

    def is_opened(self):
        return self._is_opened

    def open(self):
        self.outfile.write("opened\n")
        self.outfile.flush()
        self._is_opened = True
        return True

    def close(self):
        self.outfile.write("closed\n")
        self.outfile.flush()
        self._is_opened = False

    def deinit(self):
        self.outfile.write("deinit\n")
        self.outfile.flush()
        self.outfile.close()

    def send(self, msg):
        message_hash = utils.hash_function(str(msg))
        prev_hash = self.blockchain.get_latest_block_hash()
        if prev_hash is None:
            prev_hash = constants.GENESIS_HASH

        current_hash = utils.hash_together(message_hash, prev_hash)
        self.blockchain.add(current_hash)

        self.outfile.write("previous hash is " + prev_hash + "\n")
        self.outfile.write("current hash is " + current_hash + "\n")
        self.outfile.write("________________________\n")
        self.outfile.flush()

        return True