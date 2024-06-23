class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(curr_idx, curr_res, curr_sum, prev):
            if curr_idx >= len(num):
                if curr_sum == target:
                    res.append("".join(curr_res))
                return 
            else:
                # depth first and backtracking
                for i in range(curr_idx, len(num)):
                    # Since we want to consider digits of all length starting from this curr_ind
                    curr_str = num[curr_idx: i+1] 
                    curr_num = int(curr_str)
                    
                    if not curr_res:
                        # no operation for the first number 
                        dfs(i+1, [curr_str], curr_num, curr_num)
                    else:
                        dfs(i+1, curr_res + ["+"] + [curr_str], curr_sum + curr_num, curr_num)
                        dfs(i+1, curr_res + ["-"] + [curr_str], curr_sum - curr_num, -curr_num)
                        # undo the previous computation
                        dfs(i+1, curr_res + ["*"] + [curr_str], curr_sum - prev + curr_num * prev, curr_num * prev)
                    
                    if num[curr_idx] == '0':
                        # If current index starts with 0 we dont want to add other digits to it, so we break the loop
                        break
                    
                
        dfs(0, [], 0, 0)    
        return res