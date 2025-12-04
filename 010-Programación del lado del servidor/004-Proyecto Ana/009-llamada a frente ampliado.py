from flask import Flask, render_template, request, jsonify
import io
import contextlib
import traceback

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("frente ampliado.html")

# Use just /api as the endpoint (remove /execute)
@app.route("/api", methods=['POST'])
def api():
    try:
        data = request.get_json()
        if not data or 'code' not in data:
            return jsonify({
                'success': False,
                'output': None,
                'error': 'No code provided'
            }), 400
            
        code = data['code']
        
        # Safe execution environment
        safe_builtins = {
            'print': print,
            'range': range,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'list': list,
            'dict': dict,
            'tuple': tuple,
            'bool': bool,
            'sum': sum,
            'min': min,
            'max': max,
            'abs': abs,
            'round': round,
            'sorted': sorted,
            'enumerate': enumerate,
            'zip': zip,
        }
        
        buffer = io.StringIO()
        
        # Handle input() function
        input_data = data.get('input', '')
        input_lines = input_data.split('\n')
        input_index = [0]  # Use list to make it mutable in nested function
        
        def safe_input(prompt=""):
            if input_index[0] < len(input_lines):
                value = input_lines[input_index[0]]
                input_index[0] += 1
                return value
            return ""  # Return empty string if no more input
        
        with contextlib.redirect_stdout(buffer):
            # Create execution environment with safe builtins
            exec_globals = {
                '__builtins__': safe_builtins,
                'input': safe_input
            }
            exec(code, exec_globals, {})
        
        output = buffer.getvalue()
        return jsonify({
            'success': True,
            'output': output if output else "✅ Code executed successfully (no output)",
            'error': None
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'output': None,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
