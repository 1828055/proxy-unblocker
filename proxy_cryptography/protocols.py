class UniqueProtocol:
    def __init__(self, key, binary_format):
        """ INIT class (note that key is a string) """
        self.key = key
        self.format = binary_format

    def encrypt(self, string):
        """ This function will encrypt a message according the key provided """
        output = ''
        for i in list(string):
            try:
                output = output + " " + str(self.key.find(i))
            except:
                output = output + i
        return output.encode(self.format)

    def decrypt(self, string):
        """ This function will decrypt a message according to the key provivded """
        output = ''
        for i in string.decode(self.format).split():
            if i != " ":
                try:
                    output = output + self.key[int(i)]
                except:
                    output = output + i
        return output
