from fastapi import FastAPI
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


def main():
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)


if __name__ == '__main__':
    main()