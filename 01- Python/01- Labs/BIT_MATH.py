class BitMath:
    def __init__(self, num):
        self.num = num

    def bitwise_and(self, other):
        result_and = self.num & other
        return result_and

    def bitwise_or(self, other):
        result_or = self.num | other
        return result_or

    def bitwise_xor(self, other):
        result_xor = self.num ^ other
        return result_xor

    def bitwise_not(self):
        result_not = ~self.num
        return result_not

    def bitwise_left_shift(self, shift):
        result_left = self.num << shift
        return result_left

    def bitwise_right_shift(self, shift):
        result_right = self.num >> shift
        return result_right

    def set_bit(self, bit):
        mask = 1 << bit
        result_set = self.num | mask
        return result_set

    def clear_bit(self, bit):
        mask = ~(1 << bit)
        result_clear = self.num & mask
        return result_clear

    def toggle_bit(self, bit):
        mask = 1 << bit
        result_toggle = self.num ^ mask
        return result_toggle

# Example usage
num = 0b0101
bitmath = BitMath(num)

print("Set bit 1:", bin(bitmath.set_bit(1)))
print("Clear bit 2:", bin(bitmath.clear_bit(2)))
print("Toggle bit 0:", bin(bitmath.toggle_bit(0)))