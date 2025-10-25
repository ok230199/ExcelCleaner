from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "ファイルが選択されていません", 400

    df = pd.read_excel(file)

    df = df.replace('△', '-', regex=True)
    df = df.fillna('')

    output_buffer = io.BytesIO()
    df.to_excel(output_buffer, index=False, engine='openpyxl')
    output_buffer.seek(0)

    return send_file(
        output_buffer,
        as_attachment=True,
        download_name="cleaned_data.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == '__main__':
    app.run(debug=True)