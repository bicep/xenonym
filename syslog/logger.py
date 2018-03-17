

class LogDestination(object):

    def open(self):
        """Open a connection to the target service

        Should return False if opening fails"""
        return True

    def close(self):
        """Close the connection to the target service"""
        pass

    def is_opened(self):
        """Check if the connection to the target is able to receive messages"""
        return True

    def init(self, options):
        """This method is called at initialization time

        Should return false if initialization fails"""
        return True

    def deinit(self):
        """This method is called at deinitialization time"""
        pass

    def send(self, msg):
        """Send a message to the target service

        It should return True to indicate success, False will suspend the
        destination for a period specified by the time-reopen() option."""
        return True

class BlockchainDestination(LogDestination):
    def __init__(self):
        self.outfile = None
        self._is_opened = False

    def init(self, options):
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
        self.outfile.write("Name Value Pairs are:\n")

        for key,v in msg.items():
            self.outfile.write(str(key) + " = " + str(v) + "\n")
        self.outfile.write("________________________\n\n")
        self.outfile.flush()
        return True