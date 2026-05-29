🐍 Snake Water Gun Game
Built this to revise Python basics and how Flask works as a backend.
Simple game — Snake beats Water, Water beats Gun, Gun beats Snake.

📁 Structure
SnakeWaterGun_Game/
├── game.py       # game logic
├── app.py        # flask server
└── index.html    # ui

▶️ Run
bashpip install flask
python app.py
# open http://localhost:5000

🔁 What I Revised
Python

Dictionaries — mapping user input ("s", "w", "g") to values and back
Functions — wrapping the game logic so Flask can call it cleanly
random.choice() — for computer's move
if/elif chains — win/lose/draw conditions

Flask

@app.route() — defining URL endpoints
request.get_json() — reading data sent from the browser
jsonify() — sending data back as JSON
send_from_directory() — serving the HTML file

JS (frontend side)

fetch() with POST — sending the player's choice to Flask
Reading the JSON response and updating the DOM


Made by @harsh2005-singh
