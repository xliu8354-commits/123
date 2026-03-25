import streamlit as st

st.title("公司评分系统")

name = st.text_input("请输入公司名称：")

if st.button("提交"):
    st.write(f"""
公司名称：创新医疗  
赛道：脑机接口/n
产业链环节：下游应用（智能康复系统）/n
科技属性评分：0.46  
公司景气度评分：0.92  
风险衡量：0.56  
TRI综合评估排名：第19.4%  
""")
