from flask import render_template, url_for, redirect, request
from app import app


# Main page
@app.route('/')
def main_page():
    return render_template("index.html")
