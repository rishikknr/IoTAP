from flask import Flask, request, jsonify
app=Flask(__name__)
@app.route(rule="/api", methods=["GET", "POST"])
def handle_request():
	if request.method=="GET":
		return "This is the get endpoint"
	if request.method=="POST":
		payload=request.get_json()
		cap_text=payload['text'].upper()
		response={'cap_text':cap_text}
		print(response)
		return jsonify(response)

if __name__=="__main__":
	app.run(host="0.0.0.0", debug=True)