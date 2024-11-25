from flask import Flask,render_template,request
import RPi.GPIO as GPIO
app=Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
@app.route('/')
def index():
	gpio_status=GPIO.input(24)
	return render_template("index.html", statuses="OFF" if gpio_status else "ON")
@app.route('/toggle',methods=["POST"])
def toggle():
	gpio_status=GPIO.input(24)
	GPIO.output(24,not gpio_status)
	return render_template("index.html", statuses="OFF" if gpio_status else "ON")
if __name__=="__main__":
	app.run(host="0.0.0.0",debug=True)
