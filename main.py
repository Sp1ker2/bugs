import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit")
async def submit_form(
    product_name: str = Form(...),
    quantity: int = Form(...),
    customer_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    delivery_address: str = Form(...),
    color: str = Form(...)
):
    return {
        "product_name": product_name,
        "quantity": quantity,
        "customer_name": customer_name,
        "email": email,
        "phone": phone,
        "delivery_address": delivery_address,
        "color": color
    }
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

