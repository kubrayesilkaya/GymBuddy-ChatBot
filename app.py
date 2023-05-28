import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

openai.api_key = "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"
model_engine = "text-curie-001" 

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']

    if not is_gym_related(user_input):
        return jsonify({'bot_response': "I can't answer that, I am a gym buddy."})

    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"You are a gym buddy. You are chatting with someone who wants to improve their fitness. Provide motivational and informative responses to help them achieve their fitness goals. {user_input}",
        max_tokens=600,
        n=2,
        stop=None,
        temperature=1,
    )
    bot_response = response.choices[0].text.strip()
    return jsonify({'bot_response': bot_response})

def is_gym_related(user_input):
    # Implement your logic here to determine if the user input is gym-related
    # You can use keyword matching, regular expressions, or any other approach

    # Example keyword matching
    gym_keywords = ['gym', 'fitness', 'exercise', 'workout', 'healthy', 'weightlifting',
    'cardio', 'strength training', 'resistance training', 'HIIT', 'yoga',
    'pilates', 'crossfit', 'bodybuilding', 'aerobics', 'zumba', 'calisthenics',
    'flexibility', 'endurance', 'muscle building', 'weight loss', 'nutrition',
    'healthy eating', 'diet', 'protein', 'carbohydrates', 'fats', 'vitamins',
    'minerals', 'hydration', 'meal planning', 'macros', 'micros', 'supplements',
    'rest and recovery', 'sleep', 'stress management', 'mental well-being',
    'motivation', 'goal setting', 'progress tracking', 'circuit training',
    'functional training', 'plyometrics', 'stretching', 'body composition',
    'mind-body connection', 'sports performance', 'core strength',
    'agility training', 'interval training', 'wellness', 'active lifestyle',
    'health and fitness', 'exercise equipment', 'fitness classes', 'self-care',
    'group training', 'personal training', 'exercise form', 'workout intensity',
    'bodyweight exercises', 'fitness goals', 'fitness tracking', 'recovery methods',
    'healthy habits', 'workout routine', 'strength gains', 'endurance training',
    'weightlifting technique', 'healthy recipes', 'fitness motivation',
    'exercise benefits', 'fitness community', 'fitness tips', 'exercise frequency',
    'exercise variations', 'healthy lifestyle' ]

    for keyword in gym_keywords:
        if keyword in user_input.lower():
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
