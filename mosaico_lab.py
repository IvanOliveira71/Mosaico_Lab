import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="The Mosaico Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded")

# --- Custom CSS for Styling (Simulating the Medieval-Alchemy/Post-Modern Blend) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Roboto:wght@300;400;700&display=swap');

    .main-header {
        font-family: 'Cinzel Decorative', cursive;
        color: #8B4513; /* Earthy brown */
        text-align: center;
        padding: 20px;
        background: linear-gradient(to right, #f0e68c, #eedd82); /* Light gold/parchment */
        border-bottom: 3px solid #8B4513;
        margin-bottom: 30px;
        font-size: 3.5em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stApp {
        background-color: #FDF5E6; /* Old paper background */
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #D2B48C; /* Tan/parchment for sidebar */
        padding: 20px;
        border-right: 2px solid #8B4513;
    }
    .stButton>button {
        background-color: #6A5ACD; /* Slate blue for buttons */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        font-family: 'Roboto', sans-serif;
    }
    .stButton>button:hover {
        background-color: #483D8B; /* Darker slate blue */
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel Decorative', cursive;
        color: #556B2F; /* Dark Olive Green for headings */
    }
    p, li, .stText {
        font-family: 'Roboto', sans-serif;
        line-height: 1.6;
        color: #444;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: nowrap;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        background-color: #D2B48C;
        border: 1px solid #8B4513;
        color: #556B2F;
        font-family: 'Cinzel Decorative', cursive;
        font-size: 1.1em;
        transition: background-color 0.3s, color 0.3s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #8B4513;
        color: white;
        border-bottom: none;
    }
    .chat-message {
        background-color: #FFFACD; /* Lemon chiffon for chat bubbles */
        border-radius: 15px;
        padding: 10px 15px;
        margin-bottom: 10px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        font-family: 'Roboto', sans-serif;
    }
    .user-message {
        text-align: right;
        background-color: #E0FFFF; /* Light cyan for user message */
    }
    .bot-message {
        text-align: left;
    }
    .leaderboard-item {
        background-color: #F8F8FF; /* Ghost white */
        border-left: 5px solid #FFD700; /* Gold highlight */
        padding: 10px;
        margin-bottom: 8px;
        border-radius: 5px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Roboto', sans-serif;
    }
    .monetization-card {
        background-color: #ADD8E6; /* Light blue */
        border-left: 5px solid #4682B4; /* Steel blue */
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 8px;
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo Placeholder (You'd replace this with an actual image) ---
# To create a logo that conveys seriousness and collaboration, consider:
# - A stylized atom or scientific symbol intertwined with hands shaking or gears meshing.
# - A classic scientific element (e.g., a beaker, microscope) integrated with abstract, flowing lines representing connection and dynamism.
# - A crest-like design with scientific motifs and perhaps a subtle alchemical symbol.
# - Colors: Deep blues/greens for seriousness, gold/bronze for prestige and warmth.
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <img src="https://via.placeholder.com/200x100?text=The+Mosaico+Lab+Logo" alt="The Mosaico Lab Logo" style="max-width: 100%; height: auto;">
        <h1 class="main-header">The Mosaico Lab</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Isaaic (Bot) Functionality ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": "bot", "content": "Welcome, esteemed scientist, to The Mosaico Lab! I am Isaaic, your guide and companion in this digital realm of Eureka. What piques your scientific curiosity today?"})

def isaaic_response(user_input):
    user_input_lower = user_input.lower()
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Greetings! It's always a pleasure to meet new minds. How can I assist your journey into scientific discovery?"
    elif "mosaico lab" in user_input_lower or "eureka" in user_input_lower:
        return "The Mosaico Lab is a beacon for brilliant minds like yours, nestled in the digital village of Eureka. Here, we foster collaboration, innovation, and career growth. Explore our boroughs to see what awaits!"
    elif "tavern" in user_input_lower:
        return "Ah, The Tavern! A bustling hub for lively discussions on current scientific news and trends. Pull up a chair and join the intellectual feast!"
    elif "agora" in user_input_lower:
        return "The Agora is where ideas blossom! Promote your research, seek collaborators, and bring your visions to fruition. What grand ideas do you wish to share?"
    elif "oracle" in user_input_lower:
        return "At The Oracle, wisdom flows freely from our super experts. Seek their guidance, gain profound insights, and illuminate your path to scientific mastery."
    elif "lab" in user_input_lower:
        return "The Lab, the very heart of Mosaico! Here, you'll find state-of-the-art digital facilities to conduct your experiments and develop your scientific pursuits. What will you create?"
    elif "gamified" in user_input_lower or "rewards" in user_input_lower:
        return "Our gamified system celebrates your contributions! Engage, collaborate, and ascend the ranks to earn recognition and unlock new opportunities."
    elif "money" in user_input_lower or "monetized" in user_input_lower:
        return "Indeed! The Mosaico Lab offers unique ways to earn local currency, which can even be traded in the real world. Prestige lending is just one example of how we empower innovative minds."
    elif "thanks" in user_input_lower or "thank you" in user_input_lower:
        return "You're most welcome! My purpose is to facilitate your Mosaico Lab experience. Is there anything else I can clarify?"
    else:
        return "Fascinating! Your query sparks new thoughts. While I ponder that, perhaps you'd like to explore one of our boroughs or discuss a trendy scientific topic?"

# --- Sidebar for Isaaic Chat ---
with st.sidebar:
    st.markdown("<h3><img src='https://i.imgur.com/your_isaaic_avatar_link.png' alt='Isaaic Avatar' style='width: 30px; height: 30px; vertical-align: middle; margin-right: 10px;'>Chat with Isaaic</h3>", unsafe_allow_html=True)
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div class='chat-message user-message'><strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message bot-message'><strong>Isaaic:</strong> {message['content']}</div>", unsafe_allow_html=True)

    user_query = st.text_input("Ask Isaaic anything:", key="isaaic_input")
    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        st.session_state.chat_history.append({"role": "bot", "content": isaaic_response(user_query)})
        # Refresh the sidebar to show the new messages
        st.rerun

# --- Main Content - Borough Pages ---
st.markdown("## Explore the Boroughs of Eureka")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "The Tavern", "The Agora", "The Oracle", "The Lab", "Community & Economy"])

with tab1:
    st.markdown("### Welcome to The Mosaico Lab, Scientist!")
    st.write(
        """
        Dive into a unique digital experience where cutting-edge science meets a rich, community-driven atmosphere. 
        The Mosaico Lab is your hub for **peer support, career development, idea sharing, and unparalleled collaboration opportunities**. 
        Connect with brilliant minds, discuss trendy topics, and stay informed about grants and scholarships.
        """
    )
    st.image("https://via.placeholder.com/800x400?text=Welcome+to+The+Mosaico+Lab", caption="A Glimpse into Eureka Village")
    st.markdown(
        """
        Our design combines the serious elegance of post-modern aesthetics with the mysterious charm of medieval alchemy, 
        creating an inspiring backdrop for your scientific endeavors.
        """
    )
    st.subheader("What Awaits You:")
    st.markdown(
        """
        - **Isaaic, Your Guide**: Our intelligent avatar bot is here to welcome you and keep the conversation flowing.
        - **Four Distinct Boroughs**: Each offers a unique space for interaction and growth.
        - **Gamified Rewards**: Earn recognition and prestige for your contributions and collaborations.
        - **Monetized Interactions**: Discover new ways to leverage your expertise and support groundbreaking ideas.
        """
    )
    st.info("Ready to begin your journey? Explore the tabs above to visit our unique boroughs!")

with tab2:
    st.markdown("### The Tavern: Where Ideas Brew and News Flows")
    st.write(
        """
        Step into **The Tavern**, the vibrant social heart of The Mosaico Lab. This is where scientists from all disciplines 
        congregate to discuss the latest breakthroughs, debate trendy topics, and share their insights on current scientific news. 
        Whether it's a new publication, a controversial theory, or a fascinating discovery, The Tavern is the place to hear it first and share your thoughts.
        """
    )
    st.image("https://via.placeholder.com/700x350?text=The+Tavern+Scene", caption="Lively Discussions at The Tavern")

    st.subheader("Current Discussions:")
    discussions = [
        {"topic": "The Future of AI in Scientific Discovery", "participants": 15},
        {"topic": "Ethical Considerations in Genetic Engineering", "participants": 10},
        {"topic": "Breakthroughs in Quantum Computing", "participants": 8},
        {"topic": "Climate Change Solutions: A Global Perspective", "participants": 12},
    ]

    for d in discussions:
        st.markdown(f"**{d['topic']}** - *{d['participants']} active participants*")
        st.write("Join the conversation and add your voice!")
        st.button(f"Join {d['topic']}", key=f"join_tavern_{d['topic']}")
        st.markdown("---")

    st.subheader("Start a New Discussion:")
    new_topic = st.text_input("Propose a new topic for discussion:")
    if st.button("Start Discussion"):
        if new_topic:
            st.success(f"'{new_topic}' has been added to The Tavern discussions! Be the first to spark a conversation.")
        else:
            st.warning("Please enter a topic to start a new discussion.")

with tab3:
    st.markdown("### The Agora: Promote Your Ideas, Find Your Collaborators")
    st.write(
        """
        Welcome to **The Agora**, the bustling marketplace of ideas within The Mosaico Lab. 
        This is your dedicated space to showcase the projects you're passionate about, 
        seek out like-minded scientists for collaboration, and find the resources needed to bring your visions to life. 
        Whether you're looking for a theoretical physicist, a data scientist, or a molecular biologist, The Agora connects you.
        """
    )
    st.image("https://via.placeholder.com/700x350?text=The+Agora+Marketplace", caption="Ideas on Display at The Agora")

    st.subheader("Featured Projects Seeking Collaboration:")
    projects = [
        {"name": "Quantum Entanglement for Secure Communication", "author": "Dr. Elena Vance", "skills_needed": "Quantum Physicists, Cryptographers"},
        {"name": "AI-Driven Drug Discovery Platform", "author": "Prof. Jian Li", "skills_needed": "Machine Learning Engineers, Organic Chemists"},
        {"name": "Sustainable Energy Solutions from Algae", "author": "Dr. Sofia Rodriguez", "skills_needed": "Bioengineers, Environmental Scientists"},
    ]

    for p in projects:
        st.markdown(f"**Project: {p['name']}**")
        st.write(f"**By:** {p['author']}")
        st.write(f"**Skills Needed:** {p['skills_needed']}")
        st.button(f"Learn More & Collaborate on {p['name']}", key=f"collaborate_{p['name']}")
        st.markdown("---")

    st.subheader("Promote Your Own Idea:")
    with st.form("new_project_form"):
        project_title = st.text_input("Your Project Title:")
        project_description = st.text_area("Brief Description of Your Project:")
        skills_required = st.text_input("Skills/Expertise You're Looking For (e.g., 'Biochemists, Statisticians'):")
        submit_project = st.form_submit_button("Submit Your Project")
        if submit_project:
            if project_title and project_description and skills_required:
                st.success(f"Your project '{project_title}' has been listed on The Agora! Prepare for exciting collaborations.")
            else:
                st.warning("Please fill in all fields to promote your project.")

with tab4:
    st.markdown("### The Oracle: Illumination from Super Experts")
    st.write(
        """
        Enter **The Oracle**, a sacred space within The Mosaico Lab where unparalleled wisdom awaits. 
        Here, you can connect with **super experts** – luminaries in their respective fields – who offer invaluable mentorship, 
        profound insights, and personalized guidance to elevate your scientific journey. 
        Whether you're grappling with a complex problem, seeking career advice, or simply craving deeper understanding, The Oracle is your source.
        """
    )
    st.image("https://via.placeholder.com/700x350?text=The+Oracle+Wisdom", caption="Seeking Guidance at The Oracle")

    st.subheader("Our Esteemed Oracles:")
    oracles = [
        {"name": "Dr. Anya Sharma", "field": "Neuroscience, Cognitive Science", "focus": "Brain-computer interfaces, neural networks"},
        {"name": "Prof. Marcus Thorne", "field": "Particle Physics, Cosmology", "focus": "Dark matter, quantum gravity"},
        {"name": "Dr. Lena Petrova", "field": "Genomics, Bioinformatics", "focus": "CRISPR technology, personalized medicine"},
    ]

    for oracle in oracles:
        st.markdown(f"**{oracle['name']}** - *{oracle['field']}*")
        st.write(f"**Expertise:** {oracle['focus']}")
        st.button(f"Request Mentorship from {oracle['name']}", key=f"mentor_{oracle['name']}")
        st.markdown("---")

    st.subheader("Submit Your Query to an Oracle:")
    with st.form("oracle_query_form"):
        mentor_choice = st.selectbox("Select an Oracle:", [o['name'] for o in oracles])
        your_question = st.text_area(f"Your question for {mentor_choice}:")
        submit_query = st.form_submit_button("Send Query")
        if submit_query:
            if your_question:
                st.success(f"Your question has been sent to {mentor_choice}. They will review it and respond soon!")
            else:
                st.warning("Please enter your question for the Oracle.")

with tab5:
    st.markdown("### The Lab: Your State-of-the-Art Scientific Workspace")
    st.write(
        """
        Welcome to **The Lab**, the undisputed heart of The Mosaico Lab. This is where real science happens in the digital realm. 
        Equipped with **state-of-the-art digital facilities**, The Lab provides you with the tools and environment 
        necessary to develop your research, run simulations, analyze data, and bring your scientific projects to fruition. 
        Think of it as your personal, highly advanced, virtual research institute.
        """
    )
    st.image("https://via.placeholder.com/700x350?text=The+Lab+Workspace", caption="Innovate and Discover at The Lab")

    st.subheader("Available Digital Facilities:")
    facilities = [
        {"name": "High-Performance Computing Cluster", "description": "For complex simulations and data processing."},
        {"name": "Virtual Reality Experimentation Suite", "description": "Design and execute virtual experiments in immersive environments."},
        {"name": "Collaborative Data Visualization Tools", "description": "Analyze and present your data with peers in real-time."},
        {"name": "AI-Powered Research Assistant", "description": "Automate literature reviews, hypothesis generation, and experimental design."},
    ]

    for facility in facilities:
        st.markdown(f"**{facility['name']}**")
        st.write(f"*{facility['description']}*")
        st.button(f"Access {facility['name']}", key=f"access_lab_{facility['name']}")
        st.markdown("---")

    st.subheader("Start a New Experiment/Project:")
    with st.form("new_lab_project_form"):
        lab_project_title = st.text_input("Your Lab Project Title:")
        lab_project_description = st.text_area("Outline your experimental design or project goals:")
        required_facilities = st.multiselect("Select facilities you need:", [f['name'] for f in facilities])
        start_project = st.form_submit_button("Initiate Project")
        if start_project:
            if lab_project_title and lab_project_description and required_facilities:
                st.success(f"Project '{lab_project_title}' initiated! You now have access to the selected facilities for your research.")
            else:
                st.warning("Please fill in all details and select required facilities to start your project.")

with tab6:
    st.markdown("### Community & Economy: Rewards, Prestige, and Prosperity")
    st.write(
        """
        The Mosaico Lab thrives on interaction and collaboration, and we believe in recognizing and rewarding your contributions! 
        Our **gamified rewarding system** celebrates active participation, elevates your standing, and unlocks exciting opportunities. 
        Beyond reputation, we offer unique **monetized interactions**, allowing you to earn local currency that holds real-world value.
        """
    )
    st.image("https://via.placeholder.com/700x350?text=Rewards+and+Economy", caption="The Ecosystem of Mosaico Lab's Economy")

    st.subheader("The Gamified Rewarding System:")
    st.markdown(
        """
        Every interaction, every collaboration, every insightful discussion contributes to your standing in The Mosaico Lab. 
        Climb the ranks, unlock badges, and gain access to exclusive features and resources.
        """
    )
    st.markdown("#### Top Contributors (Leaderboard):")
    leaderboard = [
        {"name": "Dr. Ada Lovelace", "points": 1250, "rank": "Grand Alchemist"},
        {"name": "Prof. Nikola Tesla", "points": 1100, "rank": "Master Innovator"},
        {"name": "Dr. Marie Curie", "points": 980, "rank": "Senior Investigator"},
    ]
    for item in leaderboard:
        st.markdown(f"<div class='leaderboard-item'><span>**{item['name']}** ({item['rank']})</span> <span>{item['points']} Points</span></div>", unsafe_allow_html=True)

    st.subheader("Monetized Interactions & Mosaico Coins (MC):")
    st.write(
        """
        The Mosaico Lab introduces **Mosaico Coins (MC)**, our internal currency. You can earn MC through various activities:
        """
    )
    st.markdown(
        """
        * **Contribution Rewards**: Earn MC for high-quality posts, successful collaborations, and impactful mentorships.
        * **Prestige Lending**: Higher-ranked residents can "lend" their prestige (for a fee in MC) to promising ideas or less visible scientists, boosting their exposure.
        * **Bounty Programs**: Complete specific research tasks or challenges posed by other members or the community itself for MC rewards.
        * **Service Exchange**: Offer specialized scientific services (e.g., data analysis, statistical consulting) to other members for MC.
        """
    )
    st.markdown(
        """
        Eventually, accumulated Mosaico Coins can be traded for real-world value, providing tangible benefits for your digital contributions.
        """
    )
    
    st.markdown("<div class='monetization-card'><h4>Prestige Lending Example:</h4><p>Dr. Ada Lovelace (Grand Alchemist) lends her prestige to a groundbreaking research proposal by Dr. Newcomer. Dr. Newcomer's idea gains immediate visibility and funding interest, while Dr. Lovelace earns Mosaico Coins for her endorsement.</p></div>", unsafe_allow_html=True)

    st.subheader("Your Mosaico Wallet:")
    current_mc = st.number_input("Your Current Mosaico Coins:", value=500, disabled=True)
    st.write(f"You have **{current_mc} MC**. Keep contributing to earn more!")
    
    if st.button("Learn More about MC Exchange"):
        st.info("Information on how to exchange Mosaico Coins for real-world value will be provided in a dedicated section soon!")

# --- Footer (Optional) ---
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; color: #777; font-size: 0.9em;">
        The Mosaico Lab © 2025. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)
