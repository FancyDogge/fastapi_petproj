from fastapi import FastAPI


app = FastAPI(
    title='Trading App'
)


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return user_id


