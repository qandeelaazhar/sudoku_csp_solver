import copy

class sudoku_problem:
    def __init__(self, grid):
        self.vars = [(i, j) for i in range(9) for j in range(9)]
        
        self.dom = {}
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.dom[(i, j)] = {grid[i][j]}
                else:
                    self.dom[(i, j)] = set(range(1, 10))

        self.neigh = {}
        for i in range(9):
            for j in range(9):
                temp = set()

                # row + column
                for k in range(9):
                    if k != j:
                        temp.add((i, k))
                    if k != i:
                        temp.add((k, j))

                # box
                start_r = 3 * (i // 3)
                start_c = 3 * (j // 3)

                for r in range(3):
                    for c in range(3):
                        pos = (start_r + r, start_c + c)
                        if pos != (i, j):
                            temp.add(pos)

                self.neigh[(i, j)] = temp

        self.calls = 0
        self.fails = 0

def make_consistent(p, x, y):
    changed = False
    remove_vals = set()

    for val in p.dom[x]:
        ok = False
        for val2 in p.dom[y]:
            if val != val2:
                ok = True
                break
        if not ok:
            remove_vals.add(val)

    for val in remove_vals:
        p.dom[x].remove(val)
        changed = True

    return changed

def ac3_algo(p, q=None):
    if q is None:
        q = [(x, y) for x in p.vars for y in p.neigh[x]]

    while q:
        x, y = q.pop(0)

        if make_consistent(p, x, y):
            if not p.dom[x]:
                return False

            for z in p.neigh[x]:
                if z != y:
                    q.append((z, x))

    return True

def choose_var(assign, p):
    not_done = [v for v in p.vars if v not in assign]
    return min(not_done, key=lambda v: len(p.dom[v]))

def check_forward(p, var, val, assign):
    p.dom[var] = {val}
    q = [(n, var) for n in p.neigh[var] if n not in assign]
    return ac3_algo(p, q)

def solve_backtrack(assign, p):
    p.calls += 1

    if len(assign) == 81:
        return assign

    var = choose_var(assign, p)
    saved = copy.deepcopy(p.dom)

    for val in p.dom[var]:
        if check_forward(p, var, val, assign):
            assign[var] = val

            ans = solve_backtrack(assign, p)
            if ans:
                return ans

            del assign[var]

        p.dom = copy.deepcopy(saved)

    p.fails += 1
    return None

def solve_file(name):
    f = open(name, "r")
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    f.close()

    p = sudoku_problem(grid)

    ac3_algo(p)

    assign = {}
    for v in p.vars:
        if len(p.dom[v]) == 1:
            assign[v] = list(p.dom[v])[0]

    res = solve_backtrack(assign, p)

    ans_grid = [[0]*9 for _ in range(9)]

    if res:
        for (i, j), val in res.items():
            ans_grid[i][j] = val

    return ans_grid, p.calls, p.fails

if __name__ == "__main__":
    files = ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]

    for fname in files:
        print("Solving:", fname)

        try:
            sol, c, f = solve_file(fname)

            for row in sol:
                print("".join(str(x) for x in row))

            print("calls =", c, "| fails =", f)
            print()

        except:
            print("file not found\n")
