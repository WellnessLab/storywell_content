import json

def verify_story_pages(path):
    # type: (str) -> None
    with open(path) as infile:
        story_def = json.load(infile)
        index = 0
        num_of_errors = 0
        for page in story_def["contents"]:
            if page["id"] == index:
                print("Correct in page " + str(index) + ".")
            else:
                story_def["contents"][index]["id"] = index
                print("Error in page " + str(index) + ".")
                num_of_errors += 1
            index += 1
            
            if page["type"] is "REFLECTION":
                story_def["contents"][index]["nextContentId"] = index + 1
    
    print("Number of error(s): " + str(num_of_errors) + ".")
    
    if num_of_errors > 0:
        with open(path + ".rev.json", "w") as outfile:
            json.dump(story_def, outfile, indent=2, sort_keys=True)