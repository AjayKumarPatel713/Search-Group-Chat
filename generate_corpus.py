import random
from datetime import datetime, timedelta

# YAHAN create_decision_threads() FUNCTION

def create_decision_threads():
    threads = []

    # =========================
    # THREAD 1 - MANALI TRIP
    # =========================

    manali_messages = [
        ("Rahul", "Guys iss baar kuch proper plan krte hain, bas last moment cancel mat krna 😂"),
        ("Priya", "haan yaar, kahi pahado wali side chale?"),
        ("Aman", "Manali kaisa rahega?"),
        ("Neha", "Manali toh mast hai"),
        ("Rohit", "but budget ka kya scene hai?"),
        ("Priya", "around 8-10k per person possible hoga kya?"),
        ("Sneha", "hotel expensive hua toh problem hogi"),
        ("Vikash", "bus se chale toh cost kam ho jayegi"),
        ("Ananya", "Delhi se Volvo ka option bhi hai"),
        ("Rahul", "dates pehle decide kro"),
        ("Priya", "April second week mere liye ok hai"),
        ("Aman", "12-15 April?"),
        ("Neha", "13 ko meri class hai 😭"),
        ("Rohit", "11-14 kar lo"),
        ("Sneha", "Friday night nikal sakte hain"),
        ("Vikash", "Saturday morning tak pahuch jayenge"),
        ("Ananya", "hotel Mall Road ke paas lena better rahega"),
        ("Rahul", "Mall Road expensive hoga"),
        ("Priya", "thoda outside le lete hain, cab manage kar lenge"),
        ("Aman", "Solang Valley bhi cover karna hai"),
        ("Neha", "aur cafe hopping 😂"),
        ("Rohit", "bhai pehle hotel book karo"),
        ("Sneha", "maine ek decent hotel dekha hai"),
        ("Vikash", "kitna price?"),
        ("Sneha", "4 rooms around 24000 total"),
        ("Priya", "8 log hain toh 3k each hotel"),
        ("Rahul", "transport mila ke 8-9k aa jayega"),
        ("Aman", "mere hisab se manageable hai"),
        ("Neha", "same"),
        ("Rohit", "haan done"),
        ("Priya", "toh dates lock?"),
        ("Rahul", "11 April night departure"),
        ("Vikash", "14 ko return"),
        ("Ananya", "perfect"),
        ("Aman", "ticket mai check krta hu"),
        ("Neha", "hotel Sneha wala hi kar dete hain"),
        ("Rohit", "koi aur objection?"),
        ("Priya", "nahi"),
        ("Rahul", "chalo Manali fix hai")
    ]

    # =========================
    # THREAD 2 - PROJECT STACK
    # =========================

    project_messages = [
        ("Aman", "Next project ka stack decide karna hai"),
        ("Rahul", "Python toh fixed rakho"),
        ("Priya", "frontend ke liye React use kare?"),
        ("Neha", "React thoda time consuming hoga"),
        ("Rohit", "Streamlit bhi option hai"),
        ("Sneha", "agar ML project hai toh Streamlit easy rahega"),
        ("Vikash", "backend FastAPI kar sakte hain"),
        ("Ananya", "FastAPI + Streamlit sounds good"),
        ("Rahul", "database ka kya?"),
        ("Priya", "SQLite initially enough hai"),
        ("Aman", "production ke liye PostgreSQL better hai"),
        ("Neha", "but abhi prototype banana hai"),
        ("Rohit", "haan unnecessary complexity mat lao"),
        ("Sneha", "deployment bhi easy hona chahiye"),
        ("Vikash", "Streamlit cloud ka option hai"),
        ("Ananya", "FastAPI ko separately deploy kar sakte hain"),
        ("Rahul", "Docker add kare?"),
        ("Priya", "time mile toh"),
        ("Aman", "pehle core functionality"),
        ("Neha", "testing bhi important hai"),
        ("Rohit", "API documentation FastAPI automatically de dega"),
        ("Sneha", "nice"),
        ("Vikash", "React ka kya final?"),
        ("Rahul", "mujhe lagta hai React ki zarurat nahi"),
        ("Ananya", "agree"),
        ("Priya", "Streamlit enough for demo"),
        ("Aman", "backend FastAPI"),
        ("Neha", "Python ML pipeline"),
        ("Rohit", "SQLite"),
        ("Sneha", "simple and fast"),
        ("Vikash", "toh final stack confirm?"),
        ("Rahul", "Python + FastAPI + Streamlit + SQLite"),
        ("Priya", "yes"),
        ("Aman", "done"),
        ("Ananya", "lets build")
    ]

    # =========================
    # THREAD 3 - EVENT VENUE
    # =========================

    event_messages = [
        ("Neha", "Guys farewell ka venue decide karna hai"),
        ("Priya", "restaurant ya banquet?"),
        ("Rahul", "restaurant better lag raha"),
        ("Aman", "banquet me space zyada milega"),
        ("Sneha", "budget kitna hai?"),
        ("Rohit", "around 1500 per person max"),
        ("Vikash", "restaurant me ho jayega"),
        ("Ananya", "parking ka bhi dekhna"),
        ("Neha", "haan parking compulsory"),
        ("Priya", "main 3 places check karti hu"),
        ("Rahul", "City Center wala kaisa hai?"),
        ("Aman", "thoda expensive hai"),
        ("Sneha", "Railway Road side ek place hai"),
        ("Rohit", "reviews kaise hain?"),
        ("Vikash", "food reviews ache hain"),
        ("Ananya", "but parking small hai"),
        ("Neha", "then reject"),
        ("Priya", "ek aur place Ring Road pe mila"),
        ("Rahul", "price?"),
        ("Priya", "1300 per head including dinner"),
        ("Aman", "parking?"),
        ("Priya", "large parking"),
        ("Sneha", "location convenient hai"),
        ("Rohit", "music arrangement hai kya?"),
        ("Priya", "haan basic setup included"),
        ("Vikash", "sounds good"),
        ("Ananya", "timing kya milegi?"),
        ("Neha", "7 to 11 available"),
        ("Rahul", "perfect"),
        ("Aman", "advance kitna?"),
        ("Priya", "30 percent"),
        ("Sneha", "reasonable"),
        ("Rohit", "food menu check kar liya?"),
        ("Priya", "veg + nonveg dono options hain"),
        ("Vikash", "cake outside allowed?"),
        ("Priya", "yes"),
        ("Ananya", "then no issue"),
        ("Neha", "final kar dein?"),
        ("Rahul", "mere side se yes"),
        ("Aman", "same"),
        ("Sneha", "done"),
        ("Neha", "Ring Road wala venue final karte hain")
    ]

    thread_dates = [
        datetime(2026, 2, 15, 18, 0),
        datetime(2026, 4, 5, 19, 0),
        datetime(2026, 5, 20, 17, 30)
    ]

    all_threads = [
        (thread_dates[0], manali_messages),
        (thread_dates[1], project_messages),
        (thread_dates[2], event_messages)
    ]

    for start_time, messages in all_threads:

        current_time = start_time

        for sender, text in messages:

            threads.append({
                "datetime": current_time,
                "sender": sender,
                "message": text
            })

            current_time += timedelta(minutes=random.randint(2, 8))

    return threads


