﻿# Map Tile Server with Node.js

## Overview
The Map Tile Server is a Node.js-based project designed to provide a scalable and efficient solution for serving map tiles. This server is capable of generating and delivering map tiles on-the-fly, supporting a variety of map styles and configurations.

## Features
- Dynamic Tile Generation: Generate map tiles dynamically based on user requests, allowing for real-time updates and customization.

- Flexible Configuration: Easily configure map styles, layers, and data sources to suit your specific mapping needs.

- Simplicity: Coded very simple.


## Prerequisites
Before running the Map Tile Server, make sure you have the following dependencies installed:

- Node.js (version 18.)
- npm (Node Package Manager)

## Getting Started
1. Clone the repository:
 ``` bash
 git clone https://github.com/Ali-Kazzazi/NodeJs_Map_Tile_Server.git
```

2. Navigate to the project directory:
```bash
cd map-tile-server
```

3. Install dependencies:
``` bash 
npm install
```

4. Start the server:
``` bash 
npm start
```
5. Access the Map Tile Server at http://localhost:4000.


## Viewing the Map
After starting the server, open the index.html file in your browser to view the map:
``` bash
index.html
```



## Using Mapperitive to Download Tiles
To download map tiles for your Map Tile Server, follow these steps:

1. Download and install [Mapperitive](http://maperitive.net/).

2. Launch Mapperitive and configure your desired map style and parameters.

3. Export the map `tiles` to the tiles directory in the Map Tile Server project.

4. The Map Tile Server will dynamically serve the tiles from the `Tiles` directory.

## Using Docker

### Build Docker Image

Build the Docker image from the project directory:
```bash
docker build . -t tile_server
```

### Run Docker Container

Run the Docker container:
```bash
docker run -p 4000:4000 -d tile_server
```
Access the Map Tile Server at http://localhost:4000.



## Contributing
Contributions are welcome!

## License
This project is licensed under the MIT License.

---

Feel free to customize the instructions based on your specific usage of the Mapperitive app and any additional details you'd like to provide.
