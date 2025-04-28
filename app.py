import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pydeck as pdk
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from style import set_custom_style
import altair as alt
import os
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Set Page Config ---
st.set_page_config(
    page_title="Borderland Dynamics Knowledge Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.logo("pictures/Xcept-Logo-808.png", size="large")

# --- 2. Apply Custom Style ---
set_custom_style()

# Add this after imports and before st.sidebar.image
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: 0 !important;
        margin-right: auto !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100%;
        height: auto;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("🌍 Borderland Dynamics Knowledge Hub")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Project Overview",
        "📚 Conceptual Background",
        "🛠️ Computational Framework",
        "📈 Data and Methodology",
        "🗺️ Interactive Exploration",
        "🧩 Key Insights and Findings",
        "🖼️ GIS and Spatial Modeling",
        "🏛️ Policy Reflections",
        "📚 Resources and Downloads"
    ]
)

# --- PAGE LOGIC ---

# 1. Home / Project Overview
if page == "🏠 Project Overview":
    st.title("🏠 Borderland Dynamics Knowledge Hub")
    st.markdown("---")
    st.header("Project Overview")
    st.markdown("""
    This knowledge hub emerges from my work as a Fellow with the **Women Researchers Fellowship**, part of the **X-Border Local Research Network** — an initiative that supports early-career female researchers working on conflict-affected border regions across Asia, the Middle East, and the Horn of Africa.
    
    During my fellowship, I set out to develop a computational framework that could better capture the economic, security, and social dynamics shaping borderland regions. Using the Kenya–Uganda border as a case study, I combined spatial modeling with relational analysis to map trade potential, conflict risk, and informal social networks.
    
    The goal was not simply to produce new indices or maps, but to make complex realities **legible**, **interpretable**, and **actionable** for policy audiences.  
    This project reflects a growing recognition: **technical alone is not enough**. For computational research to shape real-world decisions, it must be framed around institutional questions, embedded within policy processes, and open to reflexive interpretation.
     """)
    st.markdown("""
    This Streamlit app provides a **unified platform** where users can explore the computational model interactively, read through the technical and reflexive findings, and engage with the broader **methodological conversation** around borderland research.

The hub integrates **two core research outputs**:
- **Computational Framework for Borderland Analysis**  
  ➔ Technical modeling of trade potential, conflict risk, and relational networks.
- **Borderlands, Evidence, and Methodological Pluralism**  
  ➔ Reflexive supplement on how evidence is shaped, methodological choices, and institutional contexts.



## 🛠️ How the Project Was Built

""")
    with st.expander("🔎 Click here to expand the full technical and conceptual process"):
        st.markdown("""
The project unfolded in three interlinked layers:

### 1. Theoretical Framing
- Grounded in **borderland studies**, **relational geography**, and **fragility research**.
- Recognized that **trust networks, identity ties, and informal economies** heavily shape cross-border trade.
- Emphasized the **need for pluralistic evidence**—combining hard quantitative data with relational and cultural insight.

(See 📚 *Conceptual Background* for detailed framing.)

---

### 2. Technical Spatial Analysis

**Data Collection and Merging**  
- Sources: WorldPop (population), ACLED (conflict), OpenStreetMap/Overpass Turbo (markets and roads), ESRI Africa Transport Routes.
- Merged Kenya and Uganda datasets to create a unified spatial canvas.

**Assigning Population to Markets**  
- Created **buffers** around markets (1.5 km for urban, 3 km for rural).
- Used **spatial joins** to estimate the population covered by each market.

**Conflict Exposure Index (CI)**  
- Modeled conflict risk as a function of **proximity** and **fatalities** near border posts.
- Developed a weighted index where fatalities closer to a border post mattered more.

**Market Potential Index (MPI)**  
- Modeled trade potential by combining **population reach**, **road accessibility**, and **market distance**.
- Used **travel time calculations** based on real road network data (max speed per road type).

**Mapping Relational Ties**  
- Overlaid **ethnic and linguistic group data** to model trust-based trading patterns across the border.
- Highlighted how informal networks sometimes mattered more than formal infrastructure.

---

### 3. Reflection and Institutional Relevance

**Key Lessons:**
- Data and models **alone do not answer policy questions** — co-defining goals with policymakers is essential.
- **Relational factors** (ethnicity, trust, informal ties) are crucial but often ignored in technical models.
- Computational methods should be **reflexive**: transparent about assumptions and limitations.

(See 🏛️ *Policy Reflections* for a deeper discussion.)

---

""")
    st.markdown("""
---

## 🧭 How to Navigate This Hub

| Section | Purpose |
|:--------|:--------|
| 🏠 **Project Overview** | Big-picture framing: what, why, and how. |
| 📚 **Conceptual Background** | Theories and frameworks that shaped the project. |
| 🛠️ **Computational Framework** | Deep dive into modeling choices and assumptions. |
| 📈 **Data and Methodology** | How the data was collected, processed, and modeled. |
| 🌍 **Interactive Exploration** | Explore conflict risks, market potentials, and travel networks interactively. |
| 🧩 **Key Insights and Findings** | Summarized key results and patterns. |
| 🗺️ **GIS and Spatial Modeling** | Detailed walkthrough of the GIS analysis with diagrams and visual examples. |
| 🏛️ **Policy Reflections** | Insights for making models actionable and usable for decision-making. |
| 📚 **Resources and Downloads** | Access supplementary material and additional references. |

---


I invite you to explore, reflect, and rethink evidence in cross-border settings.

""")
    st.markdown("---")

    # --- Source Papers Section ---
    st.subheader("Source Papers")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("📄 Technical Paper: Computational Framework for Borderland Analysis", expanded=False):
            st.markdown("""
            This paper presents the technical foundation of our computational approach, including:
            
            - Market Potential Index (MPI) methodology
            - Conflict Exposure Index (CI) calculation
            - Relational network mapping techniques
            
            [Download Technical Paper (PDF)](https://your-link-here.com)
            """)
    with col2:
        with st.expander("📄 Supplementary Paper: Borderlands, Evidence, and Methodological Pluralism", expanded=False):
            st.markdown("""
            This paper reflects on the policy relevance of computational methods, exploring:
            
            - How to make complex borderland dynamics legible to policymakers
            - The importance of framing research around specific institutional questions
            - The role of reflexivity in evidence-based policy
            
            [Download Supplementary Paper (PDF)](https://your-link-here.com)
            """)
    st.markdown("---")
    st.markdown("<footer>Part of the Women Researchers Fellowship, X-Border Local Research Network.</footer>", unsafe_allow_html=True)

