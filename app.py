import streamlit as st

# ---------- Configuración de la página ----------
st.set_page_config(
    page_title="Conversor de Temperaturas",
    page_icon="🌡️",
    layout="centered"
)

# ---------- Funciones ----------
def celsius_a_fahrenheit(c: float) -> float:
    return c * 9.0 / 5.0 + 32.0

def fahrenheit_a_celsius(f: float) -> float:
    return (f - 32.0) * 5.0 / 9.0

# ---------- Interfaz ----------
st.title("🌡️ Conversor de Temperaturas")
st.write("Convierte fácilmente entre *Celsius* y *Fahrenheit*")

opcion = st.radio("Selecciona el tipo de conversión:", 
                  ("Celsius → Fahrenheit", "Fahrenheit → Celsius"))

if opcion == "Celsius → Fahrenheit":
    celsius = st.number_input("Temperatura en °C", value=0.0, step=0.1)
    fahrenheit = celsius_a_fahrenheit(celsius)
    st.success(f"{celsius:.2f} °C = {fahrenheit:.2f} °F")

else:
    fahrenheit = st.number_input("Temperatura en °F", value=32.0, step=0.1)
    celsius = fahrenheit_a_celsius(fahrenheit)
    st.success(f"{fahrenheit:.2f} °F = {celsius:.2f} °C")

st.caption("Aplicación creada con ❤️ usando Streamlit")
