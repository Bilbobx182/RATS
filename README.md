# RATS
(Reverse) . Applicant . Tracking . Systems

## Introduction
Recruiters use Applicant tracking systems(ATS), to filter their applicants before even looking.
- _What if I had the capacity to see what they see?_
- _What if I could predict what the ATS would predict?_
 
Then it would be a bit more of an even playing field. No longer of a game of _cat and mouse_. _RATS_ solves that.

Armed with data, only then can you make decisions that pierce through the fog of the future.
This would empower people to make projects with technologies that are rising in demand.
No longer of a game of _cat and mouse_. _RATS_ solves that.


## Objectives 
“A goal without a plan is just a wish.”Antoine de Saint-Exupéry_.
So here are the project milestones.

### Tech Stack :  Backend

- 📦 Docker: Used as the container tool for the services.
- 💾 Postgres: Acts as the database, store the relational data.
- ⚗️ Alembic: Used as a database migration tool to link versions.
- 🗺️ SQLAlchemy: Map the database tables in objects. (ORM)
- 🍶 Flask Used to serve the GraphQL.
- 📁 GraphQL:  GraphQL is a declarative data fetching endpoint and query language for APIs

### Tech Stack : Frontend

- 😍 React   : Act as the view layer, render the pretty data.
- 🚀 Apollo  : Production ready GraphQL client.

### Phase 0 Start
- [x] Pull data from Job boards.
- [x] Create Hello World react page.
- [x] Create Alembic config and perform init migrations.
- [x] `INSERT` dummy job data into a Postgres DB.
- [X] Create the API endpoint for the frontend.
- [ ] Hook GraphQL + Apollo + React together in basic Hello world.

### Phase 1 : Leggo (Putting the building blocks together)
- [ ] Create cron to insert data
- [ ] Dockerise the frontend and backend.

- [ ] Investigate GCP (since I know how to do this in AWS best to broaden mysef)
- [ ] Create plan for cloud provider of choice (not you Azure).
- [ ] Create infra for project.
- [ ] Deploy!

