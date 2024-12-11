import re

def analyze_code(lines):

    function_declaration_pattern = r'^def (\w+)\('
    function_call_pattern = r'(\w+)\('
    
    functions = {}
    for line_number, line in enumerate(lines, start=1):
        
        declaration_match = re.match(function_declaration_pattern, line)
        if declaration_match:
            function_name = declaration_match.group(1)
            if function_name not in functions:
                functions[function_name] = {"declaration": line_number, "calls": []}
        
        
        call_matches = re.findall(function_call_pattern, line)
        for call in call_matches:
            if call in functions and line_number != functions[call]["declaration"]:
                if line_number not in functions[call]["calls"]:
                    functions[call]["calls"].append(line_number)
    
    for function, info in functions.items():
        print(f"{function}: def in {info['declaration']}, calls in {info['calls']}")


file =  open("input_7_1.txt", 'r')

line = file.readline()
lines = []

while line != '':
    lines.append(line)
    line = file.readline()

analyze_code(lines)

file.close()