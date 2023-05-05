from flask import render_template,redirect,request,flash,session


from flask_app import app




@app.route('/')
def project():
    return render_template("Projects.html")

@app.route('/Dillan_samano/About_me')
def about():
    return render_template("about.html")

@app.route('/Dillan_samano/Contact')
def contact():
    return render_template("contact.html")


@app.route("/Dillan_samano/Email_Newsletter")
def news():
    return render_template("newsletter.html")


@app.route("/Dillan_samano/Email_Promotional")
def Promo():
    return render_template("promotional.html")


@app.route("/Dillan_samano/Email_Recipt")
def recipt():
    return render_template("receipts.html")



@app.route("/Dillan_samano/success")
def sucess():
    return render_template("success.html")