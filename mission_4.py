import json

class Episode:
    def __init__(self, episode_id, title, description):
        self.episode_id = episode_id
        self.title = title
        self.description = description

class EpisodeSerializer:
    def serialize(self, episode):
        episode_info = {
            'id': episode.episode_id,
            'title': episode.title,
            'description': episode.description
        }
        return json.dumps(episode_info)

class EpisodePublisher:
    def publish(self, episode_json):
        if is_json(episode_json):
            print("Publishing episode to the podcast service")
        else:
            raise ValueError("The given episode is not on JSON format")

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True

if __name__ == "__main__":
    episode = Episode('4', 'Por si las voces vuelven', 'Angel Martin y Mai Menses charlan sin ningun ...')

    episode_json = EpisodeSerializer().serialize(episode)
    print(episode_json)
    print(EpisodePublisher().publish(episode_json))