# 2. Conceptual Background
elif page == "📚 Conceptual Background":
    # Page Title
    st.title("🧠 Conceptual Background")
    # Summary Box
    st.info("""
    **Summary:**  
    This project introduces a computational framework for analyzing borderland dynamics, integrating spatial, temporal, and relational perspectives.  
    It builds on spatial interaction theory, conflict studies, and relational geography to quantify market potential, conflict exposure, and social ties in dynamic border zones.
    """)
    st.markdown("---")
    # === Row 1: Introduction + Framework Image ===
    row1_col1, row1_col2 = st.columns([2, 1])
    with row1_col1:
        st.markdown("""
    Traditional border studies have largely relied on qualitative assessments and isolated case studies, providing valuable but fragmented insights into how borders operate as zones of economic exchange, conflict, and social interaction.  
    This perspective is evident in the evolution of border studies, transitioning from viewing borders as static lines to dynamic systems shaped by economic, social, and cultural exchanges.  
    While qualitative richness has dominated, the lack of quantitative frameworks has limited our ability to systematically capture borderland dynamics.

    This project builds upon the work of Eberhard-Ruiz, who measured conflict exposure at the border-post level along the Uganda–DRC frontier.  
    Expanding beyond static analysis, we introduce a computational framework that integrates spatial and temporal layers, offering scalable, systematic methods to quantify economic and conflict realities at borders.

    The framework combines spatial interaction theory, New Economic Geography, and conflict studies, operating across:
    - **Spatial Layer:** Infrastructure, distance, and market potential (MPI)
    - **Temporal Layer:** Conflict evolution and economic disruption (CI)
    - **Relational Layer:** Social networks and informal trade

    The Kenya–Uganda border serves as a validation case, with approximately 23,000 crossings daily along a volatile, opportunity-rich frontier.
        """, unsafe_allow_html=True)
    with row1_col2:
        try:
            st.image("pictures/framework_diagram.png", use_container_width=True)
            st.caption("**Figure:** Conceptual Framework Linking Spatial, Temporal, and Relational Layers.")
        except Exception:
            st.warning("Framework diagram not found. Please ensure 'framework_diagram.png' exists in your project folder.")
            st.markdown("**Figure:** Conceptual Framework Linking Spatial, Temporal, and Relational Layers.\n*Image not found*")
    st.markdown("---")
    # === Row 2: 3 Columns for Levels inside Expanders ===
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    with row2_col1:
        with st.expander("🌍 Spatial Level: Infrastructure and Economic Geography", expanded=False):
            st.markdown("""
    **Infrastructure and Economic Geography**

    Spatial interaction theory provides a basis for understanding how economic activities flow between locations, following a gravity-like principle: larger and closer locations interact more.

    - **Location Characteristics:** Population size and economic activity drive interactions. Busia and Malaba, for example, act as economic anchors.
    - **Transferability:** Infrastructure networks like roads and railways enhance movement and trade, transforming key crossings into hubs.
    - **Distance Decay:** Economic interactions diminish with distance. Sensitivity analysis (j=0.02, 0.03, 0.05) tests how trade flows respond to distance variations.

    While these spatial components are crucial, they alone cannot capture the disruptions caused by political instability and conflict, which leads to integrating a temporal dimension.
            """, unsafe_allow_html=True)
    with row2_col2:
        with st.expander("⏳ Temporal Level: Conflict Dynamics and Evolution", expanded=False):
            st.markdown("""
    **Conflict Dynamics and Evolution**

    Protracted Social Conflict (PSC) theory explains how conflicts embed themselves into social systems, becoming self-sustaining through feedback loops.

    - **Conflict Cycles:** Environmental stresses (e.g., droughts) and resource competition trigger cycles of violence, such as livestock raiding in the ASALs.
    - **Economic Ripple Effects:** Conflicts near trade routes (like Busia) increase transport costs and deter investment.
    - **Conflict Exposure Index (CI):** Aggregates conflict incidents using weighted severity and proximity to trade hubs, capturing both intensity and economic disruption potential.

    This temporal analysis complements spatial measures, highlighting how persistent insecurity reshapes borderland economies over time.
            """, unsafe_allow_html=True)
    with row2_col3:
        with st.expander("🤝 Relational Level: Social Networks and Cultural Connections", expanded=False):
            st.markdown("""
    **Social Networks and Cultural Connections**

    Relational space theory adds a social and cultural lens to border dynamics, focusing on localized ties across artificial boundaries.

    - **Kinship and Language:** Shared ethnicity and languages (e.g., Luhya, Kiswahili) enable trust, trade, and resilience.
    - **Mutual Intelligibility Zones:** Linguistic connections ease navigation across regulatory and social divides.
    - **Conflict Mitigation:** Customary conflict resolution mechanisms embedded within kinship networks help de-escalate tensions and maintain trade during insecurity.

    This relational layer shows how trust networks can either reinforce or bypass formal spatial and political structures.
            """, unsafe_allow_html=True)
    st.markdown("---")

