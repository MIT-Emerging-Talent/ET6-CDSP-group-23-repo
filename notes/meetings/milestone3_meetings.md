# Milestone 3 Meetings Summaries

## Weekly Check-In Summary - 05/07/2025📝

Time: 10:00–11:00 AM ET  
Attendees: Tibyan, Khusro, Saeed, AbdulQadr

### Key Points discussed

* Hamid will take care of scraping the remaining player stats for our dataset if
he’s available. If not, he should let us know ASAP so someone else can take over
and keep things moving.✅

* For our analysis strategy, we should decide when comparing average ratings,
do we do it per season or combine them across seasons?✅

* We need to plan for a mid-week meeting, preferably after scraping is done,
so we can start working on data analysis and task distribution efficiently.📅

* We need to schedule a meeting with Evan to discuss two important points:✅

1) For labeling our data, can we use average ratings from websites like
Transfermarkt or WhoScored? Or do we need to calculate them manually? That would
take a lot more time. Also, can we define our own threshold instead?
2) The reproducibility of our transfer dataset since AbdulQadr collected it
manually — how should we handle that?

* We must start putting internal deadlines for our tasks.📆

* Quick reminder to be more active on Slack! Not everything needs to wait for
a meeting, discussing on Slack can help us move faster and stay on track.⚠️

## Weekly Check-In Summary - 13/07/2025📝

Time: 10:00–11:00 AM ET  
Attendees: Tibyan, Khusro, Saeed, Hamid, AbdulQader

### Key-Points discussed

 Our main issue right now is that we have 4 different entries per player since
 we scraped stats across 4 different seasons.
Here’s the plan we agreed on to handle this:

### Tasks Division

* Task 1: Add Average Ratings

We’ll manually enter the average ratings for each player (4 different entries
per player)from Sofascore.com.
We have 5 transfer seasons, so AbdulQadr will combine the data from what he,
 Hamid, and Saeed scraped into 5 files.

Each of us will take 1 file and start entering the average ratings for the
corresponding rows.

Deadline: End of Tomorrow

Assignee: All

* Task 2: Clean and Merge the Data

Once ratings are entered:
Khusro will divide each file into pre-transfer and post-transfer datasets.

For each player, the 4 entries will be reduced to 2 (pre & post), then
 averaged into a single row for each period (1 pre-transfer entry and 1
 post-transfer entry).

Deadline: End of Tuesday

Assignee: Khusro

* Task 3: Data exploration

Data exploration for the cleaned version of the Player Stats dataset after
Khusro is done with the cleaning

Deadline: End of Wednesday

Assignee: Tibyan

* Task 4: Label the Dataset

We’ll label players as successful or not based on:
Average rating ≥ 6.7
Average minutes played ≥ 1000 minutes over 2 seasons.

Deadline: End of Wednesday

Assignee: Still not assigned to anyone

## Weekly Check-In Summary - 25/07/2025📝

Time: 10:30–11:30 AM ET  
Attendees: Tibyan, Khusro, Saeed, Hamid

### Key points discussed

* We are pretty much done for this milestone and should be able to wrap it up today.
* We will meet again on Saturday 10AM EST for our regular check-in schedule to
discuss the next steps and communication result milestone deliverables.

### Task Division

* @Saeed is going to review @Abdul Qader's work on prediction models and will add
visualizations to the non-technical report markdown file.

* @Tibyan is going to work the git tag, data exploration adjusting the main readme
of our repository.
* @Khusro is going to work on data_analysis milestones retrospective.
* @Hamid is going to work on the presentation and will share the draft tomorrow.
