Why finishing a personal project is hard

Often times you see people saying "I lost motivation" . I always think that's an interesting one. What is the cause of the loss of motivation?

- Did you finish learning what you wanted? 
- Was the scope badly defined? Did you _really_ create an minimal viable product, or smaller full product?

Life certainly gets in the way, It's _really_ hard to finish work, then go do _more_ of what you get paid to do on your free time. 

But there's a vast difference between a personal project and a work one, the major driving factor to me is the "team".
A lot of developers like to think they work better alone. But in reality, we depend on the skills and expertise of others all the time.
With this, I have come to the conclusion,  you really need to be the "mad hatter". Not in the sense of having tea parties and lots of riddles.
But rather in the sense of having a really broad skillset to finish a personal project. Take a moment, pause, and think what _do_ you need to finish one?


Of course, I expect everyone to get :

- Frontend developer : Make a pretty UI so people can interact with what you do.
- Backend developer :  Make the API / Monolith that will perform as much logic to keep the frontend dumb.


In reality though, we need a larger skillset than the above. For the frontend  we need  UX Designer skills, knowledge of their trade and using something like Sketch or Figma to create the wireframes. This really helps _how_ it's going to look.
Equally so, for the backend developer to do their work they need other helping hands. To develop anytihng you need to know what you're developing for, what system architect are you using? How are all of our components going to interact? Are we going monolithic, microservice, or even serverless? How will our cloud infrastructure work?
After that there's another hat peopel overlook, that of the DB Admin : Almost all the time, you will need to persist _some_ data is some sort of way. From the very start you you want to design the right schema. Otherwise you are going to struggle.





We're still missing a few hats in our collection though. With the hats we described above we can't deploy our application. There's no one to manage expectations, scope, and timelines. When things break due to deployments will they be caught
So let's fill out the missing hats. 

- SRE / DevOps : Use the CI/CD skills. Understanding how to implement the vision of the architect, because it's one thing to say but another to technically implemement.

- Network Engineer : You need to have at least a base understanding of TCP / UDP, security groups

- Technical Writer : Does your README have enough? Can anyone come along and help develop? Is it obvious what config are needed?

- Manager : A harsh truth is with no accountability, you will never finish any project. Defining scope is key, knowing how much to ship is vital.

- QA : You need to have tests of some sort. Integration or manual.

- Finace : Can you afford the cloud hosting? Is GCP or AWS cheaper? Or should we look at azure.

- Marketing: Can you promote your skills you learned with this project? How good are you at promoting yourself from this project?


So to finish any given personal project you need to have :
- Systems Architect
- DB Admin
- DevOps
- Network Engineer
- Backend developer
- Frontend developer
- QA
- Techincal Writer
- Manager
- Finance
- Marketing


["Yeah, mainly because I'm a terrible designer. I can never get my websites looking as good as I can almost envision in my head."](https://www.reddit.com/r/webdev/comments/3ugwz2/do_you_struggle_to_complete_personal_projects/cxex4n2/)
[The #1 thing that has helped me "finish" side projects is to release as often as possible](https://www.reddit.com/r/programming/comments/alyxfw/how_do_you_finish_big_side_projects/efjkscn/)


Of course, take all of the above with a bulk of salt, since each project is different. 
If you're doing a RUST CLI project, well of course then you don't need to deploy it to the cloud. But as a rule of thumb it's always important to evaluate what hats are important to wear.


So how to improve :


Planning and Research :
- Know your architecture first.
- Have your ERD ready at this point.
- Know what your willing to pay, and for how long.
- Know the exact scope of what you're trying to do. The very minimal amount you'd consider "OK".

Research :

- Do your due dilegence of research of approach. If you spend a few hours doing this that's great.
- If you're not fully content with something before you start do some training! Youtube has a lot, another place I really like is TeamTreehouse or Linux academy / cloud guru.


Creation :

- Write small components that do one thing well.
- As soon as you can, deploy that way you can fix it early. A stitch in time saves nine.