# 3. Computational Framework
elif page == "🛠️ Computational Framework":
    st.title("🧮 Step 2: Computational Model")
    # --- Summary Box ---
    st.info("""
    **Summary:**  
    Building on theoretical foundations, the computational framework translates spatial, temporal, and relational dynamics into measurable indices:
    - **Spatial Layer (MPI):** Economic accessibility shaped by population, infrastructure, and distance decay.
    - **Temporal Layer (CI):** Conflict exposure affecting trade disruption across time and space.
    - **Relational Layer:** Ethnic and linguistic networks mediating borderland resilience and trade patterns.
    """)
    st.markdown("---")
    # --- Row 1: Introduction + Optional Diagram ---
    row1_col1, row1_col2 = st.columns([2, 1])
    with row1_col1:
        st.markdown("""
    Building on the theoretical foundations outlined earlier, this section constructs the computational framework into three quantifiable components: the Market Potential Index (MPI), the Conflict Exposure Index (CI), and relational analysis.  
    Together, these components provide a structured framework for analyzing borderland dynamics systematically and scalably.

    - **Layer 1: Spatial Level**  
    The MPI quantifies how geographic factors such as distance, infrastructure, and population size influence trade accessibility. High-resolution datasets from WorldPop and OpenStreetMap form the backbone, incorporating conditional buffering to distinguish urban and rural markets. An exponential distance-decay function, paired with sensitivity analysis across multiple decay parameters, models how economic flows diminish over distance.

    - **Layer 2: Temporal Level**  
    The CI captures how conflict events disrupt economic activities by weighting incidents by severity and proximity to trade corridors. This dynamic index allows for analyzing conflict's cumulative and evolving effects over time, revealing how insecurity embeds itself into borderland economies.

    - **Layer 3: Relational Level**  
    Recognizing that borders are also socially and culturally embedded spaces, the relational layer overlays ethnic and linguistic geographies onto MPI and CI outcomes. Using GREG data, it investigates how cultural networks shape resilience and trade flows in ways invisible to purely spatial or conflict-only models.

    This three-layered design seeks to reveal the complex interplay of markets, security, and social trust that characterizes dynamic borderlands like Kenya–Uganda.
    """, unsafe_allow_html=True)
    with row1_col2:
        try:
            st.image("pictures/framework_diagram.png", use_container_width=True)
            st.caption("**Framework:** Translating Spatial, Temporal, and Relational Dimensions into Computable Indices")
        except Exception:
            st.warning("Framework diagram not found. Please ensure 'framework_diagram.png' exists in your project folder.")
            st.markdown("**Framework:** Translating Spatial, Temporal, and Relational Dimensions into Computable Indices\n*Image not found*")
    st.markdown("---")
    # --- Row 2: Three Expanders in Columns ---
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    # Layer 1: Spatial (MPI)
    with row2_col1:
        with st.expander("🌐 Layer 1: Spatial Level (Market Potential Index - MPI)", expanded=False):
            st.markdown("""
    **Data Sources:**
    - Population grids (WorldPop)
    - Route networks (OpenStreetMap)
    - Market and border post identifiers
    - Conditional buffering: 1.5 km (urban) and 3 km (rural)

    **MPI Formula:**
    Weighted sum of surrounding population, decayed exponentially by travel distance.

    **Decay Parameters:**
    - Low decay (j=0.02): Long-range influence
    - Medium decay (j=0.03): Balanced reach
    - High decay (j=0.05): Localized impact

    **Purpose:**
    To map areas where infrastructure investment would generate the highest market activity under different distance sensitivities.
            """, unsafe_allow_html=True)
    # Layer 2: Temporal (CI)
    with row2_col2:
        with st.expander("⏳ Layer 2: Temporal Level (Conflict Exposure Index - CI)", expanded=False):
            st.markdown("""
    **Data Sources:**
    - ACLED conflict events database (event counts, fatalities)
    - Geospatial distances to trade routes
    - Border and market identifiers

    **CI Formula:**
    Severity-weighted conflict events within proximity bands to trade routes.

    **Temporal Aggregation:**
    Annual mapping of conflict intensity, detecting spikes or chronic instability.

    **Purpose:**
    Quantify how insecurity accumulates and disrupts economic flows across space and time.
            """, unsafe_allow_html=True)
    # Layer 3: Relational (Social Networks)
    with row2_col3:
        with st.expander("🤝 Layer 3: Relational Level (Ethnic and Linguistic Networks)", expanded=False):
            st.markdown("""
    **Data Sources:**
    - GREG ethnic geographies
    - Language family overlays
    - Spatial join with MPI and CI outcomes

    **Analytical Steps:**
    - Map intersection of ethnicity/language with trade potential and conflict exposure.
    - Identify where cultural ties enhance trade or resilience.

    **Purpose:**
    Reveal how shared identities mediate both economic opportunity and vulnerability, offering critical policy insights invisible to spatial or conflict-only models.
            """, unsafe_allow_html=True)
    st.markdown("---")

