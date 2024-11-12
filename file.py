from pyrogram import Client

api_id = "13666216"
api_hash = "f3a456b486290011638fb4b312f9be70"
session_string = "BQDQh6gAxWdEbgLaPn69d_1-z31QO2hIZAoCPc6mnRkeQ-4EqKLNCSMH7DcXUyzcBEqKI8sE0xMcsmSEhEptJ3lcfhNHsnniO0pnd75EYfyYIcNtKaveAl0g62jknqVqrmYrwJZjuSrWJb8WzJ7fT7LvlJq_JRRp1hDasgFikNJshtz8MEtiWMyVc0nQr4iJ7bGbmkRThrG4NW70grXK38d54O7Dg8713Wc39zFLuZhrEX2VKThAUm-HqucFgSHxvmXk92Nc_W3mtpMHbfyV32p32-Fp4dKVk4YlU2VL6Fnihz3rEPcS8F9r4Z89RSLp1zLHZHrzwKRqCVvx2tWl9KhwMJWQ_QAAAAHUxLFoAA" 

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

# Start the client
app.start()
print(app.me)

# Stop the client
app.stop()
