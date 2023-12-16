from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databaseManagement import orders_api, paperTrades_api, paperPosition_api, paperHolding_api
from priceDataframe import priceDataframe_api
from priceDatabase import priceDatabase_api

# initating app
app = FastAPI(title="Paper Brokerage & Data",redoc_url=None)
@app.get("/")
def read_root():
    return {"message": "Invsto - Paper Brokerage & Data "}

app.include_router(orders_api)
app.include_router(paperTrades_api)
app.include_router(paperPosition_api)
app.include_router(paperHolding_api)


app.include_router(priceDatabase_api)
app.include_router(priceDataframe_api)

# creating origin list
origins = ['*']

# config CORSM
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)