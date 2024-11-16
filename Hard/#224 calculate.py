class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        def not_evalable(st):
            symbols = {'+', '(', ')'}
            return any(sym in st for sym in symbols) or ('-' in st and st[0] != '-')

        curr_str = s

        while not_evalable(curr_str):
            # Try to update curr_str

            eval_open_paren_idx = -1
            eval_close_paren_idx = len(curr_str)

            stck = []
            paren_found = False

            for i, char in enumerate(curr_str):
                if char == '(':
                    stck.append(i)
                elif char == ')':
                    eval_open_paren_idx = stck.pop()
                    eval_close_paren_idx = i
                    paren_found = True
                    break

            # Eval curr_str's parenthesis
            if paren_found:
                eval_str = curr_str[eval_open_paren_idx + 1:eval_close_paren_idx]
            else:
                eval_str = curr_str

            nums = []

            sign = -1 if eval_str[0] == '-' else 1
            run_str = ''
            print(eval_str)
            for i, char in enumerate(eval_str):
                if char in {'-', '+'}:
                    if i == 0:
                        continue
                    else:
                        nums.append(int(run_str) * sign)
                        sign = -1 if char == '-' else 1
                        run_str = ''
                else:
                    run_str += char

            if run_str:
                nums.append(int(run_str) * sign)

            eval_res = reduce(lambda x, y: x + y, nums)

            if paren_found:
                curr_str = curr_str[:eval_open_paren_idx] + str(eval_res) + curr_str[
                                                                            eval_close_paren_idx + 1:]
            else:
                curr_str = str(eval_res)

            curr_str = curr_str.replace('--', '+')
            curr_str = curr_str.replace('+-', '-')

        return int(curr_str)
