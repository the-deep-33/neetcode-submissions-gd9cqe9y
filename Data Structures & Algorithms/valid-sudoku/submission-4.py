class Solution:
    def isValidSudoku(self, board):

        valid = set()

        for i in range(9):
            brojac = 0
            valid.clear()
            for j in range(9):
                try:
                    valid.add(int(board[i][j]))
                    brojac += 1
                except:
                    continue
            if len(valid) != brojac:
                print(f"i = {i}, set = {valid}")
                print("NENENENENE")
                return False

        valid.clear()

        for i in range(9):
            brojac = 0
            valid.clear()
            for j in range(9):
                try:
                    valid.add(int(board[j][i]))
                    brojac += 1
                except:
                    continue
            if len(valid) != brojac:
                print("DADADADA")
                return False

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                brojac = 0
                valid.clear()

                for r in range(i, i+3):
                    for k in range(j, j+3):
                        try:
                            valid.add(int(board[r][k]))
                            brojac += 1
                        except:
                            continue

                if brojac != len(valid):
                    return False

        return True