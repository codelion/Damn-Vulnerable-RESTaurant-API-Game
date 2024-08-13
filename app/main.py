from apis.router import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init import load_initial_data


def start_application():
    app = FastAPI(
        title="Damn Vulnerable RESTaurant",
        description="An intentionally vulnerable API service designed for learning and training purposes for ethical hackers, security engineers, and developers.",
        version="1.0.0",
        servers=[{"url": "http://localhost:8080", "description": "Local API server"}],
    )

    trusted_domains = ['http://localhost:8080', 'https://yourtrusteddomain.com']

    app.add_middleware(
        CORSMiddleware,
        allow_origins=trusted_domains,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    load_initial_data()
    return app


app = start_application()
