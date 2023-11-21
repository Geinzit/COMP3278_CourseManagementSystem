from django.db import models

from manager.models import Teacher

# Creating instances of the Teacher model
teacher1 = Teacher(
    id=10001,
    name="Prof. Ben Kao",
    department="Department of Computer Science",
    bio=("Professor Ben Kao is a professor in the Department of Computer Science at The University of Hong Kong. "
         "He received the BSc degree in computer science from The University of Hong Kong in 1989, the PhD degree in "
         "computer science from Princeton University in 1995. From 1989-1991, he was a teaching and research assistant "
         "at Princeton University. From 1992-1995, he was a research fellow at Stanford University.")
)

teacher2 = Teacher(
    id=10002,
    name="Dr. Loretta Choi",
    department="Department of Computer Science",
    bio=("Dr. Choi received her BSc, MPhil and PhD degrees in Computer Science from the University of Hong Kong. "
         "She was selected for the Best Tutor Award in the Department in 2005 and was awarded the Li Ka Shing Prize "
         "for Best PhD Thesis in the Faculties of Dentistry, Engineering, Medicine and Science by HKU in 2009. She is "
         "also currently the Project Manager for the WATERMAN project (www.waterman.hku.hk) which is funded by The Hong "
         "Kong Jockey Club Charities Trust for developing a water quality forecast and management system for Hong Kong. "
         "Her current research interests include medical visualization, geometric computing and computer graphics.")
)

teacher3 = Teacher(
    id=10003,
    name="Dr. T.W. Chim",
    department="Department of Computer Science",
    bio=("Dr. T.W. Chim received his B.Eng, M.Phil. and Ph.D. degrees in Information Engineering, Electrical and "
         "Electronic Engineering and Computer Science, respectively, from the University of Hong Kong. He has received "
         "4 best tutor awards from the Department of Computer Science from 2008 to 2012. He has been an instructor in "
         "the Department of Computer Science since September 2012.")
)

teacher4 = Teacher(
    id=10004,
    name="Prof. S.M. Yiu",
    department="Department of Computer Science",
    bio=("Professor Yiu received a BSc in Computer Science from the Chinese University of Hong Kong, a MS in Computer "
         "and Information Science from Temple University, and a PhD in Computer Science from The University of Hong Kong. "
         "He received two research output prizes, one from the department in 2013 and one from the faculty in 2006. He "
         "was selected for Outstanding Teaching Award by the University in 2009, the Teaching Excellence Award in the "
         "Department in 2001, 2003, 2004, 2005, 2007, 2009, and 2010. He also received the Best Teacher Award of the "
         "Faculty of Engineering twice (2005 and 2009). Before he joined the Department as a faculty member, he has "
         "worked as an Analyst Programmer for a couple of years. Besides basic research, he has been involving in "
         "various industrial projects.")
)

teacher5 = Teacher(
    id=10005,
    name="Dr. H.T.H. Chan",
    department="Department of Computer Science",
    bio=("Dr Hubert Chan is currently an Associate Professor at the Department of Computer Science at the University "
         "of Hong Kong. He completed his PhD in Computer Science at Carnegie Mellon University in 2007. In his PhD "
         "thesis, he investigated notions of metric dimension and the design of algorithms whose performance adapts "
         "to the dimension of the given metric. Before taking up the faculty position at HKU, he spent two years as "
         "a post-doc at Max-Planck-Institut fuer Informatik in Germany.")
)

teacher6 = Teacher(
    id=10006,
    name="Dr. Qi Zhao",
    department="Department of Computer Science",
    bio=("Dr. Qi Zhao is a Tenure-Track Assistant Professor in the Department of Computer Science, the University of "
         "Hong Kong (HKU). His research interests include quantum simulation, quantum computing, resource theory, "
         "self-testing quantum information, and entanglement detection. He is interested in any fundamental problem "
         "in quantum information, and the practical applications of quantum computers. He received his PhD degree "
         "from Tsinghua University in Dec. 2018. Then he became a postdoctoral researcher in University of Science "
         "and Technology, China from Jan. 2019 to Oct. 2019. In Dec. 2019, he joined University Of Maryland QuICS as "
         "a Hartree Postdoctoral Fellow in quantum information science.")
)

