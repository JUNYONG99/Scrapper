from flask import Flask, render_template, request, redirect, send_file
from extractors.remoteok import extract_jobs_remoteok
from extractors.weworkremotely import extract_jobs_weworkremotely
from file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = extract_jobs_remoteok(keyword) + extract_jobs_weworkremotely(
            keyword)
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")