# --------------------------------------------------
# 1. Reproducibility
# --------------------------------------------------

random.seed(42)


# --------------------------------------------------
# 2. Group members
# --------------------------------------------------

participants = [
    "Rahul",
    "Priya",
    "Aman",
    "Neha",
    "Rohit",
    "Ananya",
    "Vikash",
    "Sneha"
]


# --------------------------------------------------
# 3. Message templates
# --------------------------------------------------

messages = [

    # Casual Hinglish
    "bhai kya scene hai?",
    "haan bhai",
    "okay done",
    "mai dekh leta hu",
    "kal bataunga",
    "haan sahi hai",
    "wait karo",
    "ek min",
    "lol 😂",
    "same bro",
    "bilkul",
    "theek hai",
    "done 👍",
    "haan karte hain",
    "dekho bhai",
    "mujhe bhi lagta hai",
    "kya plan hai?",
    "kab milna hai?",
    "aaj possible nahi hai",
    "kal karte hain",

    # Hinglish conversations
    "kal meeting ka kya scene hai?",
    "presentation ready hai?",
    "assignment submit kar diya?",
    "bhai notes bhej dena",
    "deadline kab hai?",
    "iska solution mila?",
    "mai check karta hu",
    "thoda wait karo",
    "ye wala better lag raha hai",
    "budget thoda zyada ho jayega",
    "location send kar do",
    "time confirm hai?",
    "sab log aa rahe ho?",
    "call pe discuss kar lete hain",
    "group me update kar dena",

    # English / code mixed
    "I will check this tonight",
    "Can you send the file?",
    "meeting at 5?",
    "let's discuss this tomorrow",
    "this looks good",
    "I think we should change this",
    "please send the link",
    "deadline is getting close",
    "we need to finalize this",
    "I'll handle this part",

    # Typos / messy text
    "haan krte h",
    "kal milte h",
    "bht sahi",
    "kya horha h?",
    "mai aa jaunga",
    "thoda late hoga",
    "brooo 😂",
    "okkk",
    "haan haan",
    "rukkk",
    "dekhta hu bhai",
    "samajh nhi aa rha",
    "ye sahi nhi lagrha",
    "krde bhai",
    "bhejdo pls",

    # Short replies
    "yes",
    "no",
    "maybe",
    "sure",
    "okay",
    "done",
    "haan",
    "nahi",
    "yup",
    "cool",
    "nice",
    "great",
]


