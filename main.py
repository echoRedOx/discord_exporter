import csv
import json
from dataclasses import dataclass
import yaml
import os
import sys


@dataclass
class Guild:
    def __init__(self, data):
        self.guild_data: dict = data.get('guild', {})
        self.name: str = self.guild_data.get('name')
        self.id: str = self.guild_data.get('id')


@dataclass
class Channel:
    def __init__(self, data):
        self.channel_data: dict = data.get('channel', {})
        self.name: str = self.channel_data.get('name')
        self.id: str = self.channel_data.get('id')
        self.topic: str = self.channel_data.get('topic', 'No topic')
        self.export_time: str = data.get('exportedAt')


@dataclass
class Conversation:
    def __init__(self, data: json):
        self.guild = Guild(data)
        self.channel = Channel(data)
        self.messages = []

        self.add_messages(data)

    def add_messages(self, data: json):
        msgs = data.get('messages', [])
        for msg in msgs:
            message = Message(msg)
            self.messages.append(message)

    def export_to_yaml(self, output_path):
        with open(output_path, 'w') as file:
            yaml.dump([msg.__dict__ for msg in self.messages], file)

    def export_to_csv(self, output_path):
        if not self.messages:
            print("No messages to export.")
            return
        fieldnames = list(self.messages[0].__dict__.keys())
        with open(output_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for msg in self.messages:
                writer.writerow(msg.__dict__)
    
    def export_to_txt(self, output_path):
        if not self.messages:
            print("No messages to export.")
            return
        
        with open(output_path, 'w') as file:
            file.write(f"Guild: {self.guild.name} (ID: {self.guild.id})\n")
            file.write(f"Channel: {self.channel.name} (ID: {self.channel.id})\n")
            file.write(f"Channel Topic: {self.channel.topic}\n")
            file.write(f"Exported At: {self.channel.export_time}\n")
            file.write('\n')
            
            for msg in self.messages:
                file.write("\n--- Message ---\n")
                file.write(f"Message ID: {msg.id}\n")
                file.write(f"Message Type: {msg.type}\n")
                file.write(f"Reply to: {msg.ref_to}\n")
                file.write(f"Timestamp: {msg.timestamp}\n")
                file.write(f"Author: {msg.author_nickname} ({msg.author_name})\n")
                file.write(f"Author Id: {msg.author_id}\n")
                file.write(f"Avatar URL: {msg.author_avatar_url}\n")
                file.write(f"Content: {msg.content}\n")
                file.write('--------------------\n')
    
    def print_headers(self):
        print(f"Guild: {self.guild.name} (ID: {self.guild.id})")
        print(f"Channel: {self.channel.name} (ID: {self.channel.id})")
        print(f"Channel Topic: {self.channel.topic}")
        print(f"Exported At: {self.channel.export_time}")


@dataclass
class Message:
    def __init__(self, msg):
        author: str = msg.get('author', {})
        reference: str = msg.get('reference', {})
        self.id: str = msg.get('id')
        self.type: str = msg.get('type')
        self.ref_to: str = reference.get('messageId')
        self.timestamp: str = msg.get('timestamp')
        self.author_name: str = author.get('name')
        self.author_nickname: str = author.get('nickname')
        self.author_id: str = author.get('id')
        self.author_avatar_url: str = author.get('avatarUrl')
        self.content: str = msg.get('content', '')
    
    def format_msg(self):
        return f"\n--- Message ---\nMessage ID: {self.id}\nMessage Timestamp: {self.timestamp}\nMessage Type: {self.type}\nReply To: {self.ref_to}\nAuthor: {self.author_nickname} ({self.author_name})\nAuthor ID: {self.author_id}\nAvatar URL: {self.author_avatar_url}\nContent\n{self.content}\n----------\n"

    def print_msg(self):
        print("\n--- Message ---")
        print(f"Message ID: {self.id}")
        print(f"Message Type: {self.type}")
        print(f"Reply to: {self.ref_to}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Author: {self.author_nickname} ({self.author_name})")
        print(f"Author Id: {self.author_id}")
        print(f"Avatar URL: {self.author_avatar_url}")
        print(f"Content: {self.content}")


def get_data(filepath:str):
    with open(filepath, 'r') as file:
        data = json.load(file)
    
    return data


def main(data_folder, output_dir):
    for filename in os.listdir(data_folder):
        if filename.endswith('json'):
            filepath = os.path.join(data_folder, filename)
            docname, ext = os.path.splitext(filename)
            data = get_data(filepath=filepath)
            conversation = Conversation(data=data)
            output_path = f"{output_dir}/{docname}"
            conversation.export_to_txt(output_path=output_path + '.txt')
            conversation.export_to_csv(output_path=output_path + '.csv')
            conversation.export_to_yaml(output_path=output_path + '.yaml')


if __name__ == "__main__":
    data_folder = sys.argv[1]
    output_dir = sys.argv[2]
    main(data_folder=data_folder, output_dir=output_dir)