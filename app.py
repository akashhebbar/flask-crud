from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "abc" #adding secret key


@app.route("/")#root or home page for application
def index():
    return render_template("index.html")


@app.route("/add")
def add(): #add helps to insert the record to sqlite3 database
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST": #retrieve all the fields data from form
        try:
            aid = request.form["aid"]
            qid = request.form["qid"]
            state = request.form["state"]
            amount = request.form["amount"]
            reason = request.form["reason"]
            task = request.form["task"]
            with sqlite3.connect("taskrecord.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT into record(aid, qid, State, Amount, Reason, Task_Count) values (?,?,?,?,?,?)",
                    (aid, qid, state, amount, reason, task))

                con.commit()
                msg = "Records Are Added"
        except:
            con.rollback()
            msg = "Records Insertion Failed"
        finally:
            flash("Record Inserted")

            return redirect(url_for('views', msg=msg))
            con.close()


@app.route("/views")
def views():
    con = sqlite3.connect("taskrecord.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from record")
    rows = cur.fetchall()
    return render_template("views.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    aid = request.form["aid"]
    qid = request.form["qid"]
    with sqlite3.connect("taskrecord.db") as con:
        try:
            cur = con.cursor()

            cur.execute("delete from record where aid = ?", (aid,))
            cur.execute("delete from record where qid = ?", (qid,))
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


@app.route("/update")
def update():
    return render_template("update.html")
#@app.route("/updaterecord", methods=["POST"])
#def updaterecord():

