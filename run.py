from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to FFmpeg Checker!"

# @app.route('/check-ffmpeg')
# def check_ffmpeg():
#     try:
#         # Run ffmpeg -version command
#         result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        
#         if result.returncode == 0:
#             return jsonify({
#                 "status": "success",
#                 "message": "FFmpeg is installed.",
#                 "version_info": result.stdout.split('\n')[0]
#             })
#         else:
#             return jsonify({
#                 "status": "error",
#                 "message": "FFmpeg returned a non-zero exit code.",
#                 "stderr": result.stderr
#             }), 500
#     except FileNotFoundError:
#         return jsonify({
#             "status": "error",
#             "message": "FFmpeg is not installed or not found in PATH."
#         }), 500
#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e)
#         }), 500