# 4. Data and Methodology
elif page == "📈 Data and Methodology":
    st.title("📈 Data and Methodology")
    st.header("🗂️ Data Sources")
    st.markdown("""
    This section provides technical transparency about the data and methods used in our analysis.
    """)
    with st.expander("Data Sources", expanded=False):
        st.markdown("""
        **Primary Data Sources:**
        
        - **WorldPop:** High-resolution population grids
        - **OpenStreetMap:** Road networks and infrastructure
        - **ACLED:** Geocoded conflict incident data
        - **Ethnologue:** Ethnolinguistic mapping
        
        These datasets provide the foundation for our computational framework.
        """)
    st.header("🧮 Methodology Overview")
    with st.expander("GIS Processing Steps", expanded=False):
        st.markdown("""
        **Key Processing Steps:**
        
        1. **Market Buffering:** 
           - Urban markets: 1.5km radius
           - Rural settlements: 3km radius
        
        2. **Conflict Aggregation:**
           - 20km buffer around each border point
           - Weighted by severity and proximity
        
        3. **Population Integration:**
           - Grid cells aggregated to border points
           - Distance decay applied
        
        4. **Social Network Mapping:**
           - Ethnolinguistic regions identified
           - Cross-border connections mapped
        """)
    with st.expander("Parameters and Sensitivity", expanded=False):
        st.markdown("""
        **Default Parameters:**
        
        - **MPI Decay Rates:** j = 0.02, 0.03, 0.05
        - **CI Buffer:** 20km
        - **Conflict Weights:** Based on ACLED event types
        
        These parameters were chosen based on sensitivity analysis and can be adjusted in the interactive visualization.
        """)
    st.header("🔁 Reproducibility")
    with st.expander("Code and Reproducibility", expanded=False):
        st.markdown("""
        **GitHub Repository:**
        
        All code is available in our public repository: [Computational Framework for Borderland Analysis](https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis)
        
        The repository includes:
        
        - Python scripts for data processing
        - R code for statistical analysis
        - GIS workflows
        - Documentation
        
        This ensures full reproducibility of our analysis.
        """)
    with st.expander("Assumptions and Limitations", expanded=False):
        st.markdown("""
        **Key Assumptions:**
        
        - Population distribution is relatively stable over the study period
        - Road networks are the primary means of transportation
        - Conflict events are accurately geocoded
        
        **Limitations:**
        
        - Data quality varies across regions
        - Some informal trade routes may not be captured
        - Social networks are simplified in the model
        
        These limitations should be considered when interpreting the results.
        """)

