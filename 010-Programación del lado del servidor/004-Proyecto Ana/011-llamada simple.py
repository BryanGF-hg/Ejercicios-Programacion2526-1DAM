from flask import Flask, render_template, request, jsonify
import io
import contextlib
import traceback

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("nuevo frente ampliado.html")

@app.route("/api", methods=['POST'])
def api():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code:
            return jsonify({'success': False, 'error': 'No code'}), 400
        
        # Entorno seguro básico
        safe_env = {
            'print': print,
            'range': range,
            'len': len,
            'str': str,
            'int': int,
            'float': float,
            'list': list,
            'dict': dict,
            'sum': sum,
            'min': min,
            'max': max
        }
        
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(code, {'__builtins__': safe_env}, {})
        
        output = buffer.getvalue()
        return jsonify({
            'success': True,
            'output': output or "✅ Ejecutado (sin salida)"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
