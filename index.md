---
layout: default
body_class: home-page
---

<div class="lang-bar">
  <span class="lang-btn active" data-lang="en" onclick="switchLang('en')">EN</span>
  <span class="lang-btn" data-lang="zh" onclick="switchLang('zh')">中文</span>
</div>

<!-- ===== ENGLISH VERSION ===== -->
<div markdown="1" class="lang-content" id="lang-en">

I received my B.A. degree from the School of Internet of Things Engineering at Jiangnan University in 2015. From 2016 to 2018, I pursued my Master's degree at the Jiangsu Provincial Engineering Laboratory of Pattern Recognition and Computational Intelligence, Jiangnan University. I earned my Ph.D. degree from the same laboratory at [Jiangnan University](http://www.jiangnan.edu.cn/) in December 2021, under the supervision of [Prof. Xiao-Jun Wu](http://ai.jiangnan.edu.cn/info/1013/1500.htm).

I am currently an <span class="hl">Associate Professor</span> ([home page](https://ai.jiangnan.edu.cn/info/1014/4428.htm)) at the School of Artificial Intelligence and Computer Science and the International Joint Laboratory on Artificial Intelligence of Jiangsu Province, Jiangnan University, Wuxi, China. My research interests include computer vision, <span class="hl">multi-modal image fusion</span>, multi-modal super-resolution, and multi-modal detection/tracking.

I have published numerous scientific papers, including <span class="hl">8 highly cited papers</span> and <span class="hl">2 hot papers</span>, in top-tier venues such as <span class="hl">IEEE TPAMI, IEEE TIP, IJCV, CVPR, ICML, NeurIPS, and Information Fusion</span>. I achieved top tracking performance in several international competitions, including the <span class="hl">VOT2020 RGBT challenge (ECCV20), VOT2021 RGBD challenge (ICCV21), and Anti-UAV challenge (ICCV21)</span>. I have been consistently recognized in the <span class="hl"><a href="https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/8" style="color:inherit;text-decoration:inherit;">World's Top 2% Scientists ranking</a></span> published by Stanford University (2022, 2023, 2024, 2025).

**Current research:**
+ Multimodal Large Language Model, AI4Science
+ Medical image processing, Remote sensing
+ Multi-modal fusion, super-resolution
+ Multi-modal detection, tracking

**Email:**
+ lihui.cv@jiangnan.edu.cn
+ hui_li_jnu@163.com

---

# News

- **2026.05:** Two papers led by Huan Kang and Xinchang Wang were accepted by ICML 2026.
- **2026.04:** [EvaJudge](http://www.evanet.online:5001/), a converged online image fusion evaluation platform based on our TPAMI work (**EvaNet**), is now available. **It provides a unified evaluation environment and a public leaderboard mechanism, supporting efficient evaluation of image fusion methods**.
- **2026.02:** Two papers led by Congcong Bian and Yanglin Deng were accepted by CVPR 2026.

{% assign journal_publication_count = 0 %}
{% assign conference_publication_count = 0 %}
{% assign contest_count = 0 %}
{% assign preprint_count = 0 %}
{% for site_page in site.pages %}
   {% if site_page.path == "journal-publication/index.md" %}
      {% assign journal_publication_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "preprint/index.md" %}
      {% assign preprint_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "contest/index.md" %}
      {% assign contest_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "conference-publication/index.md" %}
      {% assign conference_publication_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
{% endfor %}

<div class="publication-navigation">
   <a class="publication-navigation-item" href="{{ site.baseurl }}/journal-publication/">
      <span class="publication-navigation-title">Journal list</span>
      <span class="publication-navigation-count">{{ journal_publication_count }} publications</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/conference-publication/">
      <span class="publication-navigation-title">Conference list</span>
      <span class="publication-navigation-count">{{ conference_publication_count }} publications</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/contest/">
      <span class="publication-navigation-title">Contest list</span>
      <span class="publication-navigation-count">{{ contest_count }} contests</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/preprint/">
      <span class="publication-navigation-title">Preprint list</span>
      <span class="publication-navigation-count">{{ preprint_count }} preprints</span>
   </a>
</div>





---

# Students

Master students (Co-advised with [Prof. Xiaoning Song](https://ai.jiangnan.edu.cn/info/1013/1507.htm) and [Prof. Xiaoqing Luo](https://ai.jiangnan.edu.cn/info/1013/3246.htm))
- [Yongbiao Xiao (Graduated)](https://github.com/draymondbiao)
- [Tianyu Shen (Graduated)](https://github.com/stywmy)
- [Haolong Ma](https://github.com/zipper112)
- [Congcong Bian](https://github.com/bociic)
- [Zhiming Meng](https://github.com/ZhimingMeng)
- [Jiancong Xu](https://github.com/xjcong404)
- Sheng Huang
- [Ziyang Liu](https://github.com/Vegetvigbird)
- Zhijia Din
- Jingwen Tan
- Zhenpeng Gao
- [Xinchang Wang (undergraduate)](https://github.com/dongdongunique)

---

# Experience

**2025.07 ~ now:** Associate Professor, School of Artificial Intelligence and Computer Science, Jiangnan University, China.
**2022.01 ~ 2025.07:** Lecturer, School of Artificial Intelligence and Computer Science, Jiangnan University, China.
**2018.09 ~ 2021.12:** Ph.D candidate in Control Science and Engineering in School of IoT, Jiangnan University, China.
**2016.09 ~ 2018.06:** Master in Computer science and technology in School of IoT, Jiangnan University, China.
**2015.06 ~ 2016.08:** Software engineer in Nanjing, China.
**2011.09 ~ 2015.06:** Bachelor in Computer science and technology in school of IoT, Jiangnan University, China.

---

# Activities

Associate Editor: Springer Nature (SN) Computer Science
Reviewer: IEEE TPAMI, IJCV, IEEE TIP, CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, AAAI, IJCAI, Information Fusion ...

</div>

<!-- ===== CHINESE VERSION ===== -->
<div markdown="1" class="lang-content" id="lang-zh" style="display:none">

我于2015年获得江南大学物联网工程专业学士学位。2016年至2018年，在江南大学江苏省模式识别与计算智能工程实验室攻读硕士学位。2021年12月，于同一实验室获得博士学位，师从[吴小俊教授](http://ai.jiangnan.edu.cn/info/1013/1500.htm)。

现任江南大学人工智能与计算机学院、江苏省人工智能国际联合实验室<span class="hl">副教授</span>（[个人主页](https://ai.jiangnan.edu.cn/info/1014/4428.htm)）。研究方向包括计算机视觉、<span class="hl">多模态图像融合</span>、多模态超分辨率以及多模态检测与跟踪。

已发表多篇学术论文，其中包括<span class="hl">8篇高被引论文</span>和<span class="hl">2篇热点论文</span>，发表于<span class="hl">IEEE TPAMI、IEEE TIP、IJCV、CVPR、ICML、NeurIPS、Information Fusion</span>等顶级期刊和会议。在多项国际竞赛中取得顶尖跟踪性能，包括<span class="hl">VOT2020 RGBT挑战赛（ECCV20）、VOT2021 RGBD挑战赛（ICCV21）及Anti-UAV挑战赛（ICCV21）</span>。连续入选斯坦福大学发布的<span class="hl"><a href="https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/8" style="color:inherit;text-decoration:inherit;">世界前2%科学家排名</a></span>（2022、2023、2024、2025）。

**当前研究方向：**
+ 多模态大模型，AI4Science
+ 医学图像处理，遥感
+ 多模态融合，超分辨率
+ 多模态检测，跟踪

**邮箱：**
+ lihui.cv@jiangnan.edu.cn
+ hui_li_jnu@163.com

---

# 新闻

- **2026.05：** 由康欢和王鑫昌同学主导的两篇论文被ICML 2026接收。
- **2026.04：** 基于我们TPAMI工作（EvaNet）的在线图像融合评估平台[EvaJudge](http://www.evanet.online:5001/)现已上线。**提供统一的评估环境和公开排行榜机制，支持高效的图像融合方法评估**。
- **2026.02：** 由边聪聪和邓杨林同学主导的两篇论文被CVPR 2026接收。

{% assign journal_publication_count = 0 %}
{% assign conference_publication_count = 0 %}
{% assign contest_count = 0 %}
{% assign preprint_count = 0 %}
{% for site_page in site.pages %}
   {% if site_page.path == "journal-publication/index.md" %}
      {% assign journal_publication_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "preprint/index.md" %}
      {% assign preprint_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "contest/index.md" %}
      {% assign contest_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
   {% if site_page.path == "conference-publication/index.md" %}
      {% assign conference_publication_count = site_page.content | split: 'class="publication media paperhi"' | size | minus: 1 %}
   {% endif %}
{% endfor %}

<div class="publication-navigation">
   <a class="publication-navigation-item" href="{{ site.baseurl }}/journal-publication/">
      <span class="publication-navigation-title">期刊论文</span>
      <span class="publication-navigation-count">{{ journal_publication_count }} 篇</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/conference-publication/">
      <span class="publication-navigation-title">会议论文</span>
      <span class="publication-navigation-count">{{ conference_publication_count }} 篇</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/contest/">
      <span class="publication-navigation-title">竞赛</span>
      <span class="publication-navigation-count">{{ contest_count }} 项</span>
   </a>
   <a class="publication-navigation-item" href="{{ site.baseurl }}/preprint/">
      <span class="publication-navigation-title">预印本</span>
      <span class="publication-navigation-count">{{ preprint_count }} 篇</span>
   </a>
</div>





---

# 学生

硕士研究生（与[宋晓宁教授](https://ai.jiangnan.edu.cn/info/1013/1507.htm)、[罗晓清教授](https://ai.jiangnan.edu.cn/info/1013/3246.htm)联合指导）
- [肖永彪（已毕业）](https://github.com/draymondbiao)
- [沈天宇（已毕业）](https://github.com/stywmy)
- [马浩龙](https://github.com/zipper112)
- [边聪聪](https://github.com/bociic)
- [孟志明](https://github.com/ZhimingMeng)
- [徐建聪](https://github.com/xjcong404)
- 黄晟
- [刘子阳](https://github.com/Vegetvigbird)
- 丁志佳
- 谭靖文
- 高振鹏
- [王鑫昌（本科）](https://github.com/dongdongunique)

---

# 经历

**2025.07 ~ 至今：** 副教授，江南大学人工智能与计算机学院
**2022.01 ~ 2025.07：** 讲师，江南大学人工智能与计算机学院
**2018.09 ~ 2021.12：** 博士研究生，控制科学与工程，江南大学物联网工程学院
**2016.09 ~ 2018.06：** 硕士研究生，计算机科学与技术，江南大学物联网工程学院
**2015.06 ~ 2016.08：** 软件工程师，南京
**2011.09 ~ 2015.06：** 本科，计算机科学与技术，江南大学物联网工程学院

---

# 学术服务

副编辑：Springer Nature (SN) Computer Science
审稿人：IEEE TPAMI, IJCV, IEEE TIP, CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, AAAI, IJCAI, Information Fusion ...

</div>

<script>
function switchLang(lang) {
  document.querySelectorAll('.lang-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });
  var enBlocks = document.querySelectorAll('.lang-content[id^="lang-en"]');
  var zhBlocks = document.querySelectorAll('.lang-content[id^="lang-zh"]');
  enBlocks.forEach(function(el) {
    el.style.display = (lang === 'en') ? 'block' : 'none';
  });
  zhBlocks.forEach(function(el) {
    el.style.display = (lang === 'zh') ? 'block' : 'none';
  });
  localStorage.setItem('homepage_lang', lang);
}
(function() {
  var saved = localStorage.getItem('homepage_lang');
  if (saved && (saved === 'en' || saved === 'zh')) {
    switchLang(saved);
  }
})();
</script>
