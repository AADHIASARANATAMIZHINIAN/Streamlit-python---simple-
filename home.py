import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore
from plotly.subplots import make_subplots  # type: ignore

# Page configuration
st.set_page_config(
    page_title="Student Study Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'd:\downloads\SCREEN TIME AND STUDY HABITS AMONG STUDENTS (Responses) - Form responses 1.csv')  # type: ignore
    # Clean column names by removing extra spaces
    df.columns = [col.strip() for col in df.columns]
    return df

df = load_data()

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
pages = ["Home", "Analytics", "3D Visualizations", "Raw Data Editor", "Filtered Analysis"]
selected_page = st.sidebar.radio("Select Page", pages)

# ============================================================================
# PAGE 1: HOME
# ============================================================================
if selected_page == "Home":
    st.title("📊 Student Screen Time & Study Habits Dashboard")
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Responses", len(df))
    with col2:
        st.metric("Age Groups", df['What is your age?'].nunique())
    with col3:
        st.metric("Dataset Columns", len(df.columns))
    
    st.write("---")
    st.subheader("📝 Dataset Overview")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df.head(10), use_container_width=True)  # type: ignore
    
    st.write("---")
    st.subheader("📋 Column Information")
    for col in df.columns:
        st.write(f"**{col}:** {df[col].dtype}")

# ============================================================================
# PAGE 2: ANALYTICS (2D PLOTS)
# ============================================================================
elif selected_page == "Analytics":
    st.title("📈 Analytics & Visualizations")
    st.write("---")
    
    # Create tabs for different plot types
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Distribution", "Relationships", "Screen Time", "Study Habits", "Sleep Analysis"])
    
    with tab1:
        st.subheader("Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Age Distribution**")
            age_counts = df['What is your age?'].value_counts()
            fig_age = px.pie(values=age_counts.values, names=age_counts.index,  # type: ignore
                            title="Student Age Groups")
            st.plotly_chart(fig_age, use_container_width=True)  # type: ignore
        
        with col2:
            st.write("**Device Usage**")
            device_counts = df['What device do you use most for screen time?'].value_counts()
            fig_device = px.bar(x=device_counts.index, y=device_counts.values,  # type: ignore
                               title="Most Used Devices",
                               labels={'x': 'Device', 'y': 'Count'})
            st.plotly_chart(fig_device, use_container_width=True)  # type: ignore
        
        st.write("**Daily Study Hours Distribution**")
        study_hours = df['About how many hours a day do you spend studying?'].value_counts()
        fig_study = px.bar(x=study_hours.index, y=study_hours.values,  # type: ignore
                          title="Daily Study Hours",
                          labels={'x': 'Hours', 'y': 'Count'})
        st.plotly_chart(fig_study, use_container_width=True)  # type: ignore
    
    with tab2:
        st.subheader("Relationship Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Screen Time by Age**")
            fig_screen_age = px.histogram(df, x='What is your age?',  # type: ignore
                                         color='How many hours do you spend on screens each day?',
                                         barmode='group',
                                         title="Screen Time by Age Group")
            st.plotly_chart(fig_screen_age, use_container_width=True)  # type: ignore
        
        with col2:
            st.write("**Study Location Preference**")
            study_loc = df['Where do you usually study?'].value_counts()
            fig_loc = px.pie(values=study_loc.values, names=study_loc.index,  # type: ignore
                            title="Study Locations")
            st.plotly_chart(fig_loc, use_container_width=True)  # type: ignore
    
    with tab3:
        st.subheader("Screen Time Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Hours Spent on Screens**")
            screen_time = df['How many hours do you spend on screens each day?'].value_counts()
            fig_screen = px.bar(x=screen_time.index, y=screen_time.values,  # type: ignore
                               title="Daily Screen Time Distribution",
                               labels={'x': 'Screen Time', 'y': 'Count'})
            st.plotly_chart(fig_screen, use_container_width=True)  # type: ignore
        
        with col2:
            st.write("**Study App Preferences**")
            app_pref = df['Which app do you use most for studying?'].value_counts()
            fig_app = px.pie(values=app_pref.values, names=app_pref.index,  # type: ignore
                            title="Most Used Study Apps")
            st.plotly_chart(fig_app, use_container_width=True)  # type: ignore
    
    with tab4:
        st.subheader("Study Habits")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Break Frequency During Study**")
            breaks = df['How often do you take breaks while studying?'].value_counts()
            fig_breaks = px.bar(x=breaks.index, y=breaks.values,  # type: ignore
                               title="Break Taking Frequency",
                               labels={'x': 'Break Frequency', 'y': 'Count'})
            st.plotly_chart(fig_breaks, use_container_width=True)  # type: ignore
        
        with col2:
            st.write("**Note-Taking Methods**")
            notes = df['How do you usually take notes when studying?'].value_counts()
            fig_notes = px.bar(x=notes.index, y=notes.values,  # type: ignore
                              title="Note-Taking Methods",
                              labels={'x': 'Method', 'y': 'Count'})
            st.plotly_chart(fig_notes, use_container_width=True)  # type: ignore
    
    with tab5:
        st.subheader("Sleep Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Sleep Hours Distribution**")
            sleep = df['How many hours of sleep do you usually get on school nights?'].value_counts()
            fig_sleep = px.bar(x=sleep.index, y=sleep.values,  # type: ignore
                              title="Sleep Hours on School Nights",
                              labels={'x': 'Hours', 'y': 'Count'})
            st.plotly_chart(fig_sleep, use_container_width=True)  # type: ignore
        
        with col2:
            st.write("**Focus Level Distribution**")
            focus_data = df['How focused do you feel when you study? (1 = not focused, 5 = very focused)']
            focus_counts = focus_data.value_counts().sort_index()
            fig_focus = px.bar(x=focus_counts.index, y=focus_counts.values,  # type: ignore
                              title="Focus Level When Studying",
                              labels={'x': 'Focus Level (1-5)', 'y': 'Count'})
            st.plotly_chart(fig_focus, use_container_width=True)  # type: ignore

# ============================================================================
# PAGE 3: 3D VISUALIZATIONS
# ============================================================================
elif selected_page == "3D Visualizations":
    st.title("🎯 3D Visualizations")
    st.write("---")
    
    try:
        # Prepare data for 3D plots
        temp_df = df.copy()
        
        # Encode categorical variables
        temp_df['age_code'] = pd.Categorical(temp_df['What is your age?']).codes
        temp_df['screen_code'] = pd.Categorical(temp_df['How many hours do you spend on screens each day?']).codes
        temp_df['focus_level'] = pd.to_numeric(temp_df['How focused do you feel when you study? (1 = not focused, 5 = very focused)'], errors='coerce')  # type: ignore
        temp_df['study_hours_code'] = pd.Categorical(temp_df['About how many hours a day do you spend studying?']).codes
        
        # Use first column as name if NAME column doesn't exist
        name_col = 'NAME' if 'NAME' in temp_df.columns else temp_df.columns[0]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Age vs Screen Time vs Focus Level")
            
            fig_3d_1 = go.Figure(data=[go.Scatter3d(  # type: ignore
                x=temp_df['age_code'],
                y=temp_df['screen_code'],
                z=temp_df['focus_level'],
                mode='markers',
                marker=dict(
                    size=8,
                    color=temp_df['focus_level'],
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title="Focus Level"),
                    opacity=0.8
                ),
                text=temp_df[name_col],
                hovertemplate='<b>%{text}</b><br>Focus: %{z}<extra></extra>'
            )])
            
            age_labels = temp_df['What is your age?'].unique().tolist()
            screen_labels = temp_df['How many hours do you spend on screens each day?'].unique().tolist()
            
            fig_3d_1.update_layout(  # type: ignore
                scene=dict(
                    xaxis_title='Age Group',
                    yaxis_title='Screen Time Category',
                    zaxis_title='Focus Level',
                    xaxis=dict(tickvals=list(range(len(age_labels))), ticktext=age_labels),
                    yaxis=dict(tickvals=list(range(len(screen_labels))), ticktext=screen_labels)
                ),
                title="3D Scatter: Age × Screen Time × Focus",
                height=600
            )
            st.plotly_chart(fig_3d_1, use_container_width=True)  # type: ignore
        
        with col2:
            st.subheader("Screen Time vs Study Hours vs Focus Level")
            
            fig_3d_2 = go.Figure(data=[go.Scatter3d(  # type: ignore
                x=temp_df['screen_code'],
                y=temp_df['study_hours_code'],
                z=temp_df['focus_level'],
                mode='markers',
                marker=dict(
                    size=8,
                    color=temp_df['focus_level'],
                    colorscale='Plasma',
                    showscale=True,
                    colorbar=dict(title="Focus Level"),
                    opacity=0.8
                ),
                text=temp_df[name_col],
                hovertemplate='<b>%{text}</b><br>Focus: %{z}<extra></extra>'
            )])
            
            study_labels = temp_df['About how many hours a day do you spend studying?'].unique().tolist()
            
            fig_3d_2.update_layout(  # type: ignore
                scene=dict(
                    xaxis_title='Screen Time Category',
                    yaxis_title='Study Hours Category',
                    zaxis_title='Focus Level',
                    xaxis=dict(tickvals=list(range(len(screen_labels))), ticktext=screen_labels),
                    yaxis=dict(tickvals=list(range(len(study_labels))), ticktext=study_labels)
                ),
                title="3D Scatter: Screen Time × Study Hours × Focus",
                height=600
            )
            st.plotly_chart(fig_3d_2, use_container_width=True)  # type: ignore
        
        st.write("---")
        st.subheader("Custom 3D Visualization")
        st.write("Select axes to create your own 3D visualization:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            x_axis = st.selectbox("Select X-axis", ["age_code", "screen_code", "focus_level", "study_hours_code"])
        with col2:
            y_axis = st.selectbox("Select Y-axis", ["screen_code", "study_hours_code", "focus_level", "age_code"], index=1)
        with col3:
            z_axis = st.selectbox("Select Z-axis", ["focus_level", "age_code", "study_hours_code", "screen_code"], index=0)
        
        fig_3d_custom = go.Figure(data=[go.Scatter3d(  # type: ignore
            x=temp_df[x_axis],
            y=temp_df[y_axis],
            z=temp_df[z_axis],
            mode='markers',
            marker=dict(
                size=8,
                color=temp_df['focus_level'],
                colorscale='RdBu',
                showscale=True,
                colorbar=dict(title="Focus Level"),
                opacity=0.8
            ),
            text=temp_df[name_col],
            hovertemplate='<b>%{text}</b><extra></extra>'
        )])
        
        fig_3d_custom.update_layout(  # type: ignore
            scene=dict(
                xaxis_title=x_axis.replace('_', ' ').title(),
                yaxis_title=y_axis.replace('_', ' ').title(),
                zaxis_title=z_axis.replace('_', ' ').title()
            ),
            title=f"Custom 3D: {x_axis} × {y_axis} × {z_axis}",
            height=700
        )
        st.plotly_chart(fig_3d_custom, use_container_width=True)  # type: ignore
        
    except Exception as e:
        st.error(f"Error creating 3D visualizations: {str(e)}")
        st.info("Please check that your data is loaded correctly.")

# ============================================================================
# PAGE 4: RAW DATA EDITOR
# ============================================================================
elif selected_page == "Raw Data Editor":
    st.title("📝 Raw Data Editor")
    st.write("---")
    
    try:
        st.subheader("Edit Dataset Directly")
        st.info("You can add new rows and edit existing data. Changes are live in the editor below.")
        
        # Data editor with editable rows
        edited_df = st.data_editor(  # type: ignore
            df,
            use_container_width=True,
            num_rows="dynamic",
            key="data_editor"
        )
        
        st.write("---")
        st.subheader("Data Export Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv = edited_df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="edited_data.csv",
                mime="text/csv"
            )
        
        with col2:
            try:
                from io import BytesIO
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:  # type: ignore
                    edited_df.to_excel(writer, index=False)  # type: ignore
                excel_data = output.getvalue()
                
                st.download_button(
                    label="📥 Download Excel",
                    data=excel_data,
                    file_name="edited_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except Exception:
                st.write("Excel export requires openpyxl: pip install openpyxl")
        
        with col3:
            if st.button("🔄 Reset to Original"):
                st.rerun()
        
        st.write("---")
        st.subheader("Edited Data Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows", len(edited_df))
        with col2:
            st.metric("Total Columns", len(edited_df.columns))
        
        # Show data types
        st.write("**Data Types:**")
        st.dataframe(pd.DataFrame(edited_df.dtypes, columns=['Data Type']), use_container_width=True)  # type: ignore
        
    except Exception as e:
        st.error(f"Error in Data Editor: {str(e)}")
        st.info("Please refresh the page to reload data.")

# ============================================================================
# PAGE 5: FILTERED ANALYSIS
# ============================================================================
elif selected_page == "Filtered Analysis":
    st.title("🔍 Filtered Analysis")
    st.write("---")
    
    try:
        st.subheader("Apply Filters")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            selected_age = st.multiselect(
                "Filter by Age Group",
                options=df['What is your age?'].unique().tolist(),
                default=df['What is your age?'].unique().tolist()
            )
        
        with col2:
            selected_screen = st.multiselect(
                "Filter by Screen Time",
                options=df['How many hours do you spend on screens each day?'].unique().tolist(),
                default=df['How many hours do you spend on screens each day?'].unique().tolist()
            )
        
        with col3:
            selected_device = st.multiselect(
                "Filter by Device",
                options=df['What device do you use most for screen time?'].unique().tolist(),
                default=df['What device do you use most for screen time?'].unique().tolist()
            )
        
        # Apply filters
        filtered_df = df[
            (df['What is your age?'].isin(selected_age)) &  # cspell:disable-line # type: ignore
            (df['How many hours do you spend on screens each day?'].isin(selected_screen)) &  # cspell:disable-line # type: ignore
            (df['What device do you use most for screen time?'].isin(selected_device))  # cspell:disable-line # type: ignore
        ]
        
        st.write("---")
        st.subheader(f"Filtered Results ({len(filtered_df)} records)")
        
        if len(filtered_df) > 0:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                avg_focus = filtered_df['How focused do you feel when you study? (1 = not focused, 5 = very focused)'].mean()
                st.metric("Average Focus Level", f"{avg_focus:.2f}/5")
            
            with col2:
                most_common_loc = filtered_df['Where do you usually study?'].mode()[0]
                st.metric("Most Common Study Location", most_common_loc)
            
            with col3:
                avg_sleep_counts = filtered_df['How many hours of sleep do you usually get on school nights?'].mode()[0]
                st.metric("Most Common Sleep Duration", avg_sleep_counts)
            
            st.write("---")
            st.subheader("Filtered Data Visualizations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Study Hours Distribution (Filtered)**")
                study_dist = filtered_df['About how many hours a day do you spend studying?'].value_counts()
                fig_study_filtered = px.bar(x=study_dist.index, y=study_dist.values,  # type: ignore
                                            title="Study Hours (Filtered)",
                                            labels={'x': 'Hours', 'y': 'Count'})
                st.plotly_chart(fig_study_filtered, use_container_width=True)  # type: ignore
            
            with col2:
                st.write("**Sleep Hours Distribution (Filtered)**")
                sleep_dist = filtered_df['How many hours of sleep do you usually get on school nights?'].value_counts()
                fig_sleep_filtered = px.bar(x=sleep_dist.index, y=sleep_dist.values,  # type: ignore
                                            title="Sleep Hours (Filtered)",
                                            labels={'x': 'Hours', 'y': 'Count'})
                st.plotly_chart(fig_sleep_filtered, use_container_width=True)  # type: ignore
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Break Frequency (Filtered)**")
                break_dist = filtered_df['How often do you take breaks while studying?'].value_counts()
                if break_dist.empty:
                    st.write("No break frequency data available for the selected filters.")
                else:
                    fig_break = px.pie(values=break_dist.values, names=break_dist.index,  # type: ignore
                                       title="Break Frequency (Filtered)")
                    st.plotly_chart(fig_break, use_container_width=True)  # type: ignore
            
            with col2:
                st.write("**Note-Taking Methods (Filtered)**")
                notes_dist = filtered_df['How do you usually take notes when studying?'].value_counts()
                fig_notes = px.pie(values=notes_dist.values, names=notes_dist.index,  # type: ignore
                                  title="Note-Taking Methods")
                st.plotly_chart(fig_notes, use_container_width=True)  # type: ignore
            
            st.write("---")
            st.subheader("Filtered Dataset")
            st.dataframe(filtered_df, use_container_width=True)  # type: ignore
            
            # Download filtered data
            csv_filtered = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Filtered Data as CSV",
                data=csv_filtered,
                file_name="filtered_data.csv",
                mime="text/csv"
            )
        else:
            st.warning("No records match the selected filters. Please adjust your filter criteria.")
            
    except Exception as e:
        st.error(f"Error in Filtered Analysis: {str(e)}")
        st.info("Please check your filter selections and try again.")