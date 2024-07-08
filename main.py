
from fastapi import FastAPI 


from api import users,courses,sections

from db.db_setup import engine
from db.models import user,course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Fast API LMS",
    description="LMS for managing student and courses ",
    contact={
        "name":"Vidhan Prajapati",
        "email":"vidhanprajapati27@gmail.com"
    },
)

@app.get("/")
async def health_check():
    return "It is running fine"



app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)

# Also add flake 8 and black for formatting