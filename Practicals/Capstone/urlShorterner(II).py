from flask import Flask, request, redirect, render_template_string
import random
import string

app = Flask(__name__)

# In-memory storage for URL mappings.
# In a production app, you might use a database.
url_mapping = {}

def generate_short_id(num_chars=6):
    """Generate a random string of letters and digits of length num_chars."""
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for _ in range(num_chars))
        if short_id not in url_mapping:
            return short_id

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if not original_url:
            return "Please provide a valid URL.", 400
        
        # Generate a unique short ID and store the mapping.
        short_id = generate_short_id()
        url_mapping[short_id] = original_url
        
        # Create the short URL (assuming the app is hosted at request.host_url).
        short_url = request.host_url + short_id
        
        # Display the shortened URL.
        return render_template_string('''
            <h2>Your shortened URL is:</h2>
            <p><a href="{{ short_url }}">{{ short_url }}</a></p>
            <p><a href="/">Shorten another URL</a></p>
        ''', short_url=short_url)
    
    # HTML form for URL input.
    return '''
        <h1>Simple URL Shortener</h1>
        <form method="post">
            <label for="url">Enter URL to shorten:</label>
            <input type="text" name="url" id="url" required>
            <input type="submit" value="Shorten">
        </form>
    '''

@app.route('/<short_id>')
def redirect_to_url(short_id):
    # Look up the short_id in our mapping.
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return "Invalid or expired URL.", 404

if __name__ == '__main__':
    app.run(debug=True)
