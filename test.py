from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai

# Configure the GenAI API
genai.configure(api_key="AIzaSyAy7ECkZQx5iGdY7udfLognbScz0LxYSqI")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize FastAPI app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return html_content

@app.post("/generate", response_class=HTMLResponse)
def generate(user_input: str = Form(...)):
    try:
        test_input = 'hello man how ar eyou doing bro i a fine thank you'
        response = model.generate_content(f" if '{test_input}' and '{user_input}' are similar texts reply me with yes else no")
        generated_text = response.text
    except Exception as e:
        generated_text = f"Error: {e}"

    # Read the index.html file and replace the placeholder with the generated response
    with open("static/index.html", "r") as file:
        html_content = file.read()

    # Replace placeholder {response} with the actual generated text
    html_content = html_content.replace("{response}", generated_text)

    return HTMLResponse(content=html_content)
