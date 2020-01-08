import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

data = pd.read_csv("Pokemon.csv")

# Associate a color with each type:
colors = {
    "Grass": "#7AC74C",
    "Fire": "#EE8130",
    "Water": "#6390F0",
    "Bug": "#A6B91A",
    "Normal": "#A8A77A",
    "Poison": "#A33EA1",
    "Electric": "#F7D02C",
    "Ground": "#E2BF65",
    "Fairy": "#D685AD",
    "Fighting": "#C22E28",
    "Psychic": "#F95587",
    "Rock": "#B6A136",
    "Ghost": "#735797",
    "Ice": "#96D9D6",
    "Dragon": "#6F35FC",
    "Dark": "#705746",
    "Steel": "#B7B7CE",
    "Flying": "#A98FF3",
}

def barplt(): # Bar Plot of Averages 
    fig, axes = plt.subplots(nrows=2, ncols=1)
    df1 = data.groupby('Type 1').mean().drop(columns=['#', 'Total'])#.plot(kind='bar')
    df2 = data.groupby('Type 2').mean().drop(columns=['#', 'Total'])#.plot(kind='bar')
    df1.plot(kind='bar', ax=axes[0])
    df2.plot(kind='bar', ax=axes[1])
    plt.show()
    plt.clf()

def kdeplt(attr1, attr2, whichtype): # Kdeplot Test
    sns.set(style="whitegrid")
    _, axes = plt.subplots(3, 6, sharex=True, sharey=True)

    types = data['Type 1'].unique()

    for type1, ax in zip(types, axes.flatten()[:18]):
        df = data[data[whichtype] == type1]
        # print(df)
        sns.kdeplot(df[attr1], df[attr2], ax=ax, color=colors[type1], shade_lowest=False)
        sns.regplot(x=attr1, y=attr2, data=df, ax=ax, color=colors[type1])
        ax.set_title(type1)

    plt.xlim(-20, 250)
    plt.ylim(-20, 250)
    plt.show()
    plt.clf()

def jointkdeplt(attr1, attr2, whichtype):
    sns.set(style="whitegrid")

    types = data['Type 1'].unique()

    for type1 in types:
        df = data[data[whichtype] == type1]
        # print(df)

        # The following commented code also works, but doesn't allow changing the marginal graph types or the primary graph types.
        # Basically, the JointGrid type allows for more flexibility. However, this has more interesting display options (i.e. kind="hex").
        # sns.jointplot(
        #     pd.Series(df['Attack'], name="Attack"), pd.Series(df['Sp. Atk'], name="Special Attack"), 
        #     kind="kde", 
        #     color=colors[type1], 
        #     height=7, 
        #     space=0)

        p = sns.JointGrid(x=attr1, y=attr2, data=df, space=0, xlim=(-20, 250), ylim=(-20, 250))
        p = p.plot_joint(sns.kdeplot, color=colors[type1])
        p = p.plot_joint(sns.regplot, color=colors[type1])
        p = p.plot_marginals(sns.kdeplot, color=colors[type1], shade=True)

        print(type1)
        plt.title(type1)
        plt.show()

def pairplt(whichtype):
    sns.set(style="whitegrid")

    types = data['Type 1'].unique()

    for type1 in types:
        df = data[data[whichtype] == type1]
        df["color"] = colors[type1]
        sns.pairplot(df, height=2, vars=["Attack", "Sp. Atk", "Defense", "Sp. Def", "HP", "Speed"], hue="color", kind="reg", diag_kind="kde")
        plt.show()

def heatplt():
    df = data.groupby('Type 1').mean().drop(columns=['#', 'Total'])
    
    sns.set()
    sns.heatmap(df.transpose(), cmap="summer", annot=True, fmt=".2f", linewidths=.5)
    plt.show()
    plt.clf()
    # [df.Defense, df.Attack]
    
    df = df.reset_index()
    categories=list(df)[1:]
    N = len(categories)
    
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    plt.xticks(angles[:-1], categories)
    
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30,40,50,60,70,80,90,100,110,120,130], ["10","20","30","40","50","60","70","80","90","100","110","120","130"], color="grey", size=7)
    plt.ylim(0,130)
    
    values=df.loc[0].drop('Type 1').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
    ax.fill(angles, values, 'b', alpha=0.1)
    
    values=df.loc[16].drop('Type 1').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
    ax.fill(angles, values, 'r', alpha=0.1)
    
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()
    plt.clf()


def make_spider(row, title, color, df):
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
 
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
 
    # Initialise the spider plot
    ax = plt.subplot(3,6,row+1, polar=True)
 
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
 
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
 
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,40,70,100,130], ["10","40","70","100","130"], color="grey", size=7)
    plt.ylim(0,130)
 
    # Ind1
    values=df.loc[row].drop('Type 1').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
 
    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

def radialplt():
    sns.set_style("white")
    df = data.groupby('Type 1').mean().drop(columns=['#', 'Total'])
    df = df.reset_index()

    plt.suptitle("Means of stats across primary types")
    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    for row in range(0, len(df.index)):
        make_spider( row=row, title=df.iloc[row]['Type 1'], color=colors[df.iloc[row]['Type 1']], df=df)

    plt.show()

def main():
    # Examine parts of the data
    print(data.head())
    print(data.tail())
    print(data.sample(5))
    print("Count of rows in data: {}".format(data.count()))

    # Grab Data Frame using columns Type 1 and Type 2
    print(data[['Type 1', 'Type 2']])

    # Get mean for one numeric column
    print("Mean defense across all Pokemon: {}".format(data.Defense.mean()))

    # Grab a specific pokemon
    print(data.loc[200])

    # Bar Plot
    # barplt()

    # KDE Plots
    print("Stats to examine: HP, Speed, Attack, Sp. Atk, Defense, Sp. Def")
    attr1 = input("Provide a stat to examine: ")
    attr2 = input("Provide a second stat to examine: ")
    whichtype = input("Examine primary type (Type 1) or secondary type (Type 2): ")
    kdeplt("Speed", "HP", "Type 2")
    # jointkdeplt(attr1, attr2, whichtype)

    # Radial Plot
    # radialplt()

    # Pair Plot
    # pairplt("Type 1")

if __name__ == '__main__':
    main()