from flask import Flask
from helper import pets

# Create an instance of the Flask class
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    # Return HTML for the homepage
    return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href='/animals/dogs'>Dogs</a></li>
        <li><a href='/animals/cats'>Cats</a></li>
        <li><a href='/animals/rabbits'>Rabbits</a></li>
    </ul>
    '''

# Route for listing pets by type
@app.route('/animals/<pet_type>')
def animals(pet_type):
    # Start the HTML string with a heading
    html = f"<h1>List of {pet_type}</h1><ul>"
    # Loop through each pet in the specified type
    for index, pet in enumerate(pets[pet_type]):
        # Add each pet's name as a link to their profile
        html += f"<li><a href='/animals/{pet_type}/{index}'>{pet['name']}</a></li>"
    # Close the unordered list
    html += "</ul>"
    # Return the complete HTML
    return html

# Route for individual pet profiles
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    # Retrieve the pet's information using pet_type and pet_id
    pet = pets[pet_type][pet_id]
    # Return HTML with the pet's details
    return f'''
    <h1>{pet['name']}</h1>
    <img src="{pet['url']}" />
    <p>{pet['description']}</p>
    <ul>
        <li>Breed: {pet['breed']}</li>
        <li>Age: {pet['age']}</li>
    </ul>
    '''

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