teacher7 = Teacher(
    id=10007,
    name="Dr. Yuxiang Yang",
    department="Department of Computer Science",
    bio=("I am a quantum information theorist, currently an assistant professor at the University of Hong Kong. "
         "From 2018 to 2021, I worked at ITP, ETH Zürich (Renato Renner's group) as a postdoc. "
         "I obtained a PhD in Computer Science from the University of Hong Kong (2018; supervisor: Giulio Chiribella) "
         "and a Bachelor in Physics from Tsinghua University (2013).")
)

teacher8 = Teacher(
    id=10008,
    name="Dr. Ravi Ramanathan",
    department="Department of Computer Science",
    bio=("Dr. Ramanathan's main research interests are in Quantum Cryptography, specifically Randomness Amplification, "
         "Expansion and Key Distribution, Device-Independent Applications of Quantum Theory and Foundations of Quantum Mechanics. "
         "He has 32 refereed publications in these areas, including 10 papers in Physical Review Letters and 3 in Nature Communications. "
         "He received his B.Eng. degree from the Nanyang Technological University in 2004 and received his MSc and PhD in Physics at the "
         "National University of Singapore in 2008 and 2013. Before joining HKU, he spent four years as a Research Fellow at The National "
         "Quantum Information Centre at The University of Gdansk and two years as a Postdoctoral Researcher at Universite Libre de Bruxelles "
         "and University of Oxford.")
)

teacher9 = Teacher(
    id=10009,
    name="Dr. Kenneth Wong",
    department="Department of Computer Science",
    bio=("Dr. Wong received the BEng degree in Computer Engineering, with first class honors, from the Chinese University of Hong Kong in 1998. "
         "From 1998 to 2001, he studied in United Kingdom at the University of Cambridge, where he was a member of the Speech, Vision and Robotics Group in the "
         "Department of Engineering. He received the MPhil and PhD degrees, both in Computer Vision (Information Engineering), from the University of Cambridge "
         "in 2000 and 2001, respectively. Since 2001, he has been with the Department of Computer Science at The University of Hong Kong, where he is now an "
         "associate professor. He served as the associate head of the department, being responsible for admissions and student affairs, from 2008 to 2012, and as "
         "the programme director of the BEng(CompSci) programme from 2008 to 2015. Dr. Wong served as the vice-chairperson of ACM-HK from 2003 to 2005, and chaired "
         "the ACM Collegiate Programming Contest (Hong Kong) in 2003 and 2005. He has served as referee for various international conferences and journals, including "
         "ICCV, ECCV, ACCV, ICIP, PAMI, IJCV, IVC, etc. Dr. Wong's research interests are in image processing, computer vision and computer graphics, including image "
         "segmentation and feature extraction, camera calibration, structure and motion from image sequence, and 3D model representation.")
)

teacher10 = Teacher(
    id=10010,
    name="Dr. Chenxiong Qian",
    department="Department of Computer Science",
    bio=("I am an Assistant Professor at the Computer Science Department in The University of Hong Kong. I lead the HKUS3 Lab, where we design and build systems to "
         "automatically detect and prevent attacks in software and systems. Our research interests encompass program analysis, software debloating, dynamic/hybrid testing, "
         "and binary code analysis.")
)

teacher11 = Teacher(
    id=10011,
    name="Dr. Ting Hing Fung",
    department="Department of Computer Science",
    bio=("Dr. Ting received his PhD from Princeton University and joined this department in 1994. His research interests include bioinformatics, computational complexity "
         "and design and analysis of algorithms, and has published over forty papers in these areas. Dr. Ting is also an active member of the ACM(HK). He was the programme "
         "committee chair of the ACM(HK) Postgraduate Day 2002, and was in the programme committee of the ACM(HK) Postgraduate Day 2003. More about other publications: "
         "http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/t/Ting:Hing=Fung.html")
)

