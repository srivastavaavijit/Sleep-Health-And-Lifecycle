import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

st.set_page_config(layout='wide', page_title='Sleep Health And Lifestyle Analysis')

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

st.sidebar.title("Dataset")


def load_details_categorical(variable):
    st.header('Conclusions:', divider='rainbow')
    # describe the variable:
    st.dataframe(df[variable].describe().reset_index())
    st.bar_chart(df[variable].value_counts(), color='#FF65D4')
    if variable == 'Gender':
        st.markdown(':orange[Distribution of males upon different occupations:]')
        st.dataframe(df[df['Gender'] == 'Male'])
        st.bar_chart(df[df['Gender'] == 'Male'].groupby('Occupation').size(), color='#FF65D4')
        st.markdown(':orange[Occupation wise distribution of females.]')
        st.dataframe(df[df['Gender'] == 'Female'])
        st.bar_chart(df[df['Gender'] == 'Female'].groupby('Occupation').size(), color='#FF65D4')
        st.markdown(':orange[Females are relatively higher than males.]')

    if variable == 'Sleep Disorder':
        st.markdown(':orange[Distribution of sleep disorder among different professions.]')
        st.bar_chart(df.groupby('Occupation')['Sleep Disorder'].size())


def load_details_numerical(variable):
    st.header('Conclusions:', divider='rainbow')
    st.markdown('Statistical View of data:')
    st.dataframe(df[variable].describe())
    st.markdown(':orange[Counts of different values present in the variable:]')
    # value_counts:
    st.bar_chart(df[variable].value_counts().sort_values(ascending=False), color='#FF65D4')
    # box_plot:
    st.markdown(':orange[Box Plot of the variable:]')
    col1, col2 = st.columns(2)
    with col1:
        data = df[variable]
        fig1, ax1 = plt.subplots()
        ax1.boxplot(data)
        st.pyplot(fig1)

    if variable == 'Age':
        st.markdown(':orange[Average Distribution of age on different occupation:]')
        st.bar_chart(df.groupby('Occupation')['Age'].mean())

    if variable == 'Stress Level':
        st.markdown(':orange[Distribution of sleep level among different professions.]')
        st.bar_chart(df.groupby('Occupation')['Stress Level'].size())


def load_univariate_analysis(variable):
    if type(df[variable][0]) == type("variable"):
        load_details_categorical(variable)
    elif variable == 'Sleep Disorder':
        load_details_categorical(variable)
    else:
        load_details_numerical(variable)


def load_introduction():
    st.header('Introduction of the project:', divider='rainbow')
    st.header(':orange[Title]: Sleep Patterns and Lifestyle Habits.', divider='rainbow')
    st.header(':orange[Introduction:]')
    st.markdown(
        'In this project, we delve into the intricate relationship between sleep patterns and lifestyle habits. Sleep '
        'is a fundamental aspect of human health and well-being, and understanding the factors influencing it can '
        'offer insights into improving overall quality of life. We aim to analyze a comprehensive dataset that '
        'encompasses various dimensions of sleep and lifestyle behaviors.')
    st.header(':orange[Description Of Dataset:]')
    st.markdown(':orange[Source]: The dataset is collected from kaggle.')
    st.markdown(':orange[Size]: It consists of 374 rows and 13 variables.')
    st.markdown(
        ':orange[Variables]: Gender, Age, Sleep Duration, Quality Of Sleep, Physical Activity Level, Stress Level, '
        'BMI Category, Blood Pressure, Heart Rate, Daily Steps, Sleep Disorder. ')
    st.dataframe(df)
    st.header(':orange[Objectives:]')
    st.markdown('Explore the distribution of sleep duration and quality within the dataset.')
    st.markdown('Identify correlations between sleep patterns and lifestyle habits.')
    st.markdown('Investigate the impact of demographics on sleep patterns.')
    st.markdown('Extract actionable insights to promote healthier sleep habits and lifestyle choices.')
    st.header(':orange[Methodology:]')
    st.markdown(
        'Data Preprocessing: Handle missing values, outliers, and inconsistencies in the dataset. Perform data '
        'cleaning and normalization as necessary.')
    st.markdown(
        'Exploratory Data Analysis (EDA): Visualize sleep patterns and lifestyle habits using histograms, box plots, '
        'scatter plots, and correlation matrices.')
    st.header(':orange[Conclusion:]')
    st.markdown('''Through comprehensive analysis of the dataset, we've gained valuable insights into the complex 
    interplay between sleep patterns and lifestyle habits of different professions. Our findings underscore the 
    importance of adopting healthier practices to improve sleep quality and overall well-being of different 
    professions.''')


def load_overall_analysis():
    st.header('Overall Analysis', divider='rainbow')
    st.markdown('''
        :orange[On average female sleeps for 7.2hrs and male sleeps for 7hrs, which suggests that female needs more 20 minutes of sleep than male].'''
                )
    st.write(
        ":green[Reason]: Sleep differences between men and woman come down to numerous behavioral and biological "
        "variables that change through the different stages of life.")
    st.markdown('''
       :orange[Females have more quality of sleep than males.]'''
                )
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Gender')['Sleep Duration'].mean()
        st.bar_chart(data, y='Sleep Duration')
    with col2:
        data = df.groupby('Gender')['Quality of Sleep'].mean()
        st.bar_chart(data, y='Quality of Sleep', color=['#FF65D4'])

    st.markdown('''
        :orange[Males have higher stress level than females.]
    ''')
    st.markdown('''
        :orange[sales representative is the job with most high stress level while engineers belongs to the category with minimum average stress level.]
    ''')
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Gender')['Stress Level'].mean()
        st.bar_chart(data, y='Stress Level')
    with col2:
        data = df.groupby('Occupation')['Stress Level'].mean()
        st.bar_chart(data, y='Stress Level', color=['#FF65D4'])

    st.markdown('''
        :orange[Figure 1 shows age wise distribution of stress level among individuals of different occupations.]
    ''')
    st.markdown('''
        :orange[Overweight people mostly suffers from Insomnia and Sleep Apnea, out of which females are more likely to get affected with these sleep disorders than males.]
    ''')
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Age')['Stress Level'].mean()
        st.bar_chart(data, y='Stress Level')
    with col2:
        data = df[df['BMI Category'] == 'Overweight'].groupby('Gender')['Sleep Disorder'].size()
        st.bar_chart(data, color=['#FF65D4'])

    st.markdown('''
        :orange[Nurses are more likely to suffer from Sleep Apnea, the potential reason could be because of their job schedules.]
    ''')
    st.markdown('''
        :orange[Most of the Salesperson suffers from Insomnia.]
    ''')
    col1, col2 = st.columns(2)
    with col1:
        sleep_apnea = df[df['Sleep Disorder'] == 'Sleep Apnea']
        data = sleep_apnea.groupby('Occupation').size().sort_values(ascending=False)
        st.bar_chart(data)
    with col2:
        insomnia = df[df['Sleep Disorder'] == 'Insomnia']
        data = insomnia.groupby('Occupation').size().sort_values(ascending=False)
        st.bar_chart(data, color=['#FF65D4'])


def load_doctor_details():
    doctors = df[df['Occupation'] == 'Doctor']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(doctors.describe())
    st.markdown(':orange[Overall distribution of gender among doctors in the dataset:]')
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(doctors['Gender'].value_counts(), color=['#FF65D4'])
    with col2:
        pass

    st.markdown(':orange[Most of the doctors suffers from high stress level, it may be because of their jobs.]')
    st.markdown(':orange[Dataset also suggests that most of the doctors have low physical activity level which might '
                'also contribute to their stress level.]')
    st.dataframe(doctors[doctors['Physical Activity Level'] < 40])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(':orange[Out of all, 3 doctors suffers from Insomnia while 4 suffers from Sleep Apnea.]')
        st.bar_chart(doctors.groupby('Sleep Disorder').size(), color=['#FF65D4'])
    with col2:
        st.markdown(':orange[Distribution of BMI Category among Doctors:]')
        st.bar_chart(doctors['BMI Category'].value_counts(), color=['#FF65D4'])


def load_accountant_details():
    accountants = df[df['Occupation'] == 'Accountant']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(accountants.describe())
    st.markdown(':orange[There are total of 37 accountants in the dataset.]')
    st.markdown(
        ':orange[Out of all, seven accountants suffers from Insomnia while none of them have sleep apnea. It may be '
        'because the ones having Insomnia are having age greater than 50 while have whose age is 32 , suffers from '
        'low blood pressure.]')
    col1, col2 = st.columns(2)
    with col1:
        data = df[df['Sleep Disorder'] == 'Insomnia'].groupby('Occupation')['Sleep Disorder'].size()
        st.bar_chart(data)
    with col2:
        data = df.groupby('Occupation')['Physical Activity Level'].mean()
        st.bar_chart(data)
    accountants_insomnia = accountants[accountants['Sleep Disorder'] == 'Insomnia']
    st.header('Details of accountants suffering from Insomnia:', divider='rainbow')
    st.dataframe(accountants_insomnia.describe())


def load_engineer_details():
    engineers = df[df['Occupation'] == 'Engineer']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(engineers.describe())
    st.markdown(':orange[Engineers have minimum stress level among all other professions.]')
    st.markdown(':orange[Their sleep duration average is 7.9.]')
    col1, col2 = st.columns(2)
    with col1:
        data = engineers['Stress Level']
        fig1, ax1 = plt.subplots()
        ax1.hist(data)
        st.pyplot(fig1)
    with col2:
        data = engineers['Sleep Duration']
        fig2, ax2 = plt.subplots()
        ax2.hist(data)
        st.pyplot(fig2)
    st.markdown(':orange[They perform physical activity below than the average activity level.]')
    st.markdown(':orange[Their heart rate is normal.]')
    engineers = df[df['Occupation'] == 'Engineer']
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Occupation')['Physical Activity Level'].mean().sort_values(ascending=False)
        st.bar_chart(data)
    with col2:
        data = engineers['Sleep Duration']
        fig2, ax2 = plt.subplots()
        ax2.hist(data)
        st.pyplot(fig2)
    st.markdown(':orange[The average of their daily steps is almost 6000 steps.]')
    st.markdown(
        ':orange[Only one engineer from the dataset suffers from sleep apnea, though all the health parameters seems '
        'fine, it may be because of the age.]')
    st.markdown(
        ':orange[Three engineers suffers from insomnia, the potential reason behind this might be the age factor.]')
    engineers = df[df['Occupation'] == 'Engineer']
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Occupation')['Daily Steps'].mean().sort_values(ascending=False)
        st.bar_chart(data)
    with col2:
        pass


def load_lawyer_details():
    lawyers = df[df['Occupation'] == 'Lawyer']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(lawyers.describe())
    st.markdown(':orange[Distribution of gender upon the profession:]')
    st.markdown(':orange[Distribution suggests that males are more likely to get into Lawyer profession than females.]')
    st.bar_chart(df[df['Occupation'] == 'Lawyer']['Gender'].value_counts(), color=['#FF65D4'])
    st.markdown(':orange[It can be concluded from the dataset that lawyers have average stress level among all the '
                'mentioned professions.]')
    st.bar_chart(df.groupby('Occupation')['Stress Level'].size(), color=['#FF65D4'])
    st.markdown(':orange[Out of all lawyers, 2 suffers from Insomnia while 3 suffers from Sleep Apnea.]')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('Fig 1. shows the occupation with Sleep disorder - Insomnia.')
        st.bar_chart(df[df['Sleep Disorder'] == 'Insomnia'].groupby('Occupation')['Sleep Disorder'].size(),
                     color=['#FF65D4'])
    with col2:
        st.markdown('Fig 2. shows the occupation with Sleep disorder - Sleep Apnea.')
        st.bar_chart(df[df['Sleep Disorder'] == 'Sleep Apnea'].groupby('Occupation')['Sleep Disorder'].size(),
                     color=['#FF65D4'])


def load_manager_details():
    managers = df[df['Occupation'] == 'Manager']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(managers.describe())
    st.markdown(':orange[Dataset contains only one person with a position of Manager.]')


def load_nurse_details():
    nurses = df[df['Occupation'] == 'Nurse']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(nurses.describe())
    st.markdown(':orange[Mostly nurses are overweight in BMI category.]')
    st.markdown(':orange[Their stress level is above average of all the occupations.]')
    col1, col2 = st.columns(2)
    with col1:
        data = nurses['BMI Category'].value_counts()
        st.bar_chart(data)
    with col2:
        data = nurses['Stress Level']
        fig2, ax2 = plt.subplots()
        ax2.hist(data)
        st.pyplot(fig2)

    st.markdown(
        ':orange[Every nurse suffers from high blood pressure, it may be because of their jobs, which is quite hectic in nature.]')
    st.markdown(
        ':orange[Their are only three nurses that are into Normal weight BMI category and does not suffer from any sleep Disorder.]')
    st.markdown(':orange[Most of the nurses have high daily steps , it may be beacause of their occupation.]')
    col1, col2 = st.columns(2)
    with col1:
        data = nurses['Blood Pressure'].value_counts()
        st.bar_chart(data)
    with col2:
        data = df.groupby('Occupation')['Daily Steps'].mean()
        st.bar_chart(data)


def load_salesr_details():
    salesr = df[df['Occupation'] == 'Sales Representative']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(salesr.describe())
    st.markdown(':orange[Dataset contains only 2 persons with Sales Representative position.]')
    st.markdown(':orange[Both the Sales Representative suffers from Sleep Apnea and high blood pressure.]')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('Fig1. shows the distribution of stress level upon different occupation.')
        st.bar_chart(df.groupby('Occupation')['Stress Level'].size())
    with col2:
        st.markdown('Fig2. shows the distribution of daily steps upon different occupation.')
        st.bar_chart(df.groupby('Occupation')['Daily Steps'].size())


def load_salesp_details():
    salesp = df[df['Occupation'] == 'Salesperson']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(salesp.describe())
    st.markdown(':orange[Most of the salesperson suffers from Insomnia.]')
    st.markdown(
        ':orange[Every salesperson suffers from high blood pressure, which could be due to the problem of insomnia.]')
    col1, col2 = st.columns(2)
    with col1:
        data = df[df['Sleep Disorder'] == 'Insomnia'].groupby('Occupation')['Sleep Disorder'].size()
        st.bar_chart(data, color=['#FF65D4'])
    with col2:
        data = salesp['Blood Pressure'].value_counts()
        st.bar_chart(data, color=['#FF65D4'])
    st.markdown(':orange[Every salesperson belongs to overweight category.]')
    st.markdown(':orange[EAll of the salesperson are above the age of 40 years.]')
    col1, col2 = st.columns(2)
    with col1:
        data = df.groupby('Occupation')['Age'].mean()
        st.bar_chart(data, color=['#FF65D4'])
    with col2:
        pass
    st.markdown(':orange[Only one salesperson with ID 220 suffers from Sleep apnea.]')
    st.markdown(
        ':orange[Two salesperson with ID - 249 and 250 does not suffer from any sleep disorder but their sleep '
        'duration is below the average also have low quality of sleep and high stress level.]')


def load_se_details():
    se = df[df['Occupation'] == 'Software Engineer']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(se.describe())
    st.markdown(':orange[Data of Software Engineers:]')
    st.dataframe(df[df['Occupation'] == 'Software Engineer'])

    st.markdown(':orange[A software engineer with ID 6 suffers from Insomnia, which might be due to obese - BMI '
                'Category, which also affected sleep cycle.]')


def load_teacher_details():
    teachers = df[df['Occupation'] == 'Teacher']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(teachers.describe())
    st.markdown(':orange[Most of the teachers suffer from Insomnia.]')
    st.markdown(':green[Reason:]')
    st.markdown('Based on studies that met validity and reliability criteria, 36-61% of teachers reported insomnia '
                'symptoms. Associated factors included: being female, classroom violence, low job satisfaction, pain, '
                'depression, and rumination.')
    st.markdown(':orange[It can be noted that females are in higher ratio than males in Teacher Profession.]')
    st.markdown(':green[Reason:]')
    st.markdown('Economics suggests that the most important contributing factor to the disparity has been the pay '
                'scale distortion.')
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(teachers['Gender'].value_counts(), color=['#FF65D4'])

    with col2:
        st.bar_chart(teachers['Sleep Disorder'].value_counts())


def load_scientist_details():
    scientists = df[df['Occupation'] == 'Scientist']
    st.header('Conclusions:', divider='rainbow')
    st.dataframe(scientists.describe())
    st.markdown(':orange[Dataset contains details of only four scientists.]')
    st.dataframe(df[df['Occupation'] == 'Scientist'])
    st.markdown(':orange[Two scientist have sleep disorder - Sleep Apnea. The Potential reason could be their low sleep'
                'duration and also high stress level which might be due to thier job.]')
    st.markdown(':orange[It can also be concluded that all the scientist in the dataset belongs to overweight - BMI '
                'Category' 'that have affected their health in different parameters such as Blood Pressure , '
                'their quality of' 'sleep.]')


def load_profession_wise_details(profession):
    if profession == 'Accountant':
        load_accountant_details()
    elif profession == 'Engineer':
        load_engineer_details()
    elif profession == 'Lawyer':
        load_lawyer_details()
    elif profession == 'Manager':
        load_manager_details()
    elif profession == 'Nurse':
        load_nurse_details()
    elif profession == 'Sales Representative':
        load_salesr_details()
    elif profession == 'Salesperson':
        load_salesp_details()
    elif profession == 'Scientist':
        load_scientist_details()
    elif profession == 'Software Engineer':
        load_se_details()
    elif profession == 'Teacher':
        load_teacher_details()
    else:
        load_doctor_details()


options = st.sidebar.selectbox('Select One', ['Introduction', 'Overall Analysis', 'Profession-Wise-Analysis',
                                              'Statistical Analysis Of Variables'])

if options == 'Overall Analysis':
    load_overall_analysis()

elif options == 'Profession-Wise-Analysis':
    profession = st.sidebar.selectbox('Select Profession', sorted(df['Occupation'].unique().tolist()))
    btn1 = st.sidebar.button('Show Analysis')
    if btn1:
        load_profession_wise_details(profession)

elif options == 'Statistical Analysis Of Variables':
    variable = st.sidebar.selectbox('Select Variable', sorted(df.columns.tolist()[1:]))
    btn2 = st.sidebar.button('Show Statistical Analysis')
    if btn2:
        load_univariate_analysis(variable)
else:
    load_introduction()
