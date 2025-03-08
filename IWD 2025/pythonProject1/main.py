import pandas as pd

# Updated dataset of women in STEM with global representation, including notable Nigerian figures
data = [
    ["Ada Lovelace", "Computer Science", "UK", "First computer algorithm", 1843],
    ["Katherine Johnson", "Mathematics", "USA", "NASA calculations for Apollo 11", 1969],
    ["Marie Curie", "Physics", "France", "Discovered polonium and radium", 1898],
    ["Fei-Fei Li", "AI", "USA", "Developed ImageNet for deep learning", 2009],
    ["Radia Perlman", "Networking", "USA", "Invented Spanning Tree Protocol (STP)", 1985],
    ["Ginni Rometty", "Business/Tech", "USA", "First female CEO of IBM", 2012],
    ["Hedy Lamarr", "Engineering", "Austria", "Co-invented frequency hopping technology", 1942],
    ["Grace Hopper", "Computer Science", "USA", "Developed the first compiler", 1952],
    ["Barbara Liskov", "Computer Science", "USA", "Pioneered object-oriented programming", 2008],
    ["Tu Youyou", "Medicine", "China", "Discovered artemisinin for malaria treatment", 1972],
    ["Mary Jackson", "Aerospace Engineering", "USA", "NASA's first Black female engineer", 1958],
    ["Dorothy Vaughan", "Mathematics", "USA", "First Black supervisor at NASA", 1949],
    ["Jennifer Doudna", "Biology", "USA", "Co-developed CRISPR gene-editing", 2012],
    ["Emmanuelle Charpentier", "Biology", "France", "Co-developed CRISPR gene-editing", 2012],
    ["Vera Rubin", "Astronomy", "USA", "Provided evidence for dark matter", 1970],
    ["Rosalind Franklin", "Biology", "UK", "Captured DNA structure image", 1952],
    ["Margaret Hamilton", "Software Engineering", "USA", "Led Apollo software development", 1969],
    ["Mae Jemison", "Astronaut", "USA", "First Black woman in space", 1992],
    ["Jane Goodall", "Biology", "UK", "Pioneered chimpanzee research", 1960],
    ["Lise Meitner", "Physics", "Austria", "Co-discovered nuclear fission", 1938],
    ["Chien-Shiung Wu", "Physics", "China", "Proved weak force parity violation", 1956],
    ["Carol Shaw", "Computer Science", "USA", "First female video game developer", 1978],
    ["Shafi Goldwasser", "Cryptography", "USA", "Contributions to encryption theory", 2012],
    ["Frances Allen", "Computer Science", "USA", "First woman to win Turing Award", 2006],
    ["Maria Gaetana Agnesi", "Mathematics", "Italy", "First woman to write a calculus textbook", 1748],
    ["Donna Strickland", "Physics", "Canada", "Nobel Prize for chirped pulse amplification", 2018],
    ["Jocelyn Bell Burnell", "Astronomy", "UK", "Discovered pulsars", 1967],
    ["Sophie Germain", "Mathematics", "France", "Contributions to elasticity theory", 1816],
    ["Cecilia Payne-Gaposchkin", "Astronomy", "UK", "Discovered hydrogen as the most abundant element", 1925],
    ["Marie Van Brittan Brown", "Engineering", "USA", "Invented first home security system", 1966],
    ["Gertrude Elion", "Medicine", "USA", "Developed drugs for leukemia and AIDS", 1988],
    ["Barbara McClintock", "Biology", "USA", "Discovered transposable elements", 1950],
    ["Nina Tandon", "Biomedical Engineering", "USA", "Leader in regenerative medicine", 2015],
    ["Evelyn Boyd Granville", "Mathematics", "USA", "One of the first Black women Ph.D.s in math", 1949],
    ["Maryam Mirzakhani", "Mathematics", "Iran", "First woman to win the Fields Medal", 2014],
    ["Dorothy Crowfoot Hodgkin", "Chemistry", "UK", "Pioneered X-ray crystallography", 1964],
    ["Ola Brown", "Medicine", "Nigeria", "Founded Flying Doctors Nigeria", 2010],
    ["Ellen Ochoa", "Engineering", "USA", "First Hispanic woman in space", 1993],
    ["Nashwa Eassa", "Physics", "Sudan", "Research in nanotechnology", 2013],
    ["Maggie Aderin-Pocock", "Astronomy", "UK/Nigeria", "Developed optical instruments for satellites", 2010],
    ["Tebello Nyokong", "Chemistry", "South Africa", "Research in photodynamic therapy", 2019],
    ["Njideka U. Udochi", "Medicine", "Nigeria", "First Black woman to be Maryland’s Physician of the Year", 2021],
    ["Funke Opeke", "Telecommunications", "Nigeria", "Founded MainOne for Africa’s internet infrastructure", 2010],
    ["Tuula Teeri", "Biotechnology", "Finland", "Pioneer in enzymatic biomass conversion", 2005],
    ["France A. Córdova", "Astrophysics", "USA", "Director of the National Science Foundation", 2014],
    ["Youyou Tu", "Medicine", "China", "Nobel Prize for malaria drug Artemisinin", 2015],
    ["Mária Telkes", "Engineering", "Hungary", "Developed first thermoelectric power generator", 1947],
    ["Dame Sue Ion", "Nuclear Engineering", "UK", "Advocate for nuclear energy advancements", 2000],
    ["Adora Nwodo", "Software Engineering", "Nigeria", "Builds cloud services at Microsoft and co-founded unStack Africa", 2020],
    ["Wendy Okolo", "Aerospace Engineering", "Nigeria", "First Black woman to earn a Ph.D. in aerospace engineering from University of Texas at Arlington; aerospace research engineer at NASA Ames Research Center", 2015],
    ["Francisca Okeke", "Physics", "Nigeria", "First female professor of physics in eastern Nigeria; advocate for women in science", 2004],
    ["Omowunmi Sadik", "Chemistry", "Nigeria", "Inventor and professor known for work in biosensors and environmental chemistry", 1994],
    ["Oreoluwa Lesi", "Technology", "Nigeria", "Founder of Women's Technology Empowerment Centre (W.TEC), promoting technology among Nigerian women"]
    ]
 


# Create a DataFrame
df = pd.DataFrame(data, columns=["Name", "Field", "Country", "Achievement", "Year"])

# Save as CSV
df.to_csv("women_in_stem.csv", index=False)

print("Dataset 'women_in_stem.csv' has been updated successfully!")

import streamlit as st
import pandas as pd
import altair as alt

# Load the dataset
df = pd.read_csv("women_in_stem.csv")

# Streamlit app title
st.title("Women in STEM Achievements Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", ["All"] + sorted(df["Country"].unique()))
selected_field = st.sidebar.selectbox("Select Field", ["All"] + sorted(df["Field"].unique()))

# Apply Filters
filtered_df = df.copy()
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]
if selected_field != "All":
    filtered_df = filtered_df[filtered_df["Field"] == selected_field]

# Display Data Table
st.write("### Women in STEM Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Bar Chart: Number of Contributions Over Time
st.write("### Contributions Over the Years")
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("Year:N", title="Year"),
    y=alt.Y("count()", title="Number of Contributions"),
    tooltip=["Year", "count()"]
).properties(width=700, height=400)
st.altair_chart(chart, use_container_width=True)

# Download CSV Button
st.write("### Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_women_in_stem.csv",
    mime="text/csv"
)

st.write("### About")
st.info("This dashboard showcases the achievements of women in STEM fields globally, including contributions from Africa and Nigeria.")



