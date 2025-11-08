class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << (ord(ch) - 49)  # '1' = 49
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_id(r, c)] |= bit

        ALL = (1 << 9) - 1

        def dfs():
            if not empties:
                return True

            best_i = -1
            best_mask = 0
            min_cnt = 10
            for i, (r, c) in enumerate(empties):
                mask = ALL ^ (rows[r] | cols[c] | boxes[box_id(r, c)])
                cnt = mask.bit_count()
                if cnt < min_cnt:
                    min_cnt = cnt
                    best_i = i
                    best_mask = mask
                    if cnt == 1:
                        break
            if min_cnt == 0:
                return False

            r, c = empties.pop(best_i)
            b = box_id(r, c)
            mask = best_mask

            while mask:
                bit = mask & -mask
                d = bit.bit_length()          # 1..9
                ch = chr(48 + d)              # '0'+d
                board[r][c] = ch
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if dfs():
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'
                mask ^= bit

            empties.insert(best_i, (r, c))
            return False

        dfs()