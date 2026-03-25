import streamlit as st

# ======================
# 页面基础设置
# ======================
st.set_page_config(page_title="公司评分系统", layout="wide")

# ======================
# 自定义样式（CSS）
# ======================
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.block {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-top: 20px;
}
.title {
    font-size: 32px;
    font-weight: bold;
}
.metric {
    font-size: 18px;
    margin: 8px 0;
}
.highlight {
    color: #2c7be5;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ======================
# 标题
# ======================
st.markdown('<div class="title">📊 公司评分系统</div>', unsafe_allow_html=True)

# ======================
# 输入区（居中）
# ======================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    name = st.text_input("请输入公司名称：", placeholder="例如：创新医疗")

# ======================
# 输出区
# ======================
if st.button("提交"):
    
    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.markdown("### 🏢 基本信息")
    st.markdown(f"""
- 公司名称：**创新医疗**  
- 赛道：脑机接口  
- 产业链环节：下游应用（智能康复系统）  
""")

    st.markdown("### 📈 核心评分")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="科技属性评分", value="0.46")
    with col2:
        st.metric(label="公司景气度评分", value="0.92")
    with col3:
        st.metric(label="风险衡量", value="0.56")

    st.markdown("### 🏆 综合排名")
    st.markdown('<div class="highlight">TRI综合评估排名：第19.4%</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
