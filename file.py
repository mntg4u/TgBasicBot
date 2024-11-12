from pyrogram import Client

api_id = "13666216"
api_hash = "f3a456b486290011638fb4b312f9be70"
session_string = "" 

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

# Start the client
app.start()
print(app.me)

# Stop the client
app.stop()