teacher12 = Teacher(
    id=10012,
    name="Dr. Ruibang Luo",
    department="Department of Computer Science",
    bio=("Luo received his Ph.D. degree in computer science from the University of Hong Kong in 2015. He was a postdoctoral fellow in the Center of Computational Biology, "
         "McKusick-Nathans Institute of Genetic Medicine, Johns Hopkins University School of Medicine. Luo is a researcher working on 1) bioinformatics algorithm, 2) precision "
         "medicine, 3) metagenomics, and 4) literature mining. His research results have been published in peer-reviewed journals including Nature, Nature Biotechnology, "
         "Nature Machine Intelligence, Nature Communications, and Bioinformatics.")
)

teacher13 = Teacher(
    id=10013,
    name="Dr. Chenshu Wu",
    department="Department of Computer Science",
    bio=("I'm currently an Assistant Professor in the Department of Computer Science, The University of Hong Kong, where I lead the AIoT Lab. "
         "I served as the Chief Scientist and am now a consultant of Origin AI, a startup commercializing wireless sensing technologies and winning prestigious awards including the CES Best of Innovation Award. "
         "I was an Assistant Research Scientist in the Department of Electrical and Computer Engineering, University of Maryland, College Park and the Chief Scientist at Origin Wireless, working with Prof. K. J. Ray Liu, "
         "after working as a research associate in the Department of Computer Science, Princeton University and the School of Software, Tsinghua University. "
         "I received my Ph.D. degree in the Department of Computer Science and Technology, Tsinghua University, under supervision of Prof. Yunhao Liu. During my Ph.D., "
         "I was lucky to work with Prof. Mingyan Liu in the Department of EECS, University of Michigan and Prof. Jiannong Cao in the Department of Computing, HKPU. "
         "I received my B.E. degree from the School of Software, Tsinghua University.")
)

teacher14 = Teacher(
    id=10014,
    name="Dr. A.T.C. Tam",
    department="Department of Computer Science",
    bio=("Dr. Tam obtained a professional qualification in medical imaging during his undergraduate studies in Polytechnic. While working as a radiographer in the hospital, "
         "he started exploring the fascinating computer world by studying through distance learning mode. He received a BSc with first class honor from the EAOI "
         "(which has transformed to the current Asia International Open University, Macau). He moved on with the computer studies at Queensland University of Technology "
         "(Australia) and obtained his Master degree in 1996. He obtained his PhD in Computer Science from The University of Hong Kong in 2002. During his association "
         "with the Department of Computer Science, he has been selected as an outstanding tutor for 3 years.")
)

teacher15 = Teacher(
    id=10015,
    name="Dr. Heming Cui",
    department="Department of Computer Science",
    bio=("Dr. Cui received his bachelor and master degrees from Tsinghua University, and he joined HKU in January 2015 right after he received his PhD degree from Columbia University; "
         "all his degrees are in Computer Science. Dr. Cui is interested in building software infrastructures and tools to greatly improve the reliability, security and performance "
         "of real-world software. His PhD students' recent research has led to a series of open source projects and publications in international top conferences and journals of broad areas, "
         "including SOSP, NSDI, MICRO, ASPLOS, ATC, ICSE, EuroSys, TPDS, and TDSC. In recent three years, Dr. Cui serves at least once in the program committees of international top conferences "
         "on systems/networking/software, including OSDI, SIGCOMM, ASPLOS, NSDI, ATC, EuroSys, and DSN. Dr. Cui also serves as active reviewers for international top journals on systems/networking/software/security, "
         "including TPDS, TOCS, TSE, TON, TMC, and TDSC. He serves as the program chair of ACM ChinaSys 2023. Dr. Cui has won several worldwide competitive research awards or grants, including a Croucher Innovation Award "
         "in 2016 (HK $5 million), a best paper award from ACSAC '17, the Best Collaborating Scientist Medal from the Huawei Theory Lab in 2021, and the RGC Research Impact Fund (RIF) in 2023 (HK $4 million). "
         "He is the leader of a project (about training large AI models) funded by China's National Key R&D Program.")
)

