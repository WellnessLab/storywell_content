import json

def verify_story_pages(path):
    # type: (str) -> None
    with open(path) as infile:
        story_def = json.load(infile)
        index = 0
        for page in story_def["contents"]:
            if page["id"] == index:
                print("Corrent in page " + str(index) + ".")
            else:
                story_def["contents"][index]["id"] = index
                print("Error in page " + str(index) + ".")
            index += 1
            
            if page["type"] is "REFLECTION":
                story_def["contents"][index]["nextContentId"] = index + 1
            
    with open(path + ".rev.json", "w") as outfile:
        json.dump(story_def, outfile, indent=2, sort_keys=True)