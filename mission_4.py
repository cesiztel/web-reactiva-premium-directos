import json
from xml.etree.ElementTree import Element, SubElement, tostring

# Design pattern: Adapter

class Episode:
    def __init__(self, episode_id, title, description):
        self.episode_id = episode_id
        self.title = title
        self.description = description

class EposideXMLSerializer:
    def serialize(self, episode):
        episode_info = Element('episode', attrib={'id': episode.episode_id})
        title = SubElement(episode_info, 'title')
        title.text = episode.title
        description = SubElement(episode_info, 'description')
        description.text = episode.description
        return tostring(episode_info, encoding='unicode')

class EpisodeSerializer:
    def serialize(self, episode):
        episode_info = {
            'id': episode.episode_id,
            'title': episode.title,
            'description': episode.description
        }
        return json.dumps(episode_info)

class EposideSeralizerAdapter(EpisodeSerializer):
    def __init__(self, xml_serializer: EposideXMLSerializer):
        self.serializer = xml_serializer

    def serialize(self, episode):
        return self.serializer.serialize(episode)

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

class NewEpisodePublisher:
    def publish(self, episode_xml):
        if is_json(episode_xml) == False:
            print("Publishing episode to the (new) podcast service")
        else:
            raise ValueError("The given episode is not on XML format")


if __name__ == "__main__":
    episode = Episode('4', 'Por si las voces vuelven', 'Angel Martin y Mai Menses charlan sin ningun ...')

    episode_json = EpisodeSerializer().serialize(episode)
    print(episode_json)
    print(EpisodePublisher().publish(episode_json))

    adapter = EposideSeralizerAdapter(EposideXMLSerializer)
    print(NewEpisodePublisher().publish(adapter.serialize(episode)))
    