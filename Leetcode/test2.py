# Enter your code here. Read input from STDIN. Print output to STDOUT
# import requests
import json
import re
from collections import deque


# Function to evaluate expressions
def evaluate_expression(expression, context):
    # Replace variables in the expression with their evaluated values
    for var in context:
        expression = expression.replace(f"${{{var}}}", str(context[var]))
    return expression
    # return eval(expression)

def topological_sort(expressions):
    indegree = {expr['name']: 0 for expr in expressions}
    graph = {expr['name']: [] for expr in expressions}
    print(indegree)
    print(graph)
    
    for expr in expressions:
        for dep in expr['dependencies']:
            graph[dep].append(expr['name'])
            indegree[expr['name']] += 1
    
    queue = deque([expr['name'] for expr in expressions if indegree[expr['name']] == 0])
    print(queue)
    sorted_expressions = []
    
    while queue:
        node = queue.popleft()
        for expr in expressions:
            if expr['name'] == node:
                sorted_expressions.append(expr)
                break
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_expressions
    
# Function to process each group
def process_group(group):
    context = {}
    results = []
    sorted_expressions = topological_sort(group['expressions'])

    for expr in sorted_expressions:
        name = expr['name']
        expression_type = expr['expressionType']
        expression = expr['expression']

        if expression_type == "DIRECT":
            result = expression
        elif expression_type == "RS_EXPRESSION":
            result = f"({evaluate_expression(expression, context)}) RS"
        elif expression_type == "DOLLAR_EXPRESSION":
            result = f"({evaluate_expression(expression, context)}) $"
        
        context[name] = result
        results.append(f"{name}:{result}")
    
    return results

# Main function to process the input
def process_input(data):
    output = []

    for group in data:
        group_name = group['groupName']
        expressions = group['expressions']
        if expressions:
            group_results = process_group(group)
            output.append(f"{group_name}:{':'.join(group_results)}")
        else:
            output.append(f"{group_name}:")

    return "\n".join(output)


data = [
  {
    'groupName': 'Group1',
    'expressions': [
      {
        'name': 'a',
        'expressionType': 'DIRECT',
        'expression': '10',
        'dependencies': [
          
        ]
      },
      {
        'name': 'c',
        'expressionType': 'DOLLAR_EXPRESSION',
        'expression': '10 + ${b}',
        'dependencies': [
          'b'
        ]
      },
      {
        'name': 'b',
        'expressionType': 'RS_EXPRESSION',
        'expression': '${a} + 10',
        'dependencies': [
          'a'
        ]
      }
    ]
  },
  {
    'groupName': 'Group2',
    'expressions': [
      {
        'name': 'a',
        'expressionType': 'DIRECT',
        'expression': '20',
        'dependencies': [
          
        ]
      },
      {
        'name': 'b',
        'expressionType': 'RS_EXPRESSION',
        'expression': '${a} + 10',
        'dependencies': [
          'a'
        ]
      },
      {
        'name': 'c',
        'expressionType': 'DOLLAR_EXPRESSION',
        'expression': '10 + ${b}',
        'dependencies': [
          'b'
        ]
      }
    ]
  }
]
# response = requests.get(input())
# data = json.loads(response.text)
output = process_input(data)
print(output)
