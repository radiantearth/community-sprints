## Overview

This folder is provided as an area for work and experimentation during the sprint, and it also attempts to divide people
into small groups so we can make parallel progress during the sprint. Each group section states the goals for the sprint,
and attempts to assign people to groups based on their submitted preferences. People can switch groups, but we've found
that groups make the most progress when they are five people or less. The goal is to actually write things down and
create concrete proposals, instead of just spending hours discussing and aligning with no artifacts. So if your group gets
to 6 people or more then just split it in half, and either divide the topics up or let each group settle on an approach
and document + propose it. 

This repo can be used as a place to document the proposals if desired, or that work can be done in different repos - its
up to the group. Just be sure to link from this folder to where the relevant work is happening.

##  Groups

Note that some people are listed in multiple groups, as they expressed diverse interests. All are welcome to shift groups,
this is just meant to be a starting point.

[Implementation](implementation.md) - This is the group that is doing the most true 'sprinting' - working on software or
standing up a static catalog or service. This is the largest group, since we're not dividing it based on people's
individual projects, as many people are working independently on their 'thing'. The goal is to provide a space where
people can ask questions and test out their implementation against others to ensure it's working right. (take notes)

*Jerome, Yves, Chris B, Michael H, Andrew Y, Angelos, Brian, Mary, Joseph, Rene, Aimee, Rob, Patrick, Kirk, Sam, Hyu, Trevor* 

[Testing] - This group will help ensure that our specifications have accessible test engines that accurately represent
the current state of the spec, building on existing tools or trying new approaches. 

*Alexandra, James, Dave, Andrew Y, Chuck, Fabian*

[Beginner] - There are 2 planned sessions each on days one and two, to help introduce new people to the OAFeat and STAC 
communities. Things are actually slightly 'flipped', where day 1 is STAC focused and day 2 is OAFeat focused. This is because on 
day 1 the OAFeat people will all be occupied, and similarly day 2 will occupy STAC people. These are just a couple hours
each day, and hopefully participants get up to speed enough to join implementation or outreach groups.

*Alessandro, Christina, Oscar, Fabian, Ryan, Brian, Andrew Y, Trevor, Marc, Dave* 
**Note** - We forgot to ask for interest in the beginner track for in-person attendees, so feel free to join / add your name.

[Outreach] - This group is a great way for new community members to contribute, as the tasks don't require tons of background. 
The hope is that after learning in the beginners sessions people can take the knowledge and help explain the specs to others, 
brainstorming on new ways to share the information. 

*Chris H, Quinn, Jim, Jacques, Oscar, Ryan*

#### Spec Groups

[Filter] - Filter focuses on a key part of the Query, how to request a subset of the overall catalog, with advanced
logical, spatial, temporal and numeric comparisons.  This group will start a bit large, but is encouraged to quickly
break out to work on specific proposals, likely around CQL, a JSON one (STAC or CQL JSON or a new proposal), and GraphQL or
other ideas. 

*Janne, Peter, Josh, Andrea, Even, Phil, Sean, Tim S, Andrew L*


[Query] - Query includes a number of topics, mostly related to the mechanics of searching and getting responses. This group
includes those who are primarily interested in Query from a OGC API - Catalogue perspective, as it is a key part of that
specification. But they should focus on the reusable Query component and their requirements for it, not the whole Catalog
spec.  It is still a big group even with ~5 people focused on the Catalogue perspective, so it is strongly encouraged to
divide up the various topics (paging, sorting, properties/fields, cross-collection, aggregations, facets).

*Jeff, Matt, Alexander, Tim R, Matthias, Kevin, Andrew T Alireza, Michael S, Angelos, Mary, Joseph, Tom K*


[Transaction] - The transaction extension work will likely have more people join or at least checking in after progress on
the core filter & query. But it would be great for a core group to start making progress turning it into an OAFeat extension
and standing up the reference implementations of it, as well as discussing additions like etags, versioning and bulk transactions.	

*Alessandro, Tom I, Scott, Oscar, Chuck, Peter*

[Other OGC API - Features extensions] - No groups set to start, but for people looking to work in parallel or shift to it 
after wrapping other things up there are key topics like the OAFeat equivalent to DescribeFeatureType at the top of the list.
Plus projections, which was the first extension, but making sure it is in good shape. And more interesting future topics like
Subscriptions, static features and GRPC/protobuf. We won't try to set groups on these the first day, but they may evolve.

[STAC core] - Core STAC topics will start the second day, with some  sessions with the whole STAC group, and some breakouts. 
Participants will mostly be those who come to the bi-weekly STAC calls, but if you've got experience implementing the STAC
spec in some way you are also welcome to come and help work on the core.

*Matt, Matthias, James, Tim R, Michael S, Chris H, Sean, Alireza, Alexandra

