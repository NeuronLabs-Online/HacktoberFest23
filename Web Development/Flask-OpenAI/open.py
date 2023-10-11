from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"
model_engine = "text-davinci-003"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.9
        )
        response = completion.choices[0].text
        return render_template("home.html", response=response)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
