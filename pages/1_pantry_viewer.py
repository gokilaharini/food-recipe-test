import streamlit as st
from db_utils import init_db, get_ingredients, add_ingredient
from datetime import date

# Initialize DB
init_db()

st.title("🥬 Your Pantry")
st.markdown("Keep track of all your ingredients here!")

# 📋 Add new ingredient form
with st.expander("➕ Add New Ingredient"):
    with st.form("ingredient_form"):
        name = st.text_input("Ingredient Name")
        quantity = st.number_input("Quantity", min_value=0.0, step=0.1)
        unit = st.selectbox("Unit", ["g", "kg", "ml", "L", "pcs", "tbsp", "tsp"])
        expiry = st.date_input("Expiry Date", value=date.today())
        submit = st.form_submit_button("Add to Pantry")
        if submit:
            add_ingredient(name, quantity, unit, expiry.strftime("%Y-%m-%d"))
            st.success(f"{name} added!")

# 🧱 Display ingredients as cards
ingredients = get_ingredients()

if ingredients:
    st.subheader("🧾 Current Ingredients")

    cols = st.columns(2)
    for idx, ingredient in enumerate(ingredients):
        col = cols[idx % 2]
        with col:
            with st.container():
                st.markdown(f"### 🥣 {ingredient[1]}")
                st.markdown(f"- **Quantity:** {ingredient[2]} {ingredient[3]}")
                st.markdown(f"- **Expires:** {ingredient[4]}")
else:
    st.info("Your pantry is empty! Add some ingredients above. 🧂")
