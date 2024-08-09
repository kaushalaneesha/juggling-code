import csv

def extract_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

video_playback_logs = extract_csv('InterviewQuestions/Meta/ETL/video_playback.csv')
user_info = extract_csv('InterviewQuestions/Meta/ETL/user_info.csv')
content_info = extract_csv('InterviewQuestions/Meta/ETL/content_info.csv')

users = { user["user_id"] : user for user in user_info }
video_dict = {video["content_id"]: video for video in content_info}

# enrich playback logs with user and video information 

def enriched_logs(playback_logs):
    enriched_logs = []
    for log in video_playback_logs:
        user = users.get(log["user_id"])
        video = video_dict.get(log["video_id"])

        enriched_log = log
        enriched_log.update({
            "video_genre": video.get("genre", "Unknown"),
            "video_title": video.get("title", "Unknown"),
            "user_age": user.get("age", -1),
            "user_location": user.get("location", "Unknown")
        })
        enriched_logs.append(enriched_log)
    return enriched_logs

print(enriched_logs(video_playback_logs))

import sqlite3

def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS video_playback_logs AS (
                        video_id INT,
                        timestamp TEXT,
                        buffering_events INTEGER,
                        playback_quality TEXT,
                        user_id TEXT,
                        user_age TEXT,
                        user_location TEXT,
                        content_title TEXT,
                        content_genre TEXT
                    )
                   """)
    
    conn.commit()
    conn.close()

create_tables('data/netflix_logs.db')

def load_to_db(data, table_name, db_path):
    conn = sqlite3.connect()
    cursor = conn.cursor()

    for row in data:
        cursor.execute(f""" 
                       INSERT INTO {table_name} (
                       video_id, timestamp, buffering_events, playback_quality, 
            user_id, user_age, user_location, content_title, content_genre
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (row['video_id'], row['timestamp'], row['buffering_events'], row['playback_quality'],
            row['user_id'], row['user_age'], row['user_location'], row['content_title'], row['content_genre'])
                       )
        
    conn.commit()
    conn.close()

    