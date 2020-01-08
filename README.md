# Pokemon Data Visualization
Data Visualization practice using matplotlib, seaborn, and pandas, with Pokemon data.

This pet project was my first foray into data visualization tools in Python. My focus was on leveraging pandas for data manipulation, with matplotlib and seaborn for visualization. Please provide feedback, advice, or tips for improving!

This is, obviously, a very simple project that is quite redimentary in structure. The hope is to make an interactive UI to allow the user to pick which sets of data they want to display, and how. With that in mind, I didn't focus on a lot of terminal interactivity, but I'll explain how to switch to different visualizations by commenting and uncommenting code.

## How to Use
This program was run using Python 3, so keep that in mind when installing dependencies.

Make sure that you install the prerequisite libraries:
```
pip install matplotlib
pip install seaborn
pip install pandas
```
The python script can be run with:
```
python3 mpltest.py
```

I've prepared, what I believe to be, useful or interesting visualizations to examine trends between different stat values and typing among pokemon. There were many different bi-variate and multi-variate visualizations I tried, but I kept the ones I thought were most aesthetically appealing and most informative. That said, this project currently includes: Bar Plots and Radial Plots for mean stats across all types, Kernel Density Estimations (also with marginal distributions) for bi-variate stat comparison, and Pair Plots for each type to show pair-wise comparisons of all stats (currently kinda ugly).

To see different visualizations, go to `main()` and uncomment:
* `barplt()` for a bar plot of stat means across all types (primary above, secondary below)
* `kdeplt()` for KDE plots of pairwise stat comparisons across all types (all in one window)
* `jointkdeplt()` for KDE plots with marginal distributions of pairwise stats across all types (opens 18 windows, sequentially)
* `radialplt()` for radial plots of stat means across all primary types (all in one window)
* `pairplt()` for pairwise comparisons of all stats for all types, although color-coding based on type doesn't work, and charts aren't yet labelled based on type (opens 18 windows, sequentially)

## Further Development
Future work for this project will include a intuitive and user friendly UI for picking different chart types, stats, and typing to compare. 

Additionally, using TensorFlow to create a classifier to determine the typing of a Pokemon using just two of its statistics. 

Similarly it would be interesting to create a classifier to predict a winner in a battle between two pokemon just based on typing and ability (ability would require additional data than is provided here), that is perhaps trained on simulation data.

## Sources and Inspiration
Pokemon.csv from "Pokemon with Stats" data by Alberto Barradas on Kaggle:
https://www.kaggle.com/abcsds/pokemon

Python Graph Gallery for inspiration with multi-variate plotting:
https://python-graph-gallery.com/

From Data to Viz for being an awesome resource about benefits and caveats of different representations of data:
https://www.data-to-viz.com/
