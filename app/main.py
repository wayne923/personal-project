from fastapi import FastAPI
from utils.init_db import create_tables



app = FastAPI(
    debug=True
)

