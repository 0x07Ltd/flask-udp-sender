from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import IPAddress, NumberRange, InputRequired

from udp_sender import send

APP_NAME = "udp_sender"
app = Flask(APP_NAME)


class Form(Form):
    source_ip = StringField("Source IP", validators=(InputRequired(), IPAddress()))
    destination_ip = StringField("Destination IP", validators=(InputRequired(), IPAddress()))
    port = IntegerField("Destination Port", validators=(
        InputRequired(), NumberRange(min=1, max=65535)))
    count = IntegerField("Amount of packets to send", default=1, validators=(
        InputRequired(), NumberRange(
            min=1, max=500, message="Sending >500 packets at once is a bit OTT.")))
    payload = TextAreaField("Payload", validators=(InputRequired(),))


@app.route("/", methods=("GET", "POST"))
def index():
    form = Form()
    if form.validate_on_submit():
        send(
            dest_ip=form.destination_ip.data,
            port=form.port.data,
            src_ip=form.source_ip.data,
            payload=form.payload.data,
            count=form.count.data
        )
        return "Sent %d packet(s)." % form.count.data
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "debug"
    app.run(host="0.0.0.0", port=80)