teacher16 = Teacher(
    id=10016,
    name="Dr. Zhiyi Huang",
    department="Department of Computer Science",
    bio=("Zhiyi is an Associate Professor of Computer Science at the University of Hong Kong. He works broadly on Theoretical Computer Science and "
         "Algorithmic Game Theory, and dabbles in the theoretical aspects of related fields, including Machine Learning, and Computer Networks. Since joining "
         "HKU in 2014, Zhiyi has received the Early Career Award from the Research Grant Council of Hong Kong in 2014, and the Best Paper Award of SPAA in 2015. "
         "Before joining HKU, he was a postdoc at Stanford University from 2013 to 2014, working with Tim Roughgarden. He obtained his Ph.D. from the University "
         "of Pennsylvania under Sampath Kannan and Aaron Roth in 2013, and received the Morris and Dorothy Rubinoff Dissertation Award. Before that, Zhiyi was the "
         "recipient of the Simons Graduate Fellowship in Theoretical Computer Science from 2012 to 2013, and interned at Microsoft Research Redmond under Nikhil R. "
         "Devanur in the summers of 2011 and 2012. Prior to his Ph.D. studies, Zhiyi graduated from the first 'Yao Class' under Andrew Yao at Tsinghua University in 2008.")
)

teacher17 = Teacher(
    id=10017,
    name="Dr. B. Oliveira",
    department="Department of Computer Science",
    bio=("Dr. Bruno Oliveira received his PhD from the University of Oxford in 2008. He was a Research Professor at Seoul National University between 2009 and 2011 "
         "and then he was on a Senior Research Fellow position at the National University of Singapore until 2013. Currently, since September 2013, he is an Assistant "
         "Professor at the University of Hong Kong.")
)

teacher18 = Teacher(
    id=10018,
    name="Dr. D. Schnieders",
    department="Department of Computer Science",
    bio=("Dirk Schnieders graduated with a Diplom-Informatiker (FH) degree from the Fachhochschule Dortmund (Germany) in 2004 and received his MSc and PhD in Computer "
         "Science from The University of Hong Kong in 2007 and 2011. Currently, he is a Senior Lecturer at the Department of Computer Science, The University of Hong Kong.")
)

teacher19 = Teacher(
    id=10019,
    name="Dr. Hengshuang Zhao",
    department="Department of Computer Science",
    bio=("I am an Assistant Professor at the Department of Computer Science at The University of Hong Kong. My general research interests cover the broad area of computer vision, "
         "machine learning and artificial intelligence, with special emphasis on building intelligent visual systems. My research goal is to utilize artificial intelligence techniques "
         "to make machines perceive, understand and interact with the surrounding environment, and ultimately make high positive impacts on various fields. Previously, I have spent "
         "wonderful times as a postdoctoral researcher at Computer Science and Artificial Intelligence Laboratory (CSAIL) at MIT, working with Prof. Antonio Torralba, at Torr Vision "
         "Group at the University of Oxford, working with Prof. Philip Torr. I obtained my Ph.D. degree at CSE Department at The Chinese University of Hong Kong, supervised by Prof. Jiaya Jia. "
         "During Ph.D., I have spent wonderful times as an intern with Dr. Xiaohui Shen, Dr. Zhe Lin, Dr. Kalyan Sunkavalli, Dr. Brian Price at Adobe (San Jose), Prof. Raquel Urtasun at Uber (Toronto), "
         "and Dr. Vladlen Koltun at Intel (Santa Clara).")
)

teacher20 = Teacher(
    id=10020,
    name="Dr. Ping Luo",
    department="Department of Computer Science",
    bio=("I am recruiting a number of Postdocs, PhDs, and RAs. Ping Luo's researches aim at developing Differentiable/ Meta/ Reinforcement Learning algorithms that endow machines "
         "and devices to solve complex tasks with larger autonomy, understanding foundations of deep learning algorithms, and enabling applications in Computer Vision and Artificial Intelligence. "
         "Ping Luo received his PhD degree in 2014 in Information Engineering, the Chinese University of Hong Kong (CUHK), supervised by Prof. Xiaoou Tang (founder of SenseTime Group Ltd.) "
         "and Prof. Xiaogang Wang. He was a Research Director in SenseTime Research. He has published 70+ peer-reviewed articles in top-tier conferences and journals such as TPAMI, IJCV, ICML, ICLR, NeurIPS and CVPR. "
         "He has won a number of competitions and awards such as the first runner up in 2014 ImageNet ILSVRC Challenge, the first place in 2017 DAVIS Challenge on Video Object Segmentation, Gold medal in 2017 Youtube‐8M "
         "Video Classification Challenge, the first place in 2018 Drivable Area Segmentation Challenge for Autonomous Driving, 2011 HK PhD Fellow Award, and 2013 Microsoft Research Fellow Award.")
)

