import streamlit as st
import time
from streamlit_extras.let_it_rain import rain
from streamlit_lottie import st_lottie
import requests
import json

# --- Page Config ---
st.set_page_config(
    page_title="Quantum AI | Next-Gen Solutions",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Load Lottie Animations ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            st.warning(f"Failed to load Lottie animation from {url}. Status code: {r.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading Lottie animation: {e}")
        return None

# Lottie files from https://lottiefiles.com/
lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")  # Replace with a working URL
lottie_rocket = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")  # Replace with a working URL

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
        /* Main Styles */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            background-attachment: fixed;
        }
        
        /* Typography */
        .big-title {
            font-size: 4.5rem;
            font-weight: 800;
            text-align: center;
            color: #ffffff;
            margin-bottom: 0;
            text-shadow: 0 0 10px rgba(255,255,255,0.3);
            letter-spacing: -0.5px;
            line-height: 1.2;
            background: linear-gradient(to right, #eeaeca 0%, #94bbe9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle {
            font-size: 1.5rem;
            text-align: center;
            color: rgba(255, 255, 255, 0.8);
            margin-top: 0.5rem;
            margin-bottom: 2rem;
            font-weight: 300;
        }
        
        /* Cards and Containers */
        .feature-card {
            border-radius: 16px;
            padding: 30px 25px;
            background: rgba(255, 255, 255, 0.05);
            text-align: center;
            color: #fff;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
            height: 100%;
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 35px 0 rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
            background: linear-gradient(to right, #ff7eb3 0%, #83a4d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .feature-card p {
            font-size: 1.1rem;
            opacity: 0.9;
            line-height: 1.6;
        }
        
        /* Buttons */
        .cta-button {
            background: linear-gradient(90deg, #ff6b6b 0%, #ff8e8e 100%);
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            padding: 12px 30px;
            border-radius: 50px;
            text-align: center;
            display: inline-block;
            margin: 1rem auto;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 10px 20px rgba(255, 107, 107, 0.3);
            text-decoration: none;
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 25px rgba(255, 107, 107, 0.4);
            background: linear-gradient(90deg, #ff8e8e 0%, #ff6b6b 100%);
        }
        
        /* Testimonial Section */
        .testimonial {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .testimonial-text {
            font-style: italic;
            color: #f0f0f0;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        
        .testimonial-author {
            color: #b8c4ff;
            font-weight: 600;
            margin-top: 15px;
            text-align: right;
        }
        
        /* Stats Section */
        .stat-container {
            text-align: center;
            padding: 20px;
        }
        
        .stat-number {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }
        
        .stat-label {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1.2rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            padding-top: 30px;
            padding-bottom: 20px;
            font-size: 0.9rem;
        }
        
        /* Custom divider */
        .divider {
            height: 4px;
            background: linear-gradient(90deg, rgba(255,107,107,0.8) 0%, rgba(147,183,227,0.8) 100%);
            border-radius: 4px;
            margin: 40px 0;
            width: 100%;
        }
        
        /* Counter animation */
        @keyframes count-up {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate-count {
            animation: count-up 1s ease forwards;
        }
        
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Header text styles */
        h2 {
            font-size: 2.5rem;
            text-align: center;
            color: #ffffff;
            margin-top: 2rem;
            margin-bottom: 2rem;
            font-weight: 700;
        }
        
        /* Section spacing */
        .section {
            padding: 3rem 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero Section ---
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h1 class="big-title">Quantum AI Solutions</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Transform your business with next-generation artificial intelligence technology</p>', unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            if st.button("🚀 Get Started", key="get_started_btn", use_container_width=True):
                with st.spinner('Initializing AI environment...'):
                    time.sleep(1.5)
                st.success("Welcome aboard! Your AI journey begins now.")
                rain(emoji="✨", font_size=20, falling_speed=5, animation_length=3)
        
        with col_btn2:
            if st.button("🎥 Watch Demo", key="watch_demo_btn", use_container_width=True):
                st.video("https://youtu.be/P7_SfxRrXTE?feature=shared")
                
    with col2:
        if lottie_ai:
            st_lottie(lottie_ai, height=300, key="lottie_ai")
        else:
            st.warning("Failed to load Lottie animation.")

# --- Divider ---
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Features Section ---
st.markdown("<h2>Why Choose Quantum AI?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class='feature-card'>
            <h3>🧠 Advanced Neural Networks</h3>
            <p>Our multi-layered neural architecture delivers 10x more accurate predictions than traditional AI models.</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='feature-card'>
            <h3>🔮 Predictive Analytics</h3>
            <p>Harness the power of future-forecasting algorithms to stay ahead of market trends and consumer behaviors.</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='feature-card'>
            <h3>🛡️ Enterprise Security</h3>
            <p>Bank-level encryption and continuous monitoring ensure your data remains protected at all times.</p>
        </div>
    """, unsafe_allow_html=True)

# --- Second Row of Features ---
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("""
        <div class='feature-card'>
            <h3>⚡ Lightning Fast</h3>
            <p>Process millions of data points in milliseconds with our optimized cloud infrastructure.</p>
        </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
        <div class='feature-card'>
            <h3>📱 Cross-Platform</h3>
            <p>Seamlessly integrate with your existing systems across web, mobile, and desktop environments.</p>
        </div>
    """, unsafe_allow_html=True)
with col6:
    st.markdown("""
        <div class='feature-card'>
            <h3>📊 Custom Dashboards</h3>
            <p>Visualize complex data patterns with interactive, personalized analytics dashboards.</p>
        </div>
    """, unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Statistics Section ---
st.markdown("<h2>Proven Results</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class='stat-container animate-count'>
            <div class='stat-number'>99.8%</div>
            <div class='stat-label'>Accuracy Rate</div>
        </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
        <div class='stat-container animate-count'>
            <div class='stat-number'>500+</div>
            <div class='stat-label'>Enterprise Clients</div>
        </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
        <div class='stat-container animate-count'>
            <div class='stat-number'>85%</div>
            <div class='stat-label'>Cost Reduction</div>
        </div>
    """, unsafe_allow_html=True)
    
with col4:
    st.markdown("""
        <div class='stat-container animate-count'>
            <div class='stat-number'>24/7</div>
            <div class='stat-label'>Support</div>
        </div>
    """, unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Testimonials Section ---
st.markdown("<h2>What Our Clients Say</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class='testimonial'>
            <p class='testimonial-text'>"Quantum AI transformed our decision-making process completely. We're now able to predict market trends with 95% accuracy and have increased our ROI by 300% in just six months."</p>
            <p class='testimonial-author'>— Sarah Johnson, CTO at TechGlobal</p>
        </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
        <div class='testimonial'>
            <p class='testimonial-text'>"The implementation was seamless, and the results were immediate. Our customer satisfaction scores have increased by 45% since integrating Quantum AI into our service platform."</p>
            <p class='testimonial-author'>— Michael Chen, Director of Innovation at NextGen Solutions</p>
        </div>
    """, unsafe_allow_html=True)

# --- Call to Action Section ---
st.markdown("<h2>Ready to Transform Your Business?</h2>", unsafe_allow_html=True)

# Center the CTA section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 1.2rem; color: #fff; margin-bottom: 20px;">Join hundreds of industry leaders already leveraging the power of Quantum AI</p>
            <a href="#" class="cta-button">Schedule a Demo</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Lottie animation
    if lottie_rocket:
        st_lottie(lottie_rocket, height=200, key="lottie_rocket")
    else:
        st.warning("Failed to load Lottie animation.")

# --- Footer ---
st.markdown("""
    <div class="footer">
        <p>© 2025 Quantum AI Solutions. All Rights Reserved.</p>
        <p>Privacy Policy | Terms of Service | Contact Us</p>
    </div>
    """, unsafe_allow_html=True)

# Add subtle rain effect for a limited time
rain(
    emoji="✨",
    font_size=15,
    falling_speed=3,
    animation_length=5,
)