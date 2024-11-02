# Discord Data Exporter

This module is designed to parse and export data from Discord archives. It can process JSON-formatted data of Discord messages, extracting detailed conversation information and exporting it into structured CSV, TXT, and YAML formats for ease of analysis.

**This was written with the intention of converting the Kamala Harris campaign published discord server data by [0x0.la](https://0x0.la/cacklesllc). That data was converted and is contained in the conversations folder. The /assets folder appears to contain the avatars for each author as well a plethora of ridiculous memes and other media. That folder can be found [here](https://0x0.la/cacklesllc/assets/).**

**The data contained in the conversations folder are only those that i found to be cost beneficial to my goals. My intent is to explore and analyze the conversations.**

## Features

- **Extracts Guild and Channel Information:** Each export file includes information on the Discord server (guild) and channel where conversations occurred.
- **Parses Conversations:** Supports message extraction with metadata, including message ID, type, timestamp, author details, and message content.
- **Multiple Export Formats:** Export messages to CSV, TXT, and YAML formats for flexible analysis options.

## Prerequisites

- Python 3.x
- Required libraries: `csv`, `json`, `yaml`, `os`, `sys`
- YAML dependency: `PyYAML` (`pip install pyyaml`)

## Usage

1. **Data Preparation**: Ensure your data folder contains JSON files with structured Discord message data. Each JSON file should have a format compatible with the module's `Guild`, `Channel`, and `Message` classes.

2. **Running the Export Script**:

    ```bash
    python discord_exporter.py <data_folder> <output_dir>
    ```

    - `<data_folder>`: Path to the folder containing the JSON data files.
    - `<output_dir>`: Directory where the exported files will be saved.

### Example

```bash
python discord_exporter.py data exports
```

This will parse all JSON files in the `./data` directory and save the outputs (in CSV, TXT, and YAML) to the `./exports` directory.

## Code Structure

- **Guild**: Represents a Discord server, extracting the server name and ID.
- **Channel**: Represents a Discord channel within the server, including channel name, ID, topic, and export time.
- **Message**: Parses individual messages, storing details like message ID, author information, timestamp, and content.
- **Conversation**: Handles the overall conversation by gathering all messages and exporting to the specified formats.

## Output File Structure

- **TXT**: Contains structured conversation information, including headers for guild, channel, and message metadata.
- **CSV**: A table of messages with detailed columns for each message attribute.
- **YAML**: Hierarchical format, suitable for data interchange and structured analysis.

## Example Output

### YAML Output

```yaml
- id: "12345"
  type: "MESSAGE"
  timestamp: "2023-11-01T12:34:56Z"
  author_name: "AuthorUsername"
  content: "Sample message content"
  ...
```

### CSV Output

| Message ID | Type    | Timestamp           | Author Name | Content                |
|------------|---------|---------------------|-------------|------------------------|
| 12345      | MESSAGE | 2023-11-01 12:34:56 | AuthorUser  | Sample message content |

### TXT Output

```plaintext
Guild: Campaign Guild (ID: 123)
Channel: General (ID: 456)
Channel Topic: Campaign discussion
Exported At: 2023-11-01T12:34:56Z

--- Message ---
Message ID: 12345
Message Type: MESSAGE
Timestamp: 2023-11-01T12:34:56Z
Author: AuthorUser
Content: Sample message content
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
