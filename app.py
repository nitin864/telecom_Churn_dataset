import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#setting page and title
st.set_page_config(page_title="Churn Dashboard", layout="wide")
st.title("Telecom Churn Dashboard")

#loading data
@st.cache_data
def load_data():
    df = pd.read_csv("dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    #fix charges
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)

    #here i converted senior citizen from binary value to yes or no
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

    return df

try:
    df = load_data()
except:
    st.error("Dataset not found")
    st.stop()

#added sidebar for filters
st.sidebar.header("Filters")

gender = st.sidebar.multiselect("Gender", df["gender"].unique(), default=df["gender"].unique())
contract = st.sidebar.multiselect("Contract", df["Contract"].unique(), default=df["Contract"].unique())
internet = st.sidebar.multiselect("Internet Service", df["InternetService"].unique(), default=df["InternetService"].unique())

filtered = df[
    (df["gender"].isin(gender)) &
    (df["Contract"].isin(contract)) &
    (df["InternetService"].isin(internet))
]

if filtered.empty:
    st.warning("No data available for selected filters")
    st.stop()

#metrics
total = len(filtered)
churned = (filtered["Churn"] == "Yes").sum()
rate = churned / total * 100

col1, col2, col3 = st.columns(3)
col1.metric("Customers", total)
col2.metric("Churned", churned)
col3.metric("Churn Rate", f"{rate:.1f}%")

st.divider()

#charts
st.subheader("Overview")

c1, c2 = st.columns(2)

#pie_chart
with c1:
    fig, ax = plt.subplots()
    filtered["Churn"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_title("Churn Distribution")
    ax.set_ylabel("")
    st.pyplot(fig)

# contract vs churn
with c2:
    churn_contract = filtered.groupby("Contract")["Churn"].apply(lambda x: (x=="Yes").mean()*100)
    fig, ax = plt.subplots()
    sns.barplot(x=churn_contract.index, y=churn_contract.values, ax=ax)
    ax.set_title("Churn by Contract")
    ax.set_ylabel("Churn %")
    st.pyplot(fig)

# tenure
st.subheader("Customer Tenure")

fig, ax = plt.subplots()
sns.histplot(data=filtered, x="tenure", hue="Churn", bins=20, ax=ax)
st.pyplot(fig)

#charges
st.subheader("Charges Analysis")

fig, ax = plt.subplots()
sns.boxplot(data=filtered, x="Churn", y="MonthlyCharges", ax=ax)
st.pyplot(fig)

# raw_data
with st.expander("Show Data"):
    st.dataframe(filtered)