# 5. Interactive Exploration
elif page == "🗺️ Interactive Exploration":
    import pandas as pd
    import altair as alt
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st
    import os
    st.title("🌍 Interactive Borderland Analysis")
    st.markdown("""
    Explore the intersection of **Market Potential** and **Conflict Exposure** across the Kenya–Uganda border. This tool allows dynamic exploration of spatial, temporal, and relational trends shaping border dynamics.
    """)
    # --- Load Data ---
    mpi_border = pd.read_csv('data/mpi_border_results.csv')
    ci_results = pd.read_csv('data/ci_results.csv')
    if os.path.exists('data/mpi_summary.csv'):
        mpi_summary = pd.read_csv('data/mpi_summary.csv')
    else:
        mpi_summary = None
    decay_options = [0.02, 0.03, 0.05]
    border_options = mpi_border['Border_Name'].dropna().unique()
    year_options = ci_results['year'].dropna().unique() if 'year' in ci_results.columns else []
    ethnic_options = mpi_summary['name'].unique() if mpi_summary is not None and 'name' in mpi_summary.columns else []
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        'MPI Bar Chart', 'MPI Heatmap', 'CI Temporal Trends', 'CI Heatmap', 'Download Data'
    ])
    # --- Tab 1: MPI Bar Chart ---
    with tab1:
        st.subheader('Market Potential Index (MPI) by Border Post')
        selected_borders = st.multiselect('Select Border(s)', border_options, default=list(border_options))
        decay_cols = [f'Norm_MPI_{j}' for j in [0.02, 0.03, 0.05]]
        data = mpi_border[mpi_border['Border_Name'].isin(selected_borders)]
        if not data.empty:
            # Melt the dataframe for Altair stacking
            data_melted = data.melt(id_vars=['Border_Name'], value_vars=decay_cols, var_name='Decay', value_name='MPI')
            data_melted['Decay'] = data_melted['Decay'].str.replace('Norm_MPI_', 'Decay=')
            chart = alt.Chart(data_melted).mark_bar().encode(
                x=alt.X('Border_Name:N', title='Border Name', sort=None),
                y=alt.Y('MPI:Q', title='Market Potential Index', scale=alt.Scale(domain=[0, 1])),
                color=alt.Color('Decay:N', title='Decay Parameter'),
                tooltip=['Border_Name', 'Decay', 'MPI']
            ).properties(height=400)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info('No data for selected borders.')
    # --- Tab 2: MPI Heatmap ---
    with tab2:
        st.subheader('MPI Heatmap by Border Post')
        decay = st.selectbox('Decay Parameter', decay_options, key='heatmap_decay')
        col = f'Norm_MPI_{decay}'
        data = mpi_border.set_index('Border_Name')[[col]]
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(data, annot=True, fmt='.2f', cmap='YlGnBu', cbar_kws={'label': f'MPI (Decay {decay})'}, vmin=0, vmax=1, ax=ax)
        ax.set_title(f'MPI Heatmap (Decay {decay})')
        st.pyplot(fig)
    # --- Tab 3: CI Temporal Trends ---
    with tab3:
        st.subheader('Temporal Trends in Conflict Exposure Index (CI)')
        selected_borders = st.multiselect('Select Border(s)', border_options, default=list(border_options), key='ci_line_borders')
        data = ci_results[ci_results['Border_Name'].isin(selected_borders)]
        if not data.empty:
            chart = alt.Chart(data).mark_line(point=True).encode(
                x=alt.X('year:O', title='Year'),
                y=alt.Y('CI:Q', title='Conflict Exposure Index'),
                color='Border_Name:N',
                tooltip=['Border_Name', 'year', 'CI']
            ).properties(height=400)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info('No CI data for selected borders.')
    # --- Tab 4: CI Heatmap ---
    with tab4:
        st.subheader('CI Heatmap by Border and Year')
        ci_pivot = ci_results.pivot_table(index='Border_Name', columns='year', values='CI', aggfunc='sum')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(ci_pivot, annot=True, fmt='.2f', cmap='YlGnBu', cbar_kws={'label': 'CI Value'}, ax=ax)
        ax.set_title('Conflict Exposure Index (CI) by Border and Year')
        st.pyplot(fig)
    # --- Tab 5: Download Data ---
    with tab5:
        st.subheader('📥 Download Data')
        st.download_button(
            label="Download MPI by Border",
            data=mpi_border.to_csv(index=False),
            file_name="data/mpi_border_results.csv",
            mime="text/csv"
        )
        st.download_button(
            label="Download CI Results",
            data=ci_results.to_csv(index=False),
            file_name="data/ci_results.csv",
            mime="text/csv"
        )
        if os.path.exists('data/aggregated_market_metrics.csv'):
            aggregated_market = pd.read_csv('data/aggregated_market_metrics.csv')
            st.download_button(
                label="Download Aggregated Market Metrics",
                data=aggregated_market.to_csv(index=False),
                file_name="data/aggregated_market_metrics.csv",
                mime="text/csv"
            )
        if os.path.exists('data/aggregated_border_metrics.csv'):
            aggregated_border = pd.read_csv('data/aggregated_border_metrics.csv')
            st.download_button(
                label="Download Aggregated Border Metrics",
                data=aggregated_border.to_csv(index=False),
                file_name="data/aggregated_border_metrics.csv",
                mime="text/csv"
            )

