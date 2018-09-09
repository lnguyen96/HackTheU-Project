# HackTheU Project

Our project uses a graph data structure to model redistribution of excess renewable energy in a neighborhood. Our current design models a simple neighborhood of ten houses connected to a reserve with those reserves being connected to each other as well. Our project focuses on redistributing excess energy from households who consume less and redistributing it to households who require more energy at a reduced rate compared to the main energy providers. We currently use theoretical data to model household usage and such to generate pricing, as there is not currently data for this that is easily obtained on the internet. We plan to use fractals to scale up our model to better represent a real neighborhood or city, we also plan on implementating a max-flow algorithm to better represent and optimize our models for energy transfer in real life.

## Getting Started

Since our project only uses python3, those will currently be the only files you need to run. If you do not have python3 installed, we would recommend installing the [Anaconda](https://www.anaconda.com/download/) package for your OS.

## Generating visuals from our numerical data

If you wish to generate the visuals used in our project, change your current directory to our copy of HackTheU Project and run the command 

```
python hackathon1.py
```

## Authors

* **Long Nguyen** - University of Colorado Boulder
* **Edwin Chiang** - University of Colorado Boulder
* **Niklaus Parcell** - University of Utah
* **Deron Parcell** - University of Utah 