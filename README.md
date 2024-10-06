# Visualize the Connectivity Between Naval Vessel Routes and PACE

<center> <img src="https://github.com/gabboraron/PACEMapWithVesselRoute/blob/main/prezi/juxtapose-gif.gif"></img></center>

This project visualizes the connectivity between naval vessel routes and PACE (Plankton, Aerosol, Cloud, ocean Ecosystem) data. The visualization helps in understanding the impact of naval routes on marine ecosystems.

**More about the project:**
- [Project page on NASA Space Apps Challenge 2024](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/spacewatch/?tab=project)
- [Short video](https://obudaiegyetem-my.sharepoint.com/:v:/g/personal/buriansandor95_stud_uni-obuda_hu/EWVj81AjwghGjxzowp7CQOcB1-EH6FDnXmXI6qgE3UaD7Q?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=tmSdsJ)
- [PowerPoint presentation](https://obudaiegyetem-my.sharepoint.com/:p:/g/personal/buriansandor95_stud_uni-obuda_hu/Eb_yZgXilRRGqSAwW6lf-x4BjkHg9Xvw7mW3CYnFbbSAMg?e=4AxpXy)

---------------------------------

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
This project aims to provide a visual representation of the connectivity between naval vessel routes and PACE data. By overlaying vessel routes on PACE data, we can analyze the potential impact of shipping lanes on marine ecosystems.

## Features
- Overlay vessel routes on PACE data maps.
- Overlay datacables on PACE data maps.
- Compare different time periods using Juxtapose sliders.
- Select and compare different datasets.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install the required JavaScript libraries:
    - Include Mapbox GL JS:
        ```html
        <script src="https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.js"></script>
        <link href="https://api.mapbox.com/mapbox-gl-js/v1.12.0/mapbox-gl.css" rel="stylesheet" />
        ```
    - Include Juxtapose:
        ```html
        <script src="https://cdn.knightlab.com/libs/juxtapose/latest/js/juxtapose.min.js"></script>
        <link rel="stylesheet" href="https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css">
        ```

## Usage
1. Run the Python script to generate the visualizations:
    ```sh
    python /RAWdata/save_as_image.py
    ```

2. Open `index.html` in your web browser to view the interactive map and Juxtapose sliders.

## Data Sources
- **PACE Data**: Plankton, Aerosol, Cloud, ocean Ecosystem data from NASA.
- **Vessel Routes**: Global Shipping Lanes data from CIA.
- **Underwater Data Cables** 

More detailed description in [RAWdaata/README.md](RAWdaata/README.md)

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Created with :heart: @ [NASA Space Apps Challange](https://www.spaceappschallenge.org) - [Hungary](https://www.spaceappschallenge.org/nasa-space-apps-2024/2024-local-events/budapest/?tab=details) by [SpaceWatch](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/spacewatch/?tab=details).
