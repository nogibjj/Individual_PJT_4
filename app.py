from dotenv import load_dotenv
from flask import Flask, render_template, request
from openai import OpenAI
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def request_rep(user_input):
    prompt = f"{user_input}. Can you recommend me 3 foods specifying the restaurant chains?"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def parse_food(response):
    sentences = [x.split(" ") for x in response.split("\n")]
    output = []
    
    for sent in sentences:
        split_ind = None

        if len(sent) <= 1:
            continue
        else:
            for i in range(len(sent)):
                if sent[i] in (":", "-") or sent[i][-1] == ":":
                    split_ind = i

            sent_start = sent[0][:-1]

            try:
                sent_start = int(sent_start)
            except ValueError:
                split_ind = None

        if split_ind is not None:
            output.append(" ".join(sent[:split_ind]))

    return output

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        feeling = request.form.get("feeling", "")
        
        if not feeling:
            return render_template("home.html")
        else:
            GPT_response = request_rep(feeling)
            answer = parse_food(GPT_response)
            return render_template("response.html", gpt_response=answer)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
