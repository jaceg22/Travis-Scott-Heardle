import os
import re

# Your list of clean song titles
song_titles = [
    "16.Chapels", "Hell of a Night", "SIRENS", "3500", "High.Fashion.Ft.Future",
    "SKELETONS", "5% TINT", "High.Fashion", "SKITZO",
    "90210", "Highest in the Room", "STARGAZING", "A -Team", "I Can Tell",
    "STOP TRYING TO BE GOD", "ASTROTHUNDER", "I KNOW ?", "Skyfall",
    "Antidote", "I KNOW ？", "Sloppy Toppy", "Apple Pie", "Impossible",
    "TELEKINESIS", "BUTTERFLY EFFECT", "K-POP", "THANK GOD",
    "Back.On.It", "KICK OUT", "THE SCOTTS", "Backyard", "LOOOVE",
    "TIL FURTHER NOTICE", "Bad.Mood.Shit.On.You", "LOST FOREVER", "TOPIA TWINS",
    "Bandz", "MAFIA", "The Prayer", "Basement Freestyle", "MELTDOWN",
    "The.Curse", "Blame", "MIA", "Trance",
    "Blocka.La.Flame", "MODERN JAM", "Travis Scott - BACC (Bonus) (Official Audio)",
    "CAN'T SAY", "MY EYES", "Up.Top", "CAROUSEL", "Mamacita", "Upper.Echelon",
    "CHAMPAIN & VACAY", "Maria.I.m.Drunk", "Uptown", "CIRCUS MAXIMUS",
    "Mo City Flexologist", "WAKE UP", "COFFEE BEAN", "NC-17", "WHO? WHAT!",
    "DA WIZARD", "NO BYSTANDERS", "Watch", "DELRESTO (ECHOES)", "Naked",
    "YOSEMITE", "DUMBO", "Never.Catch.Me", "Zombies",
    "Dance on the Moon", "Nightcrawler", "biebs in the trap", "Don't Play",
    "Only 1", "coordinate", "Drive", "Overdue", "first.take",
    "Drugs.You.Should.Try.It", "PARASAIL", "goosebumps", "ESCAPE PLAN",
    "PBT", "guidance", "FE!N", "Pornography", "outside",
    "FLORIDA FLOW", "Pray.4.Love", "sdp interlude", "First.Class",
    "Quintana Pt. 2", "sweet.sweet", "GOD'S COUNTRY", "Quintana", "the ends",
    "Grey", "R.I.P. SCREW", "through the late night", "HOUSTONFORNICATION",
    "Raindrops (Insane)", "way.back", "HYAENA", "SICKO MODE", "wonderful"
]

# Folder containing your MP3 files
folder_path = "/Users/jacegandhi/Desktop/TravisScottHeardle/new-songs"

def normalize_text(text):
    """Remove special chars and lowercase for comparison"""
    return re.sub(r'[^a-z0-9]', '', text.lower())

def find_matching_title(filename, titles):
    """Find which song title matches the filename"""
    filename_normalized = normalize_text(filename)
    
    for title in titles:
        title_normalized = normalize_text(title)
        if title_normalized in filename_normalized:
            return title
    return None

# Get all MP3 files in the folder
mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

print(f"Found {len(mp3_files)} MP3 files\n")

# Rename files
renamed_count = 0
for filename in mp3_files:
    # Find matching song title
    matching_title = find_matching_title(filename, song_titles)
    
    if matching_title:
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{matching_title}.mp3"
        new_path = os.path.join(folder_path, new_filename)
        
        # Only rename if the name is different
        if filename != new_filename:
            # Check if target file already exists
            if os.path.exists(new_path):
                print(f"⚠️  SKIP: {new_filename} already exists")
            else:
                os.rename(old_path, new_path)
                print(f"✅ Renamed: {filename} → {new_filename}")
                renamed_count += 1
        else:
            print(f"✓  Already correct: {filename}")
    else:
        print(f"❌ No match found: {filename}")

print(f"\n✨ Done! Renamed {renamed_count} files.")