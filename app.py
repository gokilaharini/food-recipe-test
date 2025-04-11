import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_indian_recipes.csv")

df = load_data()

st.title("🍛 Indian Recipe Explorer")
st.markdown("Search and explore healthy Indian recipes based on your preferences!")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filter Options")
    search = st.text_input("Search Dish Name")
    dietary_filter = st.selectbox("Filter by Dietary Info", options=["All"] + df['Dietary Info'].dropna().unique().tolist())

# Apply filters
filtered_df = df.copy()
if search:
    filtered_df = filtered_df[filtered_df['Dish Name'].str.contains(search, case=False)]

if dietary_filter != "All":
    filtered_df = filtered_df[filtered_df['Dietary Info'] == dietary_filter]

# Display recipes
st.subheader(f"🍽️ Showing {len(filtered_df)} Recipes")

for i, row in filtered_df.iterrows():
    with st.expander(f"{row['Dish Name']} (⭐ {row['Rating']})"):
        st.markdown(f"**🥗 Dietary Info:** {row['Dietary Info']}")
        st.markdown(f"**🧂 Ingredients:**\n{row['Ingredients']}")
        st.markdown(f"**👨‍🍳 Instructions:**\n{row['Instructions']}")
        st.markdown("---")
