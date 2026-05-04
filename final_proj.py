# ============================================================
# INDIA ROAD ACCIDENT ANALYZER
# Complete Final Submission
# Tools: Tkinter, Pandas, NumPy, Matplotlib, MongoDB
# Dataset: data.gov.in - Traffic Accidents 2022
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pymongo import MongoClient
from datetime import datetime

# ============================================================
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    client.server_info()
    db = client["accident_db"]
    history_col = db["search_history"]
    mongo_connected = True
    print("MongoDB connected successfully")
except Exception as e:
    mongo_connected = False
    history_col = None
    print("MongoDB not connected:", e)

# ============================================================
# 2. LOAD REAL DATASET 
# ============================================================
CSV_PATH = "road_accidents.csv"

try:
    raw = pd.read_csv(CSV_PATH, index_col=0)
    raw.columns = raw.columns.str.strip()

    # Keep only the 4 columns we need and rename them
    df = raw[[
        "State/UT/City",
        "Total Traffic Accidents - Cases",
        "Total Traffic Accidents - Injured",
        "Total Traffic Accidents - Died"
    ]].copy()

    df.columns = ["State", "Total_Accidents", "Injuries", "Deaths"]

    # Remove summary rows like "Total (States)", "Total (UTs)", etc.
    df = df[~df["State"].str.contains("Total", na=False)]

    # Convert to numbers
    df["Total_Accidents"] = pd.to_numeric(df["Total_Accidents"], errors="coerce")
    df["Injuries"]        = pd.to_numeric(df["Injuries"],        errors="coerce")
    df["Deaths"]          = pd.to_numeric(df["Deaths"],          errors="coerce")

    df = df.dropna()
    df = df.reset_index(drop=True)

    print("Real dataset loaded:", df.shape[0], "rows")

except FileNotFoundError:
    print("CSV not found. Using dummy data.")
    dummy = {
        "State": ["Maharashtra", "Uttar Pradesh", "Tamil Nadu",
                  "Karnataka", "Kerala", "Madhya Pradesh",
                  "Andhra Pradesh", "Gujarat", "Rajasthan", "Delhi"],
        "Total_Accidents": [35373, 41405, 66117, 39765, 43970,
                            53479, 22099, 16549, 24562, 6356],
        "Deaths":          [18893, 28615, 19717, 11705, 4696,
                            15432, 9330,  8417,  12046, 2152],
        "Injuries":        [25564, 21735, 67892, 48154, 49318,
                            51264, 21340, 15139, 22257, 4818],
    }
    df = pd.DataFrame(dummy)

# ============================================================
# ============================================================

# Function 1: Filter by state
def filter_data(state):
    filtered = df.copy()
    if state != "All States":
        filtered = filtered[filtered["State"] == state]
    return filtered


# Function 2: Calculate stats using NumPy
def calculate_stats(filtered_df):
    total_acc      = int(filtered_df["Total_Accidents"].sum())
    total_deaths   = int(filtered_df["Deaths"].sum())
    total_injuries = int(filtered_df["Injuries"].sum())
    fatality_rate  = round(float(np.divide(total_deaths, total_acc) * 100), 2) if total_acc > 0 else 0.0
    return (total_acc, total_deaths, total_injuries, fatality_rate)


# Function 3: Save to MongoDB - INSERT
def save_to_mongo(state, stats_tuple):
    if not mongo_connected:
        return
    try:
        record = {
            "state": state,
            "year":  2022,
            "result": {
                "total_accidents": stats_tuple[0],
                "deaths":          stats_tuple[1],
                "injuries":        stats_tuple[2],
                "fatality_rate":   stats_tuple[3]
            },
            "timestamp": datetime.now()
        }
        history_col.insert_one(record)
        print("Saved to MongoDB")
    except Exception as e:
        print("MongoDB save error:", e)


# Function 4: Fetch history - READ
def fetch_history():
    if not mongo_connected:
        return []
    try:
        records = list(history_col.find().sort("timestamp", -1).limit(10))
        return records
    except Exception as e:
        print("MongoDB fetch error:", e)
        return []


# Function 5: Get states list
def get_states():
    states = sorted(df["State"].dropna().unique().tolist())
    states.insert(0, "All States")
    return states