# --------------------------------------------------
# 4. Forwarded messages
# --------------------------------------------------

forwarded_messages = [
    "Forwarded: Important announcement regarding tomorrow's event",
    "Forwarded: Please check the updated schedule",
    "Forwarded: College notice - deadline extended",
    "Forwarded: Weather update for this weekend",
    "Forwarded: Important travel advisory",
]


# --------------------------------------------------
# 5. Date range
# --------------------------------------------------

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 6, 30)


# --------------------------------------------------
# 6. Generate random date/time
# --------------------------------------------------

def random_datetime():

    total_days = (end_date - start_date).days

    random_days = random.randint(0, total_days)

    date = start_date + timedelta(days=random_days)

    hour = random.randint(8, 23)
    minute = random.randint(0, 59)

    return date.replace(
        hour=hour,
        minute=minute
    )


# --------------------------------------------------
# 7. Generate normal messages
# --------------------------------------------------

def generate_normal_message():

    sender = random.choice(participants)

    message = random.choice(messages)

    return sender, message


# --------------------------------------------------
# 8. Generate corpus
# --------------------------------------------------

TARGET_MESSAGES = 4000

chat_messages = []


for _ in range(TARGET_MESSAGES):

    date_time = random_datetime()

    sender, message = generate_normal_message()

    chat_messages.append(
        {
            "datetime": date_time,
            "sender": sender,
            "message": message
        }
    )


# --------------------------------------------------
# 9. Add forwarded messages
# --------------------------------------------------

for _ in range(30):

    date_time = random_datetime()

    sender = random.choice(participants)

    message = random.choice(forwarded_messages)

    chat_messages.append(
        {
            "datetime": date_time,
            "sender": sender,
            "message": message
        }
    )


# --------------------------------------------------
# 10. Sort messages chronologically
# --------------------------------------------------


decision_threads = create_decision_threads()
chat_messages.extend(decision_threads)


chat_messages.sort(
    key=lambda x: x["datetime"]
)


# --------------------------------------------------
# 11. Write WhatsApp-style chat export
# --------------------------------------------------

output_file = "data/chat.txt"


with open(output_file, "w", encoding="utf-8") as file:

    for item in chat_messages:

        dt = item["datetime"]

        date = dt.strftime("%d/%m/%Y")
        time = dt.strftime("%H:%M")

        file.write(
            f"{date}, {time} - "
            f"{item['sender']}: "
            f"{item['message']}\n"
        )


# --------------------------------------------------
# 12. Final information
# --------------------------------------------------

print("Corpus generated successfully!")
print("Total messages:", len(chat_messages))
print("Participants:", len(participants))
print("Start date:", start_date.strftime("%d/%m/%Y"))
print("End date:", end_date.strftime("%d/%m/%Y"))
print("Output:", output_file)