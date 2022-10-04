import json
from xml.etree.ElementTree import Element, SubElement, tostring

# SRP - Single responsibility principle
# OCP = Open close principle
# switch / if el - branching
# Metodo crecera
# dificil de mantener
# Refactoring: Extract method
# Step down rule
# Design pattern: Abstract Factory Method

class Episode:
    def __init__(self, episode_id, title, description):
        self.episode_id = episode_id
        self.title = title
        self.description = description


class EpisodeSerializer:
    def serialize(self, episode, format):
        serializer = self._get_serializer(format)
        return serializer(episode)
    
    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_json
        elif format == 'XML':
            return self._serialize_xml
        else:
            raise ValueError(format)

    def _serialize_json(self, episode):
        episode_info = {
            'id': episode.episode_id,
            'title': episode.title,
            'description': episode.description
        }
        return json.dumps(episode_info)

    def _serialize_xml(self, episode):
        episode_info = Element('episode', attrib={'id': episode.episode_id})
        title = SubElement(episode_info, 'title')
        title.text = episode.title
        description = SubElement(episode_info, 'description')
        description.text = episode.description
        return tostring(episode_info, encoding='unicode')

if __name__ == "__main__":
    episode = Episode('4', 'Por si las voces vuelven', 'Angel Martin y Mai Menses charlan sin ningun ...')
    serializer = EpisodeSerializer()

    # JSON Episode info
    print(serializer.serialize(episode, 'JSON'))

    # XML Episode info
    print(serializer.serialize(episode, 'XML'))           