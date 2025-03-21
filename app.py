from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__, template_folder=os.getcwd())  # Look for HTML files in the current directory
app.secret_key = "ffjh vofa uqym cvpd"  # Change this to a strong secret key

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
LOGIN_EMAIL = "prasadyammi2@gmail.com"
LOGIN_PASSWORD = "ffjh vofa uqym cvpd"  # Use an app password or SMTP password

# Routes for HTML Pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/features.html")
def features():
    return render_template("features.html")

@app.route("/pricing.html")
def pricing():
    return render_template("pricing.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route('/problem.html')
def problem():
    return render_template("problem.html")

# Contact Form Handler
@app.route("/send_email", methods=["POST"])
def send_email():
    try:
        name = request.form["name"]
        sender_email = request.form["email"]
        message = request.form["message"]

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = LOGIN_EMAIL
        msg["Subject"] = f"New Contact Form Submission from {name}"

        # Email Body
        body = f"""
        Name: {name}
        Email: {sender_email}

        Message:
        {message}
        """
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP and Send Email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(LOGIN_EMAIL, LOGIN_PASSWORD)
            server.sendmail(sender_email, LOGIN_EMAIL, msg.as_string())

        flash("Message sent successfully! ✅", "success")
        return redirect("/contact.html")

    except Exception as e:
        print(f"Error: {e}")
        flash("Something went wrong. Please try again.", "danger")
        return redirect("/contact.html")

if __name__ == "__main__":
    app.run(debug=True)
