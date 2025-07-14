<h1>🧠 Reddit User Persona Generator</h1>
This project scrapes Reddit user activity and uses Google Gemini (LLM) to generate rich, citation-backed user personas — ideal for research, UX design, and AI applications.

<h3>📌 Task Objective (per BeyondChats)</h3>
Build a script that:

Takes a Reddit user profile URL as input

Scrapes posts and comments

Generates a qualitative user persona

Cites exact comments/posts for each personality trait

Outputs everything in a .txt file

<h3>💡 Tech Stack</h3>
Python

praw (Reddit API)

google-generativeai (Gemini API)

python-dotenv for secure API key handling


<h2>🚀 How to Run</h2>

🔐 Step 1: Add API Keys

Create a .env file in the project root:
```bash
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=script:PersonaBuilder:v1.0 (by /u/your_reddit_username)
GEMINI_API_KEY=your_gemini_api_key
```

🔗 Get your API keys here:

Reddit: https://www.reddit.com/prefs/apps

Gemini: https://makersuite.google.com/app

⚙️ Step 2: Install Requirements
```bash
pip install -r requirements.txt
```
🧠 Step 3: Run the Script
```bash
python persona_generator.py https://www.reddit.com/user/kojied/
```
Outputs will be saved to the personas/ folder.

<h3>📂 Project Structure </h3>

```bash
reddit-persona-generator/
├── persona_generator.py       # Main script
├── reddit_scraper.py          # PRAW-based Reddit scraper
├── persona_builder.py         # Gemini persona generation logic
├── utils.py                   # Helpers: saving, cleaning, formatting
├── personas/                  # Output .txt files
│   ├── kojied_persona.txt
│   └── Hungry-Move-6603_persona.txt
├── sample_data/               # Optional raw scraped data (JSON)
├── requirements.txt
├── .env                       # [NOT included in repo]
├── .gitignore
└── README.md
```

<h3>📝 Sample Outputs</h3>
<h4>Check the following files under /personas/:</h4>
kojied_persona.txt

Hungry-Move-6603_persona.txt

Each contains:

Interests

Personality traits

Writing style

Values

Cited quotes with Reddit URLs

<h3>📜 Notes</h3>

Follows PEP-8 coding style

Modular code (scraper, builder, utils separated)

Works with free-tier Gemini & Reddit API keys

Does not push .env (uses .gitignore)

<h3>✨ Created For</h3>
BeyondChats – Generative AI Engineer Internship Assignment
Developed by Chetan Sonawane

<h3>🔒 Disclaimer</h3>
This project only uses public Reddit data. No login, posting, or scraping of private content is performed.
