import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

openai.api_key = "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"
model_engine = "text-curie-001" 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"You are a gym buddy. You are chatting with someone who wants to improve their fitness. Provide motivational and informative responses to help them achieve their fitness goals. {user_input}",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    bot_response = response.choices[0].text.strip()
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
