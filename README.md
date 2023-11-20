# Synapse-Sprinter-Crossy Road

## Inspiration
This project finds its inspiration in the challenges faced by individuals affected by Muscular Dystrophy. It aims to bring joy and assist in the rehabilitation of those with muscular impairments by integrating hardware into gaming systems. Muscular Dystrophy, a group of diseases causing progressive weakness and loss of muscle mass, serves as a poignant motivation to create an inclusive and enjoyable gaming experience for individuals with such conditions. The goal is to leverage technology not just for entertainment but as a means of therapy and empowerment for those facing muscular challenges.

## What it does
Synapse-Sprinter-Crossy Road allows two players to engage in a Crossy Roads-style game, utilizing live data obtained from muscle movements to control the players within the game environment.

## How we built it
The project involved connecting an Arduino device to our laptop, capturing real-time inputs from muscle movements, and utilizing these inputs to drive the in-game actions of the players.

## Challenges we ran into
- **Setting up Arduino:** Configuring the Arduino and establishing a stable connection with our system.
- **Reading and Parsing Data:** Extracting meaningful data from muscle inputs and converting it into usable game commands.
- **Designing the Game:** Creating an engaging game interface that effectively integrates live data for player movement.

## Accomplishments that we're proud of
- **Learning New Concepts:** Mastering the process of connecting Arduino to our system, implementing multi-threading, and successfully fetching and utilizing data from external hardware sources.
- 
## Gameplay Screenshots
![form](https://github.com/mr-fool/Synapse-Sprinter--Crossy_Road/assets/6241984/e8571f4b-192e-4c43-9332-64eb24a2a535)

![screen](https://github.com/mr-fool/Synapse-Sprinter--Crossy_Road/assets/6241984/a78e4d74-d79f-4ee7-b838-631ddd42b82c)

## What we learned
The project provided invaluable insights into the intricacies of integrating hardware systems into gaming applications. It expanded our knowledge in hardware-software interaction, offering hands-on experience in merging real-world data inputs with digital gaming environments.

## How to Run
To run the code, follow these steps:
1. Make sure you have Python installed.
2. Install necessary Python modules by running:
`pip install pyserial pygame`
3. Run the `main.py` script.
4. To run in Arduino mode, set `ARDUINO_MODE = True`.
5. To run with hardware, execute the `EEGtoKeyStroke(EEGReadings)` function.

## What's next for Synapse-Sprinter-Crossy Road
Our future goals for Synapse-Sprinter-Crossy Road include making the game accessible across multiple platforms, ensuring that the rehabilitative and entertaining aspects of the game reach a wider audience.
