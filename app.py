from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/community-hub')
def community_hub():
    return render_template('community_hub.html')

@app.route('/cultural-preservation')
def cultural_preservation():
    return render_template('cultural_preservation.html')

@app.route('/business-innovation')
def business_innovation():
    return render_template('business_innovation.html')

@app.route('/education-youth')
def education_youth():
    return render_template('education_youth.html')

@app.route('/advocacy-support')
def advocacy_support():
    return render_template('advocacy_support.html')

@app.route('/collaboration-tools')
def collaboration_tools():
    return render_template('collaboration_tools.html')

@app.route('/featured-community-voices')
def featured_community_voices():
    return render_template('featured_community_voices.html')

@app.route('/upcoming-events')
def upcoming_events():
    return render_template('upcoming_events.html')

@app.route('/join-us')
def join_us():
    return render_template('join_us.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
