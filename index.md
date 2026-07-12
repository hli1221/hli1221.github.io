---
layout: default
body_class: home-page
---

I received my B.A. degree from the School of Internet of Things Engineering at Jiangnan University in 2015. From 2016 to 2018, I pursued my Master's degree at the Jiangsu Provincial Engineering Laboratory of Pattern Recognition and Computational Intelligence, Jiangnan University. I earned my Ph.D. degree from the same laboratory at [Jiangnan University](http://www.jiangnan.edu.cn/) in December 2021, under the supervision of [Prof. Xiao-Jun Wu](http://ai.jiangnan.edu.cn/info/1013/1500.htm).

I am currently an Associate Professor ([home page](https://ai.jiangnan.edu.cn/info/1014/4428.htm)) at the School of Artificial Intelligence and Computer Science and the International Joint Laboratory on Artificial Intelligence of Jiangsu Province, Jiangnan University, Wuxi, China. I have published numerous scientific papers, including <span class="hl">8 highly cited papers and 2 hot papers</span>, in top-tier venues such as <span class="hl">IEEE TPAMI, IEEE TIP, IJCV, CVPR, ICML, NeurIPS, and Information Fusion et al.</span>. I achieved top tracking performance in several international competitions, including the VOT2020 RGBT challenge (ECCV20), VOT2021 RGBD challenge (ICCV21), and Anti-UAV challenge (ICCV21). I have been consistently recognized in the <span class="hl"><a href="https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/8" style="color:inherit;text-decoration:inherit;">World's Top 2% Scientists ranking</a></span> published by Stanford University (2022, 2023, 2024, 2025).

**Current research:**
+ Multimodal Large Model, AI4Science  
+ Medical image processing, Remote sensing  
+ Multi-modal fusion, super-resolution  
+ Multi-modal detection, tracking 

**Email:**  
+ lihui.cv@jiangnan.edu.cn  
+ hui_li_jnu@163.com  

<!-- ---
# Github Infor

[![GitHub contributions](https://github-readme-stats.vercel.app/api?username=hli1221&theme=calm&show_icons=true&hide_rank=true&hide=issues,contribs)](https://github-readme-stats.vercel.app)
[![GitHub contributions](https://github-readme-stats.vercel.app/api/top-langs/?username=hli1221&hide=html,css,Jupyter+Notebook,ruby,javascript&langs_count=6&theme=calm&layout=compact)](https://github-readme-stats.vercel.app)
 -->
 
<!-- height="165" -->
<!-- <div >
    <img align="left" src="https://github-contribution-stats.vercel.app/api/?username=hli1221" />
    <img align="left" src="https://github-readme-stats.vercel.app/api?username=hli1221&theme=calm&show_icons=true" />
    <img align="left" src="https://github-readme-stats.vercel.app/api/top-langs/?username=hli1221&hide=html,css,Jupyter+Notebook,ruby,javascript&theme=calm&langs_count=6&layout=compact" />
</div> -->

---
# News

- **2026.07:** One paper led by Kang Wang weas accepted by ACM MM 2026.
- **2026.05:** Two papers led by Huan Kang and Xinchang Wang were accepted by ICML 2026.
- **2026.04:** [EvaJudge](http://www.evanet.online:5001/), a converged online image fusion evaluation platform based on our TPAMI work (**EvaNet**), is now available. **It provides a unified evaluation environment and a public leaderboard mechanism, supporting efficient evaluation of image fusion methods**.
- **2026.02:** Two papers led by Congcong Bian and Yanglin Deng were accepted by CVPR 2026.


---
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

Mater students (Co-advised with [Prof. Xiaoning Song](https://ai.jiangnan.edu.cn/info/1013/1507.htm) and [Prof. Xiaoqing Luo](https://ai.jiangnan.edu.cn/info/1013/3246.htm))  
- [Yongbiao Xiao (Graduated)](https://github.com/draymondbiao)  
- [Tianyu Shen (Graduated)](https://github.com/stywmy)  
- [Haolong Ma (Graduated)](https://github.com/zipper112)  
- [Zhiming Meng (Graduated)](https://github.com/ZhimingMeng)  
- [Jiancong Xu (Graduated)](https://github.com/xjcong404)  
- [Congcong Bian](https://github.com/bociic)  
- Sheng Huang  
- [Ziyang Liu](https://github.com/Vegetvigbird)  
- Zhijia Din  
- Jingwen Tan  
- Zhenpeng Gao

<!-- - [Xinchang Wang (undergraduate)](https://github.com/dongdongunique) -->

	
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
