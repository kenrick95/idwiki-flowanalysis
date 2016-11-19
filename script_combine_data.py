import json

list_topics = []
list_topic_questions = []
list_topic_question_titles = []
list_topic_question_creators = []
list_topic_question_timestamps = []

def parse_timestamp(timestamp):
    return timestamp[0:4], timestamp[4:6], timestamp[6:8], timestamp[8:10], timestamp[10:12], timestamp[12:]

def iso_timestamp(timestamp):
    parsed = parse_timestamp(timestamp)
    return "%s-%s-%sT%s:%s:%sZ" % parsed

def parse_data(file_name):
    global list_topics
    global list_topic_questions
    global list_topic_question_titles
    global list_topic_question_creators
    global list_topic_question_timestamps
    with open(file_name, "r") as f:
        data = json.load(f)
        list_topics.extend(data['roots'])
        for topic_id in data['roots']:
            topic_title_id = data['posts'][topic_id][0]
            list_topic_question_titles.append(data['revisions'][topic_title_id]['content']['content'])

            reply_id = data['revisions'][topic_title_id]['replies'][0]
            post_id = data['posts'][reply_id][0]
            list_topic_questions.append(data['revisions'][post_id]['content']['content'])
            list_topic_question_creators.append(data['revisions'][post_id]['creator']['name'])
            list_topic_question_timestamps.append(iso_timestamp(data['revisions'][post_id]['timestamp']))

parse_data("flow1.json")
parse_data("flow2.json")
parse_data("flow3.json")

dumping = {
    "list_topics": list_topics,
    "list_topic_question_titles": list_topic_question_titles,
    "list_topic_questions": list_topic_questions,
    "list_topic_question_creators": list_topic_question_creators,
    "list_topic_question_timestamps": list_topic_question_timestamps
}

with open("flow_combined.json", "w") as f:
    json.dump(dumping, f)