# 6. Key Insights and Findings
elif page == "🧩 Key Insights and Findings":
    st.title("📖 Applying the Computational Framework: Insights from the Kenya–Uganda Border")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Background",
        "Spatial Analysis (MPI)",
        "Temporal Analysis (CI)",
        "Relational Analysis",
        "Conclusion"
    ])
    with tab1:
        st.header("🧭 Background")
        st.markdown("""
        The Kenya–Uganda borderland reveals a stark duality: zones of economic vibrancy and zones of persistent insecurity.  
        In the north, arid lands populated by pastoralist communities (e.g., Turkana and Karamoja) depend on cross-border mobility, yet climate change and insecurity have turned these flows into sources of tension. Scarce pasture and water resources fuel armed cattle raids, reinforcing cycles of violence.

        In the south, towns like Busia, Malaba, and Lwakhakha anchor critical trade routes, linking Kenya, Uganda, Rwanda, South Sudan, and the DRC. Although relatively small in size, these hubs play an outsized role in regional commerce, catalyzed by infrastructure development and East African Community (EAC) integration efforts.

        This diversity—from volatile pastoralist zones to booming trade corridors—demonstrates why understanding borderland dynamics requires an integrated approach spanning spatial, temporal, and relational dimensions.
        """)
    with tab2:
        st.header("🗺️ 3.1 Spatial Analysis and the Market Potential Index (MPI)")
        st.markdown("""
        The Market Potential Index (MPI) operationalizes spatial interaction theory, measuring how distance, infrastructure, and population size shape economic accessibility.

        **Key Insights:**
        - **Strategic Hubs:** Busia, Malaba, and Kisumu consistently exhibit the highest MPI scores, reflecting their infrastructural strength and location within major trade corridors.
        - **Spatial Spread:** At low decay rates, economic influence from major hubs extends broadly. As decay increases, economic potential becomes more localized.
        - **Peripheral Constraints:** Remote regions such as Kaabong and Amudat consistently score low, highlighting persistent barriers to economic integration.

        **Interpretation:**
        The findings validate core principles of spatial interaction theory: proximity and infrastructure drive economic flows.  
        Importantly, sensitivity to decay parameters emphasizes a policy-relevant point: **distance elasticity matters**.  
        Planners must account for how steeply economic opportunities fall off with distance when designing transport corridors and trade hubs.
        """)
    with tab3:
        st.header("🔥 3.2 Temporal Analysis and the Conflict Exposure Index (CI)")
        st.markdown("""
        The Conflict Exposure Index (CI) captures how recurrent insecurity shapes trade dynamics over time, aligning with protracted social conflict theory.

        **Key Insights:**
        - **Vulnerable Trade Nodes:** Busia and Kisumu show the highest and most volatile conflict exposure.
        - **Temporal Volatility:** Conflict exposure is not static; critical trade hubs can experience sudden shocks.
        - **Isolated Stability:** Border posts like Kaabong and Amudat remain insulated from conflict but economically marginalized.

        **Interpretation:**
        Spatial proximity amplifies conflict risk.  
        High-value economic corridors are particularly vulnerable to security shocks, necessitating dynamic monitoring systems.  
        Meanwhile, geographic isolation protects some regions at the cost of deeper marginalization.
        """)
    with tab4:
        st.header("🤝 3.3 Relational Layer: Social Networks and Cultural Connectivity")
        st.markdown("""
        The relational layer highlights how ethnic and linguistic networks mediate borderland interactions.

        **Key Insights:**
        - **Cultural Economies:** Cross-border trade thrives where linguistic and ethnic ties facilitate trust and reduce transaction costs.
        - **Conflict Mediation:** Kinship networks in pastoralist regions can either stabilize or destabilize trade routes.
        - **Spatial-Relational Dynamics:** Economic hubs often align with zones of strong cultural integration.

        **Interpretation:**
        Relational space is not a backdrop but an active force.  
        Economic resilience and vulnerability cannot be explained solely by physical connectivity or conflict trends;  
        they are deeply shaped by the human geographies of trust, kinship, and shared culture.
        """)
    with tab5:
        st.header("✨ Conclusion")
        st.markdown("""
        Applying the computational framework to the Kenya–Uganda border demonstrates that:

        - **Economic opportunity and conflict vulnerability are spatially and temporally intertwined.**
        - **Infrastructure and trade routes amplify both prosperity and exposure to risk.**
        - **Cultural networks mediate these dynamics, enabling both resilience and fragility.**

        Borderland development must therefore move beyond physical investment alone: it must recognize the **interlocking roles of geography, conflict patterns, and human relations** in shaping regional futures.
        """)

