from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

##send it the entries from our get_entries fxn in the model
@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

##Picks up the form that the user sends in addentry
##here we parse the actual entry - assigning name & message
##use these to call add_entry and save the message to the database
@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    ##redirect the user back to the home page.
    return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html", entries=model.get_entries())

@app.route("/delete", methods=["GET", "POST"])
def delete():
    entryid = request.form["id"]
    print("ENTRYID = " + entryid)
    model.delete_entry(entryid)
    ##extract the id from the post data, pass that id from the delete entry fxn in the model
    return redirect("/admin")

if __name__=="__main__":
    model.init()
    app.run(debug=True)
