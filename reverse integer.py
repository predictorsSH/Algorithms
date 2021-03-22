class Solution:
    def reverse(self, x: int) -> int:
        input_num_str = str(x)
        input_num_li = list(input_num_str)

        if input_num_li[0]=='-':
            new_num = input_num_li[1:]
            new_num = reversed(new_num)
            new_num = ''.join(new_num)
            new_num = '-'+new_num
            new_num = int(new_num)

        else:
            new_num = reversed(input_num_li)
            new_num = ''.join(new_num)
            new_num = int(new_num)

        if new_num > 2 ** 31 or new_num < (-2) ** 31:
            return 0
        else:
            return new_num