# 7. GIS and Spatial Modeling
elif page == "🖼️ GIS and Spatial Modeling":
    # Title and Introduction
    st.title("🛰️ GIS Analysis Workflow")
    st.markdown("""
    Welcome to the **step-by-step walkthrough** of how the GIS analysis behind the Kenya–Uganda border study was constructed. 
    This guide explains how datasets were processed, merged, and transformed into actionable spatial insights.
    Use the **Next** and **Back** buttons to explore each step.
    """)
    # Organized slides with correct pictures and text
    slides = [
        ("pictures/Merge_datasets.png", "Merging Datasets", "We merged datasets of Uganda and Kenya to create a unified foundation for analyzing cross-border trade, conflict, and population patterns."),
        ("pictures/markets with population density weight 1.png", "Population Assignment: Markets and Population", "We sourced high-resolution population data from WorldPop and assigned it to each market point."),
        ("pictures/markets with population density weight 2.png", "Market Coverage Simulation", "Urban markets received a 1.5 km buffer; rural markets a 3 km buffer, simulating service areas realistically."),
        ("pictures/Trading routes and Markets population coverage 1.png", "Trading Routes and Population Coverage (Part 1)", "Visualization showing how catchment areas relate to key trading routes."),
        ("pictures/Trading routes and Markets population coverage 2.png", "Trading Routes and Population Coverage (Part 2)", "Highlights how clustered populations align with transport corridors."),
        ("pictures/Travel Distance Calculation 1.png", "Travel Distance Calculation (Part 1)", "Using OSM data, we calculated travel distances from markets to border posts."),
        ("pictures/Travel Distance Calculation 2.png", "Travel Distance Calculation (Part 2)", "This map visualizes how accessibility varies across the region."),
        ("pictures/Road Data Preparation.png", "Road Data Preparation", "Road infrastructure was cleaned and validated to model realistic travel times."),
        ("pictures/assign pop point to market 1.png", "Assigning Population Points to Markets (Part 1)", "Spatial joins linked buffered markets to surrounding population points."),
        ("pictures/assign pop point to market 2.png", "Assigning Population Points to Markets (Part 2)", "This simulates realistic market demand by weighting markets by nearby population."),
        ("pictures/fatalities and proximity1.png", "Conflict Event Proximity (Part 1)", "Conflict event data was analyzed for proximity to critical trade routes."),
        ("pictures/fatalities and proximity2.png", "Conflict Event Proximity (Part 2)", "We weighted fatalities and conflict severity closer to borders more heavily."),
        ("pictures/Travle distance (1).jpg", "Conflict Impact on Trade Routes", "Trade routes were assessed for risk exposure to nearby conflicts."),
        ("pictures/Markets type and conflict (1).jpg", "Market Types and Conflict Exposure", "We examined how different market types faced different conflict risks."),
        ("pictures/CI (1).jpg", "Conflict Intensity Mapping", "Conflict Intensity (CI) heatmaps and timelines highlight spikes in conflict at hubs like Busia and Malaba."),
        ("pictures/Layer 3 .jpg", "Relational Networks (Ethnicity and Trade)", "We overlaid ethnic, cultural, and linguistic ties onto economic and conflict maps.")
    ]
    # Initialize slide index
    if "slide_index" not in st.session_state:
        st.session_state.slide_index = 0
    # Navigation Buttons
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.slide_index = max(st.session_state.slide_index - 1, 0)
    with col3:
        if st.button("Next ➡️"):
            st.session_state.slide_index = min(st.session_state.slide_index + 1, len(slides) - 1)
    # Display Current Slide
    image_path, title, description = slides[st.session_state.slide_index]
    st.subheader(f"**{title}**")
    st.image(image_path, use_container_width=True)
    st.markdown(f"**{description}**")
    # Optional Sidebar
    st.sidebar.markdown("🗺️ Navigate through the GIS Analysis Workflow step-by-step.")

