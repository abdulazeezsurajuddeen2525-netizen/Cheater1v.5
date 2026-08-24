import streamlit as st

st.set_page_config(
    page_title="Basic Calculator",
    page_icon="🧮"
)

st.title("🧮 Basic Python Calculator")
st.write("Perform simple calculations quickly.")

# Calculator functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y


# User interface
operation = st.selectbox(
    "Select operation",
    ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"]
)

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    if operation == "Add (+)":
        result = add(num1, num2)
    elif operation == "Subtract (-)":
        result = subtract(num1, num2)
    elif operation == "Multiply (*)":
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Result: {result}")
