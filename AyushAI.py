import streamlit as st

# ---------------------------
# 🌿 AyushAI - Nature Cure App
# ---------------------------

# Page config
st.set_page_config(page_title="AyushAI - Nature Cure", page_icon="🌱", layout="wide")

# Header
st.title("🌿 AyushAI - Traditional Nature Cure")
st.write("Your AI-powered assistant for *natural healing, diet planning, and wellness guidance.*")

# Sidebar navigation
st.sidebar.title("🔍 Menu")
choice = st.sidebar.radio("Go to:", ["Home", "Disease & Cure", "Diet Plan", "Daily Practices", "Consultation"])

# ---------------------------
#  Home
# ---------------------------
if choice == "Home":
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965567.png", width=120)
    st.subheader("Welcome to AyushAI!")
    st.write("""
    🌱 *AyushAI* is a student project that demonstrates how *AI + Tradition* can provide 
    simple, holistic health solutions.  
    - Get information about *diseases & cures*  
    - Personalized *diet suggestions*  
    - Recommended *daily practices*  
    - Option for *online consultation*  
    """)

# ---------------------------
#  Disease & Cure
# ---------------------------
elif choice == "Disease & Cure":
    st.header("🩺 Disease & Natural Cure")
    disease = st.text_input("Enter your health issue (e.g., Thyroid, Diabetes, Cold):")
    
    if st.button("Get Cure"):
        if disease.lower() == "thyroid":
            st.success("🌱 Cure for Thyroid:\n- Consume more iodine-rich foods\n- Practice yoga (Sarvangasana)\n- Avoid goitrogenic foods like cabbage, cauliflower.")
        elif disease.lower() == "diabetes":
            st.success("🌱 Cure for Diabetes:\n- Bitter gourd juice every morning\n- Fenugreek seeds soaked overnight\n- Regular walking and yoga.")
        elif disease.lower() == "cold":
            st.success("🌱 Cure for Cold:\n- Drink turmeric milk\n- Steam inhalation with eucalyptus oil\n- Tulsi + Honey tea twice daily.")
        else:
            st.warning("⚠ Sorry, cure info not available yet. (Demo Mode)")

# ---------------------------
#  Diet Plan
# ---------------------------
elif choice == "Diet Plan":
    st.header("🥗 Personalized Diet Plan")
    budget = st.slider("Select your monthly budget (₹)", 1000, 20000, 5000)
    st.write(f"Your selected budget: ₹{budget}")
    
    if budget < 3000:
        st.info("🍎 Budget Diet Plan: Seasonal fruits, sprouted pulses, buttermilk, green leafy veggies.")
    elif 3000 <= budget < 8000:
        st.info("🥗 Balanced Diet Plan: Include nuts, fresh fruits, milk, curd, millet-based diet.")
    else:
        st.info("🌟 Premium Diet Plan: Organic foods, exotic fruits, dry fruits, daily herbal supplements.")

# ---------------------------
#  Daily Practices
# ---------------------------
elif choice == "Daily Practices":
    st.header("🧘 Daily Wellness Practices")
    st.write("""
    ✅ Wake up early (Brahmamuhurta)  
    ✅ Drink warm water with lemon & honey  
    ✅ 20 mins Yoga/Pranayama  
    ✅ Eat fresh, seasonal foods  
    ✅ Avoid junk & processed food  
    ✅ Sleep 7-8 hours daily  
    """)

# ---------------------------
#  Consultation
# ---------------------------
elif choice == "Consultation":
    st.header("💬 Online Consultation")
    name = st.text_input("Enter your Name")
    problem = st.text_area("Describe your health issue")
    
    if st.button("Request Consultation"):
        if name and problem:
            st.success(f"✅ Thank you {name}! Your consultation request has been noted. A doctor will connect with you online soon. (Demo Mode)")
        else:
            st.warning("⚠ Please fill in your details first.")