teacher21 = Teacher(
    id=10021,
    name="Dr. C.K. Chui",
    department="Department of Computer Science",
    bio=("Dr. Chui is the recipient of the University Outstanding Teaching Award (Individual Award 2015-16) of the University of Hong Kong. He was also selected for the Faculty Outstanding Teaching Award (Individual Award) of the Faculty of Engineering in 2012-13. He is also a shortlisted candidate for the UGC Teaching Award (Early Career Faculty Members Individual Award) 2016, University Grants Committee. He has also received the Teaching Excellence Award in the Department of Computer Science in 2011-12, 2012-13, 2013-14, 2014-15, 2015-16 and 2016-17. Dr. Chui is also the Director of the Tam Wing Fan Innovation Wing, Faculty of Engineering of the University of Hong Kong.")
)

teacher22 = Teacher(
    id=10022,
    name="Dr. Lingpeng Kong",
    department="Department of Computer Science",
    bio=("Dr. Lingpeng Kong is an assistant professor in the Department of Computer Science at the University of Hong Kong (HKU). His research tackles the core problems in natural language processing (NLP) by designing representation learning algorithms that exploit linguistic structures. His work lies at the intersection of deep learning and structured prediction, with an application focus on syntactic parsing, speech recognition, social media analysis and machine translation. Before joining HKU, he was a research scientist at Google DeepMind from 2017 to 2020. Dr. Kong obtained his Ph.D. from Carnegie Mellon University in 2017, co-advised by Noah Smith and Chris Dyer.")
)

teacher23 = Teacher(
    id="010023",
    name="Prof. Yizhou Yu",
    department="Department of Computer Science",
    bio=("Professor Yu received his PhD degree in computer science from University of California, Berkeley in 2000. "
         "He also holds a MS degree in applied mathematics and a BE degree in computer science and engineering from Zhejiang University. "
         "He was first a tenure-track then a tenured professor at University of Illinois, Urbana-Champaign (UIUC) for 12 years. "
         "He has also collaborated with Google Brain and Microsoft Research in the past. He is an IEEE Fellow and ACM Distinguished Member. "
         "Professor Yu has made important contributions to AI and visual computing, including deep learning, computer vision, image processing, "
         "graphics, and VR/AR. His current research includes deep learning methods for machine intelligence, biomedical data analysis, computer vision, "
         "computational visual media, and geometric computing. He is an associate editor of IET Computer Vision, IEEE Transactions on Visualization and Computer Graphics, "
         "and International Journal of Software and Informatics.")
)

teacher24 = Teacher(
    id="010024",
    name="Dr. Giulio Chiribella",
    department="Department of Computer Science",
    bio=("I joined the University of Hong Kong in August 2015. "
         "Before joining HKU, I have been Associate Professor at Tsinghua University, Beijing (2012-2015), and Postdoctoral Fellow of Perimeter Institute for Theoretical Physics, "
         "Waterloo, Canada (2009-2012).")
)

teacher25 = Teacher(
    id="010025",
    name="Dr. R.C.K. Cheng",
    department="Department of Computer Science",
    bio=("Reynold Cheng is a Professor of the Department of Computer Science in the University of Hong Kong (HKU). "
         "His research interests are in data science, big graph analytics, and uncertain data management. "
         "He was an Assistant Professor in the Department of Computing of the Hong Kong Polytechnic University (HKPU) from 2005 to 2008. "
         "He received his BEng in Computer Engineering in 1998, and MPhil in Computer Science and Information Systems in 2000 from HKU, "
         "followed by MSc and PhD degrees from the Department of Computer Science of Purdue University in 2003 and 2005. "
         "Prof. Cheng has received multiple awards and recognitions, including the SIGMOD Research Highlights Reward 2020 and HKU Knowledge Exchange Award (Engineering) 2021. "
         "He is also an active member and contributor to various academic societies and conferences.")
)