# Function 6: Draw chart
def draw_chart(data, chart_type):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")
    ax.tick_params(colors="#aaa")
    ax.title.set_color("#e94560")
    for spine in ax.spines.values():
        spine.set_edgecolor("#333")

    if chart_type == "Top 10 States by Accidents":
        top10 = data.groupby("State")["Total_Accidents"].sum().nlargest(10)
        colors_bar = ["#e94560"] + ["#0f3460"] * 9
        top10.plot(kind="barh", ax=ax, color=colors_bar[::-1])
        ax.set_title("Top 10 States — Total Accidents (2022)")
        ax.set_xlabel("Total Accidents", color="#aaa")
        for label in ax.get_yticklabels():
            label.set_color("#aaa")

    elif chart_type == "Top 10 States by Deaths":
        top10 = data.groupby("State")["Deaths"].sum().nlargest(10)
        colors_bar = ["#ff6b6b"] + ["#4a0010"] * 9
        top10.plot(kind="barh", ax=ax, color=colors_bar[::-1])
        ax.set_title("Top 10 States — Deaths (2022)")
        ax.set_xlabel("Total Deaths", color="#aaa")
        for label in ax.get_yticklabels():
            label.set_color("#aaa")

    elif chart_type == "Deaths vs Injuries by State":
        top8 = data.groupby("State")["Total_Accidents"].sum().nlargest(8).index
        plot_data = data[data["State"].isin(top8)].groupby("State")[["Deaths", "Injuries"]].sum()
        x = np.arange(len(plot_data))
        ax.bar(x - 0.2, plot_data["Deaths"],   0.4, label="Deaths",   color="#e94560")
        ax.bar(x + 0.2, plot_data["Injuries"], 0.4, label="Injuries", color="#00d2ff")
        ax.set_xticks(x)
        ax.set_xticklabels(plot_data.index, rotation=30, ha="right", color="#aaa", fontsize=8)
        ax.set_title("Deaths vs Injuries — Top 8 States (2022)")
        ax.legend(facecolor="#16213e", labelcolor="#aaa")

    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# Function 7: Run analysis on button click
def run_analysis():
    state      = state_var.get()
    chart_type = chart_var.get()

    filtered = filter_data(state)

    if filtered.empty:
        messagebox.showwarning("No Data", "No data found for selected state.")
        return

    stats = calculate_stats(filtered)
    total_acc, total_deaths, total_injuries, fatality_rate = stats

    stat_labels["Total Accidents"].config(text=f"{total_acc:,}")
    stat_labels["Total Deaths"].config(text=f"{total_deaths:,}")
    stat_labels["Total Injuries"].config(text=f"{total_injuries:,}")
    stat_labels["Fatality Rate"].config(text=f"{fatality_rate}%")

    save_to_mongo(state, stats)
    draw_chart(filtered, chart_type)


# Function 8: Show history popup
def show_history():
    records = fetch_history()

    win = tk.Toplevel(root)
    win.title("Search History")
    win.geometry("580x380")
    win.configure(bg="#1a1a2e")

    tk.Label(win, text="Last 10 Searches (from MongoDB)",
             fg="#e94560", bg="#1a1a2e",
             font=("Courier New", 13, "bold")).pack(pady=12)

    if not records:
        tk.Label(win,
                 text="No history found." if mongo_connected else "MongoDB not connected.",
                 fg="#888", bg="#1a1a2e",
                 font=("Courier New", 11)).pack(pady=20)
        return

    for r in records:
        s = r.get("result", {})
        line = (f"State: {r.get('state')}  |  "
                f"Accidents: {s.get('total_accidents', '?'):,}  |  "
                f"Deaths: {s.get('deaths', '?'):,}  |  "
                f"Fatality: {s.get('fatality_rate', '?')}%")
        tk.Label(win, text=line, fg="#ccc", bg="#16213e",
                 font=("Courier New", 8), anchor="w",
                 padx=10, pady=6).pack(fill="x", padx=12, pady=2)


# Function 9: Clear history - DELETE
def clear_history():
    if not mongo_connected:
        messagebox.showinfo("MongoDB", "MongoDB not connected.")
        return
    confirm = messagebox.askyesno("Confirm", "Delete all search history?")
    if confirm:
        history_col.delete_many({})
        messagebox.showinfo("Done", "History cleared.")


# ============================================================
# 4. TKINTER GUI
# ============================================================
root = tk.Tk()
root.title("India Road Accident Analyzer 2022")
root.geometry("1100x720")
root.configure(bg="#1a1a2e")

# ── HEADER ──────────────────────────────────────────────────
header = tk.Frame(root, bg="#16213e", pady=14)
header.pack(fill="x")

tk.Label(header,
         text="India Road Accident Analyzer — 2022",
         font=("Courier New", 17, "bold"),
         fg="#e94560", bg="#16213e").pack(side="left", padx=20)

mongo_status = "● MongoDB Connected" if mongo_connected else "● MongoDB Offline"
mongo_color  = "#00ff88" if mongo_connected else "#ff4444"
tk.Label(header, text=mongo_status,
         font=("Courier New", 9),
         fg=mongo_color, bg="#16213e").pack(side="right", padx=20)

tk.Label(header,
         text="Dataset: data.gov.in | Ministry of Road Transport & Highways",
         font=("Courier New", 9),
         fg="#555", bg="#16213e").pack(side="right", padx=10)

# ── CONTROLS ────────────────────────────────────────────────
ctrl = tk.Frame(root, bg="#1a1a2e", pady=12)
ctrl.pack(fill="x", padx=20)

tk.Label(ctrl, text="State/City:", fg="#aaa", bg="#1a1a2e",
         font=("Courier New", 11)).grid(row=0, column=0, padx=(0, 5))
state_var = tk.StringVar()
state_combo = ttk.Combobox(ctrl, textvariable=state_var,
                            values=get_states(), width=28, state="readonly")
state_combo.current(0)
state_combo.grid(row=0, column=1, padx=(0, 20))

tk.Label(ctrl, text="Chart:", fg="#aaa", bg="#1a1a2e",
         font=("Courier New", 11)).grid(row=0, column=2, padx=(0, 5))
chart_var = tk.StringVar()
chart_combo = ttk.Combobox(ctrl, textvariable=chart_var,
                            values=["Top 10 States by Accidents",
                                    "Top 10 States by Deaths",
                                    "Deaths vs Injuries by State"],
                            width=26, state="readonly")
chart_combo.current(0)
chart_combo.grid(row=0, column=3, padx=(0, 20))

tk.Button(ctrl, text="  Analyze  ",
          bg="#e94560", fg="white",
          font=("Courier New", 11, "bold"),
          relief="flat", cursor="hand2",
          command=run_analysis).grid(row=0, column=4, padx=(0, 8))

tk.Button(ctrl, text="Search History",
          bg="#0f3460", fg="#aaa",
          font=("Courier New", 10),
          relief="flat", cursor="hand2",
          command=show_history).grid(row=0, column=5, padx=(0, 8))

tk.Button(ctrl, text="Clear History",
          bg="#2a0a0a", fg="#ff4444",
          font=("Courier New", 10),
          relief="flat", cursor="hand2",
          command=clear_history).grid(row=0, column=6)

# ── STATS PANEL ─────────────────────────────────────────────
stats_frame = tk.Frame(root, bg="#1a1a2e", pady=8)
stats_frame.pack(fill="x", padx=20)

stat_labels = {}
stat_names  = ["Total Accidents", "Total Deaths", "Total Injuries", "Fatality Rate"]
stat_colors = ["#e94560", "#ff6b6b", "#ffa500", "#00d2ff"]

for i in range(len(stat_names)):
    name  = stat_names[i]
    color = stat_colors[i]
    box = tk.Frame(stats_frame, bg="#16213e", padx=18, pady=10,
                   highlightbackground="#0f3460", highlightthickness=1)
    box.grid(row=0, column=i, padx=10, sticky="ew")
    stats_frame.columnconfigure(i, weight=1)
    tk.Label(box, text=name, fg="#666", bg="#16213e",
             font=("Courier New", 9)).pack()
    lbl = tk.Label(box, text="—", fg=color, bg="#16213e",
                   font=("Courier New", 16, "bold"))
    lbl.pack()
    stat_labels[name] = lbl

# ── CHART FRAME ─────────────────────────────────────────────
chart_frame = tk.Frame(root, bg="#1a1a2e")
chart_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(chart_frame,
         text="Select a state and chart type, then click Analyze",
         fg="#333", bg="#1a1a2e",
         font=("Courier New", 12)).pack(expand=True)

# ── FOOTER ──────────────────────────────────────────────────
footer = tk.Frame(root, bg="#16213e", pady=6)
footer.pack(fill="x", side="bottom")
tk.Label(footer,
         text="India Road Accident Analyzer  |  Python Project  |  data.gov.in  |  2022 Data",
         fg="#333", bg="#16213e",
         font=("Courier New", 8)).pack()

# ============================================================
# 5. RUN
# ============================================================
root.mainloop()