# 8. Policy Reflections
elif page == "🏛️ Policy Reflections":
    st.title("🏛️ Policy Reflections")
    # --- TL;DR Summary Box ---
    with st.container():
        st.info("""
        **Summary:**  
        This research project modeled the intersection of trade and conflict along the Kenya–Uganda border.  
        While computational methods provided powerful insights, the absence of co-defined policy questions limited immediate actionability.  
        This reflection highlights the importance of early co-construction with policy actors, the added value of computational approaches in decision-making, and future directions for collaborative, reflexive research.
        """)
    # --- 1. Study in Plain English ---
    st.header("1️⃣ What I Did: The Study in Plain English")
    with st.expander("Expand to read the study overview", expanded=False):
        st.markdown("""
        This project developed a computational spatial model to examine where economic opportunities and security risks overlap along the Kenya–Uganda border.  
        It consisted of three main components:
        
        - **Market Potential Index (MPI):** Measured trade potential based on population, infrastructure, and distance.
        - **Conflict Exposure Index (CI):** Measured security risks based on proximity and severity of conflict events.
        - **Relational Layer:** Mapped ethnic, linguistic, and kinship ties that shape informal trade routes and resilience patterns.
        
        **Key findings included:**
        - Busia and Malaba are high-reward, high-risk hubs: strong trade potential, but vulnerability to conflict.
        - Kaabong and Amudat are stable but neglected: minimal conflict exposure but low investment attention.
        - Social networks reroute trade flows: kinship ties often guide commerce beyond formal infrastructure.
        
        However, without a pre-agreed policy objective, translating these findings into actionable recommendations remained difficult.
        """)
    # --- 2. Why Co-Construction Matters ---
    st.header("2️⃣ Why Co-Construction Matters: Methodological Positioning")
    with st.expander("Expand to read about co-construction", expanded=False):
        st.markdown("""
        This research fits within the interpretive strand of **Computational Social Science (CSS)**, where models are informed by qualitative context as much as by data patterns.

        **Key Lessons:**
        - Without co-defining research questions with policymakers, even sophisticated models may lack decision relevance.
        - Co-construction improves both **research uptake** and **policy impact**.
        - Institutions like **UKRI** now emphasize that policy users should be involved in **all research stages** — from question formulation to analysis and communication.
        
        In this project, had we defined objectives jointly, outputs could have been timed and framed better to meet real institutional needs.
        """)
    # --- 3. The Value of Computational Approaches for Policy ---
    st.header("3️⃣ The Value of Computational Approaches for Policy")
    with st.expander("Expand to read about computational methods in policymaking", expanded=False):
        st.markdown("""
        Despite the challenges, computational methods still offer distinct advantages in complex policy settings:

        - **Mapping Complexity:** Formal models can simulate heterogeneous actors and interactions (e.g., land use, epidemics, economic shocks).
        - **Revealing Networks:** Social network analyses show relational dynamics often hidden in traditional statistics.
        - **Scenario Testing:** Agent-based and hybrid models allow testing of "what-if" policy scenarios.
        - **Decision Intelligence:** By surfacing key actors and vulnerabilities, computational models help frame strategic interventions.
        
        In fragile borderland contexts, computational tools make hidden patterns visible — a critical input for informed policymaking.
        
        **Future Approach:**
        - Reflexivity: Acknowledge biases and limits of models.
        - Embeddedness: Build stronger ties between researchers and policy institutions, e.g., via embedded researcher programs.
        """)
    # --- 4. Conclusion: Towards Collaborative Computational Policy Research ---
    st.header("4️⃣ Conclusion: Towards Collaborative Computational Policy Research")
    st.markdown("""
    Rather than an afterthought, this supplementary reflection is central to bridging the gap between computational analysis and real-world policy practice.

    **Looking ahead:**
    - Researchers should engage policymakers from the outset to define problems jointly.
    - Analytical models should be tailored to policy priorities, not just data availability.
    - Reflexive, collaborative, and integrative approaches will enhance both scientific rigor and policy utility.

    Ultimately, computational social science can become a **powerful engine for decision intelligence** — but only if it is guided by clear, co-constructed questions from the start.
    """)

# 9. Resources and Downloads
elif page == "📚 Resources and Downloads":
    st.title("📚 Resources and Downloads")
    st.header("📄 Research Reports")
    st.markdown("""
    This section provides all downloadable materials related to our research.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Research Reports")
        st.markdown("""
        - [Download Technical Paper: Computational Framework for Borderland Analysis (PDF)](https://your-link-here.com)
        - [Download Supplementary Paper: Borderlands, Evidence, and Methodological Pluralism (PDF)](https://your-link-here.com)
        """)
    with col2:
        st.subheader("Code Repository")
        st.markdown("""
        - [Computational Framework Repository](https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis)
        - [Interactive Visualization Code](https://github.com/monyas96/Computational-Framework-for-Borderland-Analysis/tree/main/visualization)
        """)
        st.subheader("References and Further Reading")
        st.markdown("""
        - WorldPop: [https://www.worldpop.org/](https://www.worldpop.org/)
        - ACLED: [https://acleddata.com/](https://acleddata.com/)
        - OpenStreetMap: [https://www.openstreetmap.org/](https://www.openstreetmap.org/)
        - Ethnologue: [https://www.ethnologue.com/](https://www.ethnologue.com/)
        """)
    st.markdown("---")
    st.markdown("""
    **License Information:**
    
    - Code: MIT License © Moneera Yassien
    - Data: CC-BY 4.0
    - Maps: OpenStreetMap License
    """)

# --- FOOTER ---
st.markdown("---")
st.caption("© 2025 Borderland Dynamics Knowledge Hub | Built with ❤️ and Streamlit")
