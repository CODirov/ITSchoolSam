from flask import render_template, request

from config import app
from msg_send import send_msg

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/our-courses/")
def courses_page():
    return render_template("our-courses-3-uzb.html")

@app.route("/our-courses/frontend/")
def frontend_course_page():
    return render_template("frontend-uzb.html")

@app.route("/our-courses/backend/")
def backend_course_page():
    return render_template("backend-uzb.html")

@app.route("/our-courses/graphic-design/")
def graphic_design_page():
    return render_template("graphic-uzb.html")

@app.route("/our-courses/foundation/")
def foundation_page():
    return render_template("foundation-uzb.html")

@app.route("/our-courses/math/")
def math_page():
    return render_template("math-uzb.html")

@app.route("/our-courses/english/")
def english_page():
    return render_template("english-uzb.html")

@app.route("/our-courses/russian/")
def russian_page():
    return render_template("russian-uzb.html")

@app.route("/our-courses/menthal/")
def menthal_page():
    return render_template("menthal-uzb.html")

@app.route("/about/")
def about_page():
    return render_template("about-us-uzb.html")

@app.route("/teachers/")
def teachers_page():
    return render_template("teachers-uzb.html")

@app.route("/teacher-details/")
def teacher_details_page():
    return render_template("teacher-details-uzb.html")

@app.route("/gallery/")
def gallery_page():
    return render_template("gallery-uzb.html")

@app.route("/contact/", methods=['GET', 'POST'])
def contact_page():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        msg = request.form['message']
        email_form = f"""Salom mening ismim {name}, pochta:{email}, telefon raqamim {phone}, meni {subject} qiziqtirmoqda.
        Izoh: {msg}"""
        # print(email_form)
        send_msg(email_form)
    return render_template("contact-uzb.html")


if __name__=="__main__":
    app.run()