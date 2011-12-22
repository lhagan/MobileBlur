# -*- coding: utf-8 -*-

from pprint import pprint

def view():
    page = int(request.vars["page"]) if request.vars.has_key("page") else 1
    requested_story_id = request.vars["story"]
    feed = newsblur.feed(request.vars["feed_id"], page=page)
    stories = feed["stories"]
    
    previous_story = None
    requested_story = None
    next_story = None
    for story in range(len(stories)):
        if stories[story]["id"] == requested_story_id:
            requested_story = stories[story]

            if story != len(stories)-1:
                stories_page = stories[story+1:]
            else:
                stories_page = newsblur.feed(request.vars["feed_id"], page=page+1)["stories"]
            filtered_stories = intelligence_filter(stories_page)
            if len(filtered_stories) > 0:
                previous_story = filtered_stories[0]

            if story != 0:
                stories_page = stories[:story]
            elif page > 1:
                stories_page = newsblur.feed(request.vars["feed_id"], page=page+1)["stories"]
            filtered_stories = intelligence_filter(stories_page)
            if len(filtered_stories) > 0:
                next_story = filtered_stories[-1]

            break

    return dict(
        previous_story=previous_story,
        requested_story=requested_story, 
        next_story=next_story,
        feed_id=feed["feed_id"],
        feed_title=request.vars["feed_title"],
    )

def mark_read():
    results = newsblur.mark_story_as_read(request.vars["story_id"], request.vars["feed_id"])
    redirect(URL("feeds", "view", args=[request.vars["feed_id"]]))