teacher26 = Teacher(
    id="010026",
    name="Dr. Alice Yuen",
    department="Department of Computer Science",
    bio=("Dr. Alice Yuen is an Associate Professor at the Department of Computer Science in the University of Hong Kong. "
         "Her research focuses on artificial intelligence, machine learning, and their applications in healthcare. "
         "Dr. Yuen joined the faculty in 2012 after a successful career in the industry. "
         "She earned her PhD in Computer Science from Stanford University, where she also completed her MSc. "
         "Her work has been recognized with several awards, including the Young Scientist Award in 2018. "
         "Dr. Yuen is committed to bridging the gap between academia and industry through collaborative projects.")
)

teacher27 = Teacher(
    id="010027",
    name="Dr. Bob He",
    department="Department of Computer Science",
    bio=("Dr. Bob He is a Senior Lecturer in the Department of Computer Science at the University of Hong Kong. "
         "He specializes in network security, cryptography, and blockchain technology. "
         "Before joining academia, Dr. He worked in the IT security industry for over a decade. "
         "He received his PhD from the University of Cambridge and has since been an advocate for practical cybersecurity education. "
         "Dr. He has received multiple grants for his research in securing digital transactions and is a frequent speaker at international conferences.")
)

teacher28 = Teacher(
    id="010028",
    name="Dr. Carol Wu",
    department="Department of Computer Science",
    bio=("Dr. Carol Wu is an Assistant Professor at the Department of Computer Science, University of Hong Kong. "
         "Her research areas include data mining, big data analytics, and computational biology. "
         "Dr. Wu obtained her PhD from MIT, where she developed several widely-used algorithms for large-scale data analysis. "
         "She has collaborated extensively with biologists to apply computational techniques in understanding genetic data. "
         "Dr. Wu has been awarded several research fellowships and grants for her innovative work in computational biology.")
)

teacher29 = Teacher(
    id="010029",
    name="Dr. David Li",
    department="Department of Computer Science",
    bio=("Dr. David Li is a Professor in the Department of Computer Science at the University of Hong Kong. "
         "His expertise lies in software engineering, distributed systems, and cloud computing. "
         "He has been with the department since 2000, contributing significantly to both teaching and research. "
         "Dr. Li completed his PhD at the University of California, Berkeley. "
         "He has published numerous papers in prestigious journals and has been a principal investigator on several major research projects funded by government and industry partners.")
)

teacher30 = Teacher(
    id="010030",
    name="Dr. Emily Zhang",
    department="Department of Computer Science",
    bio=("Dr. Emily Zhang is an Associate Professor at the University of Hong Kong, Department of Computer Science. "
         "Her research interests include human-computer interaction, virtual reality, and educational technology. "
         "After obtaining her PhD from the University of Toronto, Dr. Zhang worked in a leading tech company's R&D department. "
         "She has been instrumental in developing new methodologies for user experience research and has received accolades for her innovative teaching methods. "
         "Dr. Zhang actively collaborates with industry partners to bring advanced HCI concepts into real-world applications.")
)

Teacher.objects.all().delete()
teacher1.save()
teacher2.save()
teacher3.save()
teacher4.save()
teacher5.save()
teacher6.save()
teacher7.save()
teacher8.save()
teacher9.save()
teacher10.save()
teacher11.save()
teacher12.save()
teacher13.save()
teacher14.save()
teacher15.save()
teacher16.save()
teacher17.save()
teacher18.save()
teacher19.save()
teacher20.save()
teacher21.save()
teacher22.save()
teacher23.save()
teacher24.save()
teacher25.save()
teacher26.save()
teacher27.save()
teacher28.save()
teacher29.save()
teacher30.save()
















