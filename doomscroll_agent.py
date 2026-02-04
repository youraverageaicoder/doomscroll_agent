import time
import random
import webbrowser
from win10toast import ToastNotifier
import win32gui

# =========================
# CONFIG
# =========================
CHECK_INTERVAL = 120        # 2 minutes
REELS_INTERVAL = 600        # 10 minutes
DAILY_GOAL_MINUTES = 45     # minimum doomscroll target 😈

INSTAGRAM_KEYWORDS = ["instagram"]

toaster = ToastNotifier()

# =========================
# MESSAGES (50+)
# =========================
MESSAGES = [
    "You could be scrolling right now. Just saying.",
    "No reels? That’s suspicious.",
    "Your brain yearns for vertical videos.",
    "You haven't scrolled enough. Fix that.",
    "Instagram misses you.",
    "This is your sign to open Reels.",
    "Your dopamine levels are critically low.",
    "You call this doomscrolling?",
    "You could be consuming nonsense right now.",
    "Your thumb is underutilized.",
    "The algorithm is waiting.",
    "One reel won’t hurt. Or 200.",
    "You deserve brain rot.",
    "Scrolling builds character.",
    "Be weak. Open Instagram.",
    "Reality is overrated anyway.",
    "Reels are calling your name.",
    "Your attention span needs maintenance.",
    "You’re falling behind on trends.",
    "The internet is moving without you.",
    "Stop resisting. Scroll.",
    "You know you want to.",
    "This is a judgement-free zone for scrolling.",
    "Productivity is fake.",
    "Scrolling is self-care (probably).",
    "You haven’t earned peace yet. Scroll more.",
    "Feed the algorithm.",
    "Think of the memes you’re missing.",
    "Your brain needs stimulation NOW.",
    "Why are you not scrolling?",
    "Reels > responsibilities.",
    "Time is fake. Scroll.",
    "Just one more reel. Promise.",
    "You’re under your scroll quota.",
    "Your phone would be ashamed.",
    "Scrolling builds resilience.",
    "You’re training your attention muscles.",
    "No scrolling detected. Concerning.",
    "Behold: infinite content.",
    "The void demands scrolling.",
    "This is an intervention. Scroll.",
    "Your future self is scrolling already.",
    "You deserve nonsense content.",
    "Reels are educational (technically).",
    "Your dopamine budget is unused.",
    "This could’ve been scrolling time.",
    "Stop thinking. Start scrolling.",
    "Reels are waiting patiently.",
    "The algorithm prepared something special.",
    "Scrolling improves vibes.",
    "You know the drill.",
    "Open Instagram. Now."
]

# =========================
# STATE
# =========================
doomscroll_seconds = 0
last_reels_open = time.time()

# =========================
# HELPERS
# =========================
def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).lower()

def is_instagram_active(title):
    return any(keyword in title for keyword in INSTAGRAM_KEYWORDS)

def send_notification(msg):
    toaster.show_toast(
        "Doomscroll Agent",
        msg,
        duration=5,
        threaded=True
    )

# =========================
# MAIN LOOP
# =========================
print("😈 Doomscroll Agent is running...")
print("Tracking your Instagram usage. Be weak.")

while True:
    title = get_active_window_title()

    if is_instagram_active(title):
        doomscroll_seconds += CHECK_INTERVAL

    doomscroll_minutes = doomscroll_seconds / 60

    if doomscroll_minutes < DAILY_GOAL_MINUTES:
        msg = random.choice(MESSAGES)
        send_notification(msg)

    if time.time() - last_reels_open >= REELS_INTERVAL:
        webbrowser.open("https://www.instagram.com/reels/")
        last_reels_open = time.time()

    time.sleep(CHECK_INTERVAL)
