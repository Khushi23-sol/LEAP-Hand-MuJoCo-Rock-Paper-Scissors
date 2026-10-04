import mujoco
import mujoco.viewer
import time
import random

# Load model
model = mujoco.MjModel.from_xml_path("../models/leap_hand.xml")
data = mujoco.MjData(model)

# =========================
# 🔧 JOINT SETTINGS
# =========================

OPEN_ANGLE = [0.1, 0.2, 0.2, 0.1]     # natural slight bend
CLOSED_STRONG = [1.3, 1.4, 1.4, 1.3]  # strong curl
THUMB_CLOSED = [1.5, 1.5, 1.4, 1.3]   # thumb tuck
FULL_OPEN = [0.0, 0.0, 0.0, 0.0]

# Finger order:
# Index → Middle → Ring → Thumb

poses = {

    # ✊ ROCK
    "rock": (
        CLOSED_STRONG +
        CLOSED_STRONG +
        CLOSED_STRONG +
        THUMB_CLOSED
    ),

    # ✋ PAPER
    "paper": (
        FULL_OPEN +
        FULL_OPEN +
        FULL_OPEN +
        FULL_OPEN
    ),

    # ✌️ SCISSORS
    "scissors": (
        OPEN_ANGLE +      # index
        OPEN_ANGLE +      # middle
        CLOSED_STRONG +   # ring
        THUMB_CLOSED      # thumb
    )
}

# Apply pose
def apply_pose(choice):
    data.ctrl[:] = poses[choice]

# Result logic
def decide(user, system):
    if user == system:
        return "Draw"
    elif (user == "rock" and system == "scissors") or \
         (user == "paper" and system == "rock") or \
         (user == "scissors" and system == "paper"):
        return "User Wins"
    else:
        return "System Wins"

# Track last system move (to avoid repeat)
last_system = None

# =========================
# MAIN LOOP
# =========================
with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():

        user = input("Enter rock/paper/scissors: ").strip().lower()

        if user not in poses:
            print("Invalid input, try again.")
            continue

        # 🔥 NO-REPEAT RANDOM SYSTEM
        choices = ["rock", "paper", "scissors"]

        if last_system in choices:
            choices.remove(last_system)

        system = random.choice(choices)
        last_system = system

        print(f"User: {user} | System: {system}")

        # Reset simulation
        mujoco.mj_resetData(model, data)

        # Apply pose
        apply_pose(system)

        # Run simulation
        for _ in range(300):
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(0.02)

        print("Result:", decide(user, system))