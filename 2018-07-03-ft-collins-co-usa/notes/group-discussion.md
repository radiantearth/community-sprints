## Overview

This session went deep in to some of the major decisions to be made for STAC, that spanned the API and the static version. 

No raw notes were taken, as the normal note taker was leading the discussion. But the topics and set up were given in the
[stac-group-discussion.pdf](stac-group-discussion.pdf). The major decisions / discussion are summarized here:

### Thumbnails

One of the weirdnesses of people working with the spec has been that thumbnails is in 'links', and not in 'assets', though
it feels like an assets. Everyone present thought they make a bit more sense in assets. The group tried to remember why
it was in links in the first place, and it seemed to go back to the fact that after the first sprint we walked out with just
'links' and then assets were added in by a small group later. 

Also discussed was whether thumbnails should be *required* at all. Some providers don't have thumbnails already made, so would
have to generate them, or just use a repeating thumbnail, which isn't that useful to a user. And though thumbnails can be
made from most data they're not always useful. So the conclusion was to not make them required, but to make them strongly
recommended. And that certain 'profiles' like earth observation / imagery might look to require them. Ideally tooling that
does validation also points out a 'warning' if thumbnails aren't there. Which will require custom validation tools instead
of just json schema plus whatever schema validator. But there weren't great arguments to make it all required.

The spec will be updated for thumbnails in assets, and not made required.

### Assets to Dict, Asset Definition.

One thing discussed in the [earth observation session](stac-eo.md) was that assets are tough to use an array. Much
more useful is to make them a 'dict' with the name as the key. This was then also used as a key in the asset definition. This
will be have more detail in the EO notes, but in general the group thought this was a good idea.

Spec will be udpated so 'assets' is a dict, with a new 'asset definition' file that is referenced from an item. With the 
definitions being keyed off the same names in the 'assets' dict. Matt Hanson to take this on. 

### Name of time fields

Kasey from Planet shared how he modified the time names, to 'observed' and 'duration'. With this you could have a negative
duration, like in the case of a mosaic, and thus communicate a bit more information about if the start or end time is more 
important. There was lots of discussion of the various use cases, and where the various time schemes work less well. In many
cases two or even three are desired, but three seemed like way to much to explain to users.

Where we got to was that in the core there should just be one time. Most assets can get to a single time, and we may even
be able to use implied granularity, like just say '2018' for a mosaic. But the different 'profiles' like EO can add in
more time fields if the want. It seemed like this would make the most sense to users. 

Also discussed was making them inclusive or exclusive. The spec right now doesn't say, so will take an improvement to specify it. 

Core spec will be updated to just one time. I believe Kasey to take on. 

### Relative vs Absolute links  

The core spec left it wide open for implementations to use relative and absolute links. And several implementations would 
mix them, even in the same Item. This was seen as less desirable. The group punted on making absolute recommendations / trying
to figure out an overall scheme of when to use one or the other. Though it is desired. 

The group did reach consensus on one thing though, which is that all 'self' links should be absolute. There were some 
implementations built that , but 
all felt those are pretty useless, since it doesn't actually tell you where it should go. 

So the next spec version will require the self link be absolute.

### Naming of profiles / content extensions

One consistent source of confusion in the group is that everyone uses different names to refer to additions to the core STAC
content model. Names include 'profiles' (which the author uses, like the earth observation profile), 'extensions', 'classes', etc. There was much discussion on a new name for these, as extension and profile are both overloaded, especially as we 
merge STAC with WFS. 

One idea that had legs was 'traits'. On trying it out more it did feel less than perfect, as the 'Earth Observation Trait' seems to imply just a single thing, not a set of metadata fields. Tried out 'traitsets' which seemed perhaps a bit better.
Tim encouraged the group to look in to the real definitions of these, as 'characteristics' are the manifestation of 'traits', 
so might be more appropriate. So didn't reach any real decision point on these.
