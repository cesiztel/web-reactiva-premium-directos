import json
from xml.etree.ElementTree import Element, SubElement, tostring

class Episode:
    def __init__(self, episode_id, title, description):
        self.episode_id = episode_id
        self.title = title
        self.description = description


class EpisodeSerializer:
    def serialize(self, episode, format):
        if format == 'JSON':
            episode_info = {
                'id': episode.episode_id,
                'title': episode.title,
                'description': episode.description
            }
            return json.dumps(episode_info)
        elif format == 'XML':
            episode_info = Element('episode', attrib={'id': episode.episode_id})
            title = SubElement(episode_info, 'title')
            title.text = episode.title
            description = SubElement(episode_info, 'description')
            description.text = episode.description
            return tostring(episode_info, encoding='unicode')
        else:
            raise ValueError(format)

if __name__ == "__main__":
    episode = Episode('4', 'Por si las voces vuelven', 'Angel Martin y Mai Menses charlan sin ningun ...')
    serializer = EpisodeSerializer()

    # JSON Episode info
    print(serializer.serialize(episode, 'JSON'))

    # XML Episode info
    print(serializer.serialize(episode, 'XML'))           