# Overview

The sprint runs for 3 days, november 5, 6 and 7th. The main iractivities will run 9-5 eastern time (be sure to check the 
[start time on worldclock](https://www.timeanddate.com/worldclock/meetingdetails.html?year=2019&month=11&day=5&hour=14&min=0&sec=0&p1=263&p2=136&p3=16&p4=224&p5=145) as we're in the midst of time changes, so it 
may be different than you expect). Each day we will have a kickoff in the morning
at 9, as one big group, including remotes. But most work through the sprint will be done in smaller groups, who will work
for a time and then come together to report out and get feedback from other groups. 1-2 sessions will be done using the
conferencing facilities, and smaller groups can also set up video calls if they want to discuss with remotes. 

Each day will also have a broad theme, though those mostly at the sprint to work on coding a particular implementation are 
encouraged to mostly just focus on their coding (while feeling welcome to pop in on other discussions). The broad focus on 
the first day will be the Features API Extensions, particularly the ones of joint interest to the STAC and OAFeat community. 
On day 2 many people will continue working on turning those extensions into reality, but those who work on the STAC spec 
will break out and tackle the STAC-specific topics on day two. The goal for day 3 will be testing and finalizing.
Implementations should try out other clients / servers to get to real-world interoperability. Ideally most of the new OAFeat
extensions will be exercised in implementations as well. And spec work should move into the writing stage - creating PR's,
and getting them reviewed and merged.

### Remote participation

We aspire to make the sprint as accessible as possible to remotes. At the onsite facility there are two rooms that should
have good built-in video conferencing facilities. We will post the information here when we get it. In the agenda below
any session in **bold** will be in the 'main' room and we be sure the video works. Small groups are encouraged to have
remote participation, either on gitter / github, or setting up video conferencing.  The second room at the venue will also
be available for one group to use its video capabilities - to be determined each day.

Dial info for the **main room** is: 

* Click to join (Google Chrome recommended): https://join.iqt.org/invited.sf?secret=ea8qp4mqKF5oaEeaE4zucA&id=424374534
* IQT video system or Cisco system: stac@join.iqt.org
* Phone: 703.248.3003, call ID: 424374534

If you are presenting, install the chrome plugin to be able to share your screen.

Dial info for the second room is:

- Click to join (Google Chrome recommended): https://join.iqt.org/invited.sf?secret=yPRXYo0R0iLu3Xb84fEnxg&id=156358612
- IQT Video system or Cisco system: stac2@join.iqt.org
- Phone: 703.248.3003, call ID: 156358612

The backup zoom meeting that we are using when the main system is flaky is https://planet.zoom.us/j/8171436529. When we
use this with the main screen, audio will still come from the cisco conference, and in-person people will be using the
cisco system to present on the big screen.

The main hub of activity will likely be the [features-stac-sprint](https://gitter.im/opengeospatial/features-stac-sprint) 
channel on gitter. If the dial in is not working then check there, as we may do a backup option.

Remote participants are encouraged to work during normal hours, and please introduce yourselves on the first day, and
share what you're working on each day. 


## Day 1 - Joint STAC API / OAFeat Extensions

The goal for day one is to reach consensus on the various desired OAFeat extensions, and hopefully to get work started on all
of the key ones. The end goal is to get super clear proposals that are in a state to become 'official', with at least 3
server implementations and one client implementation, to ensure that they are truly tested. So the goal of day 1 is to 
discuss enough with everyone on that day to get everyone aligned enough to spend the rest of the sprint turning the ideas 
into reality - clear pull requests of the proposals, and progress on implementations. 

|**Time**|**Title**|**Description**|
|--------|------------|-------------------------------|
|8:30 - 9  | Arrival    | In person arrivals / breakfast at 2107 Wilson Blvd, Arlington, VA. Go to the 7th floor and enter through the glass doors with the IQT logo. Remember to bring passport or a REAL ID drivers license every day|
|9 - 9:20  | **Welcome**  | Overview of event, logistics,  etc |
|9:20 - 10:45 | **Introductions**  | Brief introductions from everyone, so we all know who else is there and where they're coming from|
|10:45 | Break| |
|11:00 - 12:00 | Group work kickoffs | Break up into small groups to advance topics |
|11:15 - 12:00 | **Beginner Session #1** | Beginner session on STAC - overview of spec, main implementations, Q&A  |
|12:00 | Lunch | Break for lunch, continue chatting on topics |
|12:30 - 2:30  | Group work continues | Continue on work in small groups |
|12:30 - 1:30 | **Beginner Session #2** | Beginner session on [PySTAC](https://github.com/azavea/pystac) - how to create static catalogs |
|2:30 - 2:50  | **Full group check-in**  | Check on status, report on progress, resolve any burning questions with the full group, figure out if we need to shift small groups|
|3:00 - 5:15  | Continued group work | |
|5:30 | Bus leaves for Happy Hour | Location: Element 84 HQ, 210 North Lee Street, Suite 203, Alexandria, VA 22314 |
|6:00 | Happy Hour starts | Informal discussion, drinks, food |
|7:00 - 8:00 | Lightning Talks | Presentations from 8 people on various topics STAC and OAFeat topics. We likely won't stream these as they are late for many people, but will try to record and post asap for those who are remote.|
|9:00 | Bus goes back to 2107 Wilson Blvd | |


## Day 2

For Day 2 group work will continue, and everyone at the sprint primarily for implementations or OAFeat extensions will continue
work on their topics, with OAFeat work moving from alignment into creating the actual specifications, and implementations that 
can provide reference implementations of the spec. The STAC group focused on the core specification will break off from the
OAFeat sessions for some dedicated STAC time, both with the full group and in smaller groups on particular topics.

|**Time**|**Title**|**Description**|
|--------|------------|-------------------------------|
|8:30 - 9:00 | Arrival | In person arrivals / breakfast at 2107 Wilson Blvd, 7th floor -  remember to bring your ID |
|9:00 - 9:45 | **Open Lightning Talks** | Up to 7 presentations by people who didn't present at Happy Hour, including remotes |
|9:45 - 10:00 | **Small group kick-off** | Set stage and goals for small group work.
|10:00 - 12:30 | Small group work | Continue in groups from previous day, and STAC will be a bigger track|
|10:15 - 11:15 | **Beginner Session #3** | Beginner session on OGC API for Features -  overview of spec,  main implementations, Q&A |
|11:15 - 12:00 | **Beginner Session #4** | Beginner session on OAFeat software - hopefully [pygeoapi](https://pygeoapi.io/)|
|12:00 | Lunch ||
|12:30 - 6:00 | Group work continues, periodic check-ins|
|7:00 | GeoDC Meetup | Join [GeoDC Meet-up) at [Local 16](https://goo.gl/maps/zyLsizoyq8w8MjYt6) |

## Day 3

For Day 3 we want to focus on 'finishing' - get the key pieces over the line. The goal is to have the 5 or so most important
OAFeat extensions in shape where they are ready to be built out in implementations, and hopefully we've at least started on
implementations. STAC spec work should also be moving into creating PR's on the specification, and laying out the roadmap to
1.0. We also will likely convene the group interested in OACat (OGC API - Catalogues) to meet and map out a plan to use
the various extensions from OAFeat and create a specification.


|**Time**|**Title**|**Description**|
|--------|------------|-------------------------------|
|8:30 - 9:00 | Arrival | In person arrivals / breakfast at 2107 Wilson Blvd, 7th floor -  remember to bring your ID |
|9:00 - 9:15 | **Welcome and kick-off**| May extend this longer if we have good topics|
|9:15 - 12:00 | Group work continues, periodic check-ins|Push for 'completion', getting things wrapped up and ready to share and demo |
|12:00 | Lunch ||
|12:30 - 3:30 | Demos and wrap-up | Show off what you've done to the group! Everyone encouraged to share. And commit to next steps and actions to keep moving forward|
