from langchain_core.tools import tool
import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def eval_expr(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        return operators[type(node.op)](
            eval_expr(node.left),
            eval_expr(node.right),
        )

    raise TypeError(node)


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """

    try:
        node = ast.parse(expression, mode="eval").body
        result = eval_expr(node)
        return str(result)

    except Exception:
        return "Invalid mathematical expression."