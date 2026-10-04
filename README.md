# 🤖 LEAP Hand Rock–Paper–Scissors Simulation (MuJoCo)

This project is a basic simulation of a robotic LEAP hand performing three familiar gestures:
- ✊ Rock  
- ✋ Paper  
- ✌️ Scissors  

I built the simulation using the **MuJoCo physics engine** and controlled it via Python. The joint movements for each gesture are defined manually in the script using control signals.

---

## 📁 Project Folder Structure

Here’s how I’ve organized the files:

DexWrist_Leap_RPS_Project/
├── models/
│ └── leap_hand.xml
├── scripts/
│ └── run_sim.py
├── output/
│ └── leap_hand_rps_demo.mp4
└── README.md


---

## 🛠️ Tools & Technologies

- Python 3.10 (set up via Conda)
- MuJoCo 3.4 (installed using pip)
- MuJoCo Viewer for real-time visualization
- OBS Studio (for screen recording the simulation)

---

## ⚙️ What the Simulation Does

- The `leap_hand.xml` file defines the hand model structure.
- The Python script (`run_sim.py`) uses MuJoCo’s API to send commands to the hand’s joints.
- The hand cycles through three predefined poses:
  - **Rock**: all fingers curled in
  - **Paper**: all fingers extended
  - **Scissors**: two fingers out, rest curled

These are controlled through the `data.ctrl[:]` values.

---

## ▶️ How to Run It

To run the simulation:

1. Open Anaconda Prompt and activate the MuJoCo environment:
   ```bash
   conda activate mujoco_env
Navigate to the simulation script directory:

cd Desktop/leap_rps_sim/scripts
Run the Python script:

python run_sim.py
Once the viewer opens, you’ll see the hand move through each of the Rock, Paper, and Scissors poses.