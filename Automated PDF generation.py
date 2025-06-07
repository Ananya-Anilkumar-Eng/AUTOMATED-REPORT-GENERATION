import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Step 1: Load the Pima Indian Diabetes Data using Pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
col=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
df=pd.read_csv(url,names=col)

# Step 2: From the data plot few valid graphs using seaborn and matplotlib
plt.figure(figsize=(4, 4))
sns.barplot(data=df[:20],x='Age',y='Pregnancies',color='red')
plt.title("Age-Pregnancies")
plt.xlabel("Age")
plt.ylabel("Pregnancies")
plt.tight_layout()
plt.savefig("AP_chart.png")

plt.figure(figsize=(4, 4))
sns.histplot(data=df[:20],x='Glucose',y='Insulin',color='red')
plt.title("Glucose-Insulin")
plt.xlabel("Glucose")
plt.ylabel("Insulin")
plt.tight_layout()
plt.savefig("GI_chart.png")
plt.close()
print("STEP2")

#Step 4: Using ReportLab create a PDF frame
doc = SimpleDocTemplate(r"C:\Users\Ananya\Desktop\pima_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("PIMA INDIAN DIABETES REPORT", styles['Title']))
elements.append(Spacer(1, 12))
print("Title")

# General Information
elements.append(Paragraph("<b><u>GENERAL INFROMATION </u></b>", styles['Italic']))

elements.append(Paragraph(f"<b>Names of columns</b>", styles['Heading3']))
l=[]
for i in df.columns:
    l.append(i)
elements.append(Paragraph(f"{l}", styles['Normal']))
elements.append(Spacer(1, 6))

elements.append(Paragraph(f"<b>Shape of dataset</b>", styles['Heading3']))
elements.append(Paragraph(f"{df.shape}", styles['Normal']))
elements.append(Spacer(1, 6))
print("General")
#Descriptive Statistics
elements.append(Paragraph("<b><u>DESCRIPTIVE STATISTICS</u></b>", styles['Italic']))
elements.append(Paragraph(f"<b>Mean</b>", styles['Heading3']))
A=df.mean()
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Spacer(1, 6))

elements.append(Paragraph(f"<b>Mode</b>", styles['Heading3']))    
elements.append(Paragraph(f"{df.mode()}",styles['Normal']))
elements.append(Spacer(1, 6))
                          
A=df.median()
elements.append(Paragraph(f"<b>Median</b>", styles['Heading3']))
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))

A=df.var()
elements.append(Paragraph(f"<b>Variance</b>", styles['Heading3']))
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Spacer(1, 6))

A=df.std()
elements.append(Paragraph(f"<b>Standard Deviation</b>", styles['Heading3']))
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))

elements.append(Paragraph(f"<b>Univariate Analysis</b>", styles['Heading3']))
elements.append(Paragraph(f"---Skewness---", styles['Normal']))
A=df.skew()
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Paragraph(f"---Kurtosis---", styles['Normal']))
A=df.kurtosis()
j=0;
for i in A:
    elements.append(Paragraph(f"{col[j],i}", styles['Normal']))
    j=j+1
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))

elements.append(Paragraph(f"<b>Bivariate Analysis</b>", styles['Heading3']))
y=df['SkinThickness']
x=df['BMI']
x=sm.add_constant(x)
m1=sm.OLS(y,x).fit()
elements.append(Paragraph(f"{m1.summary()}", styles['Normal']))
print("Descriptive")
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))
elements.append(Spacer(1, 6))
# Add Image
elements.append(Paragraph(f"<b><u>DATA VISUALIZATION</u></b>", styles['Italic']))
elements.append(Paragraph("<b>Age-Pregnancies Chart:</b>", styles['Heading3']))
elements.append(Spacer(1, 4))
elements.append(Image("AP_chart.png", width=400, height=300))
elements.append(Paragraph("<b>Glucose-Insulin Chart:</b>", styles['Heading3']))
elements.append(Spacer(1, 4))
elements.append(Image("GI_chart.png", width=400, height=300))
print("Images")

# Build PDF
doc.build(elements)

print("PDF report generated: iris_report_rl.pdf")
