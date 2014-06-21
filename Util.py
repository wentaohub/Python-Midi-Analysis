class Util:
    #returns a hex value for use in fromhex
    @staticmethod
    def paddedHex(sourceNum):
        returnVal = hex(sourceNum)[2:]
        if (len(returnVal) % 2) != 0:
            returnVal = '0' + returnVal
        return returnVal

    #returns a bytes objecte shifted left by numBits bits
    @staticmethod
    def lshiftBytes(sourceBytes, numBits):
        return bytes.fromhex(Util.paddedHex(
            int.from_bytes(sourceBytes, "big") << numBits))

    #returns a byte array shifted left by numBits bits
    @staticmethod
    def lshiftByteArray(sourceByteArray, numBits):
        return bytearray.fromhex(Util.paddedHex(
            int.from_bytes(sourceByteArray, "big") << numBits))

    #takes a bytes object formatted in variable length and
    #returns the int value represented
    @staticmethod
    def varLenVal(varLenBytes):
        if len(varLenBytes) == 0:
            return 0
        varLenArray = bytearray(varLenBytes)
        returnValBytes = bytearray.fromhex(
            Util.paddedHex(varLenArray[0] & b'\x7f'[0]))
        for i in range(len(varLenBytes) - 1):
            nextByte = varLenArray[i+1] & b'\x7f'[0]
            returnValBytes = Util.lshiftByteArray(returnValBytes, 7)
            returnValBytes[0] = returnValBytes[0] | nextByte
        print(returnValBytes)
        return int.from_bytes(returnValBytes, "big")