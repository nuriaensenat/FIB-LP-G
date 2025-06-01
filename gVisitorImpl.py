import numpy as np
from functools import reduce
from gVisitor import gVisitor


class GVisitorImpl(gVisitor):
    def __init__(self):
        super().__init__()
        self.verbs = {
            '+': np.add,
            '-': np.subtract,
            '*': np.multiply,
            '%': np.floor_divide,
            '|': lambda a, b: np.mod(b, a),
            '^': np.power,
            '>': np.greater,
            '<': np.less,
            '>=': np.greater_equal,
            '<=': np.less_equal,
            '=': np.equal,
            '<>': np.not_equal,
        }
        self.fold_verbs = {
            '+/': np.sum,
            '*/': np.prod,
            '-/': lambda x: np.subtract.reduce(x),
            '%/': lambda x: np.floor_divide.reduce(x),
            '|/': lambda x: reduce(lambda a, b: np.mod(b, a), x),
            '^/': lambda x: reduce(np.power, x),
            '>/': lambda x: reduce(np.greater, x),
            '</': lambda x: reduce(np.less, x),
            '>=/': lambda x: reduce(np.greater_equal, x),
            '<=/': lambda x: reduce(np.less_equal, x),
            '=/': lambda x: reduce(np.equal, x),
            '<>/': lambda x: reduce(np.not_equal, x),
        }
        self.adverbs = {
            ']': lambda x: x,
            '#': lambda x: len(np.array(x)),
            'i.': lambda x: np.arange(int(np.array(x).flatten()[0])),
            '+:': lambda x: np.add(x, x),
            '-:': lambda x: np.subtract(x, x),
            '*:': lambda x: np.multiply(x, x),
            '%:': lambda x: np.floor_divide(x, x),
            '|:': lambda x: np.mod(x, x)
        }
        self.operadors = {
            ',': lambda x, y: np.concatenate((x, y)),
            '#': lambda m, v: np.array(v)[np.array(m).astype(bool)],
            '{': lambda i, v: np.array(v)[np.array(i)],
            '@:': lambda f, g: (lambda x: f(g(x))),
        }
        self.variables = {}
        self.functions = {}

    def visitRoot(self, ctx):
        for instr in ctx.instruccions().instr():
            res = self.visit(instr)
            if res is not None and not callable(res):
                print(self.formatResult(res))

    def visitExprInstr(self, ctx):
        return self.visit(ctx.expr())

    def visitAssignInstr(self, ctx):
        var = ctx.VAR().getText()
        expr = self.visit(ctx.expr())
        if callable(expr):
            self.functions[var] = expr
        else:
            self.variables[var] = expr
        return None

    def visitOperacioOperadorExpr(self, ctx):
        right = self.visit(ctx.expr(1))
        left = self.visit(ctx.expr(0))
        op = ctx.OPERADOR().getText()
        if left is None or right is None:
            print("Error: un operand és none.")
            return None
        try:
            if op == '@:':
                if callable(left) and callable(right):
                    return lambda arg: left(right(arg))
                else:
                    return left(right)
            return self.operadors[op](left, right)
        except Exception as e:
            print(f"Error en '{op}': {e}.")
            return None
        
    def visitOperacioFlipExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        op = ctx.flip()
        right = self.visit(ctx.expr(1))
        
        if left is None:
            return right
        if right is None:
            return left
        
        if op.VERB():
            verb = op.VERB().getText()
            return self.verbs[verb](right, left)
        elif op.OPERADOR():
            operador = op.OPERADOR().getText()
            return self.operadors[operador](right, left)
        else:
            print(f"Error: {op} no reconegut.")
            return None   
        
    def visitOperacioFoldExpr(self, ctx):
        op = ctx.fold().getText()
        expr = self.visit(ctx.expr())
        if op not in self.fold_verbs:
            print(f"Error: {op} no reconegut.")
            return None
        if callable(expr):
            return lambda arg: self.fold_verbs[op](expr(arg))
        else:
            return self.fold_verbs[op](expr)
        
    def visitOperacioVerbExpr(self, ctx):
        right = self.visit(ctx.expr())
        left = self.visit(ctx.atom())
        op = ctx.VERB().getText()

        if left is None or right is None:
            print("Error: un operand és none.")
            return None
        if op not in self.verbs:
            print(f"Error: '{op}' no reconegut.")
            return None

        if callable(left) or callable(right):
            def composed(arg):
                left_val = left(arg) if callable(left) else left
                right_val = right(arg) if callable(right) else right
                return self.verbs[op](left_val, right_val)
            return composed

        left_array = np.array(left)
        right_array = np.array(right)

        if left_array.shape == () or right_array.shape == ():
            result = self.verbs[op](left_array, right_array)
        elif left_array.size == 1:
            result = self.verbs[op](left_array.item(), right_array)
        elif right_array.size == 1:
            result = self.verbs[op](left_array, right_array.item())
        elif left_array.shape == right_array.shape:
            result = self.verbs[op](left_array, right_array)
        else:
            print(f"Length error: {len(left_array)} i {len(right_array)}")
            return None
        return result

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())
    
    def visitOperacioAdverbExpr(self, ctx):
        expr = self.visit(ctx.expr())
        adverb = ctx.ADVERB().getText()
        if adverb in self.adverbs:
            result = self.adverbs[adverb](expr)
            return result
        else:
            print(f"Error: '{adverb}' no reconegut.")
            return None

    def visitAplicarFuncioExpr(self, ctx):
        func = self.visit(ctx.atom())
        arg = self.visit(ctx.expr())
        if callable(func):
            return func(arg)
        else:
            print(f"Error: {func} no reconeguda.")
            return None

    def visitOperacioUnariaOperadorExpr(self, ctx):
        op = ctx.OPERADOR().getText()
        expr = self.visit(ctx.expr())
        if op == ',':
            return expr
        if op == '#':
            if callable(expr):
                return lambda arg: self.adverbs[op](expr(arg))
            else:
                return self.adverbs[op](expr)
        elif op == '@:':
            return expr
        elif op == '+/':
            if callable(expr):
                return lambda arg: self.operadors[op](expr(arg))
            else:
                return self.operadors[op](expr)
        else:
            oper = self.operadors.get(op)
            if oper is not None:
                return lambda arg: oper(expr, arg)
            else:
                print(f"Error: '{op}' no reconegut.")
                return None

    def visitParentesisAtom(self, ctx):
        return self.visit(ctx.expr())

    def visitVector(self, ctx):
        ints = []
        for num in ctx.NUM():
            text = num.getText()
            neg = text.startswith('_')
            n = int(text.lstrip('_'))
            ints.append(-n if neg else n)
        return np.array(ints)

    def visitVarAtom(self, ctx):
        var_name = ctx.VAR().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        elif var_name in self.functions:
            return self.functions[var_name]
        else:
            print(f"Error: la variable '{var_name}' no està definida.")
            return None

    def visitAdverbAtom(self, ctx):
        adverb = ctx.ADVERB().getText()
        return self.adverbs.get(adverb)

    def visitVerbAtom(self, ctx):
        verb = ctx.VERB().getText()
        return self.verbs.get(verb)

    def visitNumAtom(self, ctx):
        text = ctx.NUM().getText()
        neg = text.startswith('_')
        n = int(text.lstrip('_'))
        return np.array([-n if neg else n])

    def formatResult(self, result):
        if isinstance(result, np.ndarray):
            elems = []
            for x in result.flatten():
                val = int(x)
                elems.append(f"_{abs(val)}" if val < 0 else str(val))
            return " ".join(elems)
        else:
            val = int(result)
            return f"_{abs(val)}" if val < 0 else str(val)
