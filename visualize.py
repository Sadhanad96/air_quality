import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import RadioButtons
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import rcParams

# Load merged CSV
df = pd.read_csv("air_weather_merged.csv")

# Set Seaborn style for grid and figure
sns.set(style="whitegrid")
rcParams['font.family'] = 'Comic Sans MS'  # Stylish, fun font (can change)
rcParams['axes.titlesize'] = 20
rcParams['axes.labelsize'] = 14
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['axes.titleweight'] = 'bold'

# Figure
fig, ax = plt.subplots(figsize=(12,7))
plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.15)

# Draw full page gradient background
def draw_page_gradient(fig, color1="#ff9a9e", color2="#fad0c4"):
    gradient = np.linspace(0,1,256).reshape(-1,1)
    gradient = np.repeat(gradient, 2, axis=1)
    cmap = LinearSegmentedColormap.from_list("page_grad", [color1, color2])
    fig.figimage(gradient, xo=0, yo=0, origin='lower', cmap=cmap, alpha=1, zorder=0)

draw_page_gradient(fig)

# Graph background stays white
ax.set_facecolor("white")
ax.tick_params(colors="#222222")
for spine in ax.spines.values():
    spine.set_color("#222222")

# Colors
colors = sns.color_palette("Set2", 10)

# Initial scatter
sc = ax.scatter(df['Temperature'], df['PM2.5'], s=130, c=colors[0], alpha=0.85, edgecolor='k', zorder=2)
ax.set_xlabel('Temperature (°C)', fontsize=14, fontweight='bold', color="#333333")
ax.set_ylabel('PM2.5', fontsize=14, fontweight='bold', color="#333333")
ax.set_title('🌟 PM2.5 vs Temperature 🌟', fontsize=22, fontweight='bold', color="#111111")
ax.grid(True, linestyle='--', alpha=0.5)

# Radio buttons
axcolor = '#ffe6f0'
rax = plt.axes([0.05, 0.3, 0.22, 0.4], facecolor=axcolor, zorder=5)
radio = RadioButtons(rax, ('PM2.5 vs Temp', 'PM2.5 vs Humidity', 'PM2.5 vs Wind', 'PM2.5 by City', 'Temp by City'))

# Update function
def update(label):
    ax.clear()
    ax.set_facecolor("white")
    ax.tick_params(colors="#222222")
    for spine in ax.spines.values():
        spine.set_color("#222222")
    
    if label == 'PM2.5 vs Temp':
        ax.scatter(df['Temperature'], df['PM2.5'], s=130, c=colors[0], alpha=0.85, edgecolor='k', zorder=2)
        ax.set_xlabel('Temperature (°C)', fontsize=14, fontweight='bold', color="#333333")
        ax.set_ylabel('PM2.5', fontsize=14, fontweight='bold', color="#333333")
        ax.set_title('🌟 PM2.5 vs Temperature 🌟', fontsize=22, fontweight='bold', color="#111111")
    elif label == 'PM2.5 vs Humidity':
        ax.scatter(df['Humidity'], df['PM2.5'], s=130, c=colors[1], alpha=0.85, edgecolor='k', zorder=2)
        ax.set_xlabel('Humidity (%)', fontsize=14, fontweight='bold', color="#333333")
        ax.set_ylabel('PM2.5', fontsize=14, fontweight='bold', color="#333333")
        ax.set_title('💧 PM2.5 vs Humidity 💧', fontsize=22, fontweight='bold', color="#111111")
    elif label == 'PM2.5 vs Wind':
        ax.scatter(df['WindSpeed'], df['PM2.5'], s=130, c=colors[2], alpha=0.85, edgecolor='k', zorder=2)
        ax.set_xlabel('Wind Speed (m/s)', fontsize=14, fontweight='bold', color="#333333")
        ax.set_ylabel('PM2.5', fontsize=14, fontweight='bold', color="#333333")
        ax.set_title('🌬️ PM2.5 vs Wind Speed 🌬️', fontsize=22, fontweight='bold', color="#111111")
    elif label == 'PM2.5 by City':
        df_sorted = df.sort_values('PM2.5', ascending=False)
        ax.bar(df_sorted['City'], df_sorted['PM2.5'], color=colors, alpha=0.85, edgecolor='k', zorder=2)
        ax.set_xlabel('City', fontsize=14, fontweight='bold', color="#333333")
        ax.set_ylabel('PM2.5', fontsize=14, fontweight='bold', color="#333333")
        ax.set_title('🏙️ PM2.5 by City 🏙️', fontsize=22, fontweight='bold', color="#111111")
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right', color="#222222")
    elif label == 'Temp by City':
        df_sorted = df.sort_values('Temperature', ascending=False)
        ax.bar(df_sorted['City'], df_sorted['Temperature'], color=colors, alpha=0.85, edgecolor='k', zorder=2)
        ax.set_xlabel('City', fontsize=14, fontweight='bold', color="#333333")
        ax.set_ylabel('Temperature (°C)', fontsize=14, fontweight='bold', color="#333333")
        ax.set_title('🌞 Temperature by City 🌞', fontsize=22, fontweight='bold', color="#111111")
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right', color="#222222")

    ax.grid(True, linestyle='--', alpha=0.5)
    fig.canvas.draw_idle()

radio.on_clicked(update)

# Hover annotation for scatter points
annot = ax.annotate("", xy=(0,0), xytext=(15,15), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="#ffff99", alpha=0.9),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    x, y = sc.get_offsets()[ind["ind"][0]]
    annot.xy = (x, y)
    annot.set_text(f"({x:.1f}, {y:.1f})")

def hover(event):
    if sc.contains(event)[0]:
        update_annot(sc.contains(event)[1])
        annot.set_visible(True)
        fig.canvas.draw_idle()
    else:
        annot.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
