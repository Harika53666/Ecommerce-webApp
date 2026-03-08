import streamlit as st

st.title("🛍️ Harika's Cute Shop")

# Create empty product list
if "products" not in st.session_state:
    st.session_state.products = []

menu = st.sidebar.selectbox("Menu", ["Home", "Add Product"])

# HOME PAGE
if menu == "Home":
    st.header("Available Products")

    if len(st.session_state.products) == 0:
        st.write("No products yet 😢")

    for product in st.session_state.products:
        st.image(product["image"], width=200)
        st.write(f"**{product['name']}**")
        st.write(f"Price: ₹{product['price']}")
        st.write("---")

# ADD PRODUCT PAGE
if menu == "Add Product":
    st.header("Add New Product")

    name = st.text_input("Enter Product Name")
    price = st.number_input("Enter Price", min_value=0)

    uploaded_image = st.file_uploader("Upload Product Image", type=["jpg", "png"])

    if st.button("Add Product"):
        if name and uploaded_image:
            st.session_state.products.append({
                "name": name,
                "price": price,
                "image": uploaded_image
            })
            st.success("Product Added Successfully 🎉")
        else:
            st.error("Please enter name and upload image")