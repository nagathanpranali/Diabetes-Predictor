from flask import *
from pickle import *

with open("diab.pkl", "rb") as f:
	model = load(f)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
	if request.method == "POST":
		age = float(request.form.get("age"))
		bmi = float(request.form.get("bmi"))
		fs = float(request.form.get("fs"))
		hba1c = float(request.form.get("hba1c"))
		d0 = [age, bmi, fs, hba1c]
		gender = int(request.form.get("gender"))
		if gender == 1:
			d1 = [1,0]
		else:
			d1 = [0,1]
		
		tension = int(request.form.get("tension"))
		if tension == 1:
			d2 = [1,0]
		else:
			d2 = [0,1]

		fmly = int(request.form.get("fmly"))
		if fmly == 1:
			d3 = [1,0]
		else:
			d3 = [0,1]

		d = [d0 + d1 + d2 + d3]
		res = model.predict(d)
		return render_template("home.html", msg=res[0])
	else:
		return render_template("home.html")

#if __name__ == "__main__":
	#app.run(debug=True, use_reloader=True)








