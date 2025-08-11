from flask import Flask, render_template
from flask import Flask, render_template, request
from scraper import fetch_filtered_jobs
from flask import Flask, send_file
import pandas as pd
import os
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    keyword = request.form.get("keyword").lower()
    jobs = fetch_filtered_jobs(keyword)

    if jobs:
        import pandas as pd
        from datetime import datetime

        df = pd.DataFrame(jobs)
        filename = f"jobs_{keyword}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        df.to_csv(f"static/{filename}", index=False)
        return render_template("results.html", jobs=jobs, keyword=keyword)
    else:
        return(f"There are no jobs for this keyword :(")

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('path_to_your_files', filename) 
    return send_file(file_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
   app.run()