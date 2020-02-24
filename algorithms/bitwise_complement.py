class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)[2:]
        binary = binary.replace("0", "T")
        binary = binary.replace("1", "0")
        binary = binary.replace("T", "1")
        
        return int(binary, 2)
