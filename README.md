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
- 📁 GraphQL:  GraphQL is a declarative data fetching endpoint and query language for APIs -->

### Tech Stack : Frontend

- 😍 React   : Act as the view layer, render the pretty data.
- 🚀 Apollo  : Production ready GraphQL client. -->
- 📈 [ReactChartJs2](https://github.com/jerairrest/react-chartjs-2): [_"Look at this graph"_ -nickelback](https://www.youtube.com/watch?v=sIlNIVXpIns)

### Phase 0 Start
- [x] Pull data from Job boards.
- [x] Create Hello World react page.
- [x] Create Alembic config and perform init migrations.
- [x] `INSERT` dummy job data into a Postgres DB.
- [X] Create the API endpoint for the frontend.
- [X] Hook GraphQL + Apollo + React together in basic Hello world.

### Phase 1 : K'Nex(t) (Second phase. Primarily focused on base usability of the frontend)

- [X] Create Menu section to React app.
- [X] Render graph in REACT.
- [X] Update REACT frontend to host colours for graphs in state.
- [X] Update database tables to reflect latest state.
- [X] Update backend to fix Indeed Changes.


### Phase 2 : Lego (Putting the building blocks of infrasture together)
- [X] Dockerise the frontend and backend.
- [X] Create plan for cloud provider of choice (not you Azure).
- [X] Configure DNS, add support for HTTPS, create instance, create docker container repo.
- [X] Fix small backend bug.
- [X] Deploy!

### Phase 3 : Enhance!
- [ ] Implement DB support for Cloud instances.
- [ ] Implement GraphQL Frontend Support.
- [ ] Update backend to handle inserts.
- [ ] Add search dropdown type.
- [ ] Add support for different locations, defaulted to DUBLIN, IRELAND right now.
- [ ] Add support for returning origin of data.
- [ ] Create ListView of companies and jobs posted.
- [ ] Improve backend performance to be less than 10 seconds per request.
- [ ] Implement loading icon when waiting for request to finish.
- [ ] Return failure error message on exceptions


## Architecture 

GCP Concept :
- Container Registry to hold docker containers.

-  Cloud DNS that holds the DNS for the site.

- DNS / SSL bought on namecheap then transfered to GCP.

-  Cloud compute instance running postgres (Save cost don't have an RDS for a real prod of course you would)
    - FLASK + GraphQL running as a container.
    - React Running as a container

- Why monorepo, honestly, for the sake of showing off this project, I thought it best to keep everything together. If this was a production system, I'd have split them up.