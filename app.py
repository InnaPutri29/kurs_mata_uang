# ===============================================
# 💵 Aplikasi Web Streamlit: Kurs Mata Uang terhadap USD
# ===============================================
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("💵 Kurs Mata Uang terhadap USD (Realtime)")

# Ambil data dari API
url = "https://v6.exchangerate-api.com/v6/1860a0e7fe868e4f9e744451/latest/USD"
data = requests.get(url).json()

# Transformasi data ke DataFrame
rates = data["conversion_rates"]
df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate_to_USD"])
df_sorted = df.sort_values(by="Rate_to_USD", ascending=False)

# Pilihan tampilan
st.subheader("Tabel Data Kurs")
st.dataframe(df_sorted)

# Visualisasi Top 10
st.subheader("📊 10 Mata Uang dengan Nilai Tukar Terbesar terhadap USD")
top10 = df_sorted.head(10)

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(top10["Currency"], top10["Rate_to_USD"], color="goldenrod")
ax.set_xlabel("Nilai Tukar terhadap USD")
ax.set_ylabel("Kode Mata Uang")
ax.set_title("10 Mata Uang dengan Nilai Tukar Terbesar terhadap USD")
ax.invert_yaxis()
st.pyplot(fig)

# Tombol download CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="💾 Download Data sebagai CSV",
    data=csv,
    file_name="exchange_rate_usd.csv",
    mime="text/csv